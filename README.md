# pi-zero-dns-filter
This is a local DNS proxy designed for filtering adware and malicious websites from a local network. It is built to run on a raspberry pi zero.

## Features
The software uses bash scripts and cron jobs to provide a wireless hotspot utility so that once powered up, the user can connect to the rapsberry pi and is guieded through setting their routers preferred DNS to the devices local IP address.
Once set up, the devices uses the popular "pi-hole" ad/malware filtering package inside of a docker container to provide a faster, less intrusive and more secure internet experience for any devices connected to their home network.
