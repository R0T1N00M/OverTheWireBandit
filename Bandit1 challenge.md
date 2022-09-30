# Bandit0 -> 1 Challenge
**Task:**
The password for the next level is stored in a file called readme located in the home directory. Use this password to log into bandit1 using SSH. Whenever you find a password for a level, use SSH (on port 2220) to log into that level and continue the game.

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit1.html)

**Solution**
<br>
Do a 'ls -la' and 'cat' the readme

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
cat readme

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
[Bandit0 -> 1 Script](https://github.com/R0T1N00M/OverTheWireBandit/blob/main/Bandit0skip.py) 
