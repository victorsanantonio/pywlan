from utils.scanner import deviceScanner
from utils.utils import Formatter, Viewer
from sys import exit


class Menu:

    def main_menu(self):
        print(self.generate_word_art(), self.generate_menu_options())
        self.menu_logic(self.get_option())
    
    def menu_logic(self, option):
        match option:
            case 1:
                response = deviceScanner.scan()
                formatter = Formatter()
                info = formatter.format_device_scan_response(response)
                viewer = Viewer()
                viewer.view_device_scan_response(info)
            case 2:
                print("Doing port scan")
            case 3:
                print("Doing ARP spoofing")
            case 4:
                exit("Goodbye!")
            case _:
                print("Non available option")

    def get_option(self):
        return int(input(" -> Choose an option: \n"))
    
    def generate_menu_options(self):
        return """\n
        1. Scan devices on WLAN \n
        2. Scan ports of an specific device \n
        3. ARP spoofing \n
        4. Exit \n"""

    def generate_word_art(self):
        return """
           _                                            
          | |                                           
 __      _| | __ _ _ ____   _____ _ __ ___   ___  _ __  
 \ \ /\ / / |/ _` | '_ \ \ / / _ \ '_ ` _ \ / _ \| '_ \ 
  \ V  V /| | (_| | | | \ V /  __/ | | | | | (_) | | | |
   \_/\_/ |_|\__,_|_| |_|\_/ \___|_| |_| |_|\___/|_| |_|
                                                        
                                                        """