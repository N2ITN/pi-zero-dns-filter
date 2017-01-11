import subprocess
import os

ssid = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
ssid_bash = str(subprocess.check_output(ssid, shell=True))
print(ssid_bash)
if len(ssid_bash.split('"')[1]) > 0:
    if not os.path.exists("~/mnt"):
        subprocess.call("mk_dirs.sh", shell=True)
    subprocess.Popen("bash ~/pi-zero-master/pihole_persist.sh", shell=True)
else:
    os.chdir('~/')
    wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper"]
    webServer = ['sudo python3 webserver.py']
    subprocess.Popen('; '.join([wireless_AP, webServer]), shell=True)
