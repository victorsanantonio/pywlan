from src.utils.requester import requester
from src.utils.validator import validator_execution
from src.controller.controller import ARPSpoofer


class ARPSpooferExecution:
    def spoof(self):
        try:
            target_ip = requester.request_target_ip()
            validator_execution.validate_ip(target_ip)

            gateway_ip = requester.request_gateway_ip()
            validator_execution.validate_ip(gateway_ip)

            arp_spoofer = ARPSpoofer(target_ip, gateway_ip)
            arp_spoofer.spoof()

        except Exception as exception:
            print(exception)

arp_spoofer_execution = ARPSpooferExecution()