import os
import json


class ReportController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def current_tournament_report(self, choice_of_repport):
        """Pour afficher les informations du tournoi en cours"""
        if choice_of_repport == 1:
            """Affichage terminal"""
            if self.dm.control_tournament_directory():
                tournament_info1 = self.db.get_tournament_information()
                self.view.report_message()
                self.view.print_tournament_info(tournament_info1)
                """Appel des autres méthodes pour afficher :
                    La liste des joueurs inscrits au tournoi 
                    Le tableau des équipes
                    Les rounds en cours
                    Les classements des joueurs
                 """
                self.current_player_report(choice_of_repport)
                self.match_in_progress()
                self.score_in_progress(choice_of_repport)
                self.controller.menu_controller.run_menu_report()
            else:
                self.view.message_no_tournament_directory()
                self.controller.menu_controller.run_menu_report()
        if choice_of_repport == 2:
            """Enregistrement des données dans un fichier TXT"""
            self.current_tournament_text_format(choice_of_repport)

    def current_tournament_text_format(self, choice_of_repport):
        data = os.getcwd()
        path = f"{data}/data"
        if self.dm.control_tournament_directory():
            tournament_info2 = self.db.get_tournament_information()
            list_player_select = self.current_player_report(choice_of_repport)

            with open(f"{path}/Rapport_tournoi_en_cours.txt", "w") as f:
                f.write(f"=======Rapport du tournoi en cours=======\n\n")
                for tournament_info3 in tournament_info2:
                    name = tournament_info3["nom"]
                    place = tournament_info3["lieu"]
                    date1 = tournament_info3["date1"]
                    date2 = tournament_info3["date2"]
                    remark = tournament_info3["remarques"]
                    rounds = tournament_info3["rounds"]
                    f.write(f"Nom du tournoi : {name}\n")
                    f.write(f"Lieu : {place}\n")
                    f.write(f"Date de début : {date1}\n")
                    f.write(f"Date de fin : {date2}\n")
                    f.write(f"Remarques : {remark}\n")
                    f.write(f"Nombre de Rounds : {rounds}\n")

            with open(f"{path}/Rapport_tournoi_en_cours.txt", "a") as f:
                f.write("\n=======Liste des joueurs inscrits au tournoi=======\n\n")
                for list_player_select1 in list_player_select:
                    f.write(f"ID : {list_player_select1['identifiant']} Nom : {list_player_select1['nom']}"
                            f"  {list_player_select1['prenom']:}\n")

            if self.controller.player_list_controller.list_match_file_control():
                number_files_in_list_match = self.controller.player_list_controller.number_files_in_list_match()
                number_files1 = 1

                while not number_files1 > number_files_in_list_match:
                    with open(f"{path}/Rapport_tournoi_en_cours.txt", "a") as f:
                        """Affichage du tableau des équipes """
                        match_list = self.db.get_match_list_for_report(number_files1)
                        f.write(f"\n=======Tableau des équipes Round: {number_files1}=======\n\n")
                        match_number = 1
                        for i in range(0, len(match_list), 2):
                            player1 = match_list[i]
                            player2 = match_list[i + 1]
                            f.write(f"Match {match_number}: Joueur {player1['joueur']} - {player1['nom']:<9} "
                                    f"{player1['prenom']:<10} VS\t Joueur {player2['joueur']} - {player2['nom']} "
                                    f"{player2['prenom']}\n")
                            match_number += 1
                        """Affichage des résultats des Rounds"""
                        try:
                            vs = "VS"
                            round_list = self.db.get_round_list_for_report(number_files1)
                            f.write(f"\n=======Résultats Round: {number_files1}=======\n\n")
                            for i in range(0, len(round_list), 2):
                                player1 = round_list[i]
                                player2 = round_list[i + 1]
                                f.write(f"Date et heure de début : {player1['Date et heure de debut']}\n")
                                f.write(f"Joueur {player1['joueur']} - "
                                        f"{player1['nom']} {player1['prenom']} Score {player1['score']:<5} "
                                        f"{vs:<3} Joueur {player2['joueur']} - "
                                        f"{player2['nom']} {player2['prenom']} Score {player2['score']}\n")
                                f.write(f"Date et heure de fin : {player2['Date et heure de fin']}\n")
                                f.write("\n========================================================================\n")
                            number_files1 += 1
                        except:
                            f.write(f"\n=======Aucun résultat à afficher pour le Round {number_files1}=======\n")
                            break
                with open(f"{path}/Rapport_tournoi_en_cours.txt", "a") as f:
                    f.write("==================================================================================\n")
                    f.write("=======Classement des joueurs=======\n\n")
                """Affichage du classement des joueurs"""
                list_score_sorted = self.score_in_progress(choice_of_repport)
                for list_score_sorted1 in list_score_sorted:
                    with open(f"{path}/Rapport_tournoi_en_cours.txt", "a") as f:
                        f.write(f"Joueur {list_score_sorted1['joueur']}: {list_score_sorted1['nom']:<9} "
                                f"{list_score_sorted1['prenom']:<9} Score :{list_score_sorted1['score']}\n")

                self.view.current_tournament_report_path(path)
                self.controller.menu_controller.run_menu_report()

        else:
            self.view.message_no_tournament_directory()
            self.controller.menu_controller.run_menu_report()

    def current_player_report(self, choice_of_repport):
        """Pour afficher la liste des joueurs inscrits au tournoi"""
        if choice_of_repport == 1:
            if self.controller.player_list_controller.control_player_select_controller():
                list_player_select = self.db.get_list_player_select_db()
                list_player_select = self.db.sort_player_list_db(list_player_select)
                self.view.message_list_of_players_selected()
                self.view.show_selected_players(list_player_select)
            else:
                self.view.no_list_of_players_selected()
                self.controller.menu_controller.run_menu_report()
        if choice_of_repport == 2:
            list_player_select = self.db.get_list_player_select_db()
            list_player_select = self.db.sort_player_list_db(list_player_select)
            return list_player_select

    def match_in_progress(self):
        """Pour afficher le tableau des équipes """
        if self.controller.player_list_controller.list_match_file_control():
            number_files_in_list_match = self.controller.player_list_controller.number_files_in_list_match()
            number_files1 = 1
            while not number_files1 > number_files_in_list_match:
                """Affichage du tableau des équipes """
                match_list = self.db.get_match_list_for_report(number_files1)
                self.view.table_of_teams(match_list, number_files1)
                """Affichage des résultats des Rounds"""
                try:
                    round_list = self.db.get_round_list_for_report(number_files1)
                    self.view.show_round_list(round_list, number_files1)
                    number_files1 += 1
                except:
                    self.view.no_list_of_laps_to_display(number_files1)
                    break
        else:
            self.view.no_match_list_to_display()

    def score_in_progress(self, choice_of_repport):
        """
            Pour afficher le classement des joueurs par score
        """
        if choice_of_repport == 1:
            players_score = self.get_scoreboard()
            list_score_sorted = self.db.sort_player_list_score(players_score)
            self.view.scoreboard_view(list_score_sorted)
        if choice_of_repport == 2:
            players_score = self.get_scoreboard()
            list_score_sorted = self.db.sort_player_list_score(players_score)
            return list_score_sorted

    def add_players_in_file_scoreboard(self, player_list):
        """Méthode qui permet d'enregistrer les données dans le fichier scoreboard.json """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/ScoreBoard"

        """Si le fichier scoreboard.json n'existe pas"""
        if not self.controller.player_list_controller.list_scoreboard_file_control():
            with open(f"{path2}/ScoreBoard.json", "w") as f:
                json.dump(player_list, f)
        else:
            """Si le fichier scoreboard.json existe et qu'il contient 8 joueurs"""
            news_list = []
            number_players = self.control_number_player_in_list_scoreboard()
            if number_players == 8:
                """Récupérer les données du fichier scoreboard.json et la liste contenant les 2 joueurs """
                list_scoreboard = self.get_scoreboard()
                for player_list1 in player_list:
                    player_list1_id = player_list1["identifiant"]
                    player_list1_score = player_list1["score"]

                    for list_scoreboard1 in list_scoreboard:
                        if list_scoreboard1["identifiant"] == player_list1_id:
                            list_scoreboard1["score"] = list_scoreboard1["score"] + player_list1_score
                            break
                for list_scoreboard1 in list_scoreboard:
                    news_list.append(list_scoreboard1)
                with open(f"{path2}/ScoreBoard.json", "w") as f:
                    json.dump(news_list, f)
            else:
                """Sinon si le fichier scoreboard.json existe mais ne contient pas 8 joueurs"""
                """Récupérer les données de la liste de scoreboard et la liste contenant les 2 joueurs"""
                temporary_list = []
                list_scoreboard = self.get_scoreboard()
                for list_scoreboard1 in list_scoreboard:
                    temporary_list.append(list_scoreboard1)

                for player_list1 in player_list:
                    temporary_list.append(player_list1)

                player_sorted = self.db.sorted_by_player_order(temporary_list)
                with open(f"{path2}/ScoreBoard.json", "w") as f:
                    json.dump(player_sorted, f)

    def get_scoreboard(self):
        """Méthode qui retourne les informations du fichier ScoreBoard.json """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/ScoreBoard"
        with open(f"{path2}/ScoreBoard.json", "r") as f:
            list_scoreboard = json.load(f)
            return list_scoreboard

    def control_number_player_in_list_scoreboard(self):
        """Méthode qui permet de connaitre le nombre de joueurs dans le fichier scoreboard.json"""
        list_scoreboard = self.get_scoreboard()
        numbers_in_scoreboard = len(list_scoreboard)
        return numbers_in_scoreboard

    def show_previous_tournaments(self, choice_of_repport):
        """Afficher les informations des tournois précédents"""

        """Récupération du ou des noms des répertoires des tournois précedents"""
        if choice_of_repport == 1:
            old_tournament1 = self.dm.get_old_tournaments()
            """Boucle qui va afficher le nom du premier répertoire"""
            """old_tournament1 = un nom de répertoire """
            for old_tournament2 in old_tournament1:
                """Récupération des informations du tournoi concerné"""
                tournament_info1 = self.db.get_old_tournament_information(old_tournament2)
                """Message qui affiche 'Rapport des tournois précedents'"""
                self.view.report_old_tournament()
                """Affiche les informations du tournoi concerné"""
                self.view.print_tournament_info(tournament_info1)
                """Récupération des données du fichier List_Players_Select.json"""
                list_player_select = self.db.get_list_player_select_report(old_tournament2)
                """Trier la liste par ordre alphabétique"""
                player_sorted = self.db.sort_player_list_db(list_player_select)
                """Afficher le message 'Liste des joueurs inscrits au tournoi' """
                self.view.message_list_of_players_selected()
                """Afficher la liste des joueurs"""
                self.view.show_selected_players(player_sorted)

                """Récupérer les informations de List_MatchX.json"""
                nbrs_list_match_old = self.controller.player_list_controller.nbr_files_in_list_match_old(
                    old_tournament2)
                number_files1 = 1
                while not number_files1 > nbrs_list_match_old:
                    match_list = self.db.get_match_list_old_tournament(old_tournament2, number_files1)
                    """Afficher le tableau des équipes de chaques Rounds"""
                    self.view.table_of_teams(match_list, number_files1)
                    """Affichage des résultats de chaques Rounds"""
                    round_list = self.db.get_round_list_old_tournament(old_tournament2, number_files1)
                    self.view.show_round_list(round_list, number_files1)
                    number_files1 += 1
                list_scoreboard = self.get_scoreboard_old_tournament(old_tournament2)
                list_winner = self.db.get_winner_tournament(list_scoreboard, tournament_info1)
                nbrs_in_list_winner = len(list_winner)
                self.controller.start_tournament_controller.select_winner_player_old(nbrs_in_list_winner, list_winner)
                if number_files1 > nbrs_list_match_old:
                    self.controller.menu_controller.run_menu_report()

        if choice_of_repport == 2:
            data = os.getcwd()
            path = f"{data}/data"
            old_tournament3 = self.dm.get_old_tournaments()
            with open(f"{path}/Rapport_tournois_précédents.txt", "w") as f:
                """Boucle qui va afficher le nom du premier répertoire"""
                """old_tournament1 = un nom de répertoire """
            with open(f"{path}/Rapport_tournois_précédents.txt", "a") as f:
                for old_tournament4 in old_tournament3:
                    f.write("=====================================================================\n")
                    f.write("===================Rapport des tournois précedents========================\n")
                    f.write("=====================================================================\n\n")
                    """Récupération des informations du tournoi concerné"""
                    tournament_info2 = self.db.get_old_tournament_information(old_tournament4)
                    """Affiche les informations du tournoi concerné"""
                    for tournament_info3 in tournament_info2:
                        name = tournament_info3["nom"]
                        place = tournament_info3["lieu"]
                        date1 = tournament_info3["date1"]
                        date2 = tournament_info3["date2"]
                        remark = tournament_info3["remarques"]
                        rounds = tournament_info3["rounds"]
                        f.write(f"Nom du tournoi : {name}\n")
                        f.write(f"Lieu : {place}\n")
                        f.write(f"Date de début : {date1}\n")
                        f.write(f"Date de fin : {date2}\n")
                        f.write(f"Remarques : {remark}\n")
                        f.write(f"Nombre de Rounds : {rounds}\n")

                        """Afficher le message 'Liste des joueurs inscrits au tournoi' """
                        f.write("================================================================\n")
                        f.write("=============Liste des joueurs inscrits au tournoi================\n")
                        f.write("================================================================\n\n")

                        """Récupération des données du fichier List_Players_Select.json"""
                        list_player_select = self.db.get_list_player_select_report(old_tournament4)
                        """Trier la liste par ordre alphabétique"""
                        player_sorted = self.db.sort_player_list_db(list_player_select)
                        """Afficher la liste des joueurs inscrits au tournoi"""
                        for player_sorted1 in player_sorted:
                            f.write(f"ID : {player_sorted1['identifiant']} Nom : {player_sorted1['nom']} "
                                    f"{player_sorted1['prenom']}\n")

            """Récupérer les informations de List_MatchX.json"""
            nbrs_list_match_old = \
                self.controller.player_list_controller.nbr_files_in_list_match_old(old_tournament4)
            number_files1 = 1

            while not number_files1 > nbrs_list_match_old:
                with open(f"{path}/Rapport_tournois_précédents.txt", "a") as f:
                    match_list = self.db.get_match_list_old_tournament(old_tournament4, number_files1)
                    """Afficher le tableau des équipes de chaques Rounds"""
                    match_number = 1
                    f.write("==================================================================================\n")
                    f.write(f"============Tableau des équipes Round: {number_files1}============\n\n")
                    for i in range(0, len(match_list), 2):
                        player1 = match_list[i]
                        player2 = match_list[i + 1]
                        f.write(f"Match {match_number}: Joueur {player1['joueur']} - "
                                f"{player1['nom']:<9} {player1['prenom']:<10} "
                                f"VS\t Joueur {player2['joueur']} - {player2['nom']} {player2['prenom']}\n")
                        match_number += 1
                    """Affichage des résultats de chaques Rounds"""
                    round_list = self.db.get_round_list_old_tournament(old_tournament4, number_files1)
                    vs = "VS"
                    f.write("==================================================================================\n")
                    f.write(f"============Résultats Round: {number_files1}============\n\n")
                    for i in range(0, len(round_list), 2):
                        player1 = round_list[i]
                        player2 = round_list[i + 1]
                        f.write(f"Date et heure de début : {player1['Date et heure de debut']}\n")
                        f.write(f"Joueur {player1['joueur']} - "
                                f"{player1['nom']} {player1['prenom']} Score {player1['score']:<5}"
                                f"{vs:<3} Joueur {player2['joueur']} - "
                                f"{player2['nom']} {player2['prenom']} Score {player2['score']}\n")
                        f.write(f"Date et heure de fin : {player2['Date et heure de fin']}\n")
                        f.write("==========================================================================\n")
                    number_files1 += 1
            list_scoreboard = self.get_scoreboard_old_tournament(old_tournament4)
            list_winner = self.db.get_winner_tournament(list_scoreboard, tournament_info2)
            nbrs_in_list_winner = len(list_winner)

            if nbrs_in_list_winner == 1:
                with open(f"{path}/Rapport_tournois_précédents.txt", "a") as f:
                    f.write("======================Vainqueur du tournoi=========================\n")
                    for list_winner1 in list_winner:
                        f.write(f"Nom : {list_winner1['nom']} {list_winner1['prenom']} "
                                f"avec un score de : {list_winner1['score']}\n")
            if nbrs_in_list_winner == 2:
                with open(f"{path}/Rapport_tournois_précédents.txt", "a") as f:
                    f.write("=====================Vainqueurs du tournoi par ex-aequo=======================\n")
                    for list_winner1 in list_winner:
                        f.write(f"Nom : {list_winner1['nom']} {list_winner1['prenom']} "
                                f"avec un score de : {list_winner1['score']}\n")
            if nbrs_in_list_winner == 3:
                with open(f"{path}/Rapport_tournois_précédents.txt", "a") as f:
                    f.write("=====================Vainqueurs du tournoi par ex-aequo=======================\n")
                    for list_winner1 in list_winner:
                        f.write(f"Nom : {list_winner1['nom']} {list_winner1['prenom']} "
                                f"avec un score de : {list_winner1['score']}\n")
            if nbrs_in_list_winner >= 4:
                with open(f"{path}/Rapport_tournois_précédents.txt", "a") as f:
                    f.write("============Plusieurs participants sont à égalité en tête du classement============\n")

            if number_files1 > nbrs_list_match_old:
                """Afficher l'emplacement du fichier à consulter"""
                self.view.previous_tournaments_report_path(path)
                self.controller.menu_controller.run_menu_report()

    def get_scoreboard_old_tournament(self, tournament_name):
        """Méthode qui retourne les informations du fichier ScoreBoard.json des tournois précédents """
        data = os.getcwd()
        path = f"{data}/data/tournament_old/{tournament_name}"
        with open(f"{path}/ScoreBoard/ScoreBoard.json", "r") as f:
            list_scoreboard = json.load(f)
            return list_scoreboard
