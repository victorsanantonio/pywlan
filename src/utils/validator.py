import re


class Validator:

    def valid_ip_range(self, ip):
        regex = re.compile(r"(?<![-\.\d])(?:0{0,2}?[0-9]\.|1\d?\d?\.|2[0-5]?[0-5]?\.){3}(?:0{0,2}?[0-9]|1\d?\d?|2[0-5]?[0-5]?)(?![\.\d])")
        if regex.match(ip) != None:
            return True
        else:
            return False
    
    def valid_ip(self, ip):
        regex = re.compile(r"^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$")
        if regex.match(ip) != None:
            return True
        else:
            return False
    
    def valid_port(self, port):
        if port >=1 and port <= 65000:
            return True
        else:
            return False
    
    def startport_less_than_endport(self, startport, endport):
        if startport <= endport:
            return True
        else:
            return False
    
validator = Validator()

class DeviceScannerValidator(Validator):

    def valid_ip_range(self, ip_range):
        if not super().valid_ip_range(ip_range):
            raise Exception("Invalid IP range")


deviceScannerValidator = DeviceScannerValidator()


class PortScannerValidator(Validator):

    def valid_ip(self, ip):
        if not super().valid_ip(ip):
            raise Exception("Invalid IP")
    
    def valid_startport(self, startport):
        if not startport.isnumeric():
            raise Exception("The startport must be a number")
        if not super().valid_port(int(startport)):
            raise Exception("The startport must be greater than 0 and less than 65000")
    
    def valid_endport(self, endport):
        if not endport.isnumeric():
            raise Exception("The endport must be a number")
        if not super().valid_port(int(endport)):
            raise Exception("The endport must be greater than 0 and less than 65000")
    
    def compare_ports(self, startport, endport):
        if super().startport_less_than_endport(int(startport), int(endport)):
            raise Exception("The endport must be greater than the startport")

portScannerValidator = PortScannerValidator()