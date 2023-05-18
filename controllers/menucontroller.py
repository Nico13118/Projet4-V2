
class MenuController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def run_menu(self):
        self.view.club_name()
        user_input = self.view.get_user_input_main_menu()
        if user_input == "1":
            """Créer un tournoi"""
            self.controller.tournament_controller.control_tournament_directory()
        elif user_input == "2":
            """Inscription des joueurs"""
            self.controller.player_controller.player_message()
        elif user_input == "3":
            """Gérer les joueurs"""
            self.run_menu_player()
        elif user_input == "4":
            """Gérer les tournois"""
            self.run_tournament_menu()
            """Rapport de tournoi"""
        elif user_input == "5":
            self.run_menu_report()
        elif user_input == "6":
            """Quitter l'application"""
            quit()
        elif user_input > "6":
            self.view.error_message_menuview1()
            self.run_menu()
        else:
            self.view.error_message_menuview2()
            self.run_menu()

    def run_menu_player(self):
        self.view.club_name()
        user_input = self.view.get_user_input_player_menu()
        """Voir la liste des joueurs"""
        if user_input == "1":
            self.controller.player_list_controller.print_player_list_controller()
            self.run_menu_player()
        elif user_input == "2":
            """Supprimer un joueur de la liste"""
            self.controller.player_list_controller.del_player_in_list_controller()
            self.run_menu_player()
        elif user_input == "3":
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input > "3":
            self.view.error_message_menuview1()
            self.run_menu_player()
        else:
            self.view.error_message_menuview2()
            self.run_menu_player()

    def run_tournament_menu(self):
        self.view.club_name()
        user_input = self.view.get_user_input_tournament_menu()
        if user_input == "1":
            """Ajouter des joueurs dans le tournoi"""
            self.controller.tournament_controller.add_player_in_tournament_controller()
            self.run_tournament_menu()
        elif user_input == "2":
            """liste des joueurs inscrits au tournoi"""
            self.controller.player_list_controller.print_list_player_select()
        elif user_input == "3":
            """Supprimer des joueurs du tournoi"""
            pass
        elif user_input == "4":
            """Lancer le tournoi"""
            pass
        elif user_input == "5":
            """Reprendre un tournoi"""
            pass
        elif user_input == "6":
            """Supprimer un tournoi"""
            self.controller.tournament_controller.del_tournament_directory()
        elif user_input == "7":
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input > "7":
            self.view.error_message_menuview1()
            self.run_tournament_menu()
        else:
            self.view.error_message_menuview2()
            self.run_tournament_menu()

    def run_menu_report(self):
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
