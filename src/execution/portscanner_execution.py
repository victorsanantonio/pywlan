from src.utils.requester import requester
from src.utils.validator import validator, validator_execution
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.utils.exporter import exporter
from src.controller.controller import PortScanner


class PortScannerExecution():

    def scan(self):
        DATASET_NAME = "port-scan"
        try:
            ip = requester.request_ip()
            validator_execution.validate_ip(ip)

            startport = requester.request_start_port()
            validator_execution.validate_port(startport)

            endport = requester.request_end_port()
            validator_execution.validate_port(endport)

            validator_execution.compare_ports(endport, startport)

            port_scanner = PortScanner(ip, int(startport), int(endport))
            response = port_scanner.scan()
            info = formatter.format_port_scan_response(response)
            viewer.view_port_scan_info(info)

            export_confirmation = requester.request_export_confirmation()
            confirmation = validator.valid_confirmation(export_confirmation)
            exporter.confirm_exportation(info, DATASET_NAME, confirmation)

        except Exception as exception:
            print(exception)

port_scanner_execution = PortScannerExecution()