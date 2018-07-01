import urllib.request, urllib.parse, urllib.error
import json

while True :
    apiurl = input("Enter url : ")
    if len(apiurl)<1 :
        continue
    uh = urllib.request.urlopen(apiurl)
    data = uh.read().decode()
    print(len(data))

    try:
        js = json.loads(data)
    except:
        js =None

    host = js['headers']['host']
    print(host)
