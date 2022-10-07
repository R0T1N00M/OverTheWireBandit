# Bandit24 -> 25 Challenge

**Username:**
<br>
<br>
**bandit24**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXGGar**
<br>
<br>

**Task:**
A daemon is listening on port 30002 and will give you the password for bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode. 
There is no way to retrieve the pincode except by going through all of the 10000 combinations, called brute-forcing.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit25.html)

**Solution**
<br>
Connect to localhost 30002, and get the password by making a script to brute force your way through. (Fyi, we're going to use 'nano', 'nc', and 'piping')             

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
mktemp -d
<br>
('mktemp -d' makes a Temporary Directory, example: '/tmp/tmp.DuzEylipfd')

**Step 3:**
<br>
cd /tmp/tmp."Temporary Directory"
<br>
("Temporary Directory" is from 'mktemp -d')

**Step 4:**
<br>
nano 'whatever name you want of the file'.sh
<br>
('nano' is  a  small  and friendly editor. 'whatever name you want of the file' means name it however you like with a '.sh' at the end.)

**Step 5:**
<br>
#!/bin/bash

for i in {0000..9999}
<br>
do
<br>
        _echo XXXXXXXXXXXXXXXXXXXXXXXXXXXGGar $i >> possibilities.txt
<br>
done
<br>
(Do this after getting in to the 'nano' for the file, don't forget to save the 'nano' before exiting.)

**Step 6:**
<br>
chmod +x 'whatever name you want of the file'.sh
<br>
('chmod +x' gives permissions to files or directorys for everyone.)

*Step 7:**
<br>
./'whatever name you want of the file'.sh
<br>
(Gives a little time lag.)

**Step 8:**
<br>
cat possibilities.txt | nc localhost 30002
<br>

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
