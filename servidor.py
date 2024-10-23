'''
Este servidor TCP/IP se ejecuta en PC preferentemente con IP fija y un puerto cualquiera.
La IP y el puerto se deben transcribir en el cliente que ejecuta en el controlador del robot.

Dentro del bucle principal while True se debe implementar el código que determina
las coordenadas x,y a informar al robot cuando consulte.
'''

import socket
import threading
import time

# Coordenadas de picking que se informarán al robot
x=0.2
y=0.0

# Función que ejecuta el servidor TCP/IP
def start_server():
    HOST = '192.168.0.20'  # Dirección IP de este servidor
    PORT = 65432           # Puerto donde escucha el servidor, un número inventado que no esté usado por otro servicio

    # Crear un socket TCP/IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f"Servidor escuchando en {HOST}:{PORT}...")

        # Bucle infinito para aceptar múltiples conexiones
        while True:
            # Usamos un timeout para evitar bloqueo completo en accept
            s.settimeout(1.0)
            try:
                # accept() bloquea hasta que recibe una consulta
                # addr contiene la ip de la máquina que realiza la consulta
                conn, addr = s.accept()
            except socket.timeout:
                # Si no hay conexión, seguimos esperando
                continue

            with conn:
                # Conexión establecida, recibir la consulta del cliente, una string
                data = conn.recv(1024)
                consulta = data.decode()
                print(f"Consulta: {consulta}")

                # Enviar las variables al cliente con el fomato requerido por asciiToFloat
                response = f"({x}, {y})\n"
                conn.sendall(response.encode())
                print(f"Respuesta: {response}")

                # Respuesta enviada. Conexión cerrada. Esperando nueva conexión...


# Crear un hilo para el servidor
server_thread = threading.Thread(target=start_server)
server_thread.daemon = True  # Hacer que el hilo se cierre cuando termine el programa principal
server_thread.start()

# Programa principal continúa haciendo otras cosas
print("Servidor en ejecución en segundo plano. El programa principal puede seguir trabajando.")

# Bucle principal donde se determinan las coordenadas x e y
try:
    while True:
        # Aquí se desarrolla el código de visión artificial que determina las coordenadas de picking

        # Simulación que alterna entre dos coordenadas
        x=0.5-x
        y=0.3-y

        # Pausa pequeña para permitir que el servidor siga atendiendo consultas
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Programa interrumpido por el usuario.")

