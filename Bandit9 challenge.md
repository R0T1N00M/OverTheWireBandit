# Bandit8 -> 9 Challenge

**Username:**
<br>
<br>
**bandit8**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXrBvP**
<br>
<br>

**Task:**
The password for the next level is stored in the file data.txt and is the only line of text that occurs only once

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit9.html)

**Solution**
<br>
Do a 'ls -la', and look through the 'data.txt' file while also getting the correct and only password(Fyi, 'sort' and 'uniq' is the main key.)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
sort data.txt | uniq -u
<br>
('sort' sorts through a file, 'uniq -u' finds unique lines in a file)

**Script for lvl**
<br>
[Bandit8 -> Bandit9 Script](https://github.com/R0T1N00M/OverTheWireBandit/blob/main/Bandit8-9skip.py)
