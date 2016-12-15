#!/usr/bin/python
import os 
import sys
import pendulum
import time
import subprocess
os.chdir('/home/pirate/zer0')
f = file('wifi_log','a')
sys.stdout = f
print '********'
print pendulum.now('US/Pacific-New').ctime()
def get_creds():
    with open('credentials.txt','r') as creds:
        return creds.readline().split()
try:
    print 'original wlan0 state:'
    print subprocess.check_output('ifconfig wlan0', shell=True)
    os.system('sudo pkill create_ap &&  sleep 5')
    os.system('sudo ifconfig wlan0 down')
    os.system('sudo ifconfig wlan0 up')
    print 'after wlan0 reset:'
    print subprocess.check_output('ifconfig wlan0', shell=True)
    from wifi import Cell, Scheme
    try:
        network, passkey = get_creds()
    except Exception as e:
        print e
        print 'starting webserver'
        os.system('sudo python webserver.py')
    myfi = Cell.all('wlan0')
    cell = [w for w in myfi if w.ssid==network]
    print 'trying:', network
    try:
        if len(cell) > 0:
            print 'found a match'
        else: print 'no matching network found'
        scheme = Scheme.for_cell('wlan0', 'myNetwork', cell[0], passkey)
        try:
            scheme.save()
        except Exception as e:
            print e
            print 'matching scheme'
            scheme = Scheme.find('wlan0', 'myNetwork')
        try:
            print 'activating network'
            scheme.activate()
            time.sleep(7)            
            print 'after attempting reconnect:'
            print subprocess.check_output('ifconfig wlan0', shell=True)
        except Exception as e:
            print e
            print 'something went wrong, rebooting web server'
            os.system('sudo ifconfig wlan0 down')
            os.system('sudo ifconfig wlan0 up')
            os.system('sudo python webserver.py')
    except Exception as e:
        print e
except Exception as e:
    print e
print 'closing script'
f.close()     

#poop