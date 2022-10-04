import paramiko

host = 'bandit.labs.overthewire.org'
port = 2220
username = 'bandit7'

def get_pass(n):
    with open("Passwords") as f:
       data = f.read().split()
    return data[int(n)]


password = get_pass(username[-1])

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

cmd = 'ls -la\n'
cmd += 'cat data.txt | grep millionth'

stdin,stdout,stderr = ssh.exec_command(cmd)
outlines = stdout.readlines()
resp = ''.join(outlines)
print(resp)
