class ReportView:
    def message_no_tournament_directory(self):
        print("Action impossible !! Aucun tournoi n'a été crée.")

    def message_no_tournament_old_directory(self):
        print("Action impossible !! Aucun tournoi n'a été crée.")

    def no_match_list_to_display(self):
        print("Aucune liste à afficher pour le moment.")

    def no_round_list_to_display(self):
        print("Aucune liste à afficher pour le moment.")

    def message_list_of_players_selected(self):
        print("\n==================================================================")
        print("============= Liste des joueurs inscrits au tournoi ================")

    def message_no_list_player_selected(self):
        print("============= Liste des joueurs inscrits au tournoi ================")
        print("============= Aucune liste à afficher pour le moment ===============\n")

    def report_message(self):
        print("===================================================================")
        print("================== Rapport du tournoi en cours =====================\n")

    def report_old_tournament(self):
        print("=================Rapport des tournois précedents====================")
        print("======================================================================\n")

    def print_tournament_info(self, tournament_info):
        for tournament_info1 in tournament_info:
            name = tournament_info1["nom"]
            place = tournament_info1["lieu"]
            date1 = tournament_info1["date1"]
            date2 = tournament_info1["date2"]
            remark = tournament_info1["remarques"]
            rounds = tournament_info1["rounds"]
            print(f"Nom du tournoi : {name}")
            print(f"Lieu : {place}")
            print(f"Date de début : {date1}")
            print(f"Date de fin : {date2}")
            print(f"Remarques : {remark}")
            print(f"Nombre de Rounds : {rounds}")
            print("=====================================================================\n")
            
    def show_selected_players(self, list_player_select):
        for list_player_select1 in list_player_select:
            print(f"ID : {list_player_select1['identifiant']} Nom : {list_player_select1['nom']} "
                  f"{list_player_select1['prenom']}")

    def table_of_teams(self, match_list, number_files1):
        match_number = 1
        print("=====================================================================")
        print(f"=========== Tableau des équipes Round: {number_files1} =============")
        for i in range(0, len(match_list), 2):
            player1 = match_list[i]
            player2 = match_list[i + 1]
            print(f"Match {match_number}: Joueur {player1['joueur']} - {player1['nom']:<9} {player1['prenom']:<10}"
                  f"VS\t Joueur {player2['joueur']} - {player2['nom']} {player2['prenom']}")
            match_number += 1

    def message_no_table_of_teams(self):
        print("====================== Tableau des équipes =========================")
        print("=============== Aucune équipe à afficher pour le moment ===========\n")

    def show_round_list(self, round_list, number_files1):
        vs = "VS"
        print("=====================================================================")
        print(f"================= Résultats Round: {number_files1} =================")
        for i in range(0, len(round_list), 2):
            player1 = round_list[i]
            player2 = round_list[i + 1]
            print(f"Date et heure de début : {player1['Date et heure de debut']}")
            print(f"Joueur {player1['joueur']} - {player1['nom']} {player1['prenom']} Score {player1['score']:<5}"
                  f"{vs:<3} Joueur {player2['joueur']} - {player2['nom']} {player2['prenom']} "
                  f"Score {player2['score']}")
            print(f"Date et heure de fin : {player2['Date et heure de fin']}")
            print("===============================================================\n")

    def no_round_list(self):
        print("========================== Résultats Round ==========================")
        print("============= Aucun résultat à afficher pour le moment ============\n")


    def scoreboard_view(self, list_scoreboard):
        print("=====================================================================")
        print("====================Classement des joueurs===========================")
        for list_scoreboard1 in list_scoreboard:
            print(f"Joueur {list_scoreboard1['joueur']}: {list_scoreboard1['nom']:<9} "
                  f"{list_scoreboard1['prenom']:<9} Score :{list_scoreboard1['score']}")

    def no_scoreboard_view(self):
        print("===================== Classement des joueurs ========================")
        print("============= Aucun classement à afficher pour le moment ============\n")

    def no_list_of_laps_to_display(self, number_files1):
        print("=====================================================================")
        print(f"===== Aucun résultat à afficher pour le Round {number_files1} =====\n")

    def current_tournament_report_path(self, path):
        print("Vous pouvez consulter le rapport du tournoi en cours à cet emplacement.")
        print(f"{path}/Rapport_tournoi_en_cours.txt")

    def previous_tournaments_report_path(self, path):
        print("Vous pouvez consulter le rapport des tournois précédents à cet emplacement.")
        print(f"{path}/Rapport_tournois_précdéents.txt")
