from models import PlayerModel

from datetime import datetime


class PlayerController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory


    def player_message(self):
        self.view.player_message_view()


        def player_chess_id():
            chess_id = self.view.player_chess_id_view()
            if chess_id == "":
                self.view.player_error_message_view()
                player_chess_id()
            else:
                return chess_id

        def player_name():
            name = self.view.player_name_view()
            if name == "":
                self.view.player_error_message_view()
                player_name()
            else:
                return name

        def player_first_name():
            first_name = self.view.player_first_name_view()
            if first_name == "":
                self.view.player_error_message_view()
                player_first_name()
            else:
                return first_name

        def player_birthday():
            try:
                date_string = self.view.player_birthday_view()
                date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
                birthday = date_object.strftime("%d/%m/%Y")
                return birthday
            except ValueError:
                self.view.player_date_error_message_view()

        playermodel = PlayerModel(
            player_chess_id(),
            player_name(),
            player_first_name(),
            player_birthday()
        )
        self.db.add_player_in_json(playermodel)
        self.new_player_message_controller()

    def new_player_message_controller(self):
        user_input = self.view.new_player_message_view()
        if user_input == "":
            self.view.player_error_message_view()
            self.new_player_message_controller()
        elif user_input == "y" or user_input == "yes" or user_input == "oui" or user_input == "o":
            self.controller.player_controller.player_message()

        elif user_input == "n" or user_input == "no" or user_input == "non":
            self.controller.menu_controller.run()
        else:
            self.view.player_error_message_view()
            self.new_player_message_controller()


