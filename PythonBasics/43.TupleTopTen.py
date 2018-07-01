fhand = open('C:\\Users\\mathivanan.chelladur\\Desktop\\reflex_iOS.txt')

counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] =counts.get(word,0)+1

lt =list()
for k,v in counts.items():
    lt.append((v,k))

lt = sorted(lt,reverse = True)

for v,k in lt[:5]:
    print (v,k)
