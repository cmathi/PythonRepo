fname = input('Enter the file name : ')
fhand = open(fname)
count =0
for line in fhand :
    if 'internet' in line :
        count = count+1
print('Count of The word "internet" are:',count)
