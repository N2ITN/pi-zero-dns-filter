echo “Starting piholeAP service”
echo date
export IP=$(ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\n/' | grep 192)
cd /home/pirate//pi-zero-master/webAP/ && sudo python3 web_AP.py
