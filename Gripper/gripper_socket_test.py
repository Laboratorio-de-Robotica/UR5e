# Test
import socket
import time
HOST = "192.168.0.16" # IP del robot
PORT = 63352 # port del gripper
print("Conectando a IP: ", HOST)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("conectando...")
s.connect((HOST, PORT))
time.sleep(0.5)

print("Gripper starts moving back and forth")

s.send (b"SET SPE 255\n")
s.send (b"SET FOR 50\n")
s.send (b"SET POS 255\n")
s.send (b"SET ACT 1\n")
s.send (b"SET GTO 1\n")
time.sleep(5)

s.send (b"SET SPE 255\n")
s.send (b"SET FOR 50\n")
s.send (b"SET POS 0\n")
s.send (b"SET ACT 1\n")
s.send (b"SET GTO 1\n")

data = s.recv(1024)
s.close()
print("Received from gripper", repr(data))