from scapy import *

def active_hosts():
    hosts = []
    print('Please enter network bits in decimal format. Ex. 192.168.1 ')
    network = input('>')
    ips = [network + '.'+ i for i in range(1,256)]
    hosts = scan(ips)
    for host in hosts:
        print('[*]' + host)

def scan(ips):
    active_hosts = []
    while True:
        print("[*] Scanning...")
    for ip in ips:
        icmp = IP(dst=ip)/ICMP()
        reply = sr1(icmp, timeout=2, verbose=False)
        if reply is not None:
            active_hosts.append(ip)

return active_hosts
