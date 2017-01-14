import subprocess
import os
import time

# Get current SSID of connected wifi (returns blank if not connected)
ssid_get = "iwconfig wlan0 | grep ESSID | awk -F: '{print $2}'"
ssid_bash = str(subprocess.check_output(ssid_get, shell=True))
check_ports = "sudo netstat -plnt"
print(subprocess.check_output(check_ports, shell=True))

try:
    # See if the pi is connected to a wifi network
    ssid = ssid_bash.split('"')[1]
    print('Connected to', ssid)
    time.sleep(10)
    # Start pi-hole docker container with persistent log storage
    subprocess.Popen(
        "bash /home/pirate/pi-zero-master/pihole_persist.sh", shell=True)

except IndexError as e:

    try:
        # Save list of any local wifi SSIDs
        print("scanning local wifi")
        from wifi import Cell, Scheme
        myfi = Cell.all('wlan0')
        cell = [w for w in myfi]
        with open('local_networks.txt', 'w') as ln:
            ln.write(str(cell))
    except Exception as ee:
        print('scanning failed:', ee)
        print(e)
    # If not connected to a network, start broadcasting hotspot
    print("creating hot spot")
    wireless_AP = "sudo ifdown wlan0; sudo create_ap --no-virt -n wlan0 zer0 adzapper && sudo service avahi-daemon restart"
    subprocess.Popen(wireless_AP, shell=True)
    time.sleep(10)
    # Make webpage, to chose from list of local SSIDs and enter password
    # Hash entered credentials to psk
    # Save results as default wifi network, reboot
    subprocess.Popen("cd /home/pirate/pi-zero-master/webAP && python3 gen_drop_down.py", shell=True)
    
    webserver = "cd /home/pirate/pi-zero-master/webAP && sudo python3 webserver.py &> /home/pirate/webServerlog"
    subprocess.Popen(webserver, shell=True)
    # On boot, should pass the SSID test, start pi-hole docker
