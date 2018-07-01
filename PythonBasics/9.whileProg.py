n=0
while True:
    n=n+1
    print(n)
    print('Who r u')
    un=input()
    if un != 'mathi':
        continue
    print('Hi mathi, Enter ur password')
    pw=input()
    if pw == '2520':
        break
print('Access Granted')
