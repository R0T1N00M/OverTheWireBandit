# Bandit2 -> 3 Challenge

**Username:**
<br>
<br>
**bandit2**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXlgzi**
<br>
<br>

**Task:**
The password for the next level is stored in a file called **spaces in this filename** located in the home directory

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit3.html)

**Solution**
<br>
Do a 'ls -la', cat the 'spaces in this filename' file. (Fyi, put "" or '' on the file bc it has spaces in the name.) 

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cat 'spaces in this filename'

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
[Bandit2->3 Script](https://github.com/R0T1N00M/OverTheWireBandit/blob/main/Bandit2-3skip.py)
