import json
input = '''[
{  "id" : "001",
    "x" : "2",
    "name" : "Mathi"
},{ "id" : "002",
    "x" : "7",
    "name" : "Mathis"
}
]
'''# [] ->List of two items
info =json.loads(input)
print(len(info))
for item in info: #item -> Dictionary
    print('ID',item['id'])
    print('Name',item['name'])
    print('Attribute',item['x'])
