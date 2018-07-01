astr = input('Enter a number : ')
try :
    print('Hello') #Not a dangerous line, can use outside try block
    istr =int(astr)#Dangerous line
except :
    istr = -1
if istr >0 :
    print('Number is',istr)
else:
    print('Not a number')
