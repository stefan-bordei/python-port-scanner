import socket

# inits
target = '127.0.0.1'
open_ports = []


def scan(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((target, port))
        return True
    except:
        return False


def worker(ports):
    for port in ports:
        if scan(port):
            open_ports.append(port)


print("Welcome!")
userInput = str(input('Choose a target to scan(default = localhost): '))

if userInput != '':
    target = userInput

userInput = str(input('Choose range of ports to scan (default 0-1023): '))

if userInput == '':
    port_list = range(1024)
else:
    port_list = range(int(userInput.split('-')[0]), int(userInput.split('-')[1]))

worker(port_list)
print('\n\nScanning complete!\n')
print(f'Open ports are: {open_ports}')
