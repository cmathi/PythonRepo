import xml.etree.ElementTree as ET
input = '''<stuff>
                <users>
                    <user x = "2">
                        <id>001</id>
                        <name>Mathis</name>
                    </user>
                    <user x="7">
                        <id>002</id>
                        <name>Math</name>
                    </user>
                </users>
            </stuff>'''

stuff = ET.fromstring(input)
lt = stuff.findall('users/user') # Find all the user tags inside the users tag
print('User Count : ',len(lt))
for item in lt :
    print('Name',item.find('name').text)
    print('Id',item.find('id').text)
    print('Attribute',item.get("x"))
