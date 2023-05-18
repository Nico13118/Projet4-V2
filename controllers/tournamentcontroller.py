from models import TournamentModel
from datetime import datetime
import os
import random


class TournamentController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory


    def control_tournament_directory(self):
        """
        Méthode qui contrôle si le répertoire tournament est vide ou non
        Si directory1 = True, alors il affiche un message d'erreur
        Sinon il procède à l'enregistrement du tournoi
        """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory1 = os.listdir(path)
        if directory1:
            self.view.tournament_error_message1()
            self.controller.menu_controller.run_menu()

        else:
            """Création d'un tournoi"""
            self.view.start_tournament()


        def tournament_name_controller():
            tournament_name = self.view.tournament_name()
            if tournament_name == "":
                self.view.tournament_error_message2()
                tournament_name_controller()
            else:
                self.dm.make_directory_tournament(tournament_name)
                return tournament_name

        def tournament_place_controller():
            place = self.view.tournament_place()
            if place == "":
                self.view.tournament_error_message2()
                tournament_place_controller()
            else:
                return place

        def tournament_start_date_controller():
            try:
                date_string = self.view.tournament_start_date()
                date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
                start_date = date_object.strftime("%d/%m/%Y")
                return str(start_date)
            except ValueError:
                self.view.date_error_message()
                tournament_start_date_controller()

        def tournament_end_date_controller():
            try:
                date_string = self.view.tournament_end_date()
                date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
                end_date = date_object.strftime("%d/%m/%Y")
                return str(end_date)
            except ValueError:
                self.view.date_error_message()
                tournament_end_date_controller()

        def tournament_directore_remark_controller():
            directore_remark = self.view.tournament_directore_remark()
            if directore_remark == "":
                self.view.tournament_error_message2()
                tournament_directore_remark_controller()
            else:
                return directore_remark

        tournamentmodel = TournamentModel(
            tournament_name_controller(),
            tournament_place_controller(),
            tournament_start_date_controller(),
            tournament_end_date_controller(),
            tournament_directore_remark_controller(),

        )
        self.db.add_tournament_in_json(tournamentmodel)
        self.controller.menu_controller.run_menu()

    def del_tournament_directory(self):
        """Suppression du répertoire portant le nom du tournoi"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory1 = os.listdir(path)
        if directory1:
            self.view.del_tournament_message_view1()
            self.input_control_tournament()

        else:
            self.view.del_tournament_message_view4()
            self.controller.menu_controller.run_menu_tournament()

    def input_control_tournament(self):
        user_input = self.view.del_tournament_view()
        if user_input == "":
            self.view.tournament_error_message2()
        elif user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o" or user_input == "oui":
            self.db.del_tournament_db()
            self.view.del_tournament_message_view3()
            self.controller.menu_controller.run_tournament_menu()

        elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no" or user_input == "non":
            self.controller.menu_controller.run_menu_tournament()
        else:
            self.view.del_tournament_message_view2()
            self.input_control_tournament()

    def input_control_player_in_tournament(self):
        user_input = self.view.message_select_player3_tournamentview()
        if user_input == "":
            self.view.tournament_error_message2()
        elif user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o":
            self.add_player_in_tournament_controller()
        elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no":
            self.controller.menu_controller.run_tournament_menu()
        else:
            self.view.tournament_error_message3()
            self.input_control_player_in_tournament()

    def add_player_in_tournament_controller(self):
        """Ajouter un joueur supplémentaire dans le tournoi """
        """Condition qui controle si le fichier List_Players_Select.json existe"""
        if self.controller.player_list_controller.control_player_select_controller():
            """La condition qui controle combien de joueurs sont inscrits au tournoi"""
            if self.controller.player_list_controller.control_number_player_in_list_players_select():
                list_registered_players = self.db.get_list_registered_players_and_players_select()
                self.view.print_player_list_tournamentview(list_registered_players) # Affichage de la liste list_registered_players
                user_input = self.view.message_select_player2_tournamentview() # Demande à l'utilisateur de saisir le joueur à ajouter au tournoi
                if user_input == "":
                    self.view.del_tournament_message_view2()
                    self.add_player_in_tournament_controller()
                numbers = len(list_registered_players)
                user_input = int(user_input)
                if user_input > numbers:
                    self.view.del_tournament_message_view2()
                    self.add_player_in_tournament_controller()
                elif user_input == 0:
                    self.view.del_tournament_message_view2()
                    self.add_player_in_tournament_controller()
                self.db.add_player_in_tournament_db2(user_input)
                self.input_control_player_in_tournament()
            else:
                self.view.message_select_player4_tournamentview()
                self.controller.menu_controller.run_tournament_menu()
        else:
            """Ajouter un premier joueur dans dans le tournoi """
            """ Condition qui controle si le fichier List_Registered_Players.json existe """
            if self.controller.player_list_controller.control_player_list_controller():
                self.view.message_select_player1_tournamentview()
                list_player = self.db.get_player_list()  # Extraire les données de la liste List_Registered_Players.json
                player_sorted = self.db.sort_player_list_db(list_player)  # Tries la liste des joueurs par ordre alphabétique
                self.view.print_player_list_tournamentview(player_sorted)  # Affiche la liste des joueurs par ordre alphabétique
                user_input = self.view.message_select_player2_tournamentview() # Demande à l'utilisateur de saisir le joueur à ajouter au tournoi
                self.db.add_player_in_tournament_db(user_input)
                self.input_control_player_in_tournament()

    def start_tournament(self):
        if self.controller.player_list_controller.control_player_select_controller():
            if not self.controller.player_list_controller.control_number_player_in_list_players_select():
                self.shuffle_players()
            else:
                self.view.message_message_start_tournament_missing_player()
        else:
            self.view.message_message_start_tournament_missing_player()

    def shuffle_players(self):
        """Mélanger les joueurs inscrits"""
        temporary_list = []
        player_number = 0
        color_1 = "Blanc"
        color_2 = "Noir"
        list_player_select = self.db.get_list_player_select_db()
        random.shuffle(list_player_select)
        """Assigner une couleur"""
        for list_player_select1 in list_player_select:
            color_1, color_2 = color_2, color_1
            player_number += 1
            player = {
                "couleur": color_1,
                "identifiant": list_player_select1["identifiant"],
                "nom": list_player_select1["nom"],
                "prenom": list_player_select1["prenom"],
                "naissance": list_player_select1["naissance"],
                "joueur": player_number,
                "round": list_player_select1["round"],
                "score": list_player_select1["score"]
            }
            temporary_list.append(player)

        #self.create_teams(temporary_list)
        self.db.add_player_shuffle_in_list_match_json(temporary_list)
        self.create_teams()


    def create_teams(self):
        temporary_list = self.db.get_player_list_match()
        self.view.print_match(temporary_list)



