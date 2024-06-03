import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def read(extension):
    dossier = "./" + extension + '/'
    for datacount in range(0, 7):
        # Lire le fichier NPY
        u = np.load(dossier + 'data' + extension + '_' + str(datacount*20) + '.npy') - 273.15

        # Définir les dimensions de la grille (assurez-vous qu'elles correspondent à celles utilisées lors de l'enregistrement)
        Nx, Ny, Nz = u.shape

        # Créer les coordonnées de la grille pour la tranche avec les dimensions spécifiées
        y = np.linspace(0, 25, Ny)
        z = np.linspace(0, 3, Nz)
        Y, Z = np.meshgrid(y, z, indexing='ij')

        # Sélectionner la tranche
        milieu = int(Nx / 2)
        u_slice = u[milieu, :, :]

        # Préparer les données pour la visualisation de la tranche
        y_flat = Y.flatten()
        z_flat = Z.flatten()
        u_flat = u_slice.flatten()

        # Visualiser la distribution de température de la tranche en 3D
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        scat = ax.scatter(np.full_like(y_flat, 50), y_flat, z_flat, c=u_flat, cmap='plasma')
        fig.colorbar(scat, ax=ax, label='Température (°C)')
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Z (m)')
        if datacount != 6:
            plt.title('Distribution de température en 3D à ' + str(datacount * 20) + '%')
        else:
            plt.title('Distribution de température en 3D en RP')
        plt.show()
