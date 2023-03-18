from src.execution.requestor import requestor
from src.utils.validator import validator
from src.utils.formatter import formatter
from src.utils.viewer import viewer
from src.controller.scanner import DeviceScanner


class DeviceScannerExecution():
    
    def scan(self):
        ip_range = requestor.request_ip_range()
        if validator.valid_ip_range(ip_range) == True:
            deviceScanner = DeviceScanner(ip_range)
            response = deviceScanner.scan()
            info = formatter.format_device_scan_response(response)
            viewer.view_device_scan_info(info)
        else:
            print("Invalid IP range")

deviceScannerExecution = DeviceScannerExecution()