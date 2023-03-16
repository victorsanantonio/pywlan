from src.controller.scanner import DeviceScanner
from src.utils.utils import formatter, viewer, validator
from sys import exit


class Menu:

    def exit(self):
        print("Exiting program")

    def generate_menu(self, options, exit_option):
        option = None
        while option != exit_option:
            self.show_menu(options)
            option = self.get_option(options)
            self.execute_option(option, options)

    def execute_option(self, option, options):
        options[option][1]()

    def show_menu(self, options):
        for key in sorted(options):
            print(f'\n\t{key}. {options[key][0]}')
    
    def main_menu(self):
        options =  {
            '1': ('Scan devices on WLAN', deviceScannerExecution.scan_devices),
            '2': ('Scan ports of an specific device', portScannerExecution.scan_ports),
            '3': ('ARP spoofing', arpSpoofingExecution.arp_spoofing),
            '4': ('Salir', self.exit)
        }
        self.generate_menu(options, '4')

    def get_option(self, options):
        while (a := input('\n\t\tChoose an option: ')) not in options:
            print("Option non available. Try again")
        return a

    def show_word_art(self):
        print("""
           _                                            
          | |                                           
 __      _| | __ _ _ ____   _____ _ __ ___   ___  _ __  
 \ \ /\ / / |/ _` | '_ \ \ / / _ \ '_ ` _ \ / _ \| '_ \ 
  \ V  V /| | (_| | | | \ V /  __/ | | | | | (_) | | | |
   \_/\_/ |_|\__,_|_| |_|\_/ \___|_| |_| |_|\___/|_| |_|
                                                        
                                                        """)
class DeviceScannerExecution:
    def get_ip_range(self):
        return input("\nEnter an IP range. Example: [192.168.1.1/24]: \t")
    
    def scan_devices(self):
        ip_range = self.get_ip_range()
        regex_match = validator.validate_ip_range(ip_range)
        if regex_match != None:
            deviceScanner = DeviceScanner(ip_range)
            response = deviceScanner.scan()
            info = formatter.format_device_scan_response(response)
            viewer.view_device_scan_response(info)
        else:
            print("Invalid IP range")

deviceScannerExecution = DeviceScannerExecution()


class PortScannerExecution:
    def scan_ports(self):
        print("Port scanning")

portScannerExecution = PortScannerExecution()

class ARPSpoofingExecution:
    def arp_spoofing(self):
        print("ARP spoofing")

arpSpoofingExecution = ARPSpoofingExecution()