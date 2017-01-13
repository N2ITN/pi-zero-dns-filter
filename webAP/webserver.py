from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from os import curdir, sep
import cgi
import sys
import pendulum
import subprocess
PORT_NUMBER = 80

print("**********")

print((pendulum.now('US/Pacific-New').ctime()))


#This class will handles incoming requests from the browser 
class myHandler(BaseHTTPRequestHandler):

    # Load main page from *.local
    def do_GET(self):
        self.path = "app.html"
        p = os.getcwd() + sep + self.path
        f = open(p, 'rb')
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f.read())

    # Handle ssid / password POST from browser
    def do_POST(self):
        if self.path == "/send":
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={
                    'REQUEST_METHOD': 'POST',
                    'CONTENT_TYPE': self.headers['Content-Type'],
                })
            self.send_response(200)
            self.end_headers()
            self.network = form["network"].value
            self.passkey = form["password"].value
            self.reconnect()
            #self.reboot()
            return
            
    # Set wifi defaults
    def reconnect(self):
        call = ' '.join(["(wpa_passphrase", self.network, self.passkey, ')'])
        wpa = str(subprocess.check_output(call, shell=True))

        psk = wpa.split('=')[-1].split("\\")[0]
        with open('interfaces-wlan0', 'w') as wifiCreds:
            wifiCreds.write('\n'.join([
                'allow-hotplug wlan0', 'auto wlan0', 'iface wlan0 inet dhcp',
                'wpa-ssid ' + self.network, 'wpa-psk ' + psk
            ]))
        self.wfile.write(b"Connecting to: " + bytes(self.network, ' utf-8') +
                         b'\n')
        self.wfile.write(b"Rebooting...")
        return

    def reboot(self):
        from time import sleep
        sleep(5)
        print("launch reboot script")
        subprocess.Popen('sudo bash reboot.sh', shell=True)

try:
    #Create a web server and define the handler to manage the
    #incoming request
    host = subprocess.check_output("echo $IP", shell=True).decode('utf-8')[:-1]

    server = HTTPServer((host, PORT_NUMBER), myHandler)
    print(('Started httpserver on port ', host, PORT_NUMBER))
    #Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
