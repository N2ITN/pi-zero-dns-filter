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


def terminus(items):
    print('terminating processes')
    for x in items:
        try:
            x.terminate()
        except Exception as e:
            print(e)
        # run_serial(restoreConf)
        # run_serial(envReset)


try:
    wireless_AP = ["sudo create_ap -n wlan0 zer0 adzapper"]
    ssid = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
    if len(subprocess.check_output(ssid,shell=True).split('"')[1]) > 0:
        
    webServer = ['sudo netstat -plnt', 'sudo python webserver.py']

    actionItems = [run_serial(wireless_AP), run_serial(webServer)]
    print('exiting on EOF')
    terminus(actionItems)
except Exception as e:
    if isinstance(e, KeyboardInterrupt):
        print("KeyboardInterrupt")
        terminus(actionItems)
        print(ws), print(type(ws))
    else:
        print("Error")
        print(e)
        terminus(actionItems)
