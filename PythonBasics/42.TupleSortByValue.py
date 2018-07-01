c= {'a':4,'b':2,'c':3}

lt = list()
for k,v in c.items() :
    lt.append((v,k))
print(lt)
lt = sorted(lt,reverse=True)
print(lt)
