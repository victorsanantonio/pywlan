from src.execution.devicescanner_execution import device_scanner_execution
from src.execution.portscanner_execution import port_scanner_execution
from src.execution.arp_spoofer_execution import arp_spoofer_execution


class Menu:

    def exit(self):
        print("Goodbye!")

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
            '1': ('Scan devices on WLAN', device_scanner_execution.scan),
            '2': ('Scan ports of an specific device', port_scanner_execution.scan),
            '3': ('ARP spoofing', arp_spoofer_execution.spoof),
            '4': ('Exit', self.exit)
        }
        self.generate_menu(options, '4')

    def get_option(self, options):
        while (a := input('\n\t\tChoose an option: ')) not in options:
            print("Non available option. Try again")
        return a

    def show_ascii_word_art(self):
        print("""
                       _              
                      | |             
  _ __  _   ___      _| | __ _ _ __   
 | '_ \| | | \ \ /\ / / |/ _` | '_ \  
 | |_) | |_| |\ V  V /| | (_| | | | | 
 | .__/ \__, | \_/\_/ |_|\__,_|_| |_| 
 | |     __/ |                        
 |_|    |___/                         
""")
