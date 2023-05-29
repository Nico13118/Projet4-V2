class ReportView:
    def message_no_tournament_directory(self):
        print("Action impossible !! Aucun tournoi n'a été crée.")

    def no_list_of_players_selected(self):
        print("Aucune liste à afficher pour le moment.")

    def no_match_list_to_display(self):
        print("Aucune liste à afficher pour le moment.")

    def no_round_list_to_display(self):
        print("Aucune liste à afficher pour le moment.")

    def message_list_of_players_selected(self):
        print("=============Liste des joueurs inscrits au tournoi================")

    def report_message(self):
        print("===================Rapport du tournoi en cours========================")

    def print_tournament_info(self, tournament_info):
        for tournament_info1 in tournament_info:
            name = tournament_info1["nom"]
            place = tournament_info1["lieu"]
            date1 = tournament_info1["date1"]
            date2 = tournament_info1["date2"]
            remark = tournament_info1["remarques"]
            print(f"Nom du tournoi : {name}")
            print(f"Lieu : {place}")
            print(f"Date de début : {date1}")
            print(f"Date de fin : {date2}")
            print(f"Remarques : {remark}")

    def show_selected_players(self, list_player_select):
        for list_player_select1 in list_player_select:
            print(f"ID :", list_player_select1["identifiant"], "Nom :", list_player_select1["nom"],
                  list_player_select1["prenom"])

    def table_of_teams(self, match_list, number_files1):
        match_number = 1
        print(f"==============Tableau des équipes Round: {number_files1}==================")
        for i in range(0, len(match_list), 2):
            player1 = match_list[i]
            player2 = match_list[i + 1]
            print(f"Match {match_number}:", "Joueur", player1["joueur"], "-", player1["nom"], player1["prenom"],
                  "VS", "Joueur", player2["joueur"], "-", player2["nom"], player2["prenom"])
            match_number += 1

    def show_round_list(self, round_list, number_files1):

        print(f"==============Round: {number_files1}==================")
        for i in range(0, len(round_list), 2):
            player1 = round_list[i]
            player2 = round_list[i + 1]
            print("Date et heure de début :", player1["Date et heure de debut"])
            print(f"Joueur", player1["joueur"], "-", player1["nom"], player1["prenom"], "Score", player1["score"],
                  "VS", "Joueur", player2["joueur"], "-", player2["nom"], player2["prenom"], "Score", player2["score"])
            print("Date et heure de fin", player2["Date et heure de fin"], "\n")



