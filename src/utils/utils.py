import re

class Formatter:

    def format_device_scan_response(self, response):
        clients_info = []
        for client in response:
            client_info = {
                "IP": {client.ip},
                "MAC": {client.mac}
            }
            clients_info.append(client_info)
        return clients_info

    def format_port_scan_response(self, response):
        ports_info = []
        for port in response:
            port_state = port.is_opened
            if port_state == True:
                port_state = "Opened"
            else:
                port_state = "Closed"
            port_info = {
                "Port": {port.port},
                "State": {port_state}
            }
            ports_info.append(port_info)
        print(ports_info)
        return ports_info
    
    #TODO methods for all the utils, arp spoofing etc...

formatter = Formatter()

class Viewer:

    def view_device_scan_info(self, response):
        for client in response:
            print(f"IP: {client['IP']} \t MAC: {client['MAC']}")

    def view_port_scan_info(self, response):
        for port in response:
            print(f"Port: {port['Port']} \t State: {port['State']}")

viewer = Viewer()


class Exporter:

    def export_device_scan_response(self):
        #TODO: Create an exportation to txt or csv..
        pass

exporter = Exporter()


class Validator:

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