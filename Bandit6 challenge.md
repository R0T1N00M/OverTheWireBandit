# Bandit5 -> 6 Challenge

**Username:**
<br>
<br>
**bandit5**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXEeqR**
<br>
<br>

**Task:**
The password for the next level is stored in a file somewhere under the inhere directory and has all of the following properties:
<br>
- human-readable
- 1033 bytes in size
- not executable

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit6.html)

**Solution**
<br>
Do a 'ls -la', change directory or 'cd' to "inhere" directory, sort through files for the properties then 'cat' it. (Fyi, 'find' is the main key.)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cd inhere

**Step 3:**
<br>
find -type f -size 1033c ! -executable
<br>
('-type f' finds files, '-size 1033c' find files with 1033 bytes, '! -executable' not executable)

**Step 4:**
cat ./maybehere07/.file2

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
