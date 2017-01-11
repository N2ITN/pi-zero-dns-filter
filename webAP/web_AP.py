import subprocess
import os

ssid_get = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
ssid_bash = str(subprocess.check_output(ssid_get, shell=False))
ssid = ssid_bash.split('"')[1]
if len(ssid) > 0:
    if not os.path.exists("/home/pirate/mnt"):
        subprocess.call("mk_dirs.sh", shell=False)
    subprocess.Popen("bash ~/pi-zero-master/pihole_persist.sh", shell=False)
else:
    os.chdir('~/')
    wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper"]
    webServer = ['sudo python3 webserver.py']
    subprocess.Popen('; '.join([wireless_AP, webServer]), shell=False)
