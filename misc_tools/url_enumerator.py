import requests
from pyfiglet import Figlet

def url_enum():
    title()
    print("Please enter target URL : example.com")
    url = input('URL: ')
    url = "https://" + url
    print("Please enter path to wordlist : /example/path/to/file.txt")
    wordlist = input('Wordlist: ')
    with open(wordlist) as file:
            for line in file:
                line = line.strip()
                r = requests.get(url+'/'+line)
                if r.ok:
                    print(f'(#){url}/{line}')

def title():
    title = (Figlet(font='rectangles'))
    title = title.renderText('Url Enumerator v 1.0')
    print(title)
