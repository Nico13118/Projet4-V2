class PlayerListView:

    def message_list_view(self):
        print("--------Liste des joueurs enregistrés--------")

    def message_select_player1_view(self):
        print("Selection des joueurs pour le tournoi")
        print("----------Maximum 8 joueurs------------")

    def message_select_player2_view(self):
        user_input = input("Saisir le numéro du joueur à intégrer au tournoi (1, 2, 3 ...) :")
        if user_input == "":
            print("Choix invalide")
        else:
            return user_input

    def message_error_list_view(self):
        print("Aucune liste à afficher")

    def print_player_list_view(self, list_player):
        i = 0
        for list_player1 in list_player:
            i += 1
            print(f"-{i}- ID :", list_player1["identifiant"], "Nom :", list_player1["nom"], list_player1["prenom"])
