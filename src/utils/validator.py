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

validator = Validator()