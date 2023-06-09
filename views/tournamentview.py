class TournamentView:
    def start_tournament(self):
        print("\n|================== Création d'un tournoi d'échecs ==================|")

    def tournament_name(self):
        tournament_name = input("Nom du tournoi :")
        return tournament_name

    def tournament_place(self):
        place = input("Lieu :")
        return place

    def tournament_start_date(self):
        start_date = input("Date de début (jj/mm/aaaa) :")
        return start_date

    def tournament_end_date(self):
        end_date = input("Date de fin :")
        return end_date

    def tournament_directore_remark(self):
        directore_remark = input("Remarques :")
        return directore_remark

    def tournament_number_rounds(self):
        print("Saisissez le nombre de rounds ou laissez le champ vide, "
              "le champ vide correspond à 4 rounds par défaut.")
        number_rounds = input("Quel est votre choix ?")
        return number_rounds

    def tournament_error_message1(self):
        print("Action impossible !! Vous ne pouvez pas créer d'autre tournoi !!")

    def tournament_error_message2(self):
        print("La saisie ne peut pas être vide !!")

    def tournament_error_message3(self):
        print("Saisie incorrect !! Veuillez réessayer.")

    def incorrect_entry(self):
        print("Saisie incorrect !! Veuillez réessayer.")

    def date_error_message(self):
        print("Le format de la date est incorrect ! Veuillez réessayer")

    def del_tournament_message_view1(self):
        print("Attention !! Vous êtes sur le point de supprimer un tournoi créé précédemment.")

    def del_tournament_message_view3(self):
        print("Le tournoi a été supprimé avec succès.")

    def del_tournament_message_view4(self):
        print("Action impossible !! Aucun tournoi n'a été crée.")

    def del_tournament_message_view5(self):
        print("Action impossible !! Vous devez ajouter des joueurs dans le tournoi")

    def del_tournament_view(self):
        user_input = input("Souhaitez-vous continuer ? (Y(es), N(o): ")
        return user_input

    def message_select_player1_tournamentview(self):
        print("----Selection de joueurs pour le tournoi----")
        print("----------Maximum 8 joueurs------------")

    def message_select_player2_tournamentview(self):
        print("Saisir le numéro du joueur à intégrer au tournoi (1, 2, 3 ...) :")

    def message_select_player3_tournamentview(self):
        user_input = input("Souhaitez-vous continuer ? (Y(es) / N(o) :")
        return user_input

    def message_select_player4_tournamentview(self):
        print("Vous avez atteint le nombre maximum de joueurs à inscrire.")

    def print_player_list_tournamentview(self, list_player):
        i = 0
        for list_player1 in list_player:
            i += 1
            print(f"-{i}- ID : {list_player1['identifiant']} Nom : {list_player1['nom']} {list_player1['prenom']}")

    def repeat_message(self):
        user_input = input("Faite votre choix :")
        return user_input

    def message_list_registered_player(self):
        print("Liste de joueurs manquante !!! Vous devez enregistrer des joueurs depuis le menu principal "
              "-> Gestionnaire des joueurs -> Inscription des joueurs .")

    def message_no_players_in_list_registered(self):
        print("Action impossible !! vous devez enregistrer des joueurs depuis le menu Gestionnaire de joueurs.")

    def tournament_started_message(self):
        print("Action impossible !! Tournoi déjà lancé, Vous ne pouvez plus inscrire de joueurs.")
