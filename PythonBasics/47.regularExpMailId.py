import re

line = 'my mail is cmathi1892@gmail.com and u can call me as Mathi'
mail = re.search('\S+@\S+',line)
print(mail)
