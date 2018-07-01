word = dict()
text = input('Enter the text : ')
names = text.split()
print('words are :',names)
for name in names :
    word[name] = word.get(name,0)+1
print(word)
