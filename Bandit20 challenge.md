# Bandit19 -> 20 Challenge

**Username:**
<br>
<br>
**bandit19**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXMTrC**
<br>
<br>

**Task:**
To gain access to the next level, you should use the setuid binary in the homedirectory. Execute it without arguments to find out how to use it. 
The password for this level can be found in the usual place (/etc/bandit_pass), after you have used the setuid binary.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit20.html)

**Solution**
<br>
Do a 'ls -la', We are going to get the password as bandit20.(Fyi, we are going to use 'cat' and './')

**Step 1:**
<br>
ls -la
<br>
(Looking at 'bandit20-do' it would have ‘-rwsr-x—’ this means the user bandit19 can execute the binary, but the binary is executed as user bandit20. Keep that in mind.)

**Step 2:**
<br>
./bandit20-do ls -la /etc/bandit_pass
<br>
('./' is used for special characters)

**Step 3:**
<br>
./bandit20-do cat /etc/bandit_pass/bandit20
<br>
('./' is used for special characters and '/bandit20' this is from the Step 1 note and from Step 2)

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
