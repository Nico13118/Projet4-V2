from models.tournamentmodel import TournamentModel
from models.playermodel import PlayerModel
import time
import os
import json
SCORE1 = 0.5
SCORE2 = 1.0
SCORE3 = 0.0


class DatabaseController:
    def __init__(self, controller):
        self.controller = controller

    def add_tournament_in_json(self, tournamentmodel):
        """Méthode qui enregistre les informations d'un tournoi dans Tournament_Info.json """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        tournament_model = TournamentModel
        tournament = tournament_model.tournament_registration(tournamentmodel)
        with open(f"{data}/data/tournament/{tournament_name}/Tournament_Info.json", "w") as f:
            json.dump(tournament, f)

    def add_player_in_json(self, playermodel):
        """Méthode qui enregistre les joueurs dans la base de données List_Registered_Players.json,
            La méthode peut ajouter des joueurs au fur et à mesure
        """
        temporarylist = []
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        directory1 = os.listdir(path)
        """Si le fichier json n'existe pas alors enregistre les données dans le fichier json"""
        player_model = PlayerModel
        playerlist = player_model.player_registration(playermodel)
        if not directory1:
            temporarylist.append(playerlist)
            with open(f"{path}/List_Registered_Players.json", "w") as f:
                json.dump(temporarylist, f)
        else:
            """Sinon si le fichier existe, alors extraire les données puis enregistre
                l'ensemble dans le même fichier
            """
            player = player_model.player_registration(playermodel)
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                for new_player_list in list_player:
                    temporarylist.append(new_player_list)
                temporarylist.append(player)
            with open(f"{path}/List_Registered_Players.json", "w") as g:
                json.dump(temporarylist, g)

    def add_player_in_json2(self, list_player):
        """Méthode qui enregistre les joueurs dans la base de données List_Registered_Players.json"""
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        with open(f"{path}/List_Registered_Players.json", "w") as g:
            json.dump(list_player, g)

    def add_player_in_tournament_db(self, user_input):
        """Méthode qui permet de selectionner un joueur dans la base de données puis l'enregistre dans le fichier
            pour inscription au tournoi
        """
        temporary_list = []
        user_input = int(user_input)
        user_input -= 1
        """ Extraire les données de la liste List_Registered_Players.json"""
        list_registered_players = self.get_player_list()
        """ Tries la liste des joueurs par ordre alphabétique"""
        player_sorted = self.sort_player_list_db(list_registered_players)
        """ Selection du joueur de list_registered_players"""
        player_select = player_sorted[user_input]
        """ Le joueur selectionné est ajouté dans temporary_list"""
        temporary_list.append(player_select)
        """ Enregistrement du joueur selectionné dans List_Players_Select.json"""
        self.add_player_select_in_json(temporary_list)

    def add_player_in_tournament_db2(self, user_input):
        """Méthode qui récupère la liste des joueurs inscrits au tournoi, selection du nouveau joueur inscrit
            puis enregistre l'ensemble dans le fichier List_Players_Select.json
        """
        temporary_list = []
        user_input -= 1
        """ Obtenir la liste des joueurs inscrits dans List_Players_Select.json"""
        list_player_select = self.get_list_player_select_db()
        for list_player_select1 in list_player_select:
            temporary_list.append(list_player_select1)

        """ Récupération de la base de données des joueurs"""
        list_registered_players = self.get_list_registered_players_and_players_select()
        player_select = list_registered_players[user_input]
        temporary_list.append(player_select)
        self.add_player_select_in_json(temporary_list)

    def add_player_select_in_json(self, player_select):
        """Méthode qui permet d'enregistrer un joueur selectionné pour le tournoi
            dans List_Players_Select.json
         """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Player_Select"
        with open(f"{path2}/List_Players_Select.json", "w") as f:
            json.dump(player_select, f)

    def add_player_shuffle_in_list_match_json(self, temporary_list):
        """Méthode qui permet d'enregistrer la liste des joueurs mélangés dans List_MatchX.json"""
        number_files = self.controller.player_list_controller.number_files_in_list_match()
        number_files += 1
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        with open(f"{path2}/List_Match{number_files}.json", "w") as f:
            json.dump(temporary_list, f)

    def add_players_to_file_round(self, temporary_list):
        """Méthode qui enregistre les joueurs dans le fichier RoundX.json"""
        number_files = self.controller.player_list_controller.number_files_in_list_match()
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        with open(f"{path2}/Round{number_files}.json", "w") as f:
            json.dump(temporary_list, f)

    def add_score_to_players(self, choice_score1, choice_player1, choice_player2):
        """Méthode qui ajoute les scores aux joueurs
            Si fichier RoundX.json n'existe pas
        """
        dateiso = time.strftime('%d/%m/%Y - %H:%M')
        temporary_list = []
        temporary_list_scoreboard = []
        rounds = self.controller.player_list_controller.number_files_in_list_match()

        """ Choix 1 = Match Nul"""
        if choice_score1 == 1:
            list_team = self.get_team_file_round_does_not_exist(choice_player1)
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
                    "score": SCORE1,
                    "Date et heure de fin": dateiso}

                temporary_list.append(player)
                temporary_list_scoreboard.append(player)
            self.add_players_to_file_round(temporary_list)
            self.controller.report_controller.add_players_in_file_scoreboard(temporary_list_scoreboard)

        """ Choix 2 = Gagnant / Perdant"""
        if choice_score1 == 2:
            player_wins = []
            player_loses = []
            list_team2 = self.get_winner_player(choice_player1, choice_player2)
            select_player1 = list_team2[0]
            player_wins.append(select_player1)
            for player_wins2 in player_wins:
                player = {
                    "Date et heure de debut": player_wins2["Date et heure de debut"],
                    "couleur": player_wins2["couleur"],
                    "identifiant": player_wins2["identifiant"],
                    "nom": player_wins2["nom"],
                    "prenom": player_wins2["prenom"],
                    "naissance": player_wins2["naissance"],
                    "joueur": player_wins2["joueur"],
                    "round": rounds,
                    "score": SCORE2,
                    "Date et heure de fin": dateiso}

                temporary_list.append(player)
                temporary_list_scoreboard.append(player)
            select_player2 = list_team2[1]
            player_loses.append(select_player2)
            for player_loses1 in player_loses:
                player = {
                    "Date et heure de debut": player_loses1["Date et heure de debut"],
                    "couleur": player_loses1["couleur"],
                    "identifiant": player_loses1["identifiant"],
                    "nom": player_loses1["nom"],
                    "prenom": player_loses1["prenom"],
                    "naissance": player_loses1["naissance"],
                    "joueur": player_loses1["joueur"],
                    "round": rounds,
                    "score": SCORE3,
                    "Date et heure de fin": dateiso}

                temporary_list.append(player)
                temporary_list_scoreboard.append(player)
            self.add_players_to_file_round(temporary_list)
            self.controller.report_controller.add_players_in_file_scoreboard(temporary_list_scoreboard)

    def add_score_to_players2(self, choice_score1, choice_player1, choice_player2):
        """Méthode qui ajoute les scores aux joueurs
            Si le fichier RoundX.json existe
        """
        temporary_list = []
        temporary_list_scoreboard = []
        dateiso = time.strftime('%d/%m/%Y - %H:%M')
        """ Récupération des données du Fichier RoundX.json"""
        list_round = self.get_list_round()
        rounds = self.controller.player_list_controller.number_files_in_list_match()

        """ Choix 1 = Match Nul"""
        if choice_score1 == 1:
            for list_round1 in list_round:
                temporary_list.append(list_round1)
            dateiso = time.strftime('%d/%m/%Y - %H:%M')
            """ Récupération de la liste des joueurs de list_match"""
            list_team = self.get_team_file_round_exist(choice_player1)
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
                    "score": SCORE1,
                    "Date et heure de fin": dateiso}

                temporary_list.append(player)
                temporary_list_scoreboard.append(player)
            self.add_players_to_file_round(temporary_list)
            self.controller.report_controller.add_players_in_file_scoreboard(temporary_list_scoreboard)

        """" Choix 2 = Gagnant / Perdant"""
        if choice_score1 == 2:
            player_wins = []
            player_loses = []
            for list_round1 in list_round:
                temporary_list.append(list_round1)
            list_team = self.get_winner_player(choice_player1, choice_player2)
            select_player1 = list_team[0]
            player_wins.append(select_player1)
            for player_wins1 in player_wins:
                player = {
                    "Date et heure de debut": player_wins1["Date et heure de debut"],
                    "couleur": player_wins1["couleur"],
                    "identifiant": player_wins1["identifiant"],
                    "nom": player_wins1["nom"],
                    "prenom": player_wins1["prenom"],
                    "naissance": player_wins1["naissance"],
                    "joueur": player_wins1["joueur"],
                    "round": rounds,
                    "score": SCORE2,
                    "Date et heure de fin": dateiso}

                temporary_list.append(player)
                temporary_list_scoreboard.append(player)
            select_player2 = list_team[1]
            player_loses.append(select_player2)
            for player_loses1 in player_loses:
                player = {
                    "Date et heure de debut": player_loses1["Date et heure de debut"],
                    "couleur": player_loses1["couleur"],
                    "identifiant": player_loses1["identifiant"],
                    "nom": player_loses1["nom"],
                    "prenom": player_loses1["prenom"],
                    "naissance": player_loses1["naissance"],
                    "joueur": player_loses1["joueur"],
                    "round": rounds,
                    "score": SCORE3,
                    "Date et heure de fin": dateiso}

                temporary_list.append(player)
                temporary_list_scoreboard.append(player)
            self.add_players_to_file_round(temporary_list)
            self.controller.report_controller.add_players_in_file_scoreboard(temporary_list_scoreboard)

    def chess_id_controller(self, chess_id):
        """Méthode qui permet de controller qu'il n'y a pas d'identifiant en double
            lors de l'inscription d'un joueur dans List_Registered_Players.json
        """
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
                    if list2 == chess_id:
                        return False
                return True

    def del_player_in_list_player_select_db(self, user_input):
        """Méthode qui supprime un joueur dans la liste list_player_select"""
        user_input -= 1
        """ Récupération des données de list_player_select"""
        list_player_select = self.get_list_player_select_db()
        player_sorted = self.sort_player_list_db(list_player_select)
        del player_sorted[user_input]
        self.add_player_select_in_json(player_sorted)

    def del_player_in_list_db(self, user_input):
        """Méthode qui supprime un joueur dans la liste List_Registered_Players.json"""
        user_input -= 1
        list_player = self.get_player_list()
        player_sorted = self.sort_player_list_db(list_player)
        del player_sorted[user_input]
        self.add_player_in_json2(player_sorted)

    def get_player_list(self):
        """Méthode qui retourne les informations du fichier List_Registered_Players.json """
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        with open(f"{path}/List_Registered_Players.json", "r") as f:
            list_registered_players = json.load(f)
            return list_registered_players

    def get_list_registered_players_and_players_select(self):
        """Méthode qui permet d'afficher le restant des joueurs qui n'ont pas été selectionnés
            pour inscription au tournoi
        """
        """ Base de données des joueurs"""
        list_registered_players = self.get_player_list()
        """ Liste de joueurs inscrits au tournoi"""
        list_player_select = self.get_list_player_select_db()
        for list_player_select1 in list_player_select:
            if list_player_select1 in list_registered_players:
                list_registered_players.remove(list_player_select1)
        return list_registered_players

    def get_list_match_and_round(self):
        """Méthode qui permet d'afficher les joueurs sans scores"""
        list_match = self.get_player_list_match()
        list_round = self.get_list_round()

        player_remove = [player["identifiant"] for player in list_round]
        list_match1 = [player for player in list_match if player["identifiant"] not in player_remove]
        return list_match1

    def get_list_player_select_db(self):
        """Méthode qui retourne les informations du fichier List_Players_Select.json """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Player_Select"
        with open(f"{path2}/List_Players_Select.json", "r") as f:
            list_player_select = json.load(f)
            return list_player_select

    def get_list_player_select_report(self, tournament_name):
        """Méthode qui retourne les informations du fichier List_Players_Select.json
            pour le rapport des tournois précédents
        """
        data = os.getcwd()
        with open(f"{data}/data/tournament_old/{tournament_name}/Player_Select/List_Players_Select.json", "r") as f:
            list_player_select = json.load(f)
            return list_player_select

    def get_player_list_match(self):
        """Méthode qui retourne les informations du fichier List_MatchX.json"""
        number_files = self.controller.player_list_controller.number_files_in_list_match()
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        with open(f"{path2}/List_Match{number_files}.json", "r") as f:
            temporary_list = json.load(f)
            return temporary_list

    def get_match_list_for_report(self, number_files1):
        """Méthode qui permet de retourner les données de List_MatchX.json selon le nombre de fichiers demandés"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        with open(f"{path2}/List_Match{number_files1}.json", "r") as f:
            match_list = json.load(f)
            return match_list

    def get_match_list_old_tournament(self, tournament_name, number_files1):
        """Méthode qui permet de retourner les données de List_MatchX.json pour le rapport des tournois précédents"""
        data = os.getcwd()
        path = f"{data}/data/tournament_old/"
        with open(f"{path}/{tournament_name}/Match/List_Match{number_files1}.json", "r") as f:
            infos_match_list = json.load(f)
            return infos_match_list

    def get_list_round(self):
        """Méthode qui retourne les informations du fichier RoundX.json"""
        number_files = self.controller.player_list_controller.number_files_round()
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        with open(f"{path2}/Round{number_files}.json", "r") as f:
            temporary_list = json.load(f)
            return temporary_list

    def get_round_list_for_report(self, number_files1):
        """Méthode qui permet de retourner les données de RoundsX.json selon le nombre de fichiers demandés"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        with open(f"{path2}/Round{number_files1}.json", "r") as f:
            round_list = json.load(f)
            return round_list

    def get_round_list_old_tournament(self, tournament_name, number_files1):
        """Méthode qui permet de retourner les informations du fichier RoundX.json
            pour le rapport des tournois précédents
        """
        data = os.getcwd()
        path = f"{data}/data/tournament_old"
        with open(f"{path}/{tournament_name}/Rounds/Round{number_files1}.json", "r") as f:
            round_list = json.load(f)
            return round_list

    def get_winner_player(self, choice_player1, choice_player2):
        """Méthode qui permet de selectionner le joueur qui gagne (Option Gagnant / Perdant)
            Si le fichier RoundX.json existe
        """
        number_list_match_file = self.controller.player_list_controller.number_files_in_list_match()
        number_rounds_file = self.controller.player_list_controller.number_files_round()
        if number_list_match_file == number_rounds_file:
            temporary_list = []
            choice_player1 = int(choice_player1)
            choice_player2 = int(choice_player2)
            player_list = self.get_team_file_round_exist(choice_player1)
            if choice_player2 == 1:
                select_player1 = player_list[0]
                temporary_list.append(select_player1)
                select_player2 = player_list[1]
                temporary_list.append(select_player2)
                return temporary_list

            if choice_player2 == 2:
                select_player1 = player_list[1]
                temporary_list.append(select_player1)
                select_player2 = player_list[0]
                temporary_list.append(select_player2)
                return temporary_list
        else:
            """Sinon si le fichier RoundX.json n'existe pas"""
            temporary_list = []
            player_list = self.get_team_file_round_does_not_exist(choice_player1)
            if choice_player2 == 1:
                select_player1 = player_list[0]
                temporary_list.append(select_player1)
                select_player2 = player_list[1]
                temporary_list.append(select_player2)
                return temporary_list

            if choice_player2 == 2:
                select_player1 = player_list[1]
                temporary_list.append(select_player1)
                select_player2 = player_list[0]
                temporary_list.append(select_player2)
                return temporary_list

    def get_winner_tournament(self, sort_final_scores, tournament_info):
        """Méthode qui permet de selectionner le joueur qui remporte le tournoi, mais peut selectionner
            2 à 3 joueurs si ex-eaquo.
         """
        list_winner1 = []
        list_winner2 = []
        list_winner3 = []
        list_winner4 = []
        list_winner5 = []
        list_winner6 = []
        for sort_final_scores1 in sort_final_scores:
            number_rounds = self.number_rounds_in_tournament_file(tournament_info)
            number_rounds = float(number_rounds)
            player_score = sort_final_scores1["score"]
            if player_score == number_rounds:
                list_winner1.append(sort_final_scores1)
            number_rounds -= 0.5
            if player_score == number_rounds:
                list_winner2.append(sort_final_scores1)
            number_rounds -= 0.5
            if player_score == number_rounds:
                list_winner3.append(sort_final_scores1)
            number_rounds -= 0.5
            if player_score == number_rounds:
                list_winner4.append(sort_final_scores1)
            number_rounds -= 0.5
            if player_score == number_rounds:
                list_winner5.append(sort_final_scores1)
            number_rounds -= 0.5
            if player_score == number_rounds:
                list_winner6.append(sort_final_scores1)
        info_winner1 = len(list_winner1)
        info_winner2 = len(list_winner2)
        info_winner3 = len(list_winner3)
        info_winner4 = len(list_winner4)
        info_winner5 = len(list_winner5)
        info_winner6 = len(list_winner6)
        if info_winner1 == 1 or info_winner1 == 2 or info_winner1 == 3:
            return list_winner1
        if info_winner2 == 1 or info_winner2 == 2 or info_winner2 == 3:
            return list_winner2
        if info_winner3 == 1 or info_winner3 == 2 or info_winner3 == 3:
            return list_winner3
        if info_winner4 == 1 or info_winner4 == 2 or info_winner4 == 3:
            return list_winner4
        if info_winner5 == 1 or info_winner5 == 2 or info_winner5 == 3:
            return list_winner5
        if info_winner6 == 1 or info_winner6 == 2 or info_winner6 == 3:
            return list_winner6

    def get_team_file_round_does_not_exist(self, user_input2):
        """Permet de selectionner les 2 joueurs dans list_Match
            Si mon fichier RoundX.json n'existe pas
        """
        temporary_list = []
        list_match = self.get_player_list_match()  # Récupération des données de List_MatchX.json
        user_input2 = int(user_input2)
        if user_input2 == 1 or user_input2 == 2:
            select_player1 = list_match[0]
            temporary_list.append(select_player1)
            select_player2 = list_match[1]
            temporary_list.append(select_player2)
            return temporary_list

        if user_input2 == 3 or user_input2 == 4:
            select_player1 = list_match[2]
            temporary_list.append(select_player1)
            select_player2 = list_match[3]
            temporary_list.append(select_player2)
            return temporary_list

        if user_input2 == 5 or user_input2 == 6:
            select_player1 = list_match[4]
            temporary_list.append(select_player1)
            select_player2 = list_match[5]
            temporary_list.append(select_player2)
            return temporary_list

        if user_input2 == 7 or user_input2 == 8:
            select_player1 = list_match[6]
            temporary_list.append(select_player1)
            select_player2 = list_match[7]
            temporary_list.append(select_player2)
            return temporary_list

    def get_team_file_round_exist(self, user_input2):
        """Permet de selectionner les 2 joueurs dans list_Match
            Si mon fichier RoundX.json existe.
        """
        temporary_list = []
        user_input2 = int(user_input2)
        if user_input2 == 1 or user_input2 == 2:
            """ Récupération des joueurs restants"""
            remaining_player_liste = self.get_list_match_and_round()
            select_player1 = remaining_player_liste[0]
            temporary_list.append(select_player1)
            select_player2 = remaining_player_liste[1]
            temporary_list.append(select_player2)
            return temporary_list

        if user_input2 == 3 or user_input2 == 4:
            """ Récupération des joueurs restants"""
            remaining_player_liste = self.get_list_match_and_round()
            select_player1 = remaining_player_liste[2]
            temporary_list.append(select_player1)
            select_player2 = remaining_player_liste[3]
            temporary_list.append(select_player2)
            return temporary_list

        if user_input2 == 5 or user_input2 == 6:
            """ Récupération des joueurs restants"""
            remaining_player_liste = self.get_list_match_and_round()
            select_player1 = remaining_player_liste[4]
            temporary_list.append(select_player1)
            select_player2 = remaining_player_liste[5]
            temporary_list.append(select_player2)
            return temporary_list

        if user_input2 == 7 or user_input2 == 8:
            """ Récupération des joueurs restants"""
            remaining_player_liste = self.get_list_match_and_round()
            select_player1 = remaining_player_liste[6]
            temporary_list.append(select_player1)
            select_player2 = remaining_player_liste[7]
            temporary_list.append(select_player2)
            return temporary_list

    def get_tournament_information(self):
        """Méthode qui récupère toutes les informations du fichier tournament_information.json"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        with open(f"{data}/data/tournament/{tournament_name}/Tournament_Info.json", "r") as f:
            tournament_info = json.load(f)
            return tournament_info

    def get_old_tournament_information(self, tournament_name):
        """Méthode qui récupère toutes les informations du fichier tournament_information.json du tournoi précédent"""
        data = os.getcwd()
        with open(f"{data}/data/tournament_old/{tournament_name}/Tournament_Info.json", "r") as f:
            tournament_info = json.load(f)
            return tournament_info

    def number_rounds_in_tournament_file(self, tournament_info):
        """Méthode qui récupère le nombre de Rounds qu'il y a dans le fichier Tournament_information.json """
        for tournament_info1 in tournament_info:
            number_rounds = tournament_info1["rounds"]
            return number_rounds

    def sort_player_list_db(self, list_player):
        """Méthode qui trie la liste par ordre alphabétique"""
        player_sorted = sorted(list_player, key=lambda x: (x["nom"], x["prenom"]))
        return player_sorted

    def sorted_by_player_order(self, temporary_list):
        """Méthode qui trie les joueurs par ordre de joueur"""
        players_sorted = sorted(temporary_list, key=lambda x: (x["joueur"]))
        return players_sorted

    def sort_player_list_score(self, list_score):
        """Méthode qui trie par ordre de score"""
        list_score_sorted = sorted(list_score, key=lambda x: (x["score"]), reverse=True)
        return list_score_sorted
