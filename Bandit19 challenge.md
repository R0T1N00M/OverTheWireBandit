# Bandit17 -> 18 Challenge

**Username:**
<br>
<br>
**bandit18**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXFrdg**
<br>
<br>

**Task:**
The password for the next level is stored in a file readme in the homedirectory. 
Unfortunately, someone has modified .bashrc to log you out when you log in with SSH.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit19.html)

**Solution**
<br>
We are going to get the password without logging in ish.(Fyi, we are going to use 'ls' and 'cat')

**Step 1:**
<br>
ssh bandit18@bandit.labs.overthewire.org -p 2220 ls -la
<br>
(If asked for password then put current lvl password)

**Step 2:**
<br>
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat readme
<br>
(If asked for password then put current lvl password)

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
