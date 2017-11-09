# pi-zero-dns-filter
This is a local DNS proxy designed for filtering adware and malicious websites from a local network. It is built to run on a raspberry pi zero.

## Easy configuration
The software uses bash scripts, auto-generated html and cron jobs to provide a wireless hotspot utility. Once the device is powered up, the user can connect to the rapsberry pi and is guided through setting their router's preferred DNS to the device's local IP address.
## Secure, fast internet
Once set up, the device automatically starts up the popular "pi-hole" ad/malware filtering package inside of a docker container.
This package filters requests to unwanted domains before they are initiated to provide a faster, less intrusive, and more secure internet experience. The device will work for any computer, tablet, or cell phone connected to the local network via wifi or ethernet.
