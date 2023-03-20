from src.execution.requestor import requestor
from src.utils.validator import validator, portScannerValidator
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.utils.exporter import exporter
from src.controller.scanner import PortScanner


class PortScannerExecution():

    def scan(self):
        DATASET_NAME = "port-scan"
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

            export_confirmation = requestor.request_export_confirmation()
            confirmation = validator.valid_confirmation(export_confirmation)
            exporter.confirm_exportation(info, DATASET_NAME, confirmation)

        except Exception as exception:
            print(exception)

portScannerExecution = PortScannerExecution()