import subprocess

ssid = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
if len(str(subprocess.check_output(ssid, shell=True)).split('"')[1]) > 0:
    subprocess.call("cd ~ && bash ~/pihole_persist.sh", shell=True)
else:
    os.chdir('~/')
    wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper"]
    webServer = ['sudo python3 webserver.py']

    subprocess.Popen('; '.join([wireless_AP, webServer]), shell=True)
