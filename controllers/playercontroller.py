from models import PlayerModel
from datetime import datetime
import re


class PlayerController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def player_message(self):
        self.view.player_message_view()
        if self.control_confirmation_message():
            playermodel = PlayerModel(
                self.player_chess_id(),
                self.player_name(),
                self.player_first_name(),
                self.player_birthday()
            )
            self.db.add_player_in_json(playermodel)
            self.new_player_message_controller()

    def player_chess_id(self):
        chess_id = self.view.player_chess_id_view()
        if chess_id == "":
            self.view.player_error_message_view()
            self.player_chess_id()
        else:
            if not self.db.chess_id_controller(chess_id):
                self.view.player_error_chess_id_view()
                self.player_chess_id()
            else:
                return chess_id

    def player_name(self):
        name = self.view.player_name_view()
        if name == "":
            self.view.player_error_message_view()
            self.player_name()
        else:
            return name

    def player_first_name(self):
        first_name = self.view.player_first_name_view()
        if first_name == "":
            self.view.player_error_message_view()
            self.player_first_name()
        else:
            return first_name

    def player_birthday(self):
        try:
            date_string = self.view.player_birthday_view()
            date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
            birthday = date_object.strftime("%d/%m/%Y")
            return birthday
        except ValueError:
            self.view.player_date_error_message_view()

    def new_player_message_controller(self):
        user_input2 = True
        while user_input2:
            user_input = self.view.new_player_message_view()
            if re.match(r'^[a-zA-Z0-9]+$', user_input):
                if user_input.isdigit():
                    self.view.message_error()
                if not user_input.isdigit():
                    if user_input != "y" or user_input == "yes" or user_input == "oui" or user_input == "o":
                        self.view.message_error()
                    if user_input == "y" or user_input == "yes" or user_input == "oui" or user_input == "o":
                        self.controller.player_controller.player_message()
                    elif user_input == "n" or user_input == "no" or user_input == "non":
                        self.controller.menu_controller.run_menu_player()
            else:
                self.view.message_error()

    def control_confirmation_message(self):
        user_input2 = True
        while user_input2:
            user_input = self.view.confirmation_message()
            if re.match(r'^[a-zA-Z0-9]+$', user_input):
                if user_input.isdigit():
                    self.view.message_error()
                if not user_input.isdigit():
                    if user_input != "y" or user_input == "yes" or user_input == "oui" or user_input == "o":
                        self.view.message_error()
                    if user_input == "y" or user_input == "yes" or user_input == "oui" or user_input == "o":
                        return True
                    elif user_input == "n" or user_input == "no" or user_input == "non":
                        self.controller.menu_controller.run_menu_player()
            else:
                self.view.message_error()
