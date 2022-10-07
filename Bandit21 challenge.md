# Bandit20 -> 21 Challenge

**Username:**
<br>
<br>
**bandit20**
<br>
<br>
**Password:**
<br>
<br>
**XXXXXXXXXXXXXXXXXXXXXXXXXXX95XT**
<br>
<br>

**Task:**
There is a setuid binary in the homedirectory that does the following: it makes a connection to localhost on the port you specify as a commandline argument. 
It then reads a line of text from the connection and compares it to the password in the previous level (bandit20). 
If the password is correct, it will transmit the password for the next level (bandit21).

NOTE: Try connecting to your own network daemon to see if it works as you thin
<br>
<br>
**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit20.html)

**Solution**
<br>
Do a 'ls -la', We are going to get the password from a different localhost.(Fyi, we are going to use 'echo' and 'nc')

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
echo -n 'XXXXXXXXXXXXXXXXXXXXXXXXXXX95XT' | nc -l -p 12345 &
<br>
(This connect to our 'netcat or nc' server, receive the password inputted through 'echo' and sends back the next password.)

**Step 3:**
<br>
./suconnect 12345
<br>
(If '12345' doesn't work then try '1234' this also goes for Step 2)

*Fast way to logging in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
