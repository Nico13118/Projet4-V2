class StartTournamentView:
    def message_start_tournament(self):
        print("============Lancement du tournoi====================")
        print("============Affichage des équipes===================")

    def message_end_tournament(self):
        print("============ Tournois terminé ======================")

    def message_tournament_launched(self):
        print("Le tournoi a déja été lancé, vous pouvez saisir les scores des joueurs.")

    def tournament_not_launched(self):
        print("Vous devez lancer le tournoi avant de saisir les scores")

    def message_start_tournament_missing_player(self):
        print("Action impossible, vous devez ajouter des joueurs dans le tournoi")

    def empty_user_input(self):
        print("La saisie ne peut pas être vide !!")

    def incorrect_entry(self):
        print("Saisie incorrect !! Veuillez réessayer.")

    def team_selection_view(self):
        print("============ Saisie des scores ===========")

    def winner_player_selection(self):
        user_input = input("Saisir le numéro du joueur qui remporte le match ( 1 ou 2):")
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

    def tournament_winner(self):
        print("===============Vainqueur du tournoi====================")

    def two_winners_ex_aequo(self):
        print("Vainqueurs du tournoi par ex-aequo :")
