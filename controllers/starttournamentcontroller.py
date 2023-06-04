import random
import time
import re


class StartTournamentController:
    def __init__(self, view, controller, database, directory, match):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory
        self.mc = match

    def start_tournament(self):
        if not self.dm.control_tournament_directory():
            self.view.message_no_tournament_directory()
            self.controller.menu_controller.run_tournament_menu()
        """Si le fichier List_Players_Select n'existe pas"""
        if not self.controller.player_list_controller.control_player_select_controller():
            self.view.message_start_tournament_missing_player()
            self.controller.menu_controller.run_tournament_menu()
        """Si le fichier List_Players_Select existe mais ne contient pas 8 joueurs"""
        if not self.controller.player_list_controller.control_number_player_in_list_players_select():
            self.view.message_start_tournament_missing_player()
            self.controller.menu_controller.run_tournament_menu()
        """Si le fichier List_Players_Select existe et que le fichier list_match existe"""
        if self.controller.player_list_controller.control_player_select_controller():
            if self.controller.player_list_controller.list_match_file_control():
                self.view.message_tournament_launched()
                self.controller.menu_controller.run_tournament_menu()
            else:
                self.shuffle_players()

    def shuffle_players(self):
        """Mélanger les joueurs inscrits"""
        dateiso = time.strftime('%d/%m/%Y - %H:%M')
        dateiso2 = "00/00/00 - 00:00"
        temporary_list = []
        player_number = 0
        color_1 = "Blanc"
        color_2 = "Noir"
        list_player_select = self.db.get_list_player_select_db()
        random.shuffle(list_player_select)
        """Ajouter la date et l'heure de début et de fin, assigner une couleur"""
        for list_player_select1 in list_player_select:
            color_1, color_2 = color_2, color_1
            player_number += 1
            player = {
                "Date et heure de debut": dateiso,
                "couleur": color_1,
                "identifiant": list_player_select1["identifiant"],
                "nom": list_player_select1["nom"],
                "prenom": list_player_select1["prenom"],
                "naissance": list_player_select1["naissance"],
                "joueur": player_number,
                "round": list_player_select1["round"],
                "score": list_player_select1["score"],
                "Date et heure de fin": dateiso2}
            temporary_list.append(player)

        self.db.add_player_shuffle_in_list_match_json(temporary_list)
        self.create_teams()

    def next_match(self, new_list_match):
        score = 0.0
        number_files = self.controller.player_list_controller.number_files_round()
        number_files += 1
        dateiso = time.strftime('%d/%m/%Y - %H:%M')
        dateiso2 = "00/00/00 - 00:00"
        temporary_list = []
        color_1 = "Blanc"
        color_2 = "Noir"

        """Ajouter la date et l'heure de début et de fin et assigner une couleur"""
        for new_list_match1 in new_list_match:
            color_1, color_2 = color_2, color_1
            player = {
                "Date et heure de debut": dateiso,
                "couleur": color_1,
                "identifiant": new_list_match1["identifiant"],
                "nom": new_list_match1["nom"],
                "prenom": new_list_match1["prenom"],
                "naissance": new_list_match1["naissance"],
                "joueur": new_list_match1["joueur"],
                "round": number_files,
                "score": score,
                "Date et heure de fin": dateiso2}
            temporary_list.append(player)

        self.db.add_player_shuffle_in_list_match_json(temporary_list)
        self.create_teams()

    def create_teams(self):
        temporary_list = self.db.get_player_list_match()
        select1 = temporary_list[0]
        rounds_info = select1["round"]
        """Message -Affichage des équipes- et le numéro du rounds"""
        if rounds_info == 0:
            rounds_info += 1
            self.view.display_of_teams(rounds_info)
            self.view.print_start_match(temporary_list)
            self.controller.menu_controller.run_tournament_menu()
        else:
            self.view.display_of_teams(rounds_info)
            self.view.print_start_match(temporary_list)
            self.controller.menu_controller.run_tournament_menu()

    def player_selection(self):
        """Controle que le fichier portant le nom du tournoi existe"""
        if not self.dm.control_tournament_directory():
            self.view.message_no_tournament_directory()
            self.controller.menu_controller.run_tournament_menu()
        """Controle que le tournoi a bien été lancé"""
        if not self.controller.player_list_controller.list_match_file_control():
            self.view.tournament_not_launched()
            self.controller.menu_controller.run_tournament_menu()

        """
            Si le fichier RoundX.json n'existe pas
        """
        number_list_match_file = self.controller.player_list_controller.number_files_in_list_match()
        number_rounds_file = self.controller.player_list_controller.number_files_round()
        if not number_list_match_file == number_rounds_file:
            """ Récupération des données de List_MatchX.json"""
            list_match = self.db.get_player_list_match()
            """ Affiche à l'utilisateur la liste des joueurs"""
            self.view.view_match_for_score_entry(list_match)
            """ Demande à l'utilisateur de choisir un joueur pour entrer le score"""
            self.view.get_user_input_match_for_score_entry()
            """Controle de la saisie utilisateur"""
            choice_player1 = self.user_input_control(list_match)
            """ Affiche "Saisie des scores"""
            self.view.team_selection_view()
            self.team_selection_file_round_does_not_exist(choice_player1)

        else:
            """
                Si le fichier RoundX.json existe et ne contient pas 8 joueurs
            """
            numbers_players = self.controller.player_list_controller.control_number_player_in_list_round()
            if numbers_players < 8:
                """ Récupération des joueurs n'ayant pas eu de score"""
                list_match = self.db.get_list_match_and_round()
                """ Affiche à l'utilisateur la liste des joueurs"""
                self.view.view_match_for_score_entry(list_match)
                """ choisir un joueur pour entrer le score"""
                self.view.get_user_input_match_for_score_entry()
                """Controle de la saisie utilisateur"""
                choice_player1 = self.user_input_control(list_match)
                """ Affiche "Saisie des scores"""
                self.view.team_selection_view()
                """ Question : Match Nul ou Gagnant / Perdant"""
                self.team_selection_file_round_exist(choice_player1)

            """
               Si le fichier RoundX.json existe et contient 8 joueurs
            """
            if numbers_players >= 8:
                """Récupère les informations du fichier List_Match, il commence par le premier puis les suivants"""
                list_match = self.db.get_player_list_match()
                """ Affiche à l'utilisateur la liste des joueurs"""
                self.view.view_match_for_score_entry(list_match)
                """ Demande à l'utilisateur de choisir un joueur pour entrer le score"""
                self.view.get_user_input_match_for_score_entry()
                """Controle de la saisie utilisateur"""
                choice_player1 = self.user_input_control(list_match)
                """ Affiche -Saisie des scores-"""
                self.view.team_selection_view()
                self.team_selection_file_round_does_not_exist(choice_player1)

    def team_selection_file_round_does_not_exist(self, choice_player1):
        """Si le fichier RoundX.json n'existe pas"""
        """ Question Match Nul ou Gagnant / Perdant"""
        self.view.get_user_input_match_for_score_entry2()
        choice_score1 = self.user_input_control2()
        choice_score1 = int(choice_score1)
        choice_player1 = int(choice_player1)

        """choice_score1 == 1 = Match Nul """
        if choice_score1 == 1:
            self.db.add_score_to_players(choice_score1, choice_player1, choice_player2=None)

            self.input_control_player_selection()

        """choice_score1 == 2 = Gagnant / Perdant """
        if choice_score1 == 2:
            """L'utilisateur a déjà selectionné un joueur"""
            """Récupérer les noms des 2 joueurs"""
            player_list = self.db.get_team_file_round_does_not_exist(choice_player1)
            """Afficher les joueurs à l'utilisateur"""
            self.view.view_match_for_score_entry(player_list)
            """Demander à l'utilisateur de choisir le joueur qui remporte le match"""
            self.view.winner_player_selection()
            """Controle de saisie utilisateur"""
            choice_player2 = self.user_input_control2()
            """Envoyer les informations """
            self.db.add_score_to_players(choice_score1, choice_player1, choice_player2)

            self.input_control_player_selection()

    def team_selection_file_round_exist(self, choice_player1):
        """Si le fichier RoundX.json existe"""
        """ Demande Match Nul ou Gagnant / Perdant"""
        self.view.get_user_input_match_for_score_entry2()
        choice_score1 = self.user_input_control2()
        choice_score1 = int(choice_score1)
        choice_player1 = int(choice_player1)

        """choice_score1 == 1 = Match Nul """
        if choice_score1 == 1:
            self.db.add_score_to_players2(choice_score1, choice_player1, choice_player2=None)

            """Fonctionnalité qui controle le nombre de joueurs qui se trouve dans le fichier RoundX.json"""
            numbers_players_in_list_round = self.controller.player_list_controller.control_number_player_in_list_round()
            if numbers_players_in_list_round == 8:
                self.view.end_of_game_message()

                number_files_rounds = self.controller.player_list_controller.number_files_round()
                tournament_info = self.db.get_tournament_information()
                number_rounds = self.db.number_rounds_in_tournament_file(tournament_info)
                number_rounds = int(number_rounds)
                if number_files_rounds == number_rounds:
                    """Lorsque le nombre de fichier RoundX.json est égal au nombre de Rounds"""
                    """Afficher un message indiquant la fin du tournoi"""
                    self.view.message_end_tournament()
                    final_scores = self.controller.report_controller.get_scoreboard()
                    sort_final_scores = self.db.sort_player_list_score(final_scores)
                    list_winner = self.db.get_winner_tournament(sort_final_scores, tournament_info)
                    """Afficher le joueur qui remporte le tournoi """
                    nbrs_in_list_winner = len(list_winner)
                    self.select_winner_player(nbrs_in_list_winner, list_winner)

                else:
                    """Créer le match suivant"""
                    """ Obtenir List_Match"""
                    temporary_list_match = self.db.get_player_list_match()
                    """ Obtenir List_Round"""
                    temporary_list_round = self.db.get_list_round()
                    """ Trier par score"""
                    list_round_sorted = self.db.sort_player_list_score(temporary_list_round)
                    """ Créer équipe list_Match"""
                    match_list = self.mc.make_team_list_match(temporary_list_match)
                    """ Créer équipe list_Round"""
                    round_list = self.mc.make_team_list_round(list_round_sorted)

                    numbers_player_match = self.mc.extract_player_number_from_list_match(match_list)
                    number_player_round = self.mc.extract_player_number_from_list_round(round_list)

                    final_list = self.mc.sorted_match_list_and_round(numbers_player_match, number_player_round)
                    new_list_match = self.mc.player_selection_from_list_match(final_list)
                    """Afficher Le match suivant"""
                    self.next_match(new_list_match)

            else:
                self.input_control_player_selection()

        """choice_score1 == 2 = Gagnant / Perdant """
        if choice_score1 == 2:
            """L'utilisateur a déjà selectionné un joueur"""
            """Récupérer les noms des 2 joueurs"""
            player_list = self.db.get_team_file_round_exist(choice_player1)
            """Afficher les 2 joueurs à l'utilisateur"""
            self.view.view_match_for_score_entry(player_list)
            """Demander à l'utilisateur de choisir le joueur qui remporte le match"""
            self.view.winner_player_selection()
            """Controle de saisie utilisateur"""
            choice_player2 = self.user_input_control2()
            """Envoyer les informations pour enregistrement dans le fichier json """
            self.db.add_score_to_players2(choice_score1, choice_player1, choice_player2)

            """Fonctionnalité qui control le nombre de joueurs qui se trouve dans le fichier RoundX.json"""
            numbers_players_in_list_round = self.controller.player_list_controller.control_number_player_in_list_round()
            if numbers_players_in_list_round == 8:
                self.view.end_of_game_message()

                number_files_rounds = self.controller.player_list_controller.number_files_round()
                tournament_info = self.db.get_tournament_information()
                info_rounds = self.db.number_rounds_in_tournament_file(tournament_info)
                info_rounds = int(info_rounds)
                if number_files_rounds == info_rounds:
                    """Lorsque le nombre de fichier RoundX.json est égal au nombre de Rounds"""
                    """Afficher un message indiquant la fin du tournoi"""
                    self.view.message_end_tournament()
                    final_scores = self.controller.report_controller.get_scoreboard()
                    sort_final_scores = self.db.sort_player_list_score(final_scores)
                    list_winner = self.db.get_winner_tournament(sort_final_scores, tournament_info)
                    """Afficher le ou les joueurs qui remporte le tournoi """
                    nbrs_in_list_winner = len(list_winner)
                    self.select_winner_player(nbrs_in_list_winner, list_winner)

                else:
                    """Créer le match suivant"""
                    """ Obtenir List_Match"""
                    temporary_list_match = self.db.get_player_list_match()
                    """ Obtenir List_Round"""
                    temporary_list_round = self.db.get_list_round()
                    """ Trier par score"""
                    list_round_sorted = self.db.sort_player_list_score(temporary_list_round)
                    """ Créer équipe list_Match"""
                    match_list = self.mc.make_team_list_match(temporary_list_match)
                    """ Créer équipe list_Round"""
                    round_list = self.mc.make_team_list_round(list_round_sorted)

                    numbers_player_match = self.mc.extract_player_number_from_list_match(match_list)
                    number_player_round = self.mc.extract_player_number_from_list_round(round_list)

                    final_list = self.mc.sorted_match_list_and_round(numbers_player_match, number_player_round)
                    new_list_match = self.mc.player_selection_from_list_match(final_list)
                    """Afficher Le match suivant"""
                    self.next_match(new_list_match)

            else:
                self.input_control_player_selection()

    def user_input_control2(self):
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.repeat_message()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if str(user_input).isalpha():
                        self.view.incorrect_entry()
                    if not str(user_input).isalpha():
                        user_input = int(user_input)
                        if user_input > 2:
                            self.view.incorrect_entry()
                        elif user_input <= 2:
                            return user_input
                else:
                    self.view.incorrect_entry()
            except:
                self.view.incorrect_entry()

    def user_input_control(self, list_match):
        """Controle de la saisie utilisateur
            Controle que la saisie correspond au nombre de joueurs dans la liste
        """
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.repeat_message()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if str(user_input).isalpha():
                        self.view.incorrect_entry()
                    if not str(user_input).isalpha():
                        numbers = len(list_match)
                        user_input = int(user_input)
                        if user_input == 0:
                            self.view.incorrect_entry()
                        elif user_input > numbers:
                            self.view.incorrect_entry()
                        elif user_input <= numbers:
                            return user_input
                else:
                    self.view.incorrect_entry()
            except:
                self.view.incorrect_entry()

    def input_control_player_selection(self):
        """Control de la saisie utilisateur
            Demander à l'utilisateur s'il souhaite enregistrer un autre score
        """
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.ask_to_continue()  #
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if user_input.isdigit():
                        self.view.incorrect_entry()
                    if not user_input.isdigit():
                        if user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o":
                            self.player_selection()
                        elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no":
                            self.controller.menu_controller.run_tournament_menu()
                        else:
                            self.view.incorrect_entry()
                else:
                    self.view.incorrect_entry()
            except:
                self.view.incorrect_entry()

    def show_team_table_controller(self):
        """Méthode qui permet d'afficher les équipes"""
        if not self.dm.control_tournament_directory():
            self.view.message_no_tournament_directory()
            self.controller.menu_controller.run_tournament_menu()
        if self.controller.player_list_controller.list_match_file_control():
            temporary_list = self.db.get_player_list_match()
            select1 = temporary_list[0]
            rounds_info = select1["round"]
            self.view.display_of_teams(rounds_info)
            list_match = self.db.get_player_list_match()
            self.view.print_start_match(list_match)
            self.controller.menu_controller.run_tournament_menu()
        else:
            self.view.message_show_team_table()
            self.controller.menu_controller.run_tournament_menu()

    def select_winner_player(self, nbrs_in_list_winner, list_winner):
        """Méthode qui permet de selectionner le ou les joueurs qui remport le tounoi
            et envoi le résultat dans la vue
        """
        if nbrs_in_list_winner == 1:
            self.view.tournament_winner(list_winner)
            self.dm.move_tournament_directory()
            self.controller.menu_controller.run_tournament_menu()
        if nbrs_in_list_winner == 2:
            self.view.two_winners_ex_aequo(list_winner)
            self.dm.move_tournament_directory()
            self.controller.menu_controller.run_tournament_menu()
        if nbrs_in_list_winner == 3:
            self.view.two_winners_ex_aequo(list_winner)
            self.dm.move_tournament_directory()
            self.controller.menu_controller.run_tournament_menu()

    def select_winner_player_old(self, nbrs_in_list_winner, list_winner):
        """Méthode qui permet de selectionner le ou les joueurs qui remport le tounoi
            et envoi le résultat dans la vue
        """
        if nbrs_in_list_winner == 1:
            self.view.tournament_winner(list_winner)
        if nbrs_in_list_winner == 2:
            self.view.two_winners_ex_aequo(list_winner)
        if nbrs_in_list_winner == 3:
            self.view.two_winners_ex_aequo(list_winner)

