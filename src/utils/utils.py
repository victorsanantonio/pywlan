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
    #TODO methods for all the utils, arp spoofing etc...

formatter = Formatter()

class Viewer:

    def view_device_scan_response(self, response):
        for client in response:
            print(f"IP: {client['IP']} \t MAC: {client['MAC']}")

viewer = Viewer()


class Exporter:

    def export_device_scan_response(self):
        #TODO: Create an exportation to txt or csv..
        pass

exporter = Exporter()


class Validator:

    def validate_ip_range(self, ip_range):
        regex = re.compile(r"(?<![-\.\d])(?:0{0,2}?[0-9]\.|1\d?\d?\.|2[0-5]?[0-5]?\.){3}(?:0{0,2}?[0-9]|1\d?\d?|2[0-5]?[0-5]?)(?![\.\d])")
        return regex.match(ip_range)

validator = Validator()