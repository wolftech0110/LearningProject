---
Tag: HomeLab
---
[README](../README.md)

---
## Home Lab Steps I have taken
- [x] Install ProxMox
- [x] Setup a Windows 10 Virtual Machine
- [x] Setup a Windows Server Virtual Machine
- [x] Setup a Linux Virtual Machine
- [ ] Look Into ProxMox networking
	- [ ] make a bridge connection, one to internet and one isolated
	- [ ] put a kali VM and a vulnerable machine on isolated network and make sure it cannot connect to the internet
- [ ] make a Web Server


- [ ] use below after grace period to reset evaluation days
```
slmgr -rearm
```
- [ ] How to install a web server feature via PowerShell
```
Install-WindowsFeature -name Web-Server -IncludeManagementTools
```

### How to Setup Pfsense for an AD environment 
 - turn on DNS resolver as well as -   Configure the DHCP service
    -   On the right top corner select “Tools” -> “DHCP”
    -   In the DHCP menu select IPv4 and click the “Actions” menu -> “New Scope”
    -   Click through the wizard and select a name (e.g. “BCS Lab”)
    -   Assign the IP range from 10.10.10.100 to 10.10.10.254 and Subnet mask Length “24”
    -   Click next until “Configure DHCP Options” and click “Yes”
    -   When prompted for the Router IP add the pfSense IP address (10.10.10.1 in our case)
    -   Click next and finish out the installer.
-   Add a DNS Forwarder pointing to pfSense
    -   On the right top corner select “Tools” -> “DNS”
    -   Under “DNS” right click on your workstation and select “Properties”
    -   In the new window open the “Forwarders” tab. Here you can add add a DNS forwarder, which is the server(s) that this system is using to resolve DNS queries.
    -   For default settings you can add the “pfSense” Firewall (10.10.10.1). Additionally, you can add another public facing server as a backup such as Quad9 (9.9.9.9)
    -   Save settings and close the window.

```