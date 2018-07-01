print ('Percentage of entered value : ',float(input('Type an interger value : '))/100)

i = input('Type an interger value : ')
print ('Type of entered value is ',type(i))
f = float(i)
print('After conversion',f)
print ('Type after conversion',type(f))
input('Press enter')

print('Calculation output : ',1+2*float(3)/4 - 5)

sval = input('Type an integer : ')
print('Type of entered value is ',type(sval))
try:
    print('Add with 1',int(sval)+1)
except :
    print('Not a integer')
input('Press enter')
sval2 = 'Hello'
print('Trying to Convert from string to integer')
int(sval2)
