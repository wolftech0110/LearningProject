---
Tags: MetaSploit
date: 06-14-2022
---

[Hacking](./Hacking.md)

---

- These are commands for Metasploit
```
msfconsole  'is the executable to run metasploit'
setg RHOST 192.168.1.1
set RHOST X.X.X.X
search type:auxiliary telnet
search apache
show payloads
use exploit
unset PAYLOAD
unsetg RHOST 192.168.1.1
exploit
```

## Commands and payloads used
- used tcp/portscanner in order to find ports open on an remote host machine
- learned that i could also use NMAP at the Metasploit command line as well