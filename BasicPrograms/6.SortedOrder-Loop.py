#Looping in Sorted order
colors = ['Red','Blue','Yellow','Green']
print('Ascending order')
for color in sorted(colors):
    print(color)

print('Descending order')
for color in sorted(colors,reverse=True):
    print(color)

print('Custom order')
for color in sorted(colors,key=len):
    print(color)
