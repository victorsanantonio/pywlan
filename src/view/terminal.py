from src.execution.devicescanner_execution import deviceScannerExecution
from src.execution.portscanner_execution import portScannerExecution
from src.execution.arp_spoofer_execution import arpSpoofingExecution


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
            '1': ('Scan devices on WLAN', deviceScannerExecution.scan),
            '2': ('Scan ports of an specific device', portScannerExecution.scan),
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
