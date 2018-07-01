fhand = open('C:\\Users\\mathivanan.chelladur\\Desktop\\reflex_iOS.txt')
for line in fhand :
    line=line.rstrip()# remove spaces at right hand side
    if not line.startswith('"No internet') :
        continue
    print(line)
