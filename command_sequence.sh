git clone https://github.com/N2ITN/pi-zero-accesspoint-adblocker.git zer0
cd zer0
docker pull gojira00/pi-hole-2016:arm

echo "docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock --name furiosa portainer/portainer:arm > error_catcher.s 2> /dev/null" >> ~/.profile 
echo "docker start furiosa" >> ~/.profile

sudo apt-get update
sudo aptitude upgrade -y
sudo apt-get install util-linux procps hostapd iproute2 iw haveged make dnsmasq iptables -y

# In case of git
git config --global push.default simple
git config --global user.email "z@aracel.io"
git config --global user.name "N2ITN"