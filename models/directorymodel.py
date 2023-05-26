import os
import shutil
import time


class DirectoryModel:
    def make_directory1(self):
        """
            Méthode qui recherche l'existance de plusieurs répertoires et procède à leurs créations si manquant
        """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        info_tournament = len(directory)
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

        if info_tournament >= 1:
            data_file5 = os.path.exists(f"{data}/data/tournament/{tournament_name}/Match")
            data_file6 = os.path.exists(f"{data}/data/tournament/{tournament_name}/Player_select")
            data_file7 = os.path.exists(f"{data}/data/tournament/{tournament_name}/Rounds")
            data_file8 = os.path.exists(f"{data}/data/tournament/{tournament_name}/Scores")
            data_file9 = os.path.exists(f"{data}/data/tournament/{tournament_name}/Final_Scores")
            if not data_file5:
                os.mkdir(f"{data}/data/tournament/{tournament_name}/Match")
            if not data_file6:
                os.mkdir(f"{data}/data/tournament/{tournament_name}/Player_select")
            if not data_file7:
                os.mkdir(f"{data}/data/tournament/{tournament_name}/Rounds")
            if not data_file8:
                os.mkdir(f"{data}/data/tournament/{tournament_name}/Scores")
            if not data_file9:
                os.mkdir(f"{data}/data/tournament/{tournament_name}/Final_Scores")

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

    def move_tournament_directory(self):
        dateiso = time.strftime("%Y_%m_%d_%H_%M")
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        original_path = f"{data}/data/tournament/{tournament_name}"
        destination_path = f"{data}/data/tournament_old/{dateiso}"
        shutil.move(original_path, destination_path)

