import roboticstoolbox as rtb
import numpy as np
import matplotlib.pyplot as plt
from math import pi
from spatialmath import SE3

# Definir el robot (igual que antes)
L1 = rtb.DHLink(d=50, a=0, alpha=pi/2, qlim=[np.deg2rad(-90), np.deg2rad(90)])    
L2 = rtb.DHLink(d=0, a=120, alpha=0, qlim=[np.deg2rad(45), np.deg2rad(90)])       
L3 = rtb.DHLink(d=0, a=100, alpha=0, qlim=[np.deg2rad(-45), np.deg2rad(30)])      
L4 = rtb.DHLink(d=0, a=50, alpha=0, qlim=[np.deg2rad(0), np.deg2rad(0)])        
#se forma el robot a partir de los eslabones
eezybotarm = rtb.DHRobot([L1, L2, L3, L4])

#Se define el punto de inicio y fin del efector
p_ini = (140, 40, 100)
p_fin = (200, 100, 120)

#Los puntos se transofroman en matrices de transformación homogéneas 
M_ini = SE3(p_ini)
M_fin = SE3(p_fin)
#Se calcula la cinemática, pero para este robot hay que puntualizar que solo la posición y no la orientación con mask
cin_ini = eezybotarm.ikine_LM(M_ini, mask=[1,1,1,0,0,0])
cin_fin = eezybotarm.ikine_LM(M_fin, mask=[1,1,1,0,0,0])

#condicion cinemática fuera de los límites de movimiento del robot, lo indica ikine_LM
if not (cin_ini.success and cin_fin.success):
    print("Punto fuera del límite")
else:
    #El comando ikine_LM incluye q que es el vector de las articulaciones
    q_ini = cin_ini.q
    q_fin = cin_fin.q

    # Se interpolan 50 punto para generar la trayectoria y poder ver como se desplaza
    N_puntos = 50
    tray = rtb.jtraj(q_ini, q_fin, N_puntos)

    #Se visualiza en pyplot como en la cinemática directa
    env = rtb.backends.PyPlot.PyPlot()
    env.launch(); env.add(eezybotarm)
    for q in tray.q:
        eezybotarm.q = q
        env.step()
        plt.pause(0.04)
    plt.show()

