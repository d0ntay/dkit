import nmap
from pyfiglet import Figlet

def active_hosts():
    banner()
    print("Please enter ipv4 address followed by subnet in cidr format")
    print("example : 192.168.1.26/24")
    target = input('>')
    nm = nmap.PortScanner()
    nm.scan(hosts=target, arguments='-sn')
    for host in nm.all_hosts():
        print(f'Host : {host}')

def banner():
    title = (Figlet(font='rectangles'))
    title = title.renderText('Active Hosts v 1.0')
    print(title)
