import numpy as np 
import matplotlib.pyplot as plt 

""" Equation de la chaleur sous la forme dT/dt = lambda/(rô C) d²T/dx² où lambda/(rô C) = D"""

h = 5 #W.K-1.m-2 

lambd = 0.604 #W.m-1.K-1
rho = 998 #kg.m-3 à 20 Celcius
c = 4180 #J.kg-1.k-1

D = lambd / (rho * c)
longeur = 0.3 # Longeur de la barre en m
durée = 100*60*60 # Durée de l'expérience en s
N = 100 # Nombre de points
T0 = 25 + 273.15  # Degrés Kelvin
extension = "plein_rp_moy30_convec"
#extension = "sin_amp2_moy30_convec"
temp_sol = 30 + 273.15
temp_air = 20 + 273.15

dx = longeur / N
dt = dx**2 / (2*D)

tx = np.zeros(N) + T0 # On initialise la température à T0
tx[0] = temp_sol
tx[-1] = temp_air

fig , axe = plt.subplots()
pcm = axe.pcolormesh([tx - 273.15], cmap = plt.cm.jet, vmin = 20, vmax = 30)
plt.colorbar(pcm,ax = axe)
axe.set_ylim([-2,3])


# Boucle :

temps = 0
while True :
    tx1 = tx.copy()
    tx1[0] = temp_sol
    tx1[N-1] = (dx/(h*dx+lambd)) * (h*temp_air + lambd*tx[N-1]/dx )
    for i in range (1 , N - 1):
        tx[i] = (D * dt / dx**2) * ( tx1[i+1] - 2*tx1[i] + tx1[i-1] ) + tx1[i] # Au premier ordre
    temps = temps + dt
    pcm.set_array([tx - 273.15])
    axe.set_title("Apperçu pour t =" + str(round(temps - dt,5)) + "s")
    plt.pause(0.001)
    print(tx[0])


plt.show()