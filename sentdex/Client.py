import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    msg = s.recv(8)                     # Recieving data
    if len(msg) <= 0:
        break                           # Leave loop
    full_msg += msg.decode("utf-8")
print(full_msg)