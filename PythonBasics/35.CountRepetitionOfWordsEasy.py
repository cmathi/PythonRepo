word = dict()
names = ['csv','txt','pdf','pdf','csv','doc','txt','txt','pdf']
for name in names :
    word[name] = word.get(name,0)+1
print(word)
