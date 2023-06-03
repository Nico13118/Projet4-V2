class StartTournamentView:
    def display_of_teams(self, rounds_info):
        print("==================Affichage des équipes=========================")
        print(f"====================== Rounds {rounds_info} ============================")

    def message_end_tournament(self):
        print("========================= Tournoi terminé ===========================")

    def message_tournament_launched(self):
        print("Le tournoi a déja été lancé, vous pouvez saisir les scores des joueurs.")

    def tournament_not_launched(self):
        print("Action impossible !! Vous devez lancer le tournoi avant de saisir les scores.")

    def message_show_team_table(self):
        print("Action impossible !! Pour visualiser les équipes vous devez lancer le tournoi.")

    def message_start_tournament_missing_player(self):
        print("Action impossible !! Vous devez ajouter des joueurs au tournoi.")

    def message_no_tournament_directory(self):
        print("Action impossible !! Aucun tournoi n'a été crée.")

    def empty_user_input(self):
        print("La saisie ne peut pas être vide !!")

    def incorrect_entry(self):
        print("Saisie incorrect !! Veuillez réessayer.")

    def repeat_message(self):
        user_input = input("Faite votre choix :")
        return user_input

    def team_selection_view(self):
        print("======================== Saisie des scores =========================")

    def winner_player_selection(self):
        print("Saisir le numéro du joueur qui remporte le match ( 1 ou 2):")

    def get_user_input_match_for_score_entry(self):
        print("Saisir le numéro du joueur pour la saisie du score (1, 2, 3 ...): ")

    def ask_to_continue(self):
        user_input = input("Souhaitez vous enregistrer un autre score ? Y(es) / N(o): ")
        return user_input

    def get_user_input_match_for_score_entry2(self):
        print("1 = Match Nul")
        print("2 = Gagnant / Perdant ")
        print("Quel est le résultat ? (1 ou 2) :")

    def end_of_game_message(self):
        print("=====================Round terminé====================.")

    def print_start_match(self, temporary_list):
        select1 = temporary_list[0]
        select2 = temporary_list[1]
        select3 = temporary_list[2]
        select4 = temporary_list[3]
        select5 = temporary_list[4]
        select6 = temporary_list[5]
        select7 = temporary_list[6]
        select8 = temporary_list[7]
        print(f"Équipe 1 : {select1['nom']:<9} {select1['prenom']:<9} -{select1['couleur']:<9}"
              f"-VS-\t {select2['nom']:<9} {select2['prenom']:<9} -{select2['couleur']}")

        print(f"Équipe 2 : {select3['nom']:<9} {select3['prenom']:<9} -{select3['couleur']:<9}"
              f"-VS-\t {select4['nom']:<9} {select4['prenom']:<9} -{select4['couleur']}")

        print(f"Équipe 3 : {select5['nom']:<9} {select5['prenom']:<9} -{select5['couleur']:<9}"
              f"-VS-\t {select6['nom']:<9} {select6['prenom']:<9} -{select6['couleur']}")

        print(f"Équipe 4 : {select7['nom']:<9} {select7['prenom']:<9} -{select7['couleur']:<9}"
              f"-VS-\t {select8['nom']:<9} {select8['prenom']:<9} -{select8['couleur']}")

    def view_match_for_score_entry(self, list_match):
        i = 0
        for list_match1 in list_match:
            i += 1
            print(f"-{i}-Nom : {list_match1['nom']} {list_match1['prenom']}")

    def tournament_winner(self, list_winner):
        print("======================Vainqueur du tournoi=========================")
        for list_winner1 in list_winner:
            print(f"Nom : {list_winner1['nom']} {list_winner1['prenom']} avec un score de : {list_winner1['score']}")
            print("====================== Félicitations !===========================")

    def two_winners_ex_aequo(self, list_winner):
        print("=======================Vainqueurs du tournoi par ex-aequo=========================")
        for list_winner1 in list_winner:
            print(f"Nom : {list_winner1['nom']} {list_winner1['prenom']} avec un score de : {list_winner1['score']}")
        print("======================== Félicitations !=============================")

    def no_winner(self):
        print("===================Plusieurs participants sont à égalité en tête du classement======================")
