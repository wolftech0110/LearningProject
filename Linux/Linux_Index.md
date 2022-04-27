---
Tags: Linux
---

[README](../README.md)

---

- Configure Bash Shell to have shortened path name. This can be done by editing the .bashrc file  
- #TODO refine this content
```
#edit similiar line below with this content.
if [ "$color_prompt" = yes ]; then
    PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ '
else
    PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w\$ '
fi
unset color_prompt force_color_prompt

# If this is an xterm set the title to user@host:dir
case "$TERM" in
xterm*|rxvt*)
    PS1="\[\e]0;${debian_chroot:+($debian_chroot)}\u@\h: \w\a\]$PS1"
    ;;
*)
    ;;
esac
```
- How to install debian files manually
```
 sudo dpkg -i package_file.deb
```
-  mounting a drive
```
sudo mount  //X.X.X.X/MyStuff2021 /home/useer/folder -o username=user,file_mode=0777,dir_mode=0777

```