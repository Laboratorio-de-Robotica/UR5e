# biblioteca previamente instalada con 
# pip install urx
import urx

# conectarse al brazo robot es muy simple
# colocar el IP del robot
miRobot = urx.Robot("192.168.0.16")

# mover el brazo ahora es así
miRobot.movej((1, 2, 3, 4, 5, 6))

# urx incorpora su propio comando sleep, no hace falta import time
sleep(10)

# movimiento concatenado! ejecuta uno a continuación del otro
miRobot.movejs([
  [0,0,0,0,0,0],
  [2,0,0,0,0,0],
  [0.5,0,0,0,0,0]
])

# este bucle while consulta cada décima de segundo si el robot ya terminó la operación, y cuando es así sale del bucle cuando
while True:
    sleep(0.01)
    if not miRobot.is_program_running():
        break

# imprimir la posición x,y,z
print(miRobot.get_pos())

# imprimir los ángulos de todos los joints
print(miRobot.getj())

# para terminar, se cierra la conexión
miRobot.close()