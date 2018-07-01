fhand = open('C:\\Users\\mathivanan.chelladur\\Desktop\\reflex_iOS.txt')
for line in fhand :
    line = line.rstrip()
    if 'No inrternet' in line:
        print(line)
