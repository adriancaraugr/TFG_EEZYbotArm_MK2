from myservo import myServo
from intento_funciones import inverseKinematics
import time

servo1 = myServo(4)
servo2 = myServo(5)
servo3 = myServo(18)
servo4 = myServo(19)
#Inicialización de los servomotores
servo1.myServoWriteAngle(0)
servo2.myServoWriteAngle(90)
servo3.myServoWriteAngle(90)
servo4.myServoWriteAngle(90)
#Valores maximos y minimos de cada servo
q1_min = 0
q1_max = 180
q2_min = 60
q2_max = 180
q3_min = 50
q3_max = 120
#Inicialización de variables
A1 = 0; A1_init = 1
A2 = 90; A2_init = 89
A3 = 90; A3_init = 89
A4 = 90; A4_init = 89
n = 0

#Función para controlar la velocidad y mover todos los servos a la vez.
#Esta sigue el mismo funcionamiento, sumar y restar 1 a los angulos añadiendo pausas.
#Por ello necesita un registro de desplazamiento de cada servomotor.
def mover_servos_juntos(iniciales, finales, servos, espera=0.01):
    pasos = [abs(f - i) for i, f in zip(iniciales, finales)]
    max_pasos = max(pasos)
    for paso in range(max_pasos + 1):
        for j, servo in enumerate(servos):
            if paso <= pasos[j]:
                if finales[j] >= iniciales[j]:
                    angulo = iniciales[j] + paso
                else:
                    angulo = iniciales[j] - paso
                servo.myServoWriteAngle(int(angulo))
        time.sleep(espera)
#Al igual que la cinemática directa esta función sirve para introducir las posiciones desde la consola, y cubre los errores de formato
def intrayectoria():
    while True:
        try:
            pos = input("Ingresa las posiciones en formato 'x.y.z.pinza(1-0)' (ejemplo: 100.200.100.1): ")
            trayectoria = pos.split(".")
            if len(trayectoria) != 4:
                print("Error: Debes ingresar exactamente 4 valores separados por puntos (x.y.z.pinza).")
                continue
            x, y, z, pinza = map(int, trayectoria)
            if pinza not in [0, 1]:
                print("Error: El valor de la pinza debe ser 0 o 1.")
                continue
            return [x, y, z, pinza]
        except ValueError:
            print("Error: Ingresa valores numéricos válidos en el formato correcto.")
#Se relacionan los valores introducidos con las posiciones, se calculan los angulos con la función inverseKinematics.
# En este caso es importante limmitar movimientos porque pueden romperse los servos al intentar alcanzar posiciones.
while True:
    posiciones = intrayectoria()
    angulos = inverseKinematics(int(posiciones[0]), int(posiciones[1]), int(posiciones[2]))
    A2 = int(angulos[0])
    A3 = int(angulos[1])
    A4 = int(angulos[2])
    pinza = int(posiciones[3])
    if pinza == 1:
        A1 = 100
    elif pinza == 0:
        A1 = 0
    if A2 < q1_min or A2 > q1_max:
        raise Exception('Ángulo 1 fuera de los límites:({},{})'.format(q1_min, q1_max))
    if A3 < q2_min or A3 > q2_max:
        raise Exception('Ángulo 2 fuera de los límites:({},{})'.format(q2_min, q2_max))
    if A4 < q3_min or A4 > q3_max:
        raise Exception('Ángulo 3 fuera de los límites:({},{})'.format(q3_min, q3_max))
    iniciales = [A2_init, A3_init, A4_init, A1_init]
    finales = [A2, A3, A4, A1]
    servos = [servo2, servo3, servo4, servo1]
    mover_servos_juntos(iniciales, finales, servos)
    A1_init = A1
    A2_init = A2
    A3_init = A3
    A4_init = A4
    print(A1, A2, A3, A4)

    