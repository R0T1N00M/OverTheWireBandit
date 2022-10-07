# Bandit21 -> 22 Challenge

**Username:**
<br>
<br>
**bandit21**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXIBcq**
<br>
<br>

**Task:**
A program is running automatically at regular intervals from cron, the time-based job scheduler. 
Look in /etc/cron.d/ for the configuration and see what command is being executed.

<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit22.html)

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
cat /etc/cron.d/cronjob_bandit22
<br>
(Sends what 'cronjob_bandit22' has in it.)

**Step 3:**
<br>
cat /usr/bin/cronjob_bandit22.sh
<br>
(Sends what 'cronjob_bandit22.sh' has in it.)

**Step 4:**
<br>
cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
<br>
(Sends what '/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv' has in it.)

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
