
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
            """Vérifier si l'utilisateur peut créer un tournoi"""
            self.controller.tournament_controller.control_tournament_directory()
        elif user_input == "2":
            """Inscription des joueurs"""
            self.controller.player_controller.player_message()
        elif user_input == "3":
            self.run_menu_player()
        elif user_input == "4":
            self.run_tournament_menu()
        elif user_input == "5":
            self.run_menu_report()
        elif user_input == "6":
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
        if user_input == "1":
            self.controller.player_list_controller.print_player_list_controller()
            self.run_menu_player()
        elif user_input == "2":
            """Supprimer un joueur de la liste"""
            self.controller.player_list_controller.del_player_in_list_controller()
            self.run_menu_player()

        elif user_input == "3":
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
            """Supprimer des joueurs du tournoi"""
            pass
        elif user_input == "3":
            """Lancer le tournoi"""
            pass
        elif user_input == "4":
            """Reprendre un tournoi"""
            pass
        elif user_input == "5":
            """Supprimer un tournoi"""
            self.controller.tournament_controller.del_tournament_directory()
        elif user_input == "6":
            """Retourner au menu principal"""
            self.run_menu()
        elif user_input > "6":
            self.view.error_message_menuview1()
            self.run_tournament_menu()
        else:
            self.view.error_message_menuview2()
            self.run_tournament_menu()

    def run_menu_report(self):
        self.view.club_name()
        user_input = self.view.get_user_input4()
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            self.run_menu()
        elif user_input > "3":
            self.view.error_message_menuview1()
            self.run_menu_report()
        else:
            self.view.error_message_menuview2()
            self.run_menu_report()
