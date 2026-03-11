from netmiko import ConnectHandler
from getpass import getpass

catalyst_3650 = {
    "device_type": "cisco_ios",
    "host": "192.168.20.1",
    "username": input("Username: "),
    "password": getpass("Password: "),
}

net_connect = ConnectHandler(**catalyst_3650)
net_connect.disconnect()