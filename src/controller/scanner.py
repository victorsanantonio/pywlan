import scapy.all as scapy
from src.models.client import Client

class Scanner:

    def __init__(self, timeout):
        self.timeout = timeout

    def get_ip(self, ip):
        return scapy.ARP(pdst=ip)

    def get_mac(self, mac):
        return scapy.Ether(dst=mac)
    
    def create_packet(self, arp, ether):
        return ether / arp
    
    def send_packet(self, packet, timeout):
        return scapy.srp(packet, timeout=timeout)[0]


class DeviceScanner(Scanner):

    def __init__(self, ip_range):
        super().__init__(timeout = 20)
        self.ip_range = ip_range
        self.mac = "ff:ff:ff:ff:ff:ff"

    def scan(self):
        packet = super().create_packet(super().get_ip(self.ip_range), super().get_mac(self.mac))
        response = super().send_packet(packet, self.timeout)
        clients = []
        for sent, received in response:
            clients.append(Client(received.psrc, received.hwsrc))
        return clients


class PortScanner(Scanner):
    pass