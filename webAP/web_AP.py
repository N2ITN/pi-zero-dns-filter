import subprocess
import os
import time

ssid_get = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
ssid_bash = str(subprocess.check_output(ssid_get, shell=True))

try:
    ssid = ssid_bash.split('"')[1]
    print('Connected to', ssid)
    if not os.path.exists("/home/pirate/mnt"):
        subprocess.call("mk_dirs.sh", shell=True)
    subprocess.Popen("bash ~/pi-zero-master/pihole_persist.sh", shell=True)

except IndexError as e:
    print(e)
    print("creating hot spot")
    wireless_AP = "sudo create_ap --no-virt -n wlan0 zer0 adzapper && sudo service avahi-daemon restart"
    subprocess.Popen(wireless_AP, shell=True)
    time.sleep(10)
    check_ports = "sudo netstat -plnt"
    print(subprocess.check_call(check_ports, shell=True))
    webserver = "sudo python3 /home/pirate/pi-zero-master/webAP/webserver.py &> ~/webServerlog"
    subprocess.Popen(webserver, shell=True)
