import subprocess 
from time import sleep
import shlex


def run_serial(commandList):
    if len(commandList) == 1:
        command = commandList[0]
        print (command)
    else: 
        command = "; ".join(commandList)
    print (command)
    try:
        subprocess.Popen(command,shell=True)
    except Exception as e:
        print (e)
    print ()

def terminus():
    print ('terminating processes')    
    for x in [ap, fnds,ws]:
        try:
            x.terminate()
        except Exception as e:
            print (e)
    run_serial(restoreConf)
    run_serial(envReset)

try:
    wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper" ]
    wlan0 = ["export WLAN_ADDR=`ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\\n/' | grep 192`"]
    webServer = ['sudo netstat -plnt','sudo python3 webserver.py']
    fakeDNS = ["sudo pkill dnsmasq", "cd /home/pirate/fakedns && python3 fakedns.py $WLAN_ADDR"]


    ## need to understand this part better, its the reason everything is fucked up
    '''
    'touch ~/zer0/resolv.conf && echo "nameserver $WLAN_ADDR" >> ~/zer0/resolv.conf && chmod 644 ~/zer0/resolv.conf',
    'sudo mv resolv.conf /etc/resolv.conf', 'touch ~/zer0/dnsmasq.hosts && echo "$WLAN_ADDR ad-zero.io" >> ~/zer0/dnsmasq.hosts && chmod 644 ~/zer0/dnsmasq.hosts',
    'sudo mv dnsmasq.hosts /etc/dnsmasq.hosts']
    '''

    
    ## part of the above confusion
    '''
    envReset = ['touch ~/zer0/resolv.conf && chmod 644 ~/zer0/resolv.conf', 'sudo mv resolv.conf /etc/resolv.conf', 
    'touch ~/zer0/dnsmasq.hosts && chmod 644 ~/zer0/dnsmasq.hosts','sudo mv dnsmasq.hosts /etc/dnsmasq.hosts']
    '''
    ap = run_serial(wireless_AP)
    sleep(7)
    ''' env = run_serial(envConf) '''
    wl = run_serial(wlan0)    
    ws = run_serial(webServer)
    fdns = run_serial(fakeDNS)

except Exception as e:
    if isinstance(e, KeyboardInterrupt):
        print ("KeyboardInterrupt")
        terminus()
        print (ws), print (type(ws))
    else: 
        "Error"
        print (e)
        terminus()



    

    
