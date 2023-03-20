from src.utils.requester import requester
from src.utils.validator import validator, validator_execution
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.utils.exporter import exporter
from src.controller.controller import DeviceScanner


class DeviceScannerExecution():
    
    def scan(self):
        DATASET_NAME = "device-scan"
        try:
            ip_range = requester.request_ip_range()
            validator_execution.validate_ip_range(ip_range)
            
            device_scanner = DeviceScanner(ip_range)
            response = device_scanner.scan()
            info = formatter.format_device_scan_response(response)
            viewer.view_device_scan_info(info)

            export_confirmation = requester.request_export_confirmation()
            confirmation = validator.valid_confirmation(export_confirmation)
            exporter.confirm_exportation(info, DATASET_NAME, confirmation)

        except Exception as exception:
            print(exception)

device_scanner_execution = DeviceScannerExecution()