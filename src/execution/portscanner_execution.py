from src.execution.requestor import requestor
from src.utils.validator import portScannerValidator
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.controller.scanner import PortScanner


class PortScannerExecution():

    def scan(self):
        try:
            ip = requestor.request_ip()
            portScannerValidator.valid_ip(ip)

            startport = requestor.request_start_port()
            portScannerValidator.valid_startport(startport)

            endport = requestor.request_end_port()
            portScannerValidator.valid_endport(endport)

            portScannerValidator.compare_ports(endport, startport)

            portScanner = PortScanner(ip, int(startport), int(endport))
            response = portScanner.scan()
            info = formatter.format_port_scan_response(response)
            viewer.view_port_scan_info(info)

        except Exception as exception:
            print(exception)

portScannerExecution = PortScannerExecution()