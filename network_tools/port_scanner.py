import socket
import os
import sys
from pyfiglet import Figlet

def port_scanner():
    title()
    print('Please enter target IP')
    target = input('Target: ')
    target = target.strip()
    while True:
        try:
            print('1) Broad Scan')
            print('2) Single Scan')
            choice = input()
            if choice == '1':
                clear_console()
                broad_scan(target)
                break
            elif choice == '2':
                clear_console()
                single_scan(target)
                break
        except:
            clear_console()
            sys.exit(f'\nSee you soon!')
        else:
            clear_console()
            pass
    
def broad_scan(target):
    title()
    count = 0
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    print(f'*Scanning for open ports @{target}*')
    for port in range(1,1000000):
        try:
            s.connect((target, port))
            print(f'Port {port} is open')
            count += 1
        except:
            pass 
    
    print(f'Scan complete. {count} port/s open.')

def single_scan(target):
    title()
    count = 0
    print('Which port would you like to scan?')
    port = int(input('Port: ').strip())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((target, port))
        print(f'Port {port} is open')
        count += 1
    except:
        print(f'Port {port} is closed')

    print(f'Scan complete. {count} port/s open.')

def title():
    title = (Figlet(font='rectangles'))
    title = title.renderText('Port Scanner v 1.0')
    print(title)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
