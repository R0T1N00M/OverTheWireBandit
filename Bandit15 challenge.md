# Bandit14 -> 15 Challenge

**Username:**
<br>
<br>
**bandit14**
<br>
<br>
**Password:**
<br>
<br>
**fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq**
<br>
<br>

**Task:**
The password for the next level can be retrieved by submitting the password of the current level to port 30000 on localhost.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit15.html)

**Solution**
<br>
Do a 'ls -la', and use the current lvl password to find the password for the next lvl . (Fyi, we are going to use -i)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cat /etc/bandit_pass/bandit14
<br>
('/etc/bandit_pass/bandit14' from the lvl before.)

**Step 3:**
<br>
nc localhost 30000
<br>
('nc' stands for netcat which allows user to move from ports.)

**Step 4:**
<br>
Enter current password 'fGrHPx402xGC7U7rXKDaxiWFTOiF0ENq' after doing Step 3

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
