#!/home/sketch/PycharmProjects/tools/.venv/bin/python
import subprocess as sp
import xml.etree.ElementTree as ET
import os

command = ['-sC', '-sV']
host = '127.0.0.1'

r = '\033[31m'  # red
b = '\033[34m'  # blue
g = '\033[32m'  # green
y = '\033[33m'  # yellow
m = '\033[34m'  # magenta
c = '\033[36m'  # magenta
e = '\033[0m'  # end


class NmapScan:
    def __init__(self):
        self.IP = ''
        self.PORT = ''
        self.SWITCH = ''
        self.CURRENT_PROJECT_ID = ''
        self.take_scan = ''
        self.N = 4
        self.port_divisor = 7500
        self.pause_flag = False
        self.stop_flag = False
        self.ip_count = 0

        self.options = []

    def scan(self, ip):
        try:
            p = sp.Popen(['nmap'] + self.options + ['-oX', '-', ip], shell=False, stdin=sp.PIPE, stdout=sp.PIPE,
                         stderr=sp.PIPE)
            out, err = p.communicate()
            print('\n Nmap scan is complete :')
            root = ET.fromstring(out.decode('utf-8'))
            hosts = []
            tag = root.tag
            for host in root.findall('host'):
                details = {
                    "address": host.find('address').get('addr') if host.find('address') is not None else "",
                    "name": host.find('hostnames').find('hostname').get('name') if host.find(
                        'hostnames') is not None and host.find('hostnames').find('hostname') is not None else "",
                }
                port_list = []
                for ports in host.find('ports'):
                    if ports is None:
                        continue
                    port = ports.get('portid')
                    if port is None:
                        continue
                    port_details = {
                        "port": port,
                        "protocol": ports.get('protocol'),
                    }
                    service = ports.find('service')
                    state = ports.find('state')
                    if service is not None and service.attrib is not None:
                        port_details['service'] = service.attrib.get('name')
                        port_details['product'] = service.attrib.get('product')
                        port_details['version'] = service.attrib.get('version')
                        port_details['extrainfo'] = service.attrib.get('extrainfo')
                        port_details['ostype'] = service.attrib.get('ostype')
                        port_details['cpe'] = service.attrib.get('cpe')
                    if state is not None and state.attrib is not None:
                        port_details['state'] = state.attrib.get('state')
                        port_details['reason'] = state.attrib.get('reason')
                    port_list.append(port_details)
                details['ports'] = port_list
                hosts.append(details)
            for host in hosts:
                print("---------------------------------------------")
                print("Name: ", host['name'])
                print("Address: ", host['address'])
                print("Services: ")
                for port in host['ports']:
                    print('\tService :')
                    print('\t---------------------------------------------')
                    for (key, value) in port.items():
                        print('\t', key, ' : ', value)
                    print('\t---------------------------------------------')
        except Exception as e:
            print('Exception : ', e)
