from utils.scanner import deviceScanner
from utils.utils import Formatter, Viewer
from sys import exit


class Menu:
    

    def get_ip_range(self):
        print("\nEnter an IP range. Example: [192.168.1.1/24]")
        str(input("Introduce IP range here:\t"))
    
    def scan_devices(self):
        self.get_ip_range()
        response = deviceScanner.scan()
        formatter = Formatter()
        info = formatter.format_device_scan_response(response)
        viewer = Viewer()
        viewer.view_device_scan_response(info)
    
    def scan_ports(self):
        pass
    
    def arp_spoofing(self):
        pass

    def exit(self):
        pass

    def generate_menu(self, options, exit_option):
        option = None
        while option != exit_option:
            self.show_menu(options)
            option = self.get_option()
        #TODO: Main menu improvement
        """while True:
            match option:
                case 1:
                    
                case 2:
                    print("Doing port scan")
                case 3:
                    print("Doing ARP spoofing")
                case 4:
                    exit("Goodbye!")
                case _:
                    print("Non available option")"""
    def show_menu(self, options):
        print(self.generate_word_art(), self.generate_menu_options())
        self.menu_logic(self.get_option())
    
    def main_menu(self):
        options =  {
            '1': ('Scan devices on WLAN', self.scan_devices()),
            '2': ('Scan ports of an specific device', self.scan_ports()),
            '3': ('ARP spoofing', self.arp_spoofing()),
            '4': ('Salir', self.exit())
        }
        self.generate_menu(options, '4')

    def get_option(self):
        return int(input(" -> Choose an option: \t"))

    def generate_word_art(self):
        return """
           _                                            
          | |                                           
 __      _| | __ _ _ ____   _____ _ __ ___   ___  _ __  
 \ \ /\ / / |/ _` | '_ \ \ / / _ \ '_ ` _ \ / _ \| '_ \ 
  \ V  V /| | (_| | | | \ V /  __/ | | | | | (_) | | | |
   \_/\_/ |_|\__,_|_| |_|\_/ \___|_| |_| |_|\___/|_| |_|
                                                        
                                                        """