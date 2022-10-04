# Bandit7 -> 8 Challenge
**Task:**
The password for the next level is stored in the file data.txt next to the word millionth
<br>

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit8.html)

**Solution**
<br>
Do a 'ls -la', and 'cat' the 'data.txt' file while also getting the password(Fyi, 'grep' and 'piping' is the main key.)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cat data.txt | grep millionth

**Script for lvl**
<br>
[Bandit7 -> Bandit8 Script](https://github.com/R0T1N00M/OverTheWireBandit/blob/main/Bandit7-8skip.py)
