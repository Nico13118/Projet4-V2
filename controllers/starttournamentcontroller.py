import random
import datetime


class StartTournamentController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

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

        self.db.add_player_shuffle_in_list_match_json(temporary_list)
        self.create_teams()

    def create_teams(self):
        temporary_list = self.db.get_player_list_match()

        self.view.print_match(temporary_list)