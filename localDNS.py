import socket
import subprocess

local_url = "ad-zero.login"
print local_url 
def resolve(name):
    if name == local_url:
        print 'DNS query incoming'
        return '192.168.12.1:8080' 
        #        subprocess.check_output(" ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\\n/' | grep 192",shell=True).split('\n')[0]+':8080'
        
    else :
        # you ought to add some basic checking of name here
        return socket.gethostbyname(name)

host = ''
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while 1:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        bits = data.split(":")
        if bits[0] == 'h':
            client.send(resolve(bits[1]))
    client.close()