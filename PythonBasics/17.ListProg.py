catNames = []
while True :
    print('Enter the name of the cat no '+str(len(catNames)+1)+' or press enter to stop')
    name =input()
    if name == '':
        break
    else:
        catNames = catNames +[name]
print ('The cat names are')
for name in catNames:
    print('   '+name)
