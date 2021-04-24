import requests

def ttt(s):
    print("ttt333>>", s)
    r = requests.get('https://blue.berryservice.net/ipaddress')
    print(r.text)
