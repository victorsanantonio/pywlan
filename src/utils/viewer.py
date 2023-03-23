

class Viewer:

    def view_device_scan_info(self, response):
        for client in response:
            print(f"IP: {client['IP']} \t MAC: {client['MAC']}")

    def view_port_scan_info(self, response):
        for port in response:
            print(f"Port: {port['Port']} \t State: {port['State']}")

viewer = Viewer()