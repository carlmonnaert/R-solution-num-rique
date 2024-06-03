import numpy as np 
import time
import matplotlib.pyplot as plt 

""" Equation de la chaleur sous la forme dT/dt = D * d²T/dx² + D * d²T/dy² où D = lambda/(rô C) """
D = 1.5 * 10**(-5)
largeur = 0.1 # largeur du solide en m (selon x)
longeur = 0.1 # longeur du solide en m (selon y)
durée = 100 # Durée de l'expérience en s
Nx = 50 # Nombre de points selon x
Ny = 50 # Nombre de points selon y
T0 = 20 + 273.15 # Degrés Kelvin
periode = 0 #Période d'affichage

dx = longeur / Nx
dy = largeur / Ny

dt = min(dx**2 / (4*D) , dy**2 / (4*D))

t = []
for k in range(0,Nx):
    t.append([0 for k in range(0,Ny)])
t = np.array(t) + T0

t[0,:] = 100 + 273.15
t[-1,:] = 100 + 273.15
t[:,0] = 100 + 273.15
t[:,-1] = 100 + 273.15

fig , axe = plt.subplots()
pcm = axe.pcolormesh(t - 273.15, cmap = plt.cm.jet, vmin = 0, vmax = 100)
plt.colorbar(pcm,ax = axe)

# Boucle :

temps = 0
realtime = time.time()

while temps < durée :
    t1 = t.copy()
    for i in range (1 , Nx - 1):
        for j in range (1 , Ny - 1):
            t[i,j] = (D * dt / dx**2) * ( t1[i+1,j] - 2*t1[i,j] + t1[i-1,j] ) + \
                     (D * dt / dy**2) * ( t1[i,j+1] - 2*t1[i,j] + t1[i,j-1] ) + \
                     t1[i,j] # Au premier ordre
    temps = temps + dt
    if  time.time() - realtime > periode:
        realtime = time.time()
        pcm.set_array(t - 273.15)
        axe.set_title("Apperçu pour t =" + str(round(temps - dt,5)) + "s") #-dt pour compenser le décallage
        plt.pause(0.001)


plt.show()