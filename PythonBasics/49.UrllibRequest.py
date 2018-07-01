import urllib.request, urllib.parse, urllib.error
fhand = urllib.request.urlopen('http://10.100.102.75/retail-POC/lottelatest/index.php?c=LOTTE')
for line in fhand :
    print(line.decode().strip())
