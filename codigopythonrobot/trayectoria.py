from myservo import myServo
from intento_funciones import inverseKinematics
import time
#Inicialización de los servos
servo1 = myServo(4)
servo2 = myServo(5)
servo3 = myServo(18)
servo4 = myServo(19)
servo1.myServoWriteAngle(0)
servo2.myServoWriteAngle(90)
servo3.myServoWriteAngle(90)
servo4.myServoWriteAngle(90)
#Limite de grados de los servomotores
q1_min = 0
q1_max = 180
q2_min = 60
q2_max = 180
q3_min = 50
q3_max = 120
#Valores inciales de los servomotores
A1 = 1; A1_init = 0
A2 = 90;  A2_init = 89
A3 = 90;  A3_init = 89
A4 = 90;  A4_init = 89
n = 0
#Función para mover y controlar las velocidad de los servomotores, igual que en la cinematica inversa
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

#Función para introducir los puntos de la trayectoria, se indica el número de puntos y se van añadiendo en una lista.
def intrayectoria():
    trayectoria = []
    try:
        num_posiciones = int(input("¿Cuántas posiciones quieres agregar a la trayectoria? "))
        if num_posiciones <= 0:
            print("Por favor, ingresa un número mayor a 0.")
            return None
        print("Ingresa las posiciones en formato 'x.y.z.pinza(1,0)' (ejemplo: 100.200.100.1):")
        for i in range(num_posiciones):
            while True:
                try:
                    pos = input(f"Posición {i+1}: ")
                    posiciones = pos.split(".")
                    if len(posiciones) != 4:
                        raise ValueError("Debes ingresar exactamente 4 valores separados por puntos.")
                    x, y, z, pinz = map(int, posiciones)
                    trayectoria.append((x, y, z, pinz))
                    break
                except ValueError as e:
                    print(f"Error: {e}. Intenta de nuevo.")
        return trayectoria
    except ValueError:
        print("Error: Ingresa un número válido para la cantidad de posiciones.")
        return None
#Función que extrae las posiciones de la lista, le aplica la cinemática inversa y los límites de movimiento.
def posicion(x, y, z, pinz, A1_init, A2_init, A3_init, A4_init):
    try:
        angulos = inverseKinematics(x, y, z)
        A2 = int(angulos[0])
        A3 = int(angulos[1])
        A4 = int(angulos[2])
        if pinz == 1:
            A1 = 100
        elif pinz == 0:
            A1 = 0
        if A2 < q1_min or A2 > q1_max:
            raise Exception(f'Ángulo ({A2}) fuera de los límites ({q1_min}, {q1_max})')
        if A3 < q2_min or A3 > q2_max:
            raise Exception(f'Ángulo ({A3}) fuera de los límites ({q2_min}, {q2_max})')
        if A4 < q3_min or A4 > q3_max:
            raise Exception(f'Ángulo ({A4}) fuera de los límites ({q3_min}, {q3_max})')
        iniciales = [A2_init, A3_init, A4_init, A1_init]
        finales = [A2, A3, A4, A1]
        servos = [servo2, servo3, servo4, servo1]
        mover_servos_juntos(iniciales, finales, servos)
        print(f"Ángulos ejecutados: {A1}, {A2}, {A3}, {A4}")
        time.sleep(1)
        return A1, A2, A3, A4
    except Exception as e:
        print(f"Error al ejecutar posición ({x}, {y}, {z}): {e}")
        return None
#Función que ejecuta las trayectorias.
def ejecutartrayectoria(trayectoria):
    if not trayectoria:
        print("No hay trayectoria para ejecutar.")
        return
    global A1_init, A2_init, A3_init, A4_init
    print("Ejecutando trayectoria...")
    for i, (x, y, z, pinz) in enumerate(trayectoria, start=1):
        print(f"\nPaso {i}: Posición ({x}, {y}, {z})")
        resultado = posicion(x, y, z, pinz, A1_init, A2_init, A3_init, A4_init)
        if resultado:
            A1_init, A2_init, A3_init, A4_init = resultado
        else:
            print("Error en la trayectoria.")
            break
    print("Trayectoria completada.")

#Programa principal que ejecuta las funciones.
print("Bienvenido al programa de trayectorias.")
trayectoria = intrayectoria()
ejecutartrayectoria(trayectoria)
