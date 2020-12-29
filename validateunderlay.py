import paramiko
from paramiko import SSHClient
#
switches = {'Sharedservices':'198.18.128.100', 'Fusion':'198.18.128.101', 'Core':'198.18.128.103',
'Edge1':'198.18.128.102', 'Edge2':'198.18.128.104'}
client = SSHClient()
# For loop throught the dictionary KV pairs
for switchname,switchip in switches.items():
    print('Logging into switch '+ switchname)

    try:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Auto Accepts SSH host keys from devices
        client.connect(switchip, username='dnacadmin', password='C1sco12345', timeout=5)
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("show ip ospf neighbor")
        showiproute = ssh_stdout.readlines()
        print('') # print the switch hostname and show command then the lines
        for line in showiproute:
            print(line.rstrip())

        client.connect(switchip, username='dnacadmin', password='C1sco12345', timeout=5)
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("show ip ospf int bri")
        showiproute = ssh_stdout.readlines()
        print('') # print the switch hostname and show command then the lines
        for line in showiproute:
            print(line.rstrip())

        client.connect(switchip, username='dnacadmin', password='C1sco12345', timeout=5)
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("show ip int bri")
        showiproute = ssh_stdout.readlines()
        print('') # print the switch hostname and show command then the lines
        for line in showiproute:
            print(line.rstrip())

        client.connect(switchip, username='dnacadmin', password='C1sco12345', timeout=5)
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("show spanning-tree vlan 102")
        showiproute = ssh_stdout.readlines()
        print('') # print the switch hostname and show command then the lines
        for line in showiproute:
            print(line.rstrip())

        client.connect(switchip, username='dnacadmin', password='C1sco12345', timeout=5)
        ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("ping 198.18.129.100")
        showiproute = ssh_stdout.readlines()
        print('') # print the switch hostname and show command then the lines
        for line in showiproute:
            print(line.rstrip())

    except Exception as error_message:
        print("Unable to connect")
        print(error_message)

client.close()
