from http.server import BaseHTTPRequestHandler, HTTPServer
import os
from os import curdir, sep
import cgi
import sys
import pendulum
import subprocess
PORT_NUMBER = 80
z = open('web_log', 'a')
print("**********")
sys.stdout = z
print((pendulum.now('US/Pacific-New').ctime()))


#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        if self.path == "/":
            self.path = "/app.html"
        mimetype = "text/html"
        sendReply = True
        #Open the static file requested and send it
        try:
            f = open(curdir + sep + self.path)
            self.send_response(200)
            self.send_header('Content-type', mimetype)
            self.end_headers()
            self.wfile.write("<p>You accessed path: %s</p>" % f.read())
            f.close()
        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)
            return

#Handler for the POST requests

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
            server.socket.close()

        def reconnect(self):
            psk = os.system('wpa_passphrase myssid my_very_secret_passphrase')

            with open('interfaces-wlan0', 'w') as wifiCreds:
                # /etc/network/interfaces.d/wlan0
                wifiCreds.write('\n'.join([
                    'allow-hotplug wlan0', 'auto wlan0',
                    'iface wlan0 inet dhcp', 'wpa-ssid ' + self.network,
                    'wpa-psk ' + psk
                ]))

try:
    #Create a web server and define the handler to manage the
    #incoming request
    host = str(
        subprocess.check_output(
            "ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\\n/' | grep 192",
            shell=True))[2:-3]

    #host = '192.168.12.1'
    #print os.environ.keys()
    #host = os.environ['WLAN_ADDR']
    server = HTTPServer((host, PORT_NUMBER), myHandler)
    print(('Started httpserver on port ', host, PORT_NUMBER))
    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
