from myservo import myServo
from funciones import forwardKinematics
from funciones import inverseKinematics
import time
servo1=myServo(4)
servo2=myServo(5)
servo3=myServo(18)
servo4=myServo(19)
servo1.myServoWriteAngle(0)
servo2.myServoWriteAngle(90)
servo3.myServoWriteAngle(90)
servo4.myServoWriteAngle(90)

#Inicialización de la posición de los servomotores
A1=0; A1_init=1;
A2=90; A2_init=89;
A3=90; A3_init=89;
A4=90; A4_init=89;
n=0;
#Función para controlar la velocidad mediante pasos de 1 angulo y pausas
def move(c_init, c_fin, i):
        if c_init < c_fin:
            step = 1  # Movimiento hacia adelante
        else:
            step = -1  # Movimiento hacia atrás
        
        for angle in range(c_init, c_fin, step):
            c_init=c_fin
            if i==0:
                servo1.myServoWriteAngle(angle)
            if i==1:
                servo2.myServoWriteAngle(angle)
            if i==2:
                servo3.myServoWriteAngle(angle)
            if i==3:
                servo4.myServoWriteAngle(angle)            
    
            time.sleep(0.01)
# Función para ingresar los ángulos desde la consola con errores por fallos en el formato
def inangulo():
    angulos = []
    try:
        while True:
            try:
                pos = input("Ingresa los angulos de 'pinza.base.brazo.codo' (ejemplo: 90.90.150.90):")
                angulos = pos.split(".")
                if len(angulos) != 4:
                    raise ValueError("Debes ingresar exactamente 4 valores separados por puntos.")
                break
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")
        return angulos
    except ValueError:
        print("Error: Ingresa un número válido para la cantidad de ángulos")
        return None
#Programa principal, se extraen los ángulos de la lista, y se ejecuta el movimiento
while True:
    angulos=inangulo()
    A1=int(angulos[0])
    A2=int(angulos[1])
    A3=int(angulos[2])
    A4=int(angulos[3])
    posiciones=forwardKinematics(A2,A3,A4)     
    for n in range(4):
        if n==0:
            move(A1_init,A1,0)
        if n==1:
            move(A2_init,A2,1)
        if n==2:
            move(A3_init,A3,2)
        if n==3:
            move(A4_init,A4,3)
    A1_init=A1
    A2_init=A2
    A3_init=A3
    A4_init=A4
    print("Ángulos servomotores:",A1,A2,A3,A4)
    
