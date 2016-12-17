import subprocess 
from time import sleep


# def run_parallel(commands):
# run in parallel
    # processes = [subprocess.Popen(cmd, shell=True) for cmd in commands]

def run_serial(commandList):
    if len(commandList) == 1:
        command = commandList[0]
    else: 
        command = "; ".join(commandList)
    print (command)
    process = subprocess.Popen(command, stdout=subprocess.PIPE,shell=True)
    # proc_stdout = process.communicate()[0].strip()
    # print (proc_stdout)

wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper"]
envConf = ["sudo pkill dnsmasq", "export WLAN_ADDR=`ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\n/' | grep 192`",
'touch ~/zer0/resolv.conf && echo "nameserver $WLAN_ADDR" >> ~/zer0/resolv.conf && chmod 644 ~/zer0/resolv.conf',
'sudo mv resolv.conf /etc/resolv.conf', 'touch ~/zer0/dnsmasq.hosts && echo "$WLAN_ADDR ad-zero.io" >> ~/zer0/dnsmasq.hosts && chmod 644 ~/zer0/dnsmasq.hosts',
'sudo mv dnsmasq.hosts /etc/dnsmasq.hosts']
fakeDNS = ["cd ~/fakedns && sudo python3 fakedns.py $WLAN_ADDR"]
webServer = ['cd ~/zer0 && sudo python webserver.py']
restoreConf = ['sudo echo -n "" > /etc/dnsmasq.host', 'sudo echo -n "" > /etc/resolv.conf']




try:
    ap = run_serial(wireless_AP)
    sleep(7)
    env = run_serial(envConf)
    fdns = run_serial(fakeDNS)
    ws = run_serial(webServer)

    while ws.poll:
        pass
    ap.terminate()
    fdns.terminate()    
    run_serial(restoreConf)
except KeyboardInterrupt:
    try:
        for x in [ap, fdns, ws]:
            try:
                x.terminate()
            except Exception as e:
                print (e)
    except: 
        exit()
    
