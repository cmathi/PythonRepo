import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('localhost',8080))
cmd = 'GET http://10.100.102.75/retail-POC/lottelatest/index.php?c=LOTTE '.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data)<1):
        break
    print(data.decode())
mysock.close()
