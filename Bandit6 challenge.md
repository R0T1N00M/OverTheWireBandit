# Bandit5 -> 6 Challenge
**Task:**
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
<br>
- human-readable
- 1033 bytes in size
- not executable

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit4.html)

**Solution**
<br>
Do a 'ls -la', change directory or 'cd' to "inhere" directory, cat the hidden file. (Fyi, without ls -la you can't see hiddin files.)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cd inhere

**Step 3:**
<br>
cat .hidden

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
