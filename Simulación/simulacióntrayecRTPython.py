import roboticstoolbox as rtb
import numpy as np
from math import pi
import matplotlib.pyplot as plt

#Se definen los eslabones, el parametro theta no se define porque es el que da el movimiento.
L1 = rtb.DHLink(d=50, a=0, alpha=pi/2, qlim=[np.deg2rad(-90), np.deg2rad(90)])      #Se añaden los limites para ser mas realista.
L2 = rtb.DHLink(d=0, a=120, alpha=0, qlim=[np.deg2rad(45), np.deg2rad(90)])        
L3 = rtb.DHLink(d=0, a=100, alpha=0, qlim=[np.deg2rad(-45), np.deg2rad(30)])       
L4 = rtb.DHLink(d=0, a=50, alpha=0, qlim=[np.deg2rad(0), np.deg2rad(0)])        
#se forma el robot a partir de los eslabones
eezybotarm = rtb.DHRobot([L1, L2, L3, L4])

# posición inicial y final
q0 = [0, np.deg2rad(85), np.deg2rad(-70), np.deg2rad(40)]
qf = [0, np.deg2rad(45), np.deg2rad(-90), np.deg2rad(50)]

# se genera la trayectoria con el comando jtraj con 50 puntos, una matriz de 50 filas y 4 columnas
traj = rtb.jtraj(q0, qf, 50)

# se almacenan las pociciones, T incluye traslación y orientacion, T.t extrea la matriz de traslación unicamente
pos = []
for q in traj.q:
    T = eezybotarm.fkine(q)
    pos.append(T.t)
pos = np.array(pos)

#Abre la ventana
env = rtb.backends.PyPlot.PyPlot()
env.launch()
env.add(eezybotarm)
#Simula la trayectoria en todos los puntos
for q in traj.q:
    eezybotarm.q = q
    env.step()
    plt.pause(0.05)

plt.show()
