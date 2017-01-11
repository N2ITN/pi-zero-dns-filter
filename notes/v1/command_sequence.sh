
# Get libraries
docker pull diginc/pi-hole:arm
cd ~
# git clone https://github.com/N2ITN/pi-zero-accesspoint-adblocker.git zer0
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
sudo aptitude install python3 -y
sudo aptitude install python3-pip -y
sudo pip3 install wifi
sudo pip3 install pendulum
# Add startup script command
> rc.local
echo "cd ~/zer0" >> rc.local
echo "git pull" >> rc.local
echo "sudo bash startup.sh &" >> rc.local
echo "exit 0" >> rc.local
sed -i "1i #!/bin/bash"  rc.local
chmod 755 rc.local
sudo mv rc.local /etc/rc.local


cd ~ && git clone https://github.com/pathes/fakedns.git


# Serve portainer container viewer from localhost if SSH session is started
echo "docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock --name furiosa portainer/portainer:arm > error_catcher.s 2> /dev/null" >> ~/.profile 
echo "docker start furiosa" >> ~/.profile
echo "cd zer0" >> ~/.profile


# In case of git
git config --global user.name "N2ITN"
git config --global push.default simple
git config --global user.email "z@aracel.io"