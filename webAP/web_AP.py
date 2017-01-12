import subprocess
import os
import time

ssid_get = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
ssid_bash = str(subprocess.check_output(ssid_get, shell=True))

try:
    ssid = ssid_bash.split('"')[1]
    if not os.path.exists("/home/pirate/mnt"):
        subprocess.call("mk_dirs.sh", shell=True)
    subprocess.Popen("bash ~/pi-zero-master/pihole_persist.sh", shell=True)

except IndexError:
    wireless_AP = "sudo create_ap -n wlan0 zer0 adzapper"
    webServer = "sudo python3 /home/pirate/pi-zero-master/webAP/webserver.py &> webServerlog"
    subprocess.Popen(wireless_AP, shell=True)
    time.sleep(10)
    subprocess.Popen(webServer, shell=True)
