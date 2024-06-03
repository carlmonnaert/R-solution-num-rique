import data_reader_tranche
import data_reader_ligne
import data_reader_bloc

extension = str(input("Donner le nom de l'extension du fichier à lire: "))
data_reader_tranche.read(extension)
if(str(input("Afficher en 3D ? O ou N: ")) == "O"):
    data_reader_bloc.read(extension)
print("done")