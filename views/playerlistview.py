class PlayerListView:

    def message_list_view(self):
        print("--------Liste des joueurs enregistrés--------")

    def print_list_player_select(self):
        print("Liste des joueurs inscrits au tournoi")
    def message_del_player(self):
        user_input = input("Supprimer un joueur de la liste, souhaitez-vous continuer ? (Y(es) / N(o) :")
        return user_input

    def message_del_player_in_list_view(self):
        user_input = input("Saisir le numéro du joueur à supprimer de la liste (1, 2, 3 ...) :")
        user_input = int(user_input)
        return user_input

    def message_del_player_in_list_view2(self):
        print("Joueur supprimé avec succes.")

    def message_error_list_view(self):
        print("Aucune liste à afficher")

    def message_error_list_view2(self):
        print("Choix invalide !!!")

    def print_player_list_view(self, list_player):
        i = 0
        for list_player1 in list_player:
            i += 1
            print(f"-{i}- ID :", list_player1["identifiant"], "Nom :", list_player1["nom"], list_player1["prenom"])
