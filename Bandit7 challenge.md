# Bandit6 -> 7 Challenge

**Username:**
<br>
<br>
**bandit6**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXKqJU**
<br>
<br>


**Task:**
The password for the next level is stored somewhere on the server and has all of the following properties:
<br>
- owned by user bandit7
- owned by group bandit6
- 33 bytes in size

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit7.html)

**Solution**
<br>
Do a 'ls -la', change directory or 'cd' to ".." or '/home' directory, sort through users and groups for the properties then 'cat' it. (Fyi, 'find' is the main key.)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cd .. or cd /home

**Step 3:**
<br>
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
<br>
('-type f' finds files, '-user' find users, '-group' find group, '-size 33c' finds 33 bytes, '2>/dev/null' stops errors from showing)

**Step 4:**
<br>
cat /var/lib/dpkg/info/bandit7.password

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
