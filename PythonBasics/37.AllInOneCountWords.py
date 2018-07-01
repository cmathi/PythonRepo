fname = input('Enter the file name')
fhand=open(fname)
counts =dict()
for line in fhand:
    words = line.split()
    #print(words)
    for word in words:
        counts[word]=counts.get(word,0)+1
print(counts)
bigCount =None
bigWord = None
for word,count in counts.items():
    if bigWord is None or count>bigCount:
        bigWord =word
        bigCount = count
print(bigWord,bigCount)
