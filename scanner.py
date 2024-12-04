from nmap import NmapScan
from six.moves import input as raw_input
import configparser

r = '\033[31m'  # red
b = '\033[34m'  # blue
g = '\033[32m'  # green
y = '\033[33m'  # yellow
m = '\033[34m'  # magenta
c = '\033[36m'  # magenta
e = '\033[0m'  # end


class Scanner:
    def __init__(self):
        self.nmap = NmapScan()

    @staticmethod
    def scan_type():
        while 1:
            scan_type = raw_input(
                b + "Enter Your choice: \n" + y + "\n(1) For Launching New Scan \n(2) For Launching Paused Scans\n " + e)
            try:
                if (scan_type == "1") or (scan_type == "2"):
                    break
                else:
                    print("Invalid Choice")
            except():
                return "1"
        return scan_type

    @staticmethod
    def separator():
        print(r + "----------------------------------------------" + e)

    @staticmethod
    def project_name():
        while 1:
            name = raw_input(b + "Enter Project Name (No White Spaces) : " + e)
            if name != "":
                break
            else:
                print("Invalid Project Name")
        return name

    @staticmethod
    def project_id():
        while 1:
            name = raw_input(b + "Enter Project ID : " + e)
            if name != "":
                break
            else:
                print("Invalid Project ID")
        return name

    @staticmethod
    def prompt_ips():
        ips = raw_input(b + "Type the IP range: \n>" + y)
        # IP = ips
        return ips

    def prompt_ports(self):
        ports = raw_input(b + "Type the port range: \n>" + y)
        # PORT = ports
        if ports == "":
            self.nmap.PORT = None
        elif ports == "*":
            self.nmap.PORT = "1-65535"
        else:
            self.nmap.PORT = ports
        return self.nmap.PORT

    def scan_banner(self):
        cp = configparser.RawConfigParser()
        cp.read('nmap.cfg')
        print("Select Scan Type")
        self.separator()
        print(y + "1. Intense Scan")
        print("2. Intense + UDP Scan")
        print("3. Intense + TCP Full Scan")
        print("4. Intense + No Ping Scan")
        print("5. TCP Ping Scan")
        print("6. TCP Ping Sweep")
        print("7. PCI full ports TCP")
        print("8. PCI Top 200 UDP")
        print("9. PCI Top 100 UDP")
        print("10. PCI Top 1000 TCP")

        scan_type = raw_input(b + "Select the type of Scan:\n>" + y)

        if scan_type == "1":
            self.nmap.SWITCH = cp.get('ScanType', 'Intense')
        elif scan_type == "2":
            self.nmap.SWITCH = cp.get('ScanType', 'Intense_UDP')
        elif scan_type == "3":
            self.nmap.SWITCH = cp.get('ScanType', 'Intense_TCPall')
        elif scan_type == "4":
            self.nmap.SWITCH = cp.get('ScanType', 'Intense_NoPing')
        elif scan_type == "5":
            self.nmap.SWITCH = cp.get('ScanType', 'Ping')
        elif scan_type == "6":
            self.nmap.SWITCH = cp.get('ScanType', 'PCI_Ping_Sweep')
        elif scan_type == "7":
            self.nmap.SWITCH = cp.get('ScanType', 'PCI_Top_1000_TCP')
        elif scan_type == "8":
            self.nmap.SWITCH = cp.get('ScanType', 'PCI_Top_200_UDP')
        elif scan_type == "9":
            self.nmap.SWITCH = cp.get('ScanType', 'PCI_Top_100_UDP')
        elif scan_type == "10":
            self.nmap.SWITCH = cp.get('ScanType', 'PCI_Top_1000_TCP')
        else:
            print("Invalid value supplied")
            print("Using Default(1)")
            self.nmap.SWITCH = cp.get('ScanType', 'Intense')

    @staticmethod
    def banner():
        print(" @@@@@@    @@@@@@@   @@@@@@   @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@   ")
        print("@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  ")
        print("!@@       !@@       @@!  @@@  @@!@!@@@  @@!@!@@@  @@!       @@!  @@@  ")
        print("!@!       !@!       !@!  @!@  !@!!@!@!  !@!!@!@!  !@!       !@!  @!@  ")
        print("!!@@!!    !@!       @!@!@!@!  @!@ !!@!  @!@ !!@!  @!!!:!    @!@!!@!   ")
        print(" !!@!!!   !!!       !!!@!!!!  !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    ")
        print("     !:!  :!!       !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!: :!!   ")
        print("    !:!   :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:       :!:  !:!  ")
        print(":::: ::    ::: :::  ::   :::   ::   ::   ::   ::   :: ::::  ::   :::  ")
        print(":: : :     :: :: :   :   : :  ::    :   ::    :   : :: ::    :   : : ")
        print("                                                                      ")

    def start(self):
        self.banner()
        while 1:
            self.scan_banner()
            print(self.nmap.SWITCH)


if __name__ == '__main__':
    Scanner().start()
