import re
fhand = open('C:\\Users\\mathivanan.chelladur\\Desktop\\reflex_IOS.txt')

for line in fhand:
    line = line.rstrip()
    if re.search('^"No.*"',line):
        print(line)
    if re.search('^"No\S*"',line):
        print(line)
