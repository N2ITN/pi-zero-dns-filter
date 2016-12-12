sudo netstat -plnt
sudo pkill dnsmasq
docker rm pihole
IMAGE='gojira00/pi-hole-2016:arm'
NIC='wlan0'
IP=$(ip addr show $NIC | grep "inet\b" | awk '{print $2}' | cut -d/ -f1)
docker run  -p 53:53/tcp -p 53:53/udp -p 80:80 --cap-add=NET_ADMIN -e ServerIP="$IP" --name pihole -d $IMAGE
