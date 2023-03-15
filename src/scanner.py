import scapy.all as scapy
from time import time


class Scanner:
    """
    A class to compile ARP scanner main functions

    ...

    Methods
    -------
    get_request()
        Description
    """
    def get_request(self):
        request = scapy.ARP()


class DeviceScanner(Scanner):
    def scan(self, ip):
         """
        Parameters
        ----------
        ip : str
            ip code to be scanned
        """
        scapy.arping(ip)


class PortScanner(Scanner):
    pass