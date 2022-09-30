# Bandit4 -> 5 Challenge
**Task:**
The password for the next level is stored in the only human-readable file in the inhere directory. Tip: if your terminal is messed up, try the “reset” command.

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit5.html)

**Solution**
<br>
Do a 'ls -la', change directory or 'cd' to "inhere" directory, look through each file for human-readable. (Fyi, look for ASCII text)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cd inhere

**Step 3:**
<br>
file ./*

**Step 4:**
<br>
cat ./-file07

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
