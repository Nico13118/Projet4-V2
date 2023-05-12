from models import TournamentModel, PlayerModel

import os
import json
# Liste des joueurs inscrits : "List_Registered_Players.json" --data\tournament
# Information d'un tournoi lors de sa création : "Tournament_Info.json" --data\tournament\nom_du_tournoi\
# Liste des rencontres : "List_Match.json"
# Liste des scores après chaque rencontre : "List_Score.json"
# Fin du round "Round.json"


class DatabaseController:
    def add_tournament_in_json(self, tournamentmodel):
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        tournament_model = TournamentModel
        tournament = tournament_model.tournament_registration(tournamentmodel)
        with open(f"{data}/data/tournament/{tournament_name}/Tournament_Info.json", "w") as f:
            json.dump(tournament, f)

    def add_player_in_json(self, playermodel):
        playerlist = []
        data = os.getcwd()
        path = f"{data}/data/tournament/players_list/"
        directory1 = os.listdir(path)
        # Si le fichier json n'existe pas alors enregistre les données dans le fichier json
        if not directory1:
            player_model = PlayerModel
            player = player_model.player_registration(playermodel)
            playerlist.append(player)
            with open(f"{path}/List_Registered_Players.json", "w") as f:
                json.dump(playerlist, f)
        # Sinon si le fichier existe, alors extraire les données puis enregistrer l'ensemble dans le même fichier
        else:
            player_model = PlayerModel
            player = player_model.player_registration(playermodel)
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                playerlist.append(player)
                for new_player_list in list_player:
                    playerlist.append(new_player_list)
                with open(f"{path}/List_Registered_Players.json", "w") as g:
                    json.dump(playerlist, g)

    def chess_id_controller(self, chess_id):
        data = os.getcwd()
        path = f"{data}/data/tournament/players_list/"
        playerlist = os.listdir(path)
        if not playerlist:
            return True
        else:
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                for list1 in list_player:
                    list2 = list1["identifiant"]
                    if chess_id == list2:
                        return False
                    return True

