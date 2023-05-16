from models import TournamentModel, PlayerModel

import os
import json
import shutil
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
        temporarylist = []
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        directory1 = os.listdir(path)
        # Si le fichier json n'existe pas alors enregistre les données dans le fichier json
        if not directory1:
            player_model = PlayerModel
            playerlist = player_model.player_registration(playermodel)
            temporarylist.append(playerlist)
            with open(f"{path}/List_Registered_Players.json", "w") as f:
                json.dump(temporarylist, f)
        # Sinon si le fichier existe, alors extraire les données puis enregistrer l'ensemble dans le même fichier
        else:
            player_model = PlayerModel
            player = player_model.player_registration(playermodel)
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                for new_player_list in list_player:
                    temporarylist.append(new_player_list)
                temporarylist.append(player)
            with open(f"{path}/List_Registered_Players.json", "w") as g:
                json.dump(temporarylist, g)



    def chess_id_controller(self, chess_id):
        data = os.getcwd()
        path = f"{data}/data/players_list/"
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


    def get_player_list(self):
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        playerlist = os.listdir(path)
        if not playerlist:
            return True
        else:
            with open(f"{path}/List_Registered_Players.json", "r") as f:
                list_player = json.load(f)
                return list_player

    def sort_player_list_db(self, list_player):
        player_sorted = sorted(list_player, key=lambda x: (x["nom"], x["prenom"]))
        return player_sorted

    def del_tournament_db(self):
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        shutil.rmtree(f"{data}/data/tournament/{tournament_name}")

    def add_player_in_json2(self, list_player):
        data = os.getcwd()
        path = f"{data}/data/players_list/"
        with open(f"{path}/List_Registered_Players.json", "w") as g:
            json.dump(list_player, g)

    def del_player_in_list_db(self, user_input):
        """Supprimer le joueur dans la liste"""
        user_input -= 1
        list_player = self.get_player_list()
        player_sorted = self.sort_player_list_db(list_player)
        del player_sorted[user_input]
        self.add_player_in_json2(player_sorted)


