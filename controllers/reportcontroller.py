import os
import json


class ReportController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def current_tournament_report(self):
        """Pour afficher les informations du tournoi en cours"""
        if self.dm.control_tournament_directory():
            tournament_info = self.db.get_tournament_information()
            self.view.report_message()
            self.view.print_tournament_info(tournament_info)
            """Appel des autres méthodes pour afficher :
                La liste des joueurs inscrits au tournoi 
                Le tableau des équipes
                Les rounds en cours
                Les classements des joueurs
             """
            self.current_player_report()
            self.match_in_progress()
            self.score_in_progress()
            self.controller.menu_controller.run_menu_report()
        else:
            self.view.message_no_tournament_directory()
            self.controller.menu_controller.run_menu_report()

    def current_player_report(self):
        """Pour afficher la liste des joueurs inscrits au tournoi"""
        if self.controller.player_list_controller.control_player_select_controller():
            list_player_select = self.db.get_list_player_select_db()
            list_player_select = self.db.sort_player_list_db(list_player_select)
            self.view.message_list_of_players_selected()
            self.view.show_selected_players(list_player_select)
        else:
            self.view.no_list_of_players_selected()
            self.controller.menu_controller.run_menu_report()

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

    def score_in_progress(self):
        """
            Pour afficher le classement des joueurs par score
        """
        players_score = self.get_scoreboard()
        list_score_sorted = self.db.sort_player_list_score(players_score)
        self.view.scoreboard_view(list_score_sorted)

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

    def show_previous_tournaments(self):
        """Afficher les informations des tournois précédents"""
