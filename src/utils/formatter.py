

class Formatter:

    def format_device_scan_response(self, response):
        clients_info = []
        for client in response:
            client_info = {
                "IP": client.ip,
                "MAC": client.mac
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
                "Port": port.port,
                "State": port_state
            }
            ports_info.append(port_info)
        return ports_info

formatter = Formatter()