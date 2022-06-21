---
Tags: 
date: 06-21-2022
---

[Hacking](./Hacking.md)

---

- Step one was installing Kioptrix, a vulnerable virtual Machine to scan and enumerate using kali tools.
	- https://drive.google.com/drive/folders/1z923e0icfJADbhgS0Qfaxuez-GJTWvjt
- step two is to run arp-scan -l   to find IP address of kioptrix machine, also can try netdiscover 192.168.0.0/24
- *(need to look up how to  make Virtual Machines(VMS) be on an isolated network and not accessible to the internet via the NAT network connection *)
- now we are going to use NMAP using Stealth Scan
	- nmap -sS 192.168.0.x
	- nmap -T4 -p- -A 192.168.0.x  ALL ports
	- nmap -T4  -A 192.168.0.x       common ports
- Once we get open ports back , we look at the results and then look up vulnerabilities for the open ports and reported software it returns
- take notes about what you find , such as errors with additional information or web pages that return extra information such as server or platform version numbers

- nikto -h https://192.168.0.x
- 



