
class MenuController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def run_menu(self):
        self.view.club_name()
        user_input = self.view.get_user_input()
        if user_input == "1":
            """Vérifier si l'utilisateur peut créer un tournoi"""
            self.controller.tournament_controller.control()

        elif user_input == "2":
            self.controller.player_controller.player_message()
        elif user_input == "3":
            self.run_menu_player()
        elif user_input == "4":
            self.run_menu_tournament()
        elif user_input == "5":
            print("Test4")
        elif user_input == "6":
            quit()
        else:
            self.view.tournament_error_message2()
            self.run_menu()

    def run_menu_player(self):
        self.view.club_name()
        user_input = self.view.get_user_input2()
        if user_input == "1":
            self.controller.player_list_controller.print_player_list_controller()
            self.run_menu_player()
        elif user_input == "2":
            pass
        elif user_input == "3":
            self.controller.menu_controller.run_menu()
        else:
            self.run_menu()

    def run_menu_tournament(self):
        self.view.club_name()
        user_input = self.view.get_user_input3()
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            self.controller.tournament_controller.del_tournament_controller1()
        elif user_input == "4":
            self.run_menu()
        else:
            self.run_menu()

    def run_menu_report(self):
        self.view.club_name()
        user_input = self.view.get_user_input4()
        if user_input == "1":
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            self.run_menu()
        else:
            self.run_menu()
