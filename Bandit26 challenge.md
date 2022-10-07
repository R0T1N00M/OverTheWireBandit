# Bandit25 -> 26 Challenge

**MUST READ:**
<br>
After completing the lvl don't logout yet!
<br>
<br>

**Username:**
<br>
<br>
**bandit25**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXpx8d**
<br>
<br>

**Task:**
Logging in to bandit26 from bandit25 should be fairly easy… 
The shell for user bandit26 is not /bin/bash, but something else. Find out what it is, how it works and how to break out of it.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit26.html)

**Solution**
<br>
Do a 'ls -la', and get the password from min.(Fyi, we are going to need to min the screen and the cmd 'more')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cat /etc/passwd | grep bandit26

**Step 3:**
<br>
cat /usr/bin/showtext

**Step 4:**
<br>
Shrink your console
<br>
(This helps with the process)

**Step 5:**
<br>
ssh -i ./bandit26.sshkey bandit26@localhost -p 2220
<br>
(After shrinking the console)

**Step 6:**
<br>
Press 'v'
<br>
(After it say's "More")

**Step 7:**
<br>
:set shell=/bin/bash
<br>
(After pressing "v")

**Step 8:**
<br>
:shell
<br>
(After doing Step 7)

**Step 9:**
<br>
cat /etc/bandit_pass/bandit26


*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
