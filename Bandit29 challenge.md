# Bandit28 -> 29 Challenge

**Username:**
<br>
<br>
**bandit28**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXX19nR**
<br>
<br>

**Task:**
There is a git repository at ssh://bandit28-git@localhost/home/bandit28-git/repo. 
The password for the user bandit28-git is the same as for the user bandit28.

Clone the repository and find the password for the next level.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit29.html)

**Solution**
<br>
Do a 'ls -la', and get the next password from the repository(Fyi, We are going to use 'git')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
mkdir /tmp/MyDIR28
<br>
cd /tmp/myDIR27
<br>

**Step 3:**
<br>
git clone ssh://bandit28-git@localhost:2220/home/bandit28-git/repo
<br>
(Type 'yes', then put current lvl password in.)

**Step 4:**
<br>
ls -la
<br>

**Step 6:**
<br>
cd repo/
<br>

**Step 7:**
<br>
cat README.md
<br>

**Step 8:**
<br>
git log
<br>

**Step 9:**
<br>
git checkout bdf3099fb1fb05faa29e80ea79d9db1e29d6c9b9 (or the second commit under the user 'Morla Porla')
<br>

*Step 10:**
<br>
cat README.md
<br>

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
