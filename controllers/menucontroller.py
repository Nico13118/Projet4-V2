
class MenuController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def run_menu(self):
        """"MENU PRINCIPAL"""
        self.view.club_name()
        user_input = self.view.get_user_input_main_menu()
        if user_input == "1":
            """Gestionnaire des joueurs"""
            self.run_menu_player()
        elif user_input == "2":
            """Gestionnaire des tournois"""
            self.run_tournament_menu()
        elif user_input == "3":
            """Rapport de tournoi"""
            self.run_menu_report()
        elif user_input == "4":
            """Quitter l'application"""
            quit()
        elif user_input > "4":
            self.view.error_message_menuview1()
            self.run_menu()
        else:
            self.view.error_message_menuview2()
            self.run_menu()

    def run_menu_player(self):
        """Gestionnaire de joueurs"""
        self.view.club_name()
        user_input = self.view.get_user_input_player_menu()
        if user_input == "1":
            """Inscription des joueurs"""
            self.controller.player_controller.player_message()
            self.run_menu_player()
        elif user_input == "2":
            """Voir la liste des joueurs"""
            self.controller.player_list_controller.print_player_list_controller()
        elif user_input == "3":
            """Supprimer un joueur de la liste"""
            self.controller.player_list_controller.del_player_in_list_controller()
            self.run_menu_player()
        elif user_input == "4":
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input > "4":
            self.view.error_message_menuview1()
            self.run_menu_player()
        else:
            self.view.error_message_menuview2()
            self.run_menu_player()

    def run_tournament_menu(self):
        """Gestionnaire de tournoi"""
        self.view.club_name()
        user_input = self.view.get_user_input_tournament_menu()
        if user_input == "1":
            """Créer un tournoi"""
            self.controller.tournament_controller.control_tournament_directory()
        elif user_input == "2":
            """Ajouter des joueurs dans le tournoi"""
            self.controller.tournament_controller.add_player_in_tournament_controller()
            self.run_tournament_menu()
        elif user_input == "3":
            """liste des joueurs inscrits au tournoi"""
            self.controller.player_list_controller.print_list_player_select()
        elif user_input == "4":
            """Supprimer des joueurs du tournoi"""
            self.controller.player_list_controller.del_player_in_list_player_select()
        elif user_input == "5":
            """Lancer le tournoi"""
            self.controller.start_tournament_controller.start_tournament()
        elif user_input == "6":
            """Reprendre un tournoi"""
            pass
        elif user_input == "7":
            """Supprimer un tournoi"""
            self.controller.tournament_controller.del_tournament_directory()
        elif user_input == "8":
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input > "7":
            self.view.error_message_menuview1()
            self.run_tournament_menu()
        else:
            self.view.error_message_menuview2()
            self.run_tournament_menu()

    def run_menu_report(self):
        """Rapport de tournoi"""
        self.view.club_name()
        user_input = self.view.get_user_input4()
        if user_input == "1":
            """Rapport du tournoi en cours"""
            pass
        elif user_input == "2":
            """Rapport des tournois précédents"""
            pass
        elif user_input == "3":
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input > "3":
            self.view.error_message_menuview1()
            self.run_menu_report()
        else:
            self.view.error_message_menuview2()
            self.run_menu_report()
