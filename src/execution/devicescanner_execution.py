from src.execution.requestor import requestor
from src.utils.validator import validator, deviceScannerValidator
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.utils.exporter import exporter
from src.controller.scanner import DeviceScanner


class DeviceScannerExecution():
    
    def scan(self):
        DATASET_NAME = "device-scan"
        try:
            ip_range = requestor.request_ip_range()
            deviceScannerValidator.valid_ip_range(ip_range)
            
            deviceScanner = DeviceScanner(ip_range)
            response = deviceScanner.scan()
            info = formatter.format_device_scan_response(response)
            viewer.view_device_scan_info(info)

            export_confirmation = requestor.request_export_confirmation()
            print(f"asdfasfsafas{export_confirmation}")
            confirmation = validator.valid_confirmation(export_confirmation)
            exporter.confirm_exportation(info, DATASET_NAME, confirmation)

        except Exception as exception:
            print(exception)

deviceScannerExecution = DeviceScannerExecution()