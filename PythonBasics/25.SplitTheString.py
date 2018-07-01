fhand = open('C:\\Users\\mathivanan.chelladur\\Desktop\\reflex_IOS.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('"No inrternet'):
        continue
    oneLine = line.split()
    splittedLine = oneLine[1]
    removeInternet = splittedLine.split('r') # Split the word 'internet' by r
    print(removeInternet)
