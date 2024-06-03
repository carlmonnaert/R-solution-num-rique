import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read(extension):
    dossier = "./" + extension + '/'
    Lx, Ly, Lz = 50, 25, 3  # Longueurs en mètres
    for datacount in range(6, 7):

        # Lire le fichier NPY
        u = np.load(dossier + 'data'+ extension + '_' + str(datacount*20) + '.npy') - 273.15

        # Définir les dimensions de la grille (assurez-vous qu'elles correspondent à celles utilisées lors de l'enregistrement)
        Nx, Ny, Nz = u.shape

        # Créer les coordonnées de la grille
        x = np.linspace(0, Lx, Nx)
        y = np.linspace(0, Ly, Ny)
        z = np.linspace(0, Lz, Nz)
        X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

        # Préparer les données pour la visualisation
        x_flat = X.flatten()
        y_flat = Y.flatten()
        z_flat = Z.flatten()
        u_flat = u.flatten()

        # Visualiser la distribution de température en 3D
        fig = plt.figure()
        figManager = plt.get_current_fig_manager()
        figManager.full_screen_toggle()  # Mettre la fenêtre en plein écran
        
        ax = fig.add_subplot(111, projection='3d')
        scat = ax.scatter(x_flat, y_flat, z_flat, c=u_flat, cmap='plasma')
        fig.colorbar(scat, ax=ax, label='Température au centre =' + str(round(np.min(u), 1)) + '°C')
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        if datacount != 6:
            plt.title('Distribution de température en 3D à ' + str(datacount*20) + '%')
        else:
            plt.title('Distribution de température en 3D en RP')

        plt.show()
