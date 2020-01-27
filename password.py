passwordFile= open('secretFile.txt')
secPass = passwordFile.read()
print('Enter password=')
typedPassword=input()
if typedPassword == secPass:
    print('Access Granted')
    if typedPassword == '12345':
        print('That password is not recommended')
else:
    print('Access Denied')
