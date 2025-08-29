# Proyecto TFG – Brazo Robótico Didáctico (EEZYBotArm MK2)
En este repositorio he subido todo el material que he usado para el desarrollo del trabajo final de grado, en este hay material mío y de fuentes externas que citaré a continuación.

Este trabajo tiene como finalidad el desarrollo de un brazo robótico didáctico, para ello se ha elejido el **EEZYbotArm MK2**. Este robot es del autor **daGHIZmo** bajo licencia Creative Commons - Attribution - Non-Commercial y todos los archivos STL para la impresión se pueden encontrar en Thingiverse: https://www.thingiverse.com/thing:1454048.

Al robot original se le ha cambiado la pinza pues esta no era práctica para agarrar objetos. La **pinza** es del autor **sthone** bajo licencia Creative Commons - Attribution - Non-Commercial y los archivos STL se pueden encontrar en Thingiverse: https://www.thingiverse.com/thing:4362304.

El código generado para el movimiento del robot es mío, pero para las funciones me he ayudado del autor **meisben** (MIT License Copyright (c)) https://github.com/meisben/easyEEZYbotARM. Estás funciones han sido modificadas para adaptarlas a mi código.

Para controlar el robot es usado una ESP32 y el entorno Thonny para trabajar con MicroPython.

## Simulación
Para la simulación se ha usado la librería **Robotics Toolbox for Pyhton** de **PeterCorke** https://github.com/petercorke/robotics-toolbox-python. El código de la siulación es propio pero usa esta librería.
En la parte de cinemática inversa la simulación sufre problemas pues esta librería necesita calcular a partir de posición y orientación para robots de 6GDL.


La finalidad de este repositorio es totalmente didáctica.

## Licencias
- **EEZYbotArm MK2** – © daGHIZmo – [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)  
- **Pinza de sthone** – © sthone – [CC BY-NC](https://creativecommons.org/licenses/by-nc/4.0/)  
- **Funciones base de meisben** – MIT License  
