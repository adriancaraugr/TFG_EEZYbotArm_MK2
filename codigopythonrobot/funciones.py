from math import *  
#Longitud eslabones
L1 = 92  
L2 = 135
L3 = 147
L4 = 110

def inverseKinematics(x_EE, y_EE, z_EE):

        # Calculo q1
        q1 = atan2(y_EE, x_EE)

        # Posiciones de la muñeca del robot
        x_4 = x_EE - (L4 * cos(q1))
        y_4 = y_EE - (L4 * sin(q1))
        z_4 = z_EE - L1


        # Calculo de la diagonal a 
        xy_4 = sqrt((x_4**2)+(y_4**2))
        a = sqrt((z_4**2) + (xy_4**2))

        # Calculo q3
        q3 = - (pi - acos((L2**2 + L3**2 - a**2)/(2 * L2 * L3)))

        # Calculo q2
        q2_a = atan2(z_4, xy_4)
        q2_b = acos((a**2 + L2**2 - L3**2)/(2 * a * L2))
        q2 = q2_a + q2_b
        
        #Paso a ángulos y redondeo del valor
        q1 = round(q1 * 180/pi, 2)
        q2 = round(q2 * 180/pi, 2)
        q3 = round(q3 * 180/pi, 2)
        # Calculo q1 en el servo
        servoAngle_q1 = (q1) + 90  
        servoAngle_q1 = round(servoAngle_q1, 2)

        #Calculo q2 en el servo
        servoAngle_q2 = 180 - q2  
        servoAngle_q2 = round(servoAngle_q2, 2)

        #Calculo q3 en el servo
        q3_a = 180 - (- q3)  
        servoAngle_q3 = q2 - 45 + q3_a
        servoAngle_q3 = round(servoAngle_q3, 2)
        
        print("Ángulos del servomotor:",servoAngle_q1, servoAngle_q2, servoAngle_q3)

        return servoAngle_q1, servoAngle_q2, servoAngle_q3

def forwardKinematics(A1,A2,A3):
        #Opcional, depende de que grados quieres dar, los de los eslabones o los de los motores.
        #En mi caso prefiero dar la de los motores, pues es mas certero y lo utilizo para hacer pruebas, como calcular los límites de cada servo.
        q1=A1-90
        q2=180-A2
        q3=A3-q2-135
        
        #Conversión a radianes
        q1 = q1 * pi/180
        q2 = q2 * pi/180
        q3 = q3 * pi/180


        #Cinemática directa, calculo x,y,z
        x_EE = round((cos(q1) * (cos(q2+q3)*L3 + cos(q2)*L2))+(L4*cos(q1)), 3)
        y_EE = round((sin(q1) * (cos(q2+q3)*L3 + cos(q2)*L2))+(L4*sin(q1)), 3)
        z_EE = round((L1 + sin(q2)*L2 + sin(q2+q3)*L3), 3)
        
        
        print("Posición efector:", x_EE,y_EE,z_EE)

 
        return x_EE, y_EE, z_EE
