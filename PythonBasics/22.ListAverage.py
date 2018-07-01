numList = list()
while True :
    inp = input('Enter the number : ')
    if inp == 'done':
        break
    value = float(inp)
    numList.append(value) # add a value to the list

average = sum(numList)/len(numList)
print(average)
