import scapy.all as scapy
from src.models.client import Client
from src.models.port import Port


class Scanner:

    def __init__(self, timeout):
        self.timeout = timeout

    def get_arp(self, value):
        return scapy.ARP(pdst=value)

    def get_ether(self, value):
        return scapy.Ether(dst=value)
    
    def get_ip(self, value):
        return scapy.IP(dst=value)

    def get_tcp(self, port, flag):
        return scapy.TCP(dport=port, flags=flag)

    def create_srp_packet(self, arp, ether):
        return ether / arp
    
    def create_srp1_packet(self, ip, tcp):
        return ip / tcp

    def send_srp_packet(self, packet, timeout):
        return scapy.srp(packet, timeout=timeout)[0]
    
    def send_srp1_packet(self, packet, timeout):
        return scapy.srp1(packet, timeout=timeout)


class DeviceScanner(Scanner):

    def __init__(self, ip_range):
        super().__init__(timeout = 20)
        self.ip_range = ip_range
        self.mac = "ff:ff:ff:ff:ff:ff"

    def scan(self):
        packet = super().create_srp_packet(super().get_arp(self.ip_range), super().get_ether(self.mac))
        response = super().send_srp_packet(packet, self.timeout)
        clients = []
        for sent, received in response:
            clients.append(Client(received.psrc, received.hwsrc))
        return clients


class PortScanner(Scanner):

    def __init__(self, ip, startport, endport):
        super().__init__(timeout = 0.5)
        self.ip = ip
        self.startport = startport
        self.endport = endport
    
    def scan(self):
        ports = []
        for port in range(self.startport, self.endport+1):
            packet = super().create_srp1_packet(super().get_ip(self.ip), super().get_tcp(port, 'S'))
            response = super().send_srp1_packet(packet, self.timeout)
            if response == None:
                ports.append(Port(port, False))
            elif response.haslayer(scapy.TCP) and response.getlayer(scapy.TCP).flags==0x12:
                ports.append(Port(port, True))
        
        return ports

