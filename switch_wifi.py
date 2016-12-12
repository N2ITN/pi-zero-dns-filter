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
    os.system('sudo pkill create_ap')
    os.system('sudo ifconfig wlan0 down')
    os.system('sudo ifconfig wlan0 up')
    print 'after wlan0 reset:'
    print subprocess.check_output('ifconfig wlan0', shell=True)
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
            time.sleep(7)            
            print 'after attempting reconnect:'
            print subprocess.check_output('ifconfig wlan0', shell=True)
            print 'connected, starting adblock service'
            os.system('cp start_adblock startAP.sh')
            os.system('./pihole.sh')
        except Exception as e:
            print e
            print 'something went wrong, rebooting web server'
            os.system('cp start_webserver startAP.sh')
            os.system('sudo ifconfig wlan0 down')
            os.system('sudo ifconfig wlan0 up')
            os.system('./startAP.sh')
    except Exception as e:
        print e
except Exception as e:
    print e
print 'closing script'
f.close()     
exit()
