#!/usr/bin/python3
# -*- coding: utf-8 -*-
import nmap
import re
from time import sleep
#def amount of ports and reg ex
ip_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_pattern = re.compile("([0-9]+)-([0-9]+)")
port_min = 0

port_max = 65535
# banner stuff
bred = "\033[1;31m"

banner = f""" {bred}
██████╗ ███████╗██████╗ ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗ 
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗
██║  ██║█████╗  ██║  ██║███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝
██║  ██║██╔══╝  ██║  ██║╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗
██████╔╝███████╗██████╔╝███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║
╚═════╝ ╚══════╝╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
"""
print (banner)
ports = []
#gathering ip and ports to scan
while True:
    IP = input("please supply the IP:   ")
    if ip_pattern.search(IP):
        print (f"{IP} is a valid IP ")
        break

while True:
    print ("please supply the range of ports you want to scan i,e 21-8080")
    port_range = input("please supply the range: ")
    valid_ports = port_pattern.search(port_range.replace(" ",""))
    if valid_ports:
        min_port = int(valid_ports.group(1))
        max_port = int(valid_ports.group(2))
        break

nm = nmap.PortScanner()
for port in range(min_port, max_port + 1):
    try:
        result = nm.scan(IP, str(port))
        print(result)
        port_status = (result['scan'][IP]['tcp'][port]['state'])
        print(f"the port {port} is {port_status}")
    except:
        print(f"couldn't scan port {port}")
