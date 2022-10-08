# Bandit27 -> 28 Challenge

**Username:**
<br>
<br>
**bandit27**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXEuas**
<br>
<br>

**Task:**
<br>
There is a git repository at ssh://bandit27-git@localhost/home/bandit27-git/repo. 
The password for the user bandit27-git is the same as for the user bandit27.
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit28.html)

**Solution**
<br>
Do a 'ls -la', and get the password from the 'ssh' given (Fyi,We are using 'git')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
mkdir /tmp/myDIR27
<br>

**Step 3:**
<br>
cd /tmp/myDIR27
<br>

**Step 4:**
<br>
git clone ssh://bandit27-git@localhost:2220/home/bandit27-git/repo
<br>
(Type 'yes', then put current lvl password in.)

**Step 5:**
<br>
ls -la
<br>

**Step 6:**
<br>
cd repo/
<br>

**Step 7:**
<br>
cat README
<br>

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
