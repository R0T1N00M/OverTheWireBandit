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
**From Bandit16 -> 17**
<br>
<br>

**Task:**
There are 2 files in the homedirectory: passwords.old and passwords.new. 
The password for the next level is in passwords.new and is the only line that has been changed between passwords.old and passwords.new

NOTE: if you have solved this level and see ‘Byebye!’ when trying to log into bandit18, this is related to the next level, bandit19
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit18.html)

**Solution**
<br>
Do a 'ls -la', and find the password between the two files. (Fyi, we are going to use 'diff')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
diff passwords.old passwords.new
<br>
('diff' Compares FILES line by line.)

**Step 3:**
<br>
cat passwords.new | grep "1st password got from Step 2"

**Step 4:**
<br>
cat passwords.new | grep "2nd password got from Step 2"


*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
