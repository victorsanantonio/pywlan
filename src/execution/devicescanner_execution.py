from src.execution.requestor import requestor
from src.utils.validator import deviceScannerValidator
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.controller.scanner import DeviceScanner


class DeviceScannerExecution():
    
    def scan(self):
        try:
            ip_range = requestor.request_ip_range()
            deviceScannerValidator.valid_ip_range(ip_range)
            
            deviceScanner = DeviceScanner(ip_range)
            response = deviceScanner.scan()
            info = formatter.format_device_scan_response(response)
            viewer.view_device_scan_info(info)
        except Exception as exception:
            print(exception)

deviceScannerExecution = DeviceScannerExecution()