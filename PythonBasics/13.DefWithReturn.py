def city(pincode):
    if pincode ==21:
        return 'Wanarpet'
    elif pincode == 81:
        return 'Tondiarpet'
    elif pincode ==17:
        return 'TNagar'
    else :
        return 'Area not listed'

area = city(int(input('Enter the last two digitsof pincode : ')))
print(area)
