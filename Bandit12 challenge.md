# Bandit11 -> 12 Challenge

**Username:**
<br>
<br>
**bandit11**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXXHBM**
<br>
<br>

**Task:**
The password for the next level is stored in the file data.txt, where all lowercase (a-z) and uppercase (A-Z) letters have been rotated by 13 positions

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit12.html)

**Solution**
<br>
Do a 'ls -la', 'cat' the data.txt file for the password and decode it. (Fyi, we are going to use 'tr')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
<br>
('tr' A translate cmd)

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
