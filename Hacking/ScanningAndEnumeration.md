---
Tags: 
date: 06-21-2022
---

[Hacking](./Hacking.md)

---

- Step one was installing Kioptrix, a vulnerable virtual Machine to scan and enumerate using kali tools.
	- https://drive.google.com/drive/folders/1z923e0icfJADbhgS0Qfaxuez-GJTWvjt
- step two is to run arp-scan -l   to find IP address of kioptrix machine, also can try netdiscover 192.168.0.0/24
- *(need to look up how to  make Virtual Machines(VMS) be on an isolated network and not accessible to the internet via the NAT network connection *) john TwoCows2
- now we are going to use NMAP using Stealth Scan
	- nmap -sS 192.168.0.x
	- nmap -T4 -p- -A 192.168.0.x  ALL ports
	- nmap -T4  -A 192.168.0.x       common ports
- Once we get open ports back , we look at the results and then look up vulnerabilities for the open ports and reported software it returns
- take notes about what you find , such as errors with additional information or web pages that return extra information such as server or platform version numbers
### For scanning directories
- nikto -h https://192.168.0.x
- dirbuster&   starts  it in background


---
## Customer released notes
- Default webpage discloses extra server information
- Information Disclosure - on the 404 page
- Information Disclosure - server headers disclose version information 
- mod_ssl/2.8.4 vulnerable to CVE-2002-0082,OSVDB-756
	- https://www.exploit-db.com/exploits/764 - may not work 
	- https://github.com/heltonWernik/OpenLuck
- webalizer version 2.01 - http://10.0.2.15/usage/usage_200909.html
- has Samba 2.2.1a
	- https://www.rapid7.com/db/modules/exploit/linux/samba/trans2open/
	- https://www.exploit-db.com/exploits/7
	- 
- using smbclient -L \\\\10.0.2.15\\

 ```
Sharename       Type      Comment
        ---------       ----      -------
        IPC$            IPC       IPC Service (Samba Server)
        ADMIN$          IPC       IPC Service (Samba Server)
Reconnecting with SMB1 for workgroup listing.
Server does not support EXTENDED_SECURITY  but 'client use spnego = yes' and 'client ntlmv2 auth = yes' is set
Anonymous login successful

        Server               Comment
        ---------            -------
        KIOPTRIX             Samba Server

        Workgroup            Master
        ---------            -------
        MYGROUP              KIOPTRIX


```
 - attempted to use 
	 - ssh 10.0.2.15 -oKexAlgorithms=+diffie-hellman-group1-sha1 -c aes128-cbc
	- and it did not return anything useful (maybe wrong VM version different from guide)

## Researching Vulnerabilities
*Add Screenshots pointing to  interesting information*
- mod_ssl/2.8.4 vulnerable to CVE-2002-0082,OSVDB-756
	- https://www.exploit-db.com/exploits/764 - may not work 
	- https://github.com/heltonWernik/OpenLuck
- has Samba 2.2.1a
	- https://www.rapid7.com/db/modules/exploit/linux/samba/trans2open/
	- https://www.exploit-db.com/exploits/7
- searchsploit openssh 2.9