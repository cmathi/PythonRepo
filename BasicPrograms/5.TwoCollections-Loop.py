#Looping over two collections
animals= ['Dog','Rabbit','Ox','Deer','Cat']
colors = ['Red','Blue','Yellow','Green']

for animal,color in zip(animals,colors):
    print(animal,'-->',color)
