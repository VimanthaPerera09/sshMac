import paramiko
import sys

host = sys.argv[1]
port = 22
username = sys.argv[2]
password = sys.argv[3]

command = "ifconfig"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)


print("connecting............")
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()
#print(type(lines))
fw = open('allDet.txt', 'w')
for x in lines:
    fw.write(x + "\n")

fw.close()


fr = open("allDet.txt", "r")
searchlines = fr.readlines()
fr.close()

f = open('Macs.txt', 'w')
           
for i, line in enumerate(searchlines):
    if "HW" in line:
        f.write(line + "\n")  
f.close()
         
            
                