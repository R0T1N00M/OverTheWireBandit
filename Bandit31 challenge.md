# Bandit30 -> 31 Challenge

**Username:**
<br>
<br>
**bandit30**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXXEOnS**
<br>
<br>

**Task:**
There is a git repository at ssh://bandit30-git@localhost/home/bandit30-git/repo. 
The password for the user bandit30-git is the same as for the user bandit30.

Clone the repository and find the password for the next level.
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit31.html)

**Solution**
<br>
Do a 'ls -la', and get the next password from the repository(Fyi, We are going to use 'git')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
mkdir /tmp/MyDIR30
<br>

**Step 3:**
<br>
cd /tmp/MyDIR30
<br>

**Step 4:**
<br>
git clone ssh://bandit30-git@localhost:2220/home/bandit30-git/repo
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
git branch -a
<br>
('git branch -a' shows all the branchs that are remote-tracking branches and local branches.)

**Step 9:**
<br>
git tag
<br>

**Step 10:**
<br>
git show secret
<br>

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
