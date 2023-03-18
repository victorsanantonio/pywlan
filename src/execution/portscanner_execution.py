from src.execution.requestor import requestor
from src.utils.validator import validator
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.controller.scanner import PortScanner

class PortScannerExecution():

    #TODO: Improve validations and code quality
    def scan(self):
        ip = requestor.request_ip()
        if validator.valid_ip(ip) == True:
            startport = requestor.request_start_port()
            if startport.isnumeric():
                int_startport = int(startport)
                if validator.valid_port(int_startport) == True:
                    endport = requestor.request_end_port()
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