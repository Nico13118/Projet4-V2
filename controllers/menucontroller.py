
class MenuController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def run(self):
        self.view.club_name()
        user_input = self.view.get_user_input()
        if user_input == "1":
            """Vérifier si l'utilisateur peut créer un tournoi"""
            self.controller.tournament_controller.control()

        elif user_input == "2":
            self.controller.player_controller.player_message()
        elif user_input == "3":
            print("Test3")
        elif user_input == "4":
            print("Test4")
        elif user_input == "5":
            quit()
        else:
            self.view.tournament_error_message2()
            self.run()





