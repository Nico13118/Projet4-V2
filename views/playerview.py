class PlayerView:
    def player_message_view(self):
        print("\n|================== Inscription des joueurs ==================|")

    def player_chess_id_view(self):
        chess_id = input("Identifiant national d'échecs :")
        return chess_id

    def player_name_view(self):
        name = input("Nom :")
        return name

    def player_first_name_view(self):
        first_name = input("Prénom :")
        return first_name

    def player_birthday_view(self):
        birthday = input("Date de naissance (jj/mm/aaaa) :")
        return birthday

    def player_error_message_view(self):
        print("La saisie ne peut pas être vide !!")

    def player_date_error_message_view(self):
        print("Le format de la date est incorrect ! Veuillez réessayer")

    def new_player_message_view(self):
        user_input = input("Souhaitez-vous inscrire un nouveau joueur ? (Y(es) / N(o) : ")
        return user_input
