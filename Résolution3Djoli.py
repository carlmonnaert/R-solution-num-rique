import numpy as np 
import time
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# Paramètres
D = 1.5 * 10**(-5)
largeur = 0.1  # Largeur du solide en m (selon x)
longueur = 0.1  # Longueur du solide en m (selon y)
hauteur = 0.1  # Hauteur du solide en m (selon z)
durée = 60  # Durée de l'expérience en s
Nx = 20  # Nombre de points selon x
Ny = 20  # Nombre de points selon y
Nz = 20  # Nombre de points selon z
T0 = 20 + 273.15  # Degrés Kelvin
periode = 0 # Période d'affichage

dx = longueur / Nx
dy = largeur / Ny
dz = hauteur / Nz

dt = min(dx**2 / (6*D), dy**2 / (6*D), dz**2 / (6*D))

t = np.zeros((Nx, Ny, Nz)) + T0

# Conditions aux limites
t[0, :, :] = 100 + 273.15
t[-1, :, :] = 100 + 273.15
t[:, 0, :] = 100 + 273.15
t[:, -1, :] = 100 + 273.15
t[:, :, 0] = 100 + 273.15
t[:, :, -1] = 100 + 273.15

# Créer une figure et des axes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Boucle de simulation
temps = 0
realtime = time.time()
while temps < durée:
    t1 = t.copy()
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            for k in range(1, Nz - 1):
                t[i, j, k] = (D * dt / dx**2) * (t1[i+1, j, k] - 2*t1[i, j, k] + t1[i-1, j, k]) + \
                             (D * dt / dy**2) * (t1[i, j+1, k] - 2*t1[i, j, k] + t1[i, j-1, k]) + \
                             (D * dt / dz**2) * (t1[i, j, k+1] - 2*t1[i, j, k] + t1[i, j, k-1]) + t1[i,j,k]
    temps += dt
    if  time.time() - realtime > periode:
        realtime = time.time()
        # Tracer la distribution de température en 3D
        ax.clear()
        X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), np.arange(Nz))
        ax.scatter(X, Y, Z, c=t.flatten() - 273.15, cmap=plt.cm.jet, vmin=0, vmax=100)
        ax.set_title("Distribution de température à t = " + str(round(temps, 5)) + " s")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.pause(0.001)

plt.show()
