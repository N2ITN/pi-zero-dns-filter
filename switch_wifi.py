#!/usr/bin/python
import os 
import sys
import pendulum
os.chdir('/home/pirate/zer0')
f = file('pyfi_log.txt','w')
sys.stdout = f

print pendulum.now('US/Pacific-New').ctime()
def get_creds():
    with open('credentials.txt','r') as creds:
        return creds.readline().split()
try:
    os.system('sudo ifconfig wlan0 down')
    os.system('sudo ifconfig wlan0 up')
    from wifi import Cell, Scheme
    network, passkey = get_creds()
    myfi = Cell.all('wlan0')
    cell = [w for w in myfi if w.ssid==network]
    print 'got',network, passkey
    try:
        cell = cell[0]  
        print cell
        scheme = Scheme.for_cell('wlan0', 'myNetwork', cell, passkey)
        try:
            scheme.save()
        except Exception as e:
            print e
            print 'finding scheme'
            scheme = Scheme.find('wlan0', 'myNetwork')
        try:
            print 'activating network'
            scheme.activate()

        except Exception as e:
            print e
            os.system('cp start_webserver startAP.sh')
            os.system('sudo ifconfig wlan0 down')
            os.system('sudo ifconfig wlan0 up')
            os.system('sudo bash startAP.sh')
    except Exception as e:
        print e
except Exception as e:
    print e
print 'closing script'
f.close()     
exit()