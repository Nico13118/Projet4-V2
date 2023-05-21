from models import TournamentModel, PlayerModel

import os
import json
import shutil
SCORE1 = 0.5
SCORE2 = 1.0
SCORE3 = 0.0

class DatabaseController:
    def add_tournament_in_json(self, tournamentmodel):
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        tournament_model = TournamentModel
        tournament = tournament_model.tournament_registration(tournamentmodel)
        with open(f"{data}/data/tournament/{tournament_name}/Tournament_Info.json", "w") as f:
            json.dump(tournament, f)

    def add_player_in_json(self, playermodel):
        """Méthode qui enregistre les joueurs dans la base de données List_Registered_Players.json, méthode qui peut ajouter des joueurs
        au fur et à mesure
        """
        temporarylist = []
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        directory1 = os.listdir(path)
        # Si le fichier json n'existe pas alors enregistre les données dans le fichier json
        if not directory1:
            player_model = PlayerModel
            playerlist = player_model.player_registration(playermodel)
            temporarylist.append(playerlist)
            with open(f"{path}/List_Registered_Players.json", "w") as f:
                json.dump(temporarylist, f)
        # Sinon si le fichier existe, alors extraire les données puis enregistrer l'ensemble dans le même fichier
        else:
            player_model = PlayerModel
            player = player_model.player_registration(playermodel)
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                for new_player_list in list_player:
                    temporarylist.append(new_player_list)
                temporarylist.append(player)
            with open(f"{path}/List_Registered_Players.json", "w") as g:
                json.dump(temporarylist, g)

    def chess_id_controller(self, chess_id):
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        playerlist = os.listdir(path)
        if not playerlist:
            return True
        else:
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                for list1 in list_player:
                    list2 = list1["identifiant"]
                    if chess_id == list2:
                        return False
                    return True

    def get_player_list(self):
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        playerlist = os.listdir(path)
        if not playerlist:
            return True
        else:
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                return list_player

    def sort_player_list_db(self, list_player):
        player_sorted = sorted(list_player, key=lambda x: (x["nom"], x["prenom"]))
        return player_sorted

    def sorted_by_player_order(self, temporary_list):
        """Méthode qui trie les joueurs par ordre de joueur"""
        players_sorted = sorted(temporary_list, key=lambda x: (x["joueur"]))
        return players_sorted

    def del_tournament_db(self):
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        shutil.rmtree(f"{data}/data/tournament/{tournament_name}")

    def add_player_in_json2(self, list_player):
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        with open(f"{path}/List_Registered_Players.json", "w") as g:
            json.dump(list_player, g)

    def del_player_in_list_db(self, user_input):
        """Supprimer le joueur dans la liste List_Registered_Players.json"""
        user_input -= 1
        list_player = self.get_player_list()
        player_sorted = self.sort_player_list_db(list_player)
        del player_sorted[user_input]
        self.add_player_in_json2(player_sorted)

    def get_list_registered_players_and_players_select(self):
        list_registered_players = self.get_player_list() # Base de données des joueurs
        list_player_select = self.get_list_player_select_db() # Liste de joueurs inscrits au tournoi
        for list_player_select1 in list_player_select:
            if list_player_select1 in list_registered_players:
                list_registered_players.remove(list_player_select1)
        return list_registered_players

    def get_list_match_and_round(self):
        """Méthode qui permet d'afficher les joueurs restants"""
        list_match = self.get_player_list_match()
        list_round = self.get_list_round()

        player_remove = [player["identifiant"] for player in list_round]
        list_match = [player for player in list_match if player["identifiant"] not in player_remove]
        return list_match



    def add_player_in_tournament_db(self, user_input):
        temporary_list = []
        user_input = int(user_input)
        user_input -= 1
        list_registered_players = self.get_player_list()  # Extraire les données de la liste List_Registered_Players.json
        player_sorted = self.sort_player_list_db(list_registered_players)  # Tries la liste des joueurs par ordre alphabétique
        player_select = player_sorted[user_input]  # Selection du joueur de list_registered_players
        temporary_list.append(player_select) # Le joueur selectionné est ajouté dans temporary_list
        self.add_player_select_in_json(temporary_list) # Enregistrement du joueur selectionné dans List_Players_Select.json

    def add_player_in_tournament_db2(self, user_input):
        temporary_list = []
        user_input -= 1
        list_player_select = self.get_list_player_select_db() # Obtenir la liste des joueurs inscrits dans List_Players_Select.json
        for list_player_select1 in list_player_select:
            temporary_list.append(list_player_select1)

        list_registered_players = self.get_list_registered_players_and_players_select() # Récupération de la base de données des joueurs
        player_select = list_registered_players[user_input]
        temporary_list.append(player_select)
        self.add_player_select_in_json(temporary_list)


    def del_player_in_list_player_select_db(self, user_input):
        user_input -= 1
        list_player_select = self.get_list_player_select_db()  # Récupération des données de list_player_select
        player_sorted = self.sort_player_list_db(list_player_select)
        del player_sorted[user_input]
        self.add_player_select_in_json(player_sorted)


    def add_player_select_in_json(self, player_select):
        """Enregistrement du ou des joueurs selectionné dans List_Players_Select.json"""

        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])

        path2 = f"{data}/data/tournament/{tournament_name}/Player_Select"
        with open(f"{path2}/List_Players_Select.json", "w") as f:
            json.dump(player_select, f)

    def get_list_player_select_db(self):
        """Récupération des données du fichier List_Players_Select.json """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Player_Select"
        with open(f"{path2}/List_Players_Select.json", "r") as f:
            list_player_select = json.load(f)
            return list_player_select

    def add_player_shuffle_in_list_match_json(self, temporary_list):
        number_files = self.number_files_in_list_match()
        number_files += 1
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        with open(f"{path2}/List_Match{number_files}.json", "w") as f:
            json.dump(temporary_list, f)

    def get_player_list_match(self):
        number_files = self.number_files_in_list_match()

        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        with open(f"{path2}/List_Match{number_files}.json", "r") as f:
            temporary_list = json.load(f)
            return temporary_list

    def get_list_round(self):
        number_files = self.number_files_in_list_match()

        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        with open(f"{path2}/Round{number_files}.json", "r") as f:
            temporary_list = json.load(f)
            return temporary_list

    def number_files_in_list_match(self):
        data = os.getcwd()
        path1 = f"{data}/data/tournament/"
        directory1 = os.listdir(path1)
        tournament_name = str(directory1[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        directory2 = os.listdir(path2)
        number_files = len(directory2)
        return number_files

    def number_files_round(self):
        data = os.getcwd()
        path1 = f"{data}/data/tournament/"
        directory1 = os.listdir(path1)
        tournament_name = str(directory1[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        directory2 = os.listdir(path2)
        number_files = len(directory2)
        return number_files

    def add_score_to_players(self, user_input, user_input2):

        if self.round_file_control():
            """Lorsque le fichier RoundX.json existe"""
            temporary_list = []
            list_player1 = []
            list_player2 = []
            list_round = self.get_list_round()  # Récupération des données du Fichier RoundX.json
            rounds = self.number_files_in_list_match()

            if user_input == 1:  # Choix 1 = Match Nul
                list_team = self.get_team(user_input2)  # Récupération de la liste des joueurs de list_match
                for list_team1 in list_team:
                    player = {
                        "Date et heure de debut": list_team1["Date et heure de debut"],
                        "couleur": list_team1["couleur"],
                        "identifiant": list_team1["identifiant"],
                        "nom": list_team1["nom"],
                        "prenom": list_team1["prenom"],
                        "naissance": list_team1["naissance"],
                        "joueur": list_team1["joueur"],
                        "round": rounds,
                        "score": SCORE1
                    }

                    temporary_list.append(player)
                for list_round1 in list_round:
                    temporary_list.append(list_round1)
                self.add_players_to_file_round2(temporary_list)

            if user_input == 2:  # Choix 1 = Gagnant / Perdant
                list_team = self.get_team(user_input2)
                select_player1 = list_team[0]
                list_player1.append(select_player1)
                for list_player2 in list_player1:
                    player = {
                        "Date et heure de debut": list_player2["Date et heure de debut"],
                        "couleur": list_player2["couleur"],
                        "identifiant": list_player2["identifiant"],
                        "nom": list_player2["nom"],
                        "prenom": list_player2["prenom"],
                        "naissance": list_player2["naissance"],
                        "joueur": list_player2["joueur"],
                        "round": rounds,
                        "score": SCORE2
                    }

                    temporary_list.append(player)
                list_team = self.get_team(user_input2)
                select_player2 = list_team[1]
                list_player2.append(select_player2)
                for list_player3 in list_player2:
                    player = {
                        "Date et heure de debut": list_player3["Date et heure de debut"],
                        "couleur": list_player3["couleur"],
                        "identifiant": list_player3["identifiant"],
                        "nom": list_player3["nom"],
                        "prenom": list_player3["prenom"],
                        "naissance": list_player3["naissance"],
                        "joueur": list_player3["joueur"],
                        "round": rounds,
                        "score": SCORE3
                    }

                    temporary_list.append(player)
                for list_round1 in list_round:
                    temporary_list.append(list_round1)
                self.add_players_to_file_round2(temporary_list)

        if not self.round_file_control():
            """ Si fichier RoundX.json n'existe pas"""
            temporary_list = []
            list_player1 = []
            list_player2 = []
            rounds = self.number_files_in_list_match()
            if user_input == 1: # Choix 1 = Match Nul
                list_team = self.get_team(user_input2)
                for list_team1 in list_team:
                    player = {
                        "Date et heure de debut": list_team1["Date et heure de debut"],
                        "couleur": list_team1["couleur"],
                        "identifiant": list_team1["identifiant"],
                        "nom": list_team1["nom"],
                        "prenom": list_team1["prenom"],
                        "naissance": list_team1["naissance"],
                        "joueur": list_team1["joueur"],
                        "round": rounds,
                        "score": SCORE1
                    }

                    temporary_list.append(player)

                self.add_players_to_file_round(temporary_list)

            if user_input == 2: # Choix 1 = Gagnant / Perdant
                list_team = self.get_team(user_input2)
                select_player1 = list_team[0]
                list_player1.append(select_player1)
                for list_player2 in list_player1:
                    player = {
                        "Date et heure de debut": list_player2["Date et heure de debut"],
                        "couleur": list_player2["couleur"],
                        "identifiant": list_player2["identifiant"],
                        "nom": list_player2["nom"],
                        "prenom": list_player2["prenom"],
                        "naissance": list_player2["naissance"],
                        "joueur": list_player2["joueur"],
                        "round": rounds,
                        "score": SCORE2
                    }

                    temporary_list.append(player)
                list_team = self.get_team(user_input2)
                select_player2 = list_team[1]
                list_player2.append(select_player2)
                for list_player3 in list_player2:
                    player = {
                        "Date et heure de debut": list_player3["Date et heure de debut"],
                        "couleur": list_player3["couleur"],
                        "identifiant": list_player3["identifiant"],
                        "nom": list_player3["nom"],
                        "prenom": list_player3["prenom"],
                        "naissance": list_player3["naissance"],
                        "joueur": list_player3["joueur"],
                        "round": rounds,
                        "score": SCORE3
                    }

                    temporary_list.append(player)

                self.add_players_to_file_round(temporary_list)


    def get_team(self, user_input2):
        """Permet de selectionner les 2 joueurs dans list_Match"""
        temporary_list = []

        if user_input2 == 1 or user_input2 == 2:
            if not self.round_file_control(): # Si mon fichier Round n'existe pas
                list_match = self.get_player_list_match()  # Récupération des données de List_MatchX.json
                select_player1 = list_match[0]
                temporary_list.append(select_player1)
                select_player2 = list_match[1]
                temporary_list.append(select_player2)
                return temporary_list
            if self.round_file_control(): # Si mon fichier Round existe
                list_match = self.get_list_match_and_round() # Récupération des joueurs restants
                select_player1 = list_match[0]
                temporary_list.append(select_player1)
                select_player2 = list_match[1]
                temporary_list.append(select_player2)
                return temporary_list

        if user_input2 == 3 or user_input2 == 4:
            if not self.round_file_control():
                list_match = self.get_player_list_match()  # Récupération des données de List_MatchX.json
                select_player1 = list_match[2]
                temporary_list.append(select_player1)
                select_player2 = list_match[3]
                temporary_list.append(select_player2)
                return temporary_list
            if self.round_file_control():
                list_match = self.get_list_match_and_round()
                select_player1 = list_match[2]
                temporary_list.append(select_player1)
                select_player2 = list_match[3]
                temporary_list.append(select_player2)
                return temporary_list

        if user_input2 == 5 or user_input2 == 6:
            if not self.round_file_control():
                list_match = self.get_player_list_match()  # Récupération des données de List_MatchX.json
                select_player1 = list_match[4]
                temporary_list.append(select_player1)
                select_player2 = list_match[5]
                temporary_list.append(select_player2)
                return temporary_list
            if self.round_file_control():
                list_match = self.get_list_match_and_round()
                select_player1 = list_match[4]
                temporary_list.append(select_player1)
                select_player2 = list_match[5]
                temporary_list.append(select_player2)
                return temporary_list

        if user_input2 == 7 or user_input2 == 8:
            if not self.round_file_control():
                list_match = self.get_player_list_match()  # Récupération des données de List_MatchX.json
                select_player1 = list_match[6]
                temporary_list.append(select_player1)
                select_player2 = list_match[7]
                temporary_list.append(select_player2)
                return temporary_list
            if self.round_file_control():
                list_match = self.get_list_match_and_round()
                select_player1 = list_match[6]
                temporary_list.append(select_player1)
                select_player2 = list_match[7]
                temporary_list.append(select_player2)
                return temporary_list

    def add_players_to_file_round(self, temporary_list):
        """Lorsque le fichier RoundX.json n'existe pas"""
        number_files = self.number_files_in_list_match()
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        with open(f"{path2}/Round{number_files}.json", "w") as f:
            json.dump(temporary_list, f)

    def add_players_to_file_round2(self, temporary_list):
        """Lorsque le fichier RoundX.json existe"""
        number_files = self.number_files_in_list_match()
        #number_files += 1
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        with open(f"{path2}/Round{number_files}.json", "w") as f:
            json.dump(temporary_list, f)

    def round_file_control(self):
        """Méthode qui controle la présence du fichier Round"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        directory_rounds = os.listdir(path2)
        if directory_rounds:
            return True
        else:
            return False

    def add_scores_to_players_in_file_score(self, temporary_list):
        number_files = self.number_files_in_list_match()
        # number_files += 1
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Scores"
        with open(f"{path2}/Score{number_files}.json", "w") as f:
            json.dump(temporary_list, f)
