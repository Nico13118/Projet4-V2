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

