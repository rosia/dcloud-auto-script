import paramiko
from paramiko import SSHClient

client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Auto Accepts SSH host keys from devices
client.connect('10.66.50.135', username='dna-8', password='cisco!123')
ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("show ip route")
output = ssh_stdout.readlines()
for line in output:
    print(line.rstrip())
