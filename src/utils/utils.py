

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

class Viewer:

    def view_device_scan_response(self, response):
        for client in response:
            print(f"\n IP: {client['IP']} \t MAC: {client['MAC']}")


class Exporter:

    def export_device_scan_response(self):
        #TODO: Create an exportation to txt or csv..
        pass