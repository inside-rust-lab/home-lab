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

routes = "show ip route"
routes_output = net_connect.send_command(routes)
print(routes_output)

version = "show version"
version_output = net_connect.send_command(version)
print(version_output)

net_connect.disconnect()