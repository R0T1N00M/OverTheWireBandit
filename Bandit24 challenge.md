# Bandit23 -> 24 Challenge

**Username:**
<br>
<br>
**bandit23**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXyR2G**
<br>
<br>

**Task:**
A program is running automatically at regular intervals from cron, the time-based job scheduler.
Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: This level requires you to create your own first shell-script. This is a very big step and you should be proud of yourself when you beat this level!

NOTE 2: Keep in mind that your shell script is removed once executed, so you may want to keep a copy around…
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit24.html)

**Solution**
<br>
Do a 'ls -la', and get to to (/etc/cron.d/).(Fyi, we are going to use 'cron' and 'nano')

**Step 1:**
<br>
ls -la /etc/cron.d/
<br>
('ls -la /etc/cron.d/' Shows whats inside the 'cron.d' directory)

**Step 2:**
<br>
cat /etc/cron.d/cronjob_bandit24
<br>
(Sends what 'cronjob_bandit24' has in it.)

**Step 3:**
<br>
cat /usr/bin/cronjob_bandit24.sh
<br>
(Sends what 'cronjob_bandit24.sh' has in it.)

**Step 4:**
<br>
mktemp -d
<br>
('mktemp -d' makes a Temporary Directory, example: '/tmp/tmp.DuzEylipfd')

**Step 5:**
<br>
cd /tmp/tmp."Temporary Directory"
<br>
("Temporary Directory" is from 'mktemp -d')

**Step 6:**
<br>
nano 'whatever name you want of the file'.sh
<br>
('nano' is  a  small  and friendly editor. 'whatever name you want of the file' means name it however you like with a '.sh' at the end.)

*Step 7:**
<br>
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/tmp."Temporary Directory"/password.txt
<br>
(Do this after getting in to the 'nano' for the file, don't forget to save the 'nano' before exiting.)

**Step 8:**
<br>
chmod +x 'whatever name you want of the file'.sh
<br>
('chmod +x' gives permissions to files or directorys for everyone.)

**Step 9:**
<br>
chmod 777 .
<br>
('chmod 777' gives permissions to read, write and execute for everyone. If that doesn't work try 'chmod +w')

**Step 10:**
<br>
cp 'whatever name you want of the file'.sh /var/spool/bandit24/
<br>
('cp' copies 'whatever name you want of the file.sh' to '/var/spool/bandit24/' which was from Step 3.)
<br>
(Wait a minute or less to see a file called 'password.txt' from Step 7, if not then check the 'whatever name you want of the file'.sh for miss spelling.)

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**

