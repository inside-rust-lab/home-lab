from netmiko import ConnectHandler
from getpass import getpass

username = input("Username: ")
password = getpass("Password: ")

catalyst_3650 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.1",
    "username": username,
    "password": password,
    "secret": password
}

net_connect = ConnectHandler(**catalyst_3650)
net_connect.enable()
print(net_connect.find_prompt())
net_connect.disconnect()