class StartTournamentView:
    def message_start_tournament(self):
        print("============Lancement du tournoi====================")
        print("============Affichage des équipes===================")

    def message_tournament_launched(self):
        print("Le tournoi a déja été lancé, vous pouvez saisir les scores des joueurs.")

    def message_start_tournament_missing_player(self):
        print("Action impossible, vous devez ajouter des joueurs dans le tournoi")

    def empty_user_input(self):
        print("La saisie ne peut pas être vide !!")

    def incorrect_entry(self):
        print("Saisie incorrect !! Veuillez réessayer.")

    def team_selection_view(self):
        print("============ Saisie des scores ===========")

    def winner_player_selection(self):
        user_input = input("Saisir le numéro du joueur qui remporte la partie ( 1 ou 2)")
        return user_input
    def get_user_input_match_for_score_entry(self):
        user_input = input("Saisir le numéro du joueur pour la saisie du score (1, 2, 3 ...) ")
        return user_input
    def ask_to_continue(self):
        user_input = input("Souhaitez vous enregistrer un autre score ? Y(es) / N(o): ")
        return user_input

    def get_user_input_match_for_score_entry2(self):
        print("1 = Match Nul")
        print("2 = Gagnant / Perdant ")
        user_input = input("Quel est le résultat ? (1 ou 2) :")
        return user_input

    def end_of_game_message(self):
        print("Match terminé.")

    def print_message_team_table(self):
        print("\n===============Tableau des équipes===============")

    def print_start_match(self, temporary_list):
        select1 = temporary_list[0]
        select2 = temporary_list[1]
        select3 = temporary_list[2]
        select4 = temporary_list[3]
        select5 = temporary_list[4]
        select6 = temporary_list[5]
        select7 = temporary_list[6]
        select8 = temporary_list[7]
        print(f"Équipe 1 :", select1["nom"], select1["prenom"], "(", select1["couleur"], ")", "-VS-",
              select2["nom"], select2["prenom"], "(", select2["couleur"], ")")

        print(f"Équipe 2 :", select3["nom"], select3["prenom"], "(", select3["couleur"], ")", "-VS-",
              select4["nom"], select4["prenom"], "(", select4["couleur"], ")")

        print(f"Équipe 3 :", select5["nom"], select5["prenom"], "(", select5["couleur"], ")", "-VS-",
              select6["nom"], select6["prenom"], "(", select6["couleur"], ")")

        print(f"Équipe 4 :", select7["nom"], select7["prenom"], "(", select7["couleur"], ")", "-VS-",
              select8["nom"], select8["prenom"], "(", select8["couleur"], ")")

    def view_match_for_score_entry(self, list_match):
        i = 0
        for list_match1 in list_match:
            i += 1
            print(f"-{i}-", "Nom :", list_match1["nom"], list_match1["prenom"])



    def print_team_1(self, list_match):
        select1 = list_match[0]
        select2 = list_match[1]
        print(f"Équipe 1 :")
        print("-1-", select1["nom"], select1["prenom"])
        print("-2-", select2["nom"], select2["prenom"])
    def print_team_2(self, list_match):
        select3 = list_match[2]
        select4 = list_match[3]
        print(f"Équipe 2 :")
        print("-1-", select3["nom"], select3["prenom"])
        print("-2-", select4["nom"], select4["prenom"])

    def print_team_3(self, list_match):
        select5 = list_match[4]
        select6 = list_match[5]
        print(f"Équipe 3 :")
        print("-1-", select5["nom"], select5["prenom"])
        print("-2-", select6["nom"], select6["prenom"])
    def print_team_4(self, list_match):
        select7 = list_match[6]
        select8 = list_match[7]
        print(f"Équipe 4 :")
        print("-1-", select7["nom"], select7["prenom"])
        print("-2-", select8["nom"], select8["prenom"])

