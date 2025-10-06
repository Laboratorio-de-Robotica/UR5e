# Picking
Este código conforma un sistema de Picking para el robot UR5e.
El sistema consta de:

- sistema de visión que determina las coordenadas de picking
- publicador en PC que recibe las coordenadas del sistema de visión y las envía a los suscriptores por TCP/IP
- suscriptor en el robot que recibe las coordenadas del publicador
- programa de movimiento del robot

## Instalación
En PC:

- publisher.py
- sistema de visión

En el robot:

- biblioteca picking.script
- transcripción del pseudocódigo picking.urp, con las adaptaciones necesarias para la aplicación específica

## Funcionamiento

En el robot el programa se suscribe al publicador para recibir coordenadas de picking.  Las coordenadas están expresadas en el sistema de referencia del robot.

En la PC el publicador atiende las suscripciones e informa nuevas coordenadas.  Esto se puede implementar de dos maneras: 

- publica todas las coordenadas detectadas una a continuación de la otra, y el robot las almacena en su buffer TCP/IP y las va consumiendo y atendiendo de a una de manera secuencial
- cada vez que el robot informa que está IDLE, el sistema determina una coordenada y la publica
