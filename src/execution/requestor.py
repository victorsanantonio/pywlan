

class Requestor:
    def request_ip_range(self):
        return input("\nEnter an IP range. Example: [192.168.1.1/24]:\t")

    def request_ip(self):
        return input("\nEnter a valid IP. Example: [192.168.1.1]:\t")
    
    def request_start_port(self):
        return input("\nEnter start port:\t")
    
    def request_end_port(self):
        return input("\nEnter end port:\t")

    def request_export_confirmation(self):
        return input("\nDo you want to export the results? (Y/n):\t")
    
requestor = Requestor()