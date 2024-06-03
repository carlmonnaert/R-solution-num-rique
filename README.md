# Résolution-numérique
Résolution numérique de l'équation de la chaleur en 1D, 2D, 3D et lecteur de données

![alt_text, width="1px"](https://github.com/carlmonnaert/Resolution-numerique/blob/main/bloc_lignes_epaisses_mur_rp.png?raw=true)
![alt_text](https://github.com/carlmonnaert/Resolution-numerique/blob/main/bloc_plein_rp.png?raw=true)





## Résolution dans des cas simples:

Le fichier `Résolution1D.py` affiche la résolution de l'équation de la chaleur en 1D en temps réel pour une barre de conductivité thermique modifiable en début de code.
Cette barre est soumise à une température imposée à l'extrémité droite (temp_sol) et un flux conducto-convectif à gauche

Le fichier `Résolution2D.py` affiche la résolution de l'équation de la chaleur en 2D en temps réel pour un plan de conductivité thermique modifiable en début de code.
Ce plan est souis à une température imposée sur le tour (temp_sol)

Le fichier `Résolution3Djoli.py` affiche une résolution en 3D avec les mêmes conditions aux limites que pour la résolution en 2D


## Résolution dans des cas particuliers:

Les fichiers suivant résolvent l'équation de la chaleur pour un bassin de piscine soumis à une conducto-convection à sa surface, aucun flux thermique sur les côtés du bassin et une grille d'échangeur de géométrie personalisable sur le fond du bassin et éventuellement les côtés.

Les fichiers `Résolution3Drp.py` et `Résolution3Dopti.py` permettent la résolution de l'équation de la chaleur pour un bassin de piscine de dimensions olympiques et peut être adapté à tout autre système régi par la conduction thermique.

Il est nécessaire de créer un dossier du même nom que la variable extension, dossier dans lequel seront enregistrées des données par les exécutions de `Résolution3Drp.py` et `Résolution3Dopti.py`, auxquelles on pourra accéder par le lecteur `reader_all.py` dans lequel on entrera l'extension (nom du dossier) à visualiser.

L'exécution de Résolution3Drp étant très longue (environ 5 heures pour les fichiers joints), on présente dans les dossiers joints les résultats pour différentes géométries de l'échangeur eau chauffée/eau du bassin.

Ces données peuvent être visionnées par l'exécution de `reader_all.py`
