# Bandit12 -> 13 Challenge
**Task:**
The password for the next level is stored in the file data.txt, which is a hexdump of a file that has been repeatedly compressed. 
For this level it may be useful to create a directory under /tmp in which you can work using mkdir. For example: mkdir /tmp/myname123. 
Then copy the datafile using cp, and rename it using mv (read the manpages!)

**OverTheWire Levels**
<br>
[Overthewire.org](https://overthewire.org/wargames/bandit/bandit13.html)

**Solution**
<br>
Do a 'ls -la', and see the data.txt file, decompress the file until a ASCII TEXT file shows(Fyi, the cmd 'mkdir' is going to help in decompressing and the cmd 'file' is going to show what file type it is.)

**Step 1:**
<br>
ls -la

**Step 2:**
<br>
mkdir /tmp/mylvlnice

**Step 3:**
<br>
cat data.txt | xxd -r > /tmp/mylvlnice/data1
<br>
('xxd -r' make a hexdump or do the reverse -reverts it)

**Step 4:**
<br>
cd /tmp/mylvlnice

**Step 5:**
<br>
file data1

**Step 6:**
<br>
mv data1 ./data2.gz

**Step 7:**
<br>
gzip -d data2.gz
<br>
('gzip -d' decompresses gzip files)

**Step 8:**
<br>
file data2

**Step 9:**
<br>
mv data2 ./data2.bz2

**Step 10:**
<br>
bzip2 -d data2.bz2
<br>
('bzip2 -d' decompresses bzip2 files)

**Step 11:**
<br>
file data2

**Step 12:**
<br>
mv data2 ./data2.gz

**Step 13:**
<br>
gzip -d data2.gz

**Step 14:**
<br>
file data2

**Step 15:**
<br>
mv data2 ./data2.tar

**Step 16:**
<br>
tar -xf data2.tar
<br>
('tar -xf' decompresses tar files)

**Step 17:**
<br>
file data5.bin

**Step 18:**
<br>
tar -xf data5.bin
<br>
('tar -xf' decompresses tar files)

**Step 19:**
<br>
file data6.bin.out

**Step 20:**
<br>
tar -xf data6.bin.out
<br>
('tar -xf' decompresses tar files)

**Step 19:**
<br>
file data8.bin

**Step 21:**
<br>
mv data8.bin ./data8.gz

**Step 22:**
<br>
gzip -d data8.gz
<br>
('gzip -d' decompresses gzip files)

**Step 23:**
<br>
cat data8

*Fast way to logining in:*
<br>
ssh bandit.labs.overthewire.org -p 2220 -l bandit (whatever lvl you are on)

**Script for lvl**
<br>
**To be continued**
