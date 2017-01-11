import subprocess
from time import sleep
import shlex


def run_serial(commandList):
    if len(commandList) == 1:
        command = commandList[0]
        print(command)
    else:
        command = "; ".join(commandList)
    print(command)
    try:
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print(e)
    print()


if len(str(subprocess.check_output(ssid, shell=True)).split('"')[1]) > 0:
    ssid = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
    subprocess.call("cd ~ && bash pihole_persist.sh")
else:
    os.chdir('~/')
    wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper"]
    webServer = ['sudo python3 webserver.py']
    actionItems = [run_serial(wireless_AP), run_serial(webServer)]


