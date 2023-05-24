import os
import shutil

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
        data_file4 = os.path.exists(f"{data}/data/players_list")
        if not data_file1:
            os.mkdir(f"{data}/data")
        if not data_file2:
            os.mkdir(f"{data}/data/tournament")
        if not data_file3:
            os.mkdir(f"{data}/data/tournament_old")
        if not data_file4:
            os.mkdir(f"{data}/data/tournament/players_list")

    def make_directory_tournament(self, tournament_name):
        data = os.getcwd()
        os.mkdir(f"{data}/data/tournament/{tournament_name}")
        os.mkdir(f"{data}/data/tournament/{tournament_name}/Rounds")
        os.mkdir(f"{data}/data/tournament/{tournament_name}/Scores")
        os.mkdir(f"{data}/data/tournament/{tournament_name}/Player_Select")
        os.mkdir(f"{data}/data/tournament/{tournament_name}/Match")

    def del_tournament_db(self):
        """Méthode qui permet de supprimer le répertoire tournament """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        shutil.rmtree(f"{data}/data/tournament/{tournament_name}")
        