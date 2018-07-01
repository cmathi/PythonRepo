fname = input('enter The file name : ')
fhand =open(fname)

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0)+1
lt =list()
for val,key in sorted([(k,v) for v,k in counts.items()],reverse=True)[:10]:
    print(key,val)

biggcount =None
bigword =None
for val,ky in lt:
    if biggcount is None or val>biggcount:
        biggcount = val
        bigword = ky
#print(bigword,biggcount)
