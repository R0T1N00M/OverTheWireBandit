# Bandit10 -> 11 Challenge

**Username:**
<br>
<br>
**bandit10**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXyp6s**
<br>
<br>

**Task:**
The password for the next level is stored in the file data.txt, which contains base64 encoded data

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit11.html)

**Solution**
<br>
Do a 'ls -la', 'cat' the data.txt file for the password and decode it. (Fyi, we are going to use base64)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
base64 -d data.txt
<br>
('base64 -d' decodes in [base64](https://en.wikipedia.org/wiki/Base64))

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
