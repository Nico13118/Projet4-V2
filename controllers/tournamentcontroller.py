from models.tournamentmodel import TournamentModel
from datetime import datetime
import re
DEFAULT_NUMBER_OF_ROUNDS = 4


class TournamentController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def tournament_registration(self):
        if self.dm.control_tournament_directory():
            self.view.tournament_error_message1()
            self.controller.menu_controller.run_tournament_menu()
        else:
            self.view.start_tournament()

            tournamentmodel = TournamentModel(
                self.tournament_name_controller(),
                self.tournament_place_controller(),
                self.tournament_start_date_controller(),
                self.tournament_end_date_controller(),
                self.tournament_directore_remark_controller(),
                self.number_rounds_controller())
            self.db.add_tournament_in_json(tournamentmodel)
            self.controller.menu_controller.run_tournament_menu()

    def tournament_name_controller(self):
        tournament_name = self.view.tournament_name()
        if tournament_name == "":
            self.view.tournament_error_message2()
            self.tournament_name_controller()
        else:
            self.dm.make_directory_tournament(tournament_name)
            return tournament_name

    def tournament_place_controller(self):
        place = self.view.tournament_place()
        if place == "":
            self.view.tournament_error_message2()
            self.tournament_place_controller()
        else:
            return place

    def tournament_start_date_controller(self):
        try:
            date_string = self.view.tournament_start_date()
            date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
            start_date = date_object.strftime("%d/%m/%Y")
            return str(start_date)
        except ValueError:
            self.view.date_error_message()
            self.tournament_start_date_controller()

    def tournament_end_date_controller(self):
        try:
            date_string = self.view.tournament_end_date()
            date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
            end_date = date_object.strftime("%d/%m/%Y")
            return str(end_date)
        except ValueError:
            self.view.date_error_message()
            self.tournament_end_date_controller()

    def tournament_directore_remark_controller(self):
        directore_remark = self.view.tournament_directore_remark()
        if directore_remark == "":
            self.view.tournament_error_message2()
            self.tournament_directore_remark_controller()
        else:
            return directore_remark

    def number_rounds_controller(self):
        """Méthode qui permet d'ajouter par défaut le nombre de Rounds si l'utilisateur ne saisit rien
            Retourne par défaut 4 ou le choix de l'utilisateur
        """
        number_rounds = self.view.tournament_number_rounds()
        if number_rounds == "":
            number_rounds = DEFAULT_NUMBER_OF_ROUNDS
            return number_rounds
        else:
            return number_rounds

    def del_tournament_directory(self):
        """Suppression du répertoire portant le nom du tournoi"""
        if not self.dm.control_tournament_directory():
            self.view.del_tournament_message_view4()
            self.controller.menu_controller.run_tournament_menu()

        self.view.del_tournament_message_view1()
        if self.input_control_tournament():
            self.dm.del_tournament()
            self.view.del_tournament_message_view3()
            self.controller.menu_controller.run_tournament_menu()

    def input_control_tournament(self):
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.del_tournament_view()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if user_input.isdigit():
                        self.view.tournament_error_message3()
                    if not user_input.isdigit():
                        if user_input == "Y" or user_input == "y" or user_input == "O" \
                                or user_input == "o" or user_input == "oui":
                            return True
                        if user_input == "N" or user_input == "n" or user_input == "No" \
                                or user_input == "no" or user_input == "non":
                            self.controller.menu_controller.run_tournament_menu()
                        else:
                            self.view.incorrect_entry()
                else:
                    self.view.incorrect_entry()
            except ValueError:
                self.view.incorrect_entry()

    def input_control_player_in_tournament(self):
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.message_select_player3_tournamentview()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if user_input.isdigit():
                        self.view.incorrect_entry()
                    if not user_input.isdigit():
                        if user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o":
                            self.add_player_in_tournament_controller()
                        elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no":
                            self.controller.menu_controller.run_tournament_menu()
                        else:
                            self.view.incorrect_entry()
                else:
                    self.view.incorrect_entry()
            except ValueError:
                self.view.incorrect_entry()

    def add_player_in_tournament_controller(self):
        """Méthode qui permet d'inscrire des joueurs dans le tournoi"""
        if not self.dm.control_tournament_directory():
            """Controle la présence d'un répertoire dans le répertoire tournament"""
            self.view.del_tournament_message_view4()
            self.controller.menu_controller.run_tournament_menu()
        if self.controller.player_list_controller.list_match_file_control():
            """Controle si le fichier List_MatchX.json existe"""
            self.view.tournament_started_message()
            self.controller.menu_controller.run_tournament_menu()

        else:
            """Ajouter un joueur supplémentaire dans le tournoi """
            """ Si le fichier List_Players_Select.json existe et contient 8 joueurs"""
            if self.controller.player_list_controller.control_player_select_controller():
                if self.controller.player_list_controller.control_number_player_in_list_players_select():
                    self.view.message_select_player4_tournamentview()
                    self.controller.menu_controller.run_tournament_menu()

                """ Si le fichier List_Players_Select ne contient pas 8 joueurs"""
                list_registered_players = self.db.get_list_registered_players_and_players_select()
                """ Affichage de la liste list_registered_players"""
                self.view.print_player_list_tournamentview(list_registered_players)
                """ Demande à l'utilisateur de saisir le joueur à ajouter au tournoi"""
                self.view.message_select_player2_tournamentview()
                user_input = self.user_input_control(list_registered_players)
                self.db.add_player_in_tournament_db2(user_input)
                self.input_control_player_in_tournament()

            else:
                """Ajouter un premier joueur dans le tournoi """
                """ Si le fichier List_Registered_Players.json existe """
                if self.controller.player_list_controller.control_player_list_controller():
                    nbrs_players = self.controller.player_list_controller.control_number_player_in_list_registered()
                    if nbrs_players >= 1:
                        self.view.message_select_player1_tournamentview()
                        """ Extraire les données de la liste List_Registered_Players.json"""
                        list_player = self.db.get_player_list()
                        """ Tries la liste des joueurs par ordre alphabétique"""
                        player_sorted = self.db.sort_player_list_db(list_player)
                        """ Affiche la liste des joueurs par ordre alphabétique"""
                        self.view.print_player_list_tournamentview(player_sorted)
                        """ Demande à l'utilisateur de saisir le joueur à ajouter au tournoi"""
                        self.view.message_select_player2_tournamentview()
                        user_input = self.user_input_control(player_sorted)
                        self.db.add_player_in_tournament_db(user_input)
                        self.input_control_player_in_tournament()
                    else:
                        self.view.message_no_players_in_list_registered()
                        self.controller.menu_controller.run_tournament_menu()
                else:
                    self.view.message_no_players_in_list_registered()
                    self.controller.menu_controller.run_tournament_menu()

    def user_input_control(self, list_match):
        """Controle de la saisie utilisateur
            Controle que la saisie correspond au nombre de joueurs dans la liste
        """
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.repeat_message()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if str(user_input).isalpha():
                        self.view.incorrect_entry()
                    if not str(user_input).isalpha():
                        numbers = len(list_match)
                        user_input = int(user_input)
                        if user_input == 0:
                            self.view.incorrect_entry()
                        elif user_input <= numbers:
                            return user_input
                        elif user_input > numbers:
                            self.view.incorrect_entry()
                else:
                    self.view.incorrect_entry()
            except ValueError:
                self.view.incorrect_entry()
