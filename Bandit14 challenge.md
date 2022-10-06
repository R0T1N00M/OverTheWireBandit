# Bandit13 -> 14 Challenge

**Username**
bandit13
<br>
**Password**
wbWdlBxEir4CaE8LaPhauuOo6pwRmrDw

**Task:**
The password for the next level is stored in /etc/bandit_pass/bandit14 and can only be read by user bandit14. 
For this level, you don’t get the next password, but you get a private SSH key that can be used to log into the next level. 
Note: localhost is a hostname that refers to the machine you are working on
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit14.html)

**Solution**
<br>
Do a 'ls -la', and use the sshkey to login to next lvl. (Fyi, we are going to use -i)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
ssh -i sshkey.private bandit14@bandit.labs.overthewire.org -p 2220
<br>
('-i' stands for “interactive.”)

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
