# Résolution-numérique
Résolution numérique de l'équation de la chaleur en 1D , 2D , 3D et lecteur de données


## Résolution dans des cas simples:

Le fichier `Résolution1D.py` affiche la résolution de l'équation de la chaleur en 1D en temps réel pour une barre de conductivité thermique modifiable en début de code.
Cette barre est soumise à une température imposée à l'extrémité droite (temp_sol) et un flux conducto-convectif à gauche

Le fichier 'Résolution2D.py' affiche la résolution de l'équation de la chaleur en 2D en temps réel pour un plan de conductivité thermique modifiable en début de code.
Ce plan est souis à une température imposée sur le tour (temp_sol)

Le fichier Résolution3Djoli affiche une résolution en 3D avec les mêmes conditions aux limites que pour la résolution en 2D


## Résolution dans des cas particuliers:

Les fichiers suivant résolvent l'équation de la chaleur pour un bassin de piscine soumis à une conducto-convection à sa surface, aucun flux thermique sur les côtés du bassin et une grille d'échangeur de géométrie personalisable sur le fond du bassin et éventuellement les côtés.

Les fichiers Résolution3Drp et Résolution3Dopti permettent la résolution de l'équation de la chaleur pour un bassin de piscine de dimensions olympiques et peut être adapté à tout autre système régi par la conduction thermique.

Il est nécéssaire de crééer un dossier du même nom que la variable extension, dossier dans lequel seront enregistrés des données auxquelles on pourra accéder par le lecteur reader_all dans lequel on entrera l'extension choisie.

L'exécution de Résolution3Drp étant très longue (environ 5 heures pour les conditions données), on présente dans les fichiers plein_rp_moy30_convection et deux_lignes_mur_1m25_rp_moy30_convec les résultats pour deux dispositions différentes de l'échangeur eau chauffée/eau du bassin.
Ces données peuvent être lues par reader_all en enregistrant les fichiers dans un dossier portant le nom de l'extension, dossier enregistré dans le même que le reste des codes python
