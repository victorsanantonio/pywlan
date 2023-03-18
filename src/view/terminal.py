from src.controller.scanner import DeviceScanner, PortScanner
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

    def show_ascii_word_art(self):
        print("""
           _                                            
          | |                                           
 __      _| | __ _ _ ____   _____ _ __   ___  _ __ ___  
 \ \ /\ / / |/ _` | '_ \ \ / / _ \ '_ \ / _ \| '_ ` _ \ 
  \ V  V /| | (_| | | | \ V /  __/ | | | (_) | | | | | |
   \_/\_/ |_|\__,_|_| |_|\_/ \___|_| |_|\___/|_| |_| |_|
                                                        """)


class Execution:
    
    def request_ip_range(self):
        return input("\nEnter an IP range. Example: [192.168.1.1/24]:\t")

    def request_ip(self):
        return input("\nEnter a valid IP. Example: [192.168.1.1]:\t")
    
    def request_start_port(self):
        return input("\nEnter start port:\t")
    
    def request_end_port(self):
        return input("\nEnter end port:\t")
    
class DeviceScannerExecution(Execution):
    
    def scan_devices(self):
        ip_range = super().request_ip_range()
        if validator.valid_ip(ip_range) == True:
            deviceScanner = DeviceScanner(ip_range)
            response = deviceScanner.scan()
            info = formatter.format_device_scan_response(response)
            viewer.view_device_scan_info(info)
        else:
            print("Invalid IP range")

deviceScannerExecution = DeviceScannerExecution()


class PortScannerExecution(Execution):

    #TODO: Improve validations and code quality
    def scan_ports(self):
        ip = super().request_ip()
        if validator.valid_ip(ip) == True:
            startport = super().request_start_port()
            if startport.isnumeric():
                int_startport = int(startport)
                if validator.valid_port(int_startport) == True:
                    endport = super().request_end_port()
                    if startport.isnumeric():
                        int_endport = int(endport)
                        if validator.valid_port(int_endport) == True:
                            portScanner = PortScanner(ip, int_startport, int_endport)
                            response = portScanner.scan()
                            info = formatter.format_port_scan_response(response)
                            viewer.view_port_scan_info(info)
                        else:
                            print("The end port must be greater than 0 and less than 65000")
                    else:
                        print("The start port must be a number")
                else:
                    print("The start port must be greater than 0 and less than 65000")
            else:
                print("The start port must be a number")
        else:
            print("Invalid ip")

portScannerExecution = PortScannerExecution()

class ARPSpoofingExecution:
    def arp_spoofing(self):
        print("ARP spoofing")

arpSpoofingExecution = ARPSpoofingExecution()