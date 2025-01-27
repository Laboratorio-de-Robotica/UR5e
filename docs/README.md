# Código para UR5e

<img align="right" src="/UR5e/assets/ur5e.png">

- [Repositorio](https://github.com/Laboratorio-de-Robotica/UR5e)
- [Sitio del robot](https://sites.google.com/ing.austral.edu.ar/jacobot/sobre-el-cobot/documentaci%C3%B3n?authuser=0)
- [Sitio del laboratorio](https://sites.google.com/ing.austral.edu.ar/laboratoriodeingeniera/inicio)

Este repositorio contiene código para usar con el robot colaborativo UR5e con objetivos académicos, dividido en carpetas independientes, que se describen a continuación.

## Curso Remote control
Código relativo al [Curso Remote control](https://campusvirtual.austral.edu.ar/course/view.php?id=16181&section=0) en el campus virtual.

- Remote control
  - primeros pasos para enviar comandos de movimiento de la PC con Python al robot
  - `remote_control_test.py` abre un socket que envía comandos en forma de strings, demostrando las comunicaciones de bajo nivel.
  - `urx_example.py` usa la biblioteca URX que oculta las comunicaciones de bajo nivel, implementando los comandos como métodos.
    - La biblioteca URX se instala con `pip install urx`
- Gripper
  - los ejemplos anteriores mueven el robot pero no el gripper, que es un sistema independiente
  - estos códigos no fueron debidamente testeados todavía
  - `gripper_socket_test.py` usa comandos TCP/IP GET y SET para abrir y cerrar el gripper
  - `gripper_urx_test.py` usa la biblioteca URX para comunicarse con el robot, y la biblioteca `robotiq_two_finger.py` para comunicarse con el gripper y cerrarlo
  - `robotiq_two_finger.py` es la biblioteca
- Socket communication
  - ejemplo de la tecnología usada en la industria: el robot consulta coordenadas a un servidor en PC
  - `servidor.py` es el servidor que atiende las consultas del robot
  - `picking.urp` es pseudocódigo para programar directamente en el teach pendant del robot