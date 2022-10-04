# Bandit9 -> 10 Challenge
**Task:**
The password for the next level is stored in the file data.txt in one of the few human-readable strings, preceded by several ‘=’ characters.

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit10.html)

**Solution**
<br>
Do a 'ls -la', and 'cat' the 'data.txt' file while also getting the password(Fyi, 'strings' and 'grep' is the main key.)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
strings data.txt | grep ===
<br>
('strings' looks for texts through a file, 'grep' gets a pacific thing)

**Script for lvl**
<br>
[Bandit9 -> Bandit10 Script](https://github.com/R0T1N00M/OverTheWireBandit/blob/main/Bandit9-10skip.py)
