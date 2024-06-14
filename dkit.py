import os
import sys
from pyfiglet import Figlet
from network_tools.active_hosts import active_hosts
from network_tools.port_scanner import port_scanner
from misc_tools.url_enumerator import url_enum

def main():
    tool_select()
#figlet setup
def paste_title():
    title = (Figlet(font='rounded'))
    title = title.renderText('Dkit v 1.0')
    print(title)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#genre selection
def tool_select():
    while True:
        clear_console()
        paste_title()
        try:
            print('Welcome Back')
            print('1) Network')
            print('2) Misc')
            choice = input()
            if choice == '1':
                clear_console()
                network_tools()
                break
            elif choice == '2':
                clear_console()
                misc_tools()
                break
        except:
            clear_console()
            sys.exit(f'\nSee you soon!')
        else:
            clear_console()
            pass


#network tool selection
def network_tools():
    while True:
        paste_title()
        try:
            print('Network tools')
            print('0) Back')
            print('1) Active Hosts')
            print('2) Port Scanner')
            choice = input()
            if choice == '1':
                clear_console()
                active_hosts()
                break
            elif choice == '2':
                clear_console()
                port_scanner()
                break
            elif choice == '0':
                clear_console()
                tool_select()
                break
        except:
            clear_console()
            sys.exit('GoodBye')
        else:
            clear_console()
            pass

#misc tool selection
def misc_tools():
    while True:
        paste_title()
        try:
            print('Miscellaneous tools')
            print('0) Back')
            print('1) URL Enumerator')
            choice = input()
            if choice == '1':
                clear_console()
                url_enum()
                break
            elif choice == '0':
                clear_console()
                tool_select()
                break
        except:
            clear_console()
            sys.exit('GoodBye')
        else:
            clear_console()
            pass

if __name__ == "__main__":
    main()
