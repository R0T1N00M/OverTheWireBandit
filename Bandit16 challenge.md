# Bandit15 -> 16 Challenge

**Username:**
<br>
<br>
**bandit15**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXX6tnt**
<br>
<br>

**Task:**
The password for the next level can be retrieved by submitting the password of the current level to port 30001 on localhost using SSL encryption.
Helpful note: Getting “HEARTBEATING” and “Read R BLOCK”? Use -ign_eof and read the “CONNECTED COMMANDS” section in the manpage.
Next to ‘R’ and ‘Q’, the ‘B’ command also works in this version of that command…
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit16.html)

**Solution**
<br>
Do a 'ls -la', and change ports to get password for the next lvl. (Fyi, we are going to use 'openssl' and 's_client')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
openssl s_client -connect localhost:30001
<br>
('openssl' is a general purpose cryptography library that provides an open source and 's_client' is implements a generic SSL/TLS client which connects to a remote host.)

**Step 3:**
<br>
Enter current lvl password after doing Step 2

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
