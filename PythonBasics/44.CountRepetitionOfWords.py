word = dict()
names = ['csv','txt','pdf','pdf','csv','doc','txt','txt','pdf']
for name in names :
    if name not in word :
        word[name] = 1
    else :
        word[name] = word[name]+1
print(word)
