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
        data = os.getcwd()
        path = f"{data}/data/tournament/players_list/"
        directory1 = os.listdir(path)
        # Si le fichier json n'existe pas alors enregistre les données dans le fichier json
        if not directory1:
            player_model = PlayerModel
            player = player_model.player_registration(playermodel)
            with open(f"{path}/List_Registered_Players.json", "w") as f:
                json.dump(player, f)
        # Sinon si le fichier existe, alors extraire les données puis enregistrer l'ensemble dans le même fichier
        else:
            player_model = PlayerModel
            player = player_model.player_registration(playermodel)
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                for new_player_list in zip(player, list_player):
                    with open(f"{path}/List_Registered_Players.json", "w") as g:
                        json.dump(new_player_list, g)


