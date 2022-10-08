# Bandit31 -> 32 Challenge

**Username:**
<br>
<br>
**bandit31**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXMhmt**
<br>
<br>

**Task:**
There is a git repository at ssh://bandit31-git@localhost/home/bandit31-git/repo. 
The password for the user bandit31-git is the same as for the user bandit31.

Clone the repository and find the password for the next level.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit32.html)

**Solution**
<br>
Do a 'ls -la', and get the next password from the repository(Fyi, We are going to use 'git')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
mkdir /tmp/MyDIR31
<br>

**Step 3:**
<br>
cd /tmp/MyDIR31
<br>

**Step 4:**
<br>
git clone ssh://bandit31-git@localhost:2220/home/bandit31-git/repo
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
cat README.md
<br>

**Step 8:**
<br>
nano key.txt
<br>

**Step 9:**
<br>
('Inside Nano')
<br>
May I come in?
<br>
(Once done exit out of nano)
<br>

**Step 10:**
<br>
rm .gitignore
<br>
('rm .gitignore' This is going to block the .txt file.)

**Step 11:**
<br>
git add key.txt
<br>

**Step 12:**
<br>
git status
<br>
('git status' To see if it's there.)

**Step 13:**
<br>
git commit -m "hello"
<br>

**Step 14:**
<br>
git log
<br>
('git log' To see if it's there)

**Step 15:**
<br>
git push
<br>

**Step 16:**
<br>
Put in current lvl password.

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
