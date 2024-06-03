import numpy as np 
import time
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D

# Paramètres
h = 5 #W.K-1.m-2 

lambd = 0.604 #W.m-1.K-1
rho = 998 #kg.m-3 à 20 Celcius
c = 4180 #J.kg-1.k-1

D = lambd / (rho * c)
largeur = 25  # Largeur du solide en m (selon x)
longueur = 50  # Longueur du solide en m (selon y)
hauteur = 3  # Hauteur du solide en m (selon z)
durée = 10*60*60  # Durée de l'expérience en s
Nx = 100 # Nombre de points selon x
Ny = 100  # Nombre de points selon y
Nz = 50  # Nombre de points selon z
T0 = 28 + 273.15  # Degrés Kelvin
extension = "caca"
#extension = "sin_amp2_moy30_convec"
temp_sol = 30 + 273.15
temp_air = 20 + 273.15


#éléments infinitésimaux
dx = longueur / Nx
dy = largeur / Ny
dz = hauteur / Nz
dt = min(dx**2 / (6*D), dy**2 / (6*D), dz**2 / (6*D))

print(durée/dt)

def save(tableau,extension,count):
    np.save('./' + extension + '/data' + extension + '_' + str(count*20) + '.npy', tableau)

#tableau de température 3D
t = np.zeros((Nx, Ny, Nz)) + T0

def est_sur_arrete(x,y,z):
    return \
    (z==0 and (x == 0 or x == Nx-1 or y==0 or y == Ny-1)) or (z==Nz-1 and (x == 0 or x == Nx-1 or y==0 or y == Ny-1)) or\
    (x==0 and (y == 0 or y == Ny-1 or z==0 or z == Nz-1)) or (x==Nx-1 and (y == 0 or y == Ny-1 or z==0 or z == Nz-1)) or\
    (y==0 and (x == 0 or x == Nx-1 or z==0 or z == Nz-1)) or (y==Ny-1 and (x == 0 or x == Nx-1 or z==0 or z == Nz-1))

def est_sur_sol(x,y,z):
    return z==0

def est_sur_lignes_sol_mur(x,y,z):
    return ( (z==0) and (int(Ny/3)-2 <=y and y<= int(Ny/3)+2 or 2*int(Ny/3)-2 <=y and y<= 2*int(Ny/3)+2)) \
        or (((y==0) or (y==Nx-1)) and (int(Nz/2)-2 <=z and z<= int(Nz/2)+2))

def est_sur_surface(x,y,z):
    return z==Nz-1
##################################################### Implémentation avec température sinusoîdale
periode_sin = 60*60 # 1 heure
pulsation_sin = 2*np.pi/periode_sin # rad.s**(-1)
moy_sin = temp_sol # Kelvin
amp_sin = 2 # Kelvin

def temp_sin(t,omega,a,temp_moy):
    return a*np.sin(omega * t) + temp_moy


#####################################################

# Créer une figure et des axes 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Boucle de simulation
temps = 0
tslice = durée / 5
count = 0


while temps < durée:
    ################################## Conditions aux limites temporelles
    """
    t_init = temp_sin(0,pulsation_sin,amp_sin,moy_sin)
    t[0, :, :] = t_init
    t[-1, :, :] = t_init
    t[:, 0, :] = t_init
    t[:, -1, :] = t_init
    t[:, :, 0] = t_init
    t[:, :, -1] = t_init
    """
    ##################################

    ################################## Conditions aux limites spaciales
    
    ##################################
    t1 = t.copy()
    for i in range(0, Nx):
        for j in range(0, Ny):
            for k in range(0, Nz):
                if est_sur_lignes_sol_mur(i,j,k):
                    t[i,j,k] = temp_sol                    
                elif est_sur_surface(i,j,k):
                    t[i,j,k] = (dz/(h*dz+lambd)) * (h*temp_air + lambd*t[i,j,k-1]/dz )
                else:
                    i1=i
                    j1=j
                    k1=k
                    D1=D

                    if i==0:
                        i1 = i+1
                    
                    if i==Nx-1:
                        i1=i-1
                    
                    if j==0:
                        j1 = j1+1
                    
                    if j==Ny-1:
                        j1 = j1-1
                    
                    if k ==0:
                        k1=k+1
                    
                    t[i, j, k] = (D1 * dt / dx**2) * (t1[i1+1, j, k] - 2*t1[i1, j, k] + t1[i1-1, j, k]) + \
                                (D1 * dt / dy**2) * (t1[i, j1+1, k] - 2*t1[i, j1, k] + t1[i, j1-1, k]) + \
                                (D1 * dt / dz**2) * (t1[i, j, k1+1] - 2*t1[i, j, k1] + t1[i, j, k1-1]) + t1[i,j,k]
    temps += dt
    if temps >= tslice*count :
        count = count + 1
        # Tracer la distribution de température en 3D
        ax.clear()
        X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), np.arange(Nz))
        ax.scatter(X, Y, Z, c=t.flatten() - 273.15, cmap=plt.cm.jet, vmin=0, vmax=100)
        ax.set_title("Distribution de température à t = " + str(round(temps, 5)) + " s")
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        save(t,extension,count-1)
        print(str(count*20 -20) + '%')

ax.clear()
X, Y, Z = np.meshgrid(np.arange(Nx), np.arange(Ny), np.arange(Nz))
ax.scatter(X, Y, Z, c=t.flatten() - 273.15, cmap=plt.cm.jet, vmin=0, vmax=100)
ax.set_title("Distribution de température à t = " + str(round(temps, 5)) + " s")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
save(t,extension,5)
print("done")