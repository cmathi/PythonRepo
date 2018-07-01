import json
import urllib.request,urllib.parse,urllib.error


apiurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

while True :
    address = input('Enter address : ')
    if len(address) < 1 : break
    url = apiurl + urllib.parse.urlencode({'address':address})
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    try :
        js = json.loads(data)
    except :
        js = None
    if not js or 'status' not in js or js['status'] != 'OK':
        print('===Failed to retrieve===')
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("Latitude :",lat,"Longitude :",lng)
    loc = js["results"][0]['formatted_address']
    print(loc)
