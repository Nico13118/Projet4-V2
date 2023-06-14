import re


class MenuController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def run_menu(self):
        """"MENU PRINCIPAL"""
        self.view.club_name()
        number = 4
        self.view.get_user_input_main_menu()
        user_input = self.control_user_input_run_menu(number)
        if user_input == 1:
            """Gestionnaire des joueurs"""
            self.run_menu_player()
        elif user_input == 2:
            """Gestionnaire des tournois"""
            self.run_tournament_menu()
        elif user_input == 3:
            """Rapport de tournoi"""
            self.run_menu_report()
        elif user_input == 4:
            """Quitter l'application"""
            quit()

    def run_menu_player(self):
        """Gestionnaire de joueurs"""
        self.view.club_name()
        number = 3
        self.view.get_user_input_player_menu()
        user_input = self.control_user_input(number)
        if user_input == 0:
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input == 1:
            """Inscription des joueurs"""
            self.controller.player_controller.player_message()
            self.run_menu_player()
        elif user_input == 2:
            """Voir la liste des joueurs"""
            self.controller.player_list_controller.print_player_list_controller()
        elif user_input == 3:
            """Supprimer un joueur de la liste"""
            self.controller.player_list_controller.del_player_in_list_controller()

    def run_tournament_menu(self):
        """Gestionnaire de tournoi"""
        self.view.club_name()
        number = 8
        self.view.get_user_input_tournament_menu()
        user_input = self.control_user_input(number)
        if user_input == 0:
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input == 1:
            """Créer un tournoi"""
            self.controller.tournament_controller.tournament_registration()
        elif user_input == 2:
            """Ajouter des joueurs au tournoi"""
            self.controller.tournament_controller.add_player_in_tournament_controller()
            self.run_tournament_menu()
        elif user_input == 3:
            """liste des joueurs inscrits au tournoi"""
            self.controller.player_list_controller.print_list_player_select()
        elif user_input == 4:
            """Supprimer des joueurs du tournoi"""
            self.controller.player_list_controller.del_player_in_list_player_select()
        elif user_input == 5:
            """Lancer le tournoi"""
            self.controller.start_tournament_controller.start_tournament()
        elif user_input == 6:
            """Saisir les scores"""
            self.controller.start_tournament_controller.player_selection()
        elif user_input == 7:
            """Tableau des équipes"""
            self.controller.start_tournament_controller.show_team_table_controller()
        elif user_input == 8:
            """Supprimer un tournoi"""
            self.controller.tournament_controller.del_tournament_directory()

    def run_menu_report(self):
        """Rapport de tournoi"""
        self.view.club_name()
        number = 4
        self.view.get_user_input4()
        user_input = self.control_user_input(number)
        if user_input == 0:
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input == 1:
            """Rapport du tournoi en cours"""
            choice_of_repport = 1
            self.controller.report_controller.current_tournament_report(choice_of_repport)
        elif user_input == 2:
            """Rapport des tournois précédents."""
            choice_of_repport = 1
            self.controller.report_controller.show_previous_tournaments(choice_of_repport)
        elif user_input == 3:
            """Rapport du tournoi en cours (format txt)."""
            choice_of_repport = 2
            self.controller.report_controller.current_tournament_report(choice_of_repport)
        elif user_input == 4:
            """Rapport des tournois précédents (format txt)."""
            choice_of_repport = 2
            self.controller.report_controller.show_previous_tournaments(choice_of_repport)

    def control_user_input(self, number):
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.repeat_message()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if str(user_input).isalpha():
                        self.view.error_message_menuview1()
                    if not str(user_input).isalpha():
                        user_input = int(user_input)
                        if user_input > number:
                            self.view.error_message_menuview1()
                        if user_input <= number:
                            return user_input
                        else:
                            self.view.incorrect_entry()
                    else:
                        self.view.incorrect_entry()

                else:
                    self.view.incorrect_entry()
            except ValueError:
                self.view.incorrect_entry()

    def control_user_input_run_menu(self, number):
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.repeat_message()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if str(user_input).isalpha():
                        self.view.error_message_menuview1()
                    if not str(user_input).isalpha():
                        user_input = int(user_input)
                        if user_input > number:
                            self.view.error_message_menuview1()
                        if user_input == 0:
                            self.view.error_message_menuview1()
                        if user_input <= number:
                            return user_input
                        else:
                            self.view.incorrect_entry()
                    else:
                        self.view.incorrect_entry()
                else:
                    self.view.incorrect_entry()
            except ValueError:
                self.view.incorrect_entry()
