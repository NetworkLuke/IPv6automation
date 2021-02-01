from netmiko import ConnectHandler

devices = (input("Please enter router IP address: ")) .strip().splitlines()

device_type = 'cisco_ios_telnet'
username = "networkluke"
password = "networkluke"

print(devices)

for device in devices:
    print("Connecting to device: " + device)
    net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
    prompter = net_connect.find_prompt()
    if '>' in prompter:
        net_connect.enable()
        
    IPv6_on = ['ipv6 unicast']
    output = net_connect.send_command('show run')
    if not 'ipv6 unicast-routing' in output:
        print("IPv6 is not currently enabled on this device")
        print("Enabling IPv6 on " + device)
        output = net_connect.send_config_set(IPv6_on)
    else:
        print("IPv6 is already enabled on this device")
        