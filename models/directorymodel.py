import os


class DirectoryModel:
    def make_directory1(self):
        """
        Méthode qui détecte les fichiers : data, tournament, tournament_old et procède
        à leurs créations si manquant
        """
        data = os.getcwd()
        data_file1 = os.path.exists(f"{data}/data")
        data_file2 = os.path.exists(f"{data}/data/tournament/")
        data_file3 = os.path.exists(f"{data}/data/tournament_old")
        if not data_file1:
            os.mkdir(f"{data}/data")
        if not data_file2:
            os.mkdir(f"{data}/data/tournament")
        if not data_file3:
            os.mkdir(f"{data}/data/tournament_old")
