

# TODO

## replace offical pi-hole img with my clone:
docker pull gojira00/pi-hole-2016:arm

## produce install script that clone from git
change absolute paths in code to my repo

## script replacement of `create_ap/create_ap` with modified file

## try on pi zero

# portainer - monitor containers
`docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock --name furiosa portainer/portainer:arm > error_catcher.s 2> /dev/null`
`docker start furiosa`

# get current IP
 ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\n/' | grep 192


# to see free space: 
`df -k .`
Filesystem     1K-blocks    Used Available Use% Mounted on
/dev/root       14182384 1350704  12206988  10% /

# to see current SSID:
` iwconfig wlan0 | grep ESSID | awk -F: '{print $2}' `


## to see PID using 53: 
`sudo netstat -plnt`

`sudo pkill dnsmasq`

# TODO
# sync with weaved with ssh 
`sudo apt-get install weavedconnectd`

https://www.reddit.com/r/pihole/comments/441k6q/changing_the_blank_image_that_takes_the_place_of/


DNS SETUP:
    /etc/resolve.conf:
    192.168.12.1 ad-zero.net
        note (try 
        export WLAN_ADDR=ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\n/' | grep 192
        )

export WLAN_ADDR=ifconfig wlan0 | grep 'inet addr' | awk '{print $2}' | sed -e 's/:/\n/' | grep 192
touch resolv.conf && echo "$WLAN_ADDR ad-zero.io" >> resolv.conf && chmod 644 resolv.conf



    cd ~/fakedns
    sudo python3 fakedns.py 192.168.1.12   
#### ADD TO COMMANDS     







steps:
    first boot:
        hotspot, web server
        get credentials
        reset wlan0 and reconnect
        change boot script to connect + start pihole
    subsequent boots:
        start script to connect + start pihole
TODO:
    add flexibility for error handling
    if wifi spot is NOT found: revert to first boot 



# note - connect to running docker container
`docker exec -it [container-id] bash`



# Install access point via create_ap
``bash
sudo apt-get install util-linux procps hostapd iproute2 iw iwconfig haveged make dnsmasq iptables
git clone https://github.com/oblique/create_ap
cd create_ap
make install 
``

# to set up:
sudo nano /etc/rc.local
# add:
cd /home/pirate/zer0 && sudo create_ap -n wlan0 zer0 adzapper



sudo echo "cd ~/zer0 && bash startup.sh" >> /etc/rc.local


important ( see https://github.com/oblique/create_ap/issues/78): 



### in `create_ap/create_ap`, starting 1268 on line change:
```
if [[ $DAEMONIZE -eq 1 && $RUNNING_AS_DAEMON -eq 0 ]]; then
    echo "Running as Daemon..."
    # run a detached create_ap
    RUNNING_AS_DAEMON=1 setsid "$0" "${ARGS[@]}" &
    exit 0
fi
```
### to
```
if [[ $DAEMONIZE -eq 1 && $RUNNING_AS_DAEMON -eq 0 ]]; then
    echo "Running as Daemon..."
    # run a detached create_ap
    read SSID
    read PASSPHRASE
    echo -e "$SSID\n$PASSPHRASE" | RUNNING_AS_DAEMON=1 setsid "$0" "${ARGS[@]}" &
    exit 0
fi 
```


