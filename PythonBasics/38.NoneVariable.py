smallest = None
print('before')
for num in (9,41,12,3,74,15) :
    if smallest is None :
        smallest = num
    elif smallest > num :
        smallest = num
    print(smallest,num)
print('After',smallest)
