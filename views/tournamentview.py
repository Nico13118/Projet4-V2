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
        print("Action impossible, vous devez ajouter les joueurs dans le tournoi")

    def del_tournament_message_view6(self):
        print("Action impossible car aucun tournoi n'a été crée ")

    def del_tournament_view(self):
        user_input = input("Souhaitez-vous continuer ? (Y(es), N(o) ")
        return user_input
