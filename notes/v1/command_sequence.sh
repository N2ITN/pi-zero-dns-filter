
# Get libraries
docker pull diginc/pi-hole:arm
cd ~
git clone https://github.com/N2ITN/pi-zero-accesspoint-adblocker.git pi-zero-master
git clone https://github.com/N2ITN/create_ap.git


# Update system
sudo aptitude update
sudo aptitude upgrade -y

''' sudo  dpkg-reconfigure tzdata  ## america/los angeles'''
# Install access point dependencies
sudo aptitude install ntp util-linux procps hostapd iproute2 iw haveged make dnsmasq iptables -y
# Python dependencies
sudo aptitude install python3 python3-pip -y
sudo pip3 install wifi
sudo pip3 install pendulum

# Install access point
cd ~/create_ap
sudo make install

cd ~

# Add directory structure for pihole persistence
cd /home/pirate/
sudo mkdir mnt
sudo mkdir mnt/etc/
sudo mkdir mnt/log/
sudo mkdir mnt/html
sudo chmod 755 mnt/html
sudo touch mnt/log/pihole.log
sudo chmod 755  mnt/log/pihole.log

# Add auto config service
sudo mv pi-zero-master/etc/init.d/piholeAP /etc/init.d/piholeAP
sudo update-rc.d piholeAP defaults



# In case of git
git config --global user.name "N2ITN"
git config --global push.default simple
git config --global user.email "z@aracel.io"