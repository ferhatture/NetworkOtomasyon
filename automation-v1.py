import getpass
#telnetlib yeni versiyon ile silindi ve telnetlib3 olarak güncellendi :
#pip install telnetlib3
#python.exe -m pip install --upgrade pip
import telnetlib3  

HOST = "192.168.78.72"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib3.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"enable\n")
tn.write(b"cisco\n")
tn.write(b"conf t\n")
tn.write(b"vlan 2\n")
tn.write(b"name PythonVLAN2\n")
tn.write(b"vlan 3\n")
tn.write(b"name PythonVLAN3\n")
tn.write(b"vlan 4\n")
tn.write(b"name PythonVLAN4\n")
tn.write(b"vlan 5\n")
tn.write(b"name PythonVLAN5\n")
tn.write(b"vlan 6\n")
tn.write(b"name PythonVLAN6\n")
tn.write(b"vlan 7\n")
tn.write(b"name PythonVLAN7\n")
tn.write(b"vlan 8\n")
tn.write(b"name PythonVLAN8\n")
tn.write(b"end\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))