# Bandit22 -> 23 Challenge

**Username:**
<br>
<br>
**bandit22**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXEZff**
<br>
<br>

**Task:**
A program is running automatically at regular intervals from cron, the time-based job scheduler. 
Look in /etc/cron.d/ for the configuration and see what command is being executed.

NOTE: Looking at shell scripts written by other people is a very useful skill. The script for this level is intentionally made easy to read. 
If you are having problems understanding what it does, try executing it to see the debug information it prints.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit23.html)

**Solution**
<br>
Do a 'ls -la', and get to to (/etc/cron.d/).(Fyi, we are going to use 'cat' and 'ls -la')

**Step 1:**
<br>
ls -la /etc/cron.d/
<br>
('ls -la /etc/cron.d/' Shows whats inside the 'cron.d' directory)

**Step 2:**
<br>
cat /etc/cron.d/cronjob_bandit23
<br>
(Sends what 'cronjob_bandit23' has in it.)

**Step 3:**
<br>
cat /usr/bin/cronjob_bandit23.sh
<br>
(Sends what 'cronjob_bandit23.sh' has in it.)

**Step 4:**
<br>
echo I am user bandit23 | md5sum | cut -d ' ' -f 1
<br>
(This is from Step 3)

**Step 5:**
<br>
cat /tmp/$mytarget
<br>
($mytarget is from Step 4)

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
