# Bandit1 -> 2 Challenge

**Username:**
<br>
<br>
**bandit1**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXVXjL**
<br>
<br>

**Task:**
The password for the next level is stored in a file called - located in the home directory

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit2.html)

**Solution**
<br>
Do a 'ls -la', cat the '-' file. (Fyi, do a "./-" on the file bc it's a special charcter.) 

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cat ./-

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
[Bandit1 -> 2 Script](https://github.com/R0T1N00M/OverTheWireBandit/blob/main/Bandit1-2skip.py)
