
# Get libraries
docker pull gojira00/pi-hole-2016:arm
cd ~
git clone https://github.com/N2ITN/pi-zero-accesspoint-adblocker.git zer0
git clone https://github.com/N2ITN/create_ap.git


# Update system
sudo aptitude update
sudo aptitude upgrade -y


# Install access point
sudo apt-get install util-linux procps hostapd iproute2 iw haveged make dnsmasq iptables -y
cd ~/create_ap
sudo make install



cd ~/zer0

# pip wifi module
sudo aptitude install python-pip -y
sudo pip install wifi
sudo pip install pendulum
# Add startup script command
> rc.local
echo "cd ~/zer0" >> rc.local
echo "sudo bash startAP.sh" >> rc.local
echo "exit 0" >> rc.local
sed -i "1i #!/bin/bash -e"  rc.local
chmod 755 rc.local
sudo mv rc.local /etc/rc.local


# Serve portainer container viewer from localhost if SSH session is started
echo "docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock --name furiosa portainer/portainer:arm > error_catcher.s 2> /dev/null" >> ~/.profile 
echo "docker start furiosa" >> ~/.profile
echo "cd zero" >> ~/.profile


# In case of git
git config --global user.name "N2ITN"
git config --global push.default simple
git config --global user.email "z@aracel.io"