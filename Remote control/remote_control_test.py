# Test
import socket
import time
HOST = "192.168.0.16" # IP del robot
PORT = 30002 # port: 30001, 30002 o 30003, en ambos extremos
print("Conectando a IP: ", HOST)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("conectando...")
s.connect((HOST, PORT))
time.sleep(0.5)

print("Robot starts Moving to 3 positions based on joint positions")
#s.send (b"movej([-1.95, -1.58, 1.16, -1.15, -1.55, 1.18], a=1.0, v=0.1)\n")
#time.sleep(10)
#s.send (b"movej([-1.95, -1.66, 1.71, -1.62, -1.56, 1.19], a=1.0, v=0.1)\n")
#time.sleep(10)
#s.send (b"movej([-1.96, -1.53, 2.08, -2.12, -1.56, 1.19], a=1.0, v=0.1)\n")
#time.sleep(10)
print("Robot starts Moving to 3 positions based on pose positions")
s.send (b"movej(p[0.00, 0.3, 0.4, 2.22, -2.22, 0.00], a=1.0, v=0.1)\n")
time.sleep(10)
s.send (b"movej(p[0.00, 0.3, 0.3, 2.22, -2.22, 0.00], a=1.0, v=0.1)\n")
time.sleep(10)
s.send (b"movej(p[0.00, 0.3, 0.2, 2.22, -2.22, 0.00], a=1.0, v=0.1)\n")
time.sleep(10)
data = s.recv(1024)

s.close()
print("Received", repr(data))
print("Status data received from robot")