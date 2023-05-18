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

    def tournament_error_message1(self):
        print("Vous ne pouvez pas créer d'autre tournoi !!")

    def tournament_error_message2(self):
        print("La saisie ne peut pas être vide !!")

    def tournament_error_message3(self):
        print("Saisie incorrect !! Veuillez réessayer.")

    def date_error_message(self):
        print("Le format de la date est incorrect ! Veuillez réessayer")

    def del_tournament_message_view1(self):
        print("Attention !! Vous êtes sur le point de supprimer un tournoi créé précédemment.")

    def del_tournament_message_view2(self):
        print("Saisie incorrect, veuillez réessayer !")

    def del_tournament_message_view3(self):
        print("Le tournoi a été supprimé avec succès.")

    def del_tournament_message_view4(self):
        print("Action impossible, aucun tournoi n'a été crée.")

    def del_tournament_message_view5(self):
        print("Action impossible, vous devez ajouter des joueurs dans le tournoi")

    def del_tournament_message_view6(self):
        print("Action impossible car aucun tournoi n'a été crée ")

    def del_tournament_view(self):
        user_input = input("Souhaitez-vous continuer ? (Y(es), N(o) ")
        return user_input

    def message_select_player1_tournamentview(self):
        print("----Selection de joueurs pour le tournoi----")
        print("----------Maximum 8 joueurs------------")

    def message_select_player2_tournamentview(self):
        user_input = input("Saisir le numéro du joueur à intégrer au tournoi (1, 2, 3 ...) :")
        return user_input

    def message_select_player3_tournamentview(self):
        user_input = input("Souhaitez-vous continuer ? (Y(es) / N(o) :")
        return user_input

    def message_select_player4_tournamentview(self):
        print("Vous avez atteint le nombre maximum de joueurs à inscrire.")

    def print_player_list_tournamentview(self, list_player):
        i = 0
        for list_player1 in list_player:
            i += 1
            print(f"-{i}- ID :", list_player1["identifiant"], "Nom :", list_player1["nom"], list_player1["prenom"])

    def message_start_tournament(self):
        print("Lancement du tournoi")

    def message_start_tournament_missing_player(self):
        print("Action impossible, vous devez ajouter des joueurs dans le tournoi")

    def print_match(self, temporary_list):
        select1 = temporary_list[0]
        select2 = temporary_list[1]
        select3 = temporary_list[2]
        select4 = temporary_list[3]
        select5 = temporary_list[4]
        select6 = temporary_list[5]
        select7 = temporary_list[6]
        select8 = temporary_list[7]
        print(f"Équipe 1 :", select1["nom"], select1["prenom"], "(", select1["couleur"], ")", "VS",
              select2["nom"], select2["prenom"], "(", select2["couleur"], ")")
        print(f"Équipe 2 :", select3["nom"], select3["prenom"], "(", select3["couleur"], ")", "VS",
              select4["nom"], select4["prenom"], "(", select4["couleur"], ")")
        print(f"Équipe 3 :", select5["nom"], select5["prenom"], "(", select5["couleur"], ")", "VS",
              select6["nom"], select6["prenom"], "Couleur:", select6["couleur"])
        print(f"Équipe 4 :", select7["nom"], select7["prenom"], "(", select7["couleur"], ")", "VS",
              select8["nom"], select8["prenom"], "(", select8["couleur"], ")")

