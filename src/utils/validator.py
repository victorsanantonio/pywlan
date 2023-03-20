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
    
    def valid_confirmation(self, confirmation):
        confirmation_casefold = confirmation.casefold()
        if confirmation_casefold == "y" or confirmation_casefold =="yes":
            return True
        else:
            return False
    
validator = Validator()


class ValidatorExecution(Validator):

    def validate_ip(self, ip):
        if not super().valid_ip(ip):
            raise Exception("Invalid IP")
    
    def validate_ip_range(self, ip_range):
        if not super().valid_ip_range(ip_range):
            raise Exception("Invalid IP range")
    
    def validate_port(self, port):
        if not port.isnumeric():
            raise Exception("The port must be a number")
        if not super().valid_port(int(port)):
            raise Exception("The port must be greater than 0 and less than 65000")
        
    def compare_ports(self, startport, endport):
        if super().startport_less_than_endport(int(startport), int(endport)):
            raise Exception("The end port must be greater than the start port")

validator_execution = ValidatorExecution()