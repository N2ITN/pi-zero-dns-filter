docker stop pihole
docker rm pihole
IMAGE='diginc/pi-hole:arm'
NIC='wlan0'
IP=$(ip addr show $NIC | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
echo $IP
sudo service dnsmasq stop
docker run -v /home/pirate/mnt/log/pihole.log:/var/log/pihole.log -v /home/pirate/mnt/etc/:/etc/pihole/ -v ~/mnt/html/pihole:/var/www/html/pihole -p 53:53/tcp -p 53:53/udp -p 80:80 --cap-add=NET_ADMIN -e ServerIP="$IP" --name pihole -d $IMAGE

# Recommended auto ad list updates & log rotation:
wget -O- https://raw.githubusercontent.com/diginc/docker-pi-hole/master/docker-pi-hole.cron | sudo tee /etc/cron.d/docker-pi-hole


