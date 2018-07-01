fhand = open('C:\\Users\\mathivanan.chelladur\\Desktop\\reflex_iOS.txt')
for line in fhand :
    if line.startswith('"No internet') :
        print(line)
