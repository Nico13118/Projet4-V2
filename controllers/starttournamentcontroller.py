import random
import time

class StartTournamentController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def start_tournament(self):
        if self.controller.player_list_controller.list_match_file_control():
            self.view.message_tournament_launched()
            self.controller.menu_controller.run_tournament_menu()
        if self.controller.player_list_controller.control_player_select_controller():
            if self.controller.player_list_controller.control_number_player_in_list_players_select():
                self.shuffle_players()
            else:
                self.view.message_message_start_tournament_missing_player()
        else:
            self.view.message_message_start_tournament_missing_player()

    def shuffle_players(self):
        """Mélanger les joueurs inscrits"""
        dateiso = time.strftime('%d/%m/%Y - %H:%M')
        temporary_list = []
        player_number = 0
        color_1 = "Blanc"
        color_2 = "Noir"
        list_player_select = self.db.get_list_player_select_db()
        random.shuffle(list_player_select)
        """Ajouter la date et l'heure de début et assigner une couleur"""
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
                "score": list_player_select1["score"]
            }
            temporary_list.append(player)

        self.db.add_player_shuffle_in_list_match_json(temporary_list)
        self.create_teams()

    def create_teams(self):
        temporary_list = self.db.get_player_list_match()
        self.view.message_start_tournament()
        self.view.print_start_match(temporary_list)
        self.controller.menu_controller.run_tournament_menu()

    def player_selection(self):
        """Si le fichier Round1.json n'existe pas"""
        if not self.controller.player_list_controller.round_file_control():
            list_match = self.db.get_player_list_match() # Récupération des données de List_MatchX.json
            self.view.view_match_for_score_entry(list_match) # Affiche à l'utilisateur la liste des joueurs
            user_input = self.view.get_user_input_match_for_score_entry() # Demande à l'utilisateur de saisir un joueur pour entrer le score
            """Control de la saisie utilisateur"""
            self.user_input_control(user_input, list_match)
            self.view.team_selection_view() # Affiche "Saisie des scores"
            self.team_selection(user_input)

        """Si le fichier Round1.json existe"""
        list_match = self.db.get_list_match_and_round() # Récupération des joueurs n'ayant pas eu de score
        self.view.view_match_for_score_entry(list_match)  # Affiche à l'utilisateur la liste des joueurs
        """Control de la saisie utilisateur"""
        """ Demande à l'utilisateur de saisir un joueur pour entrer le score"""
        user_input2 = self.view.get_user_input_match_for_score_entry()
        self.user_input_control(user_input2, list_match) # Controle de la saisie utilisateur
        self.view.team_selection_view() # Affiche "Saisie des scores"
        self.team_selection(user_input2) # Demande à l'utilisateur Match Nul ou Gagnant / Perdant

    def team_selection(self, user_input2):
        """Si le fichier Round1.json n'existe pas"""
        if not self.controller.player_list_controller.round_file_control():
            user_input = self.view.get_user_input_match_for_score_entry2() # Demande Match Nul ou Gagnant / Perdant
            self.user_input_control2(user_input)
            user_input = int(user_input)
            user_input2 = int(user_input2)
            self.db.add_score_to_players(user_input, user_input2)
            self.input_control_player_selection()

        """Si le fichier Round1.json existe"""
        user_input = self.view.get_user_input_match_for_score_entry2()  # Demande Match Nul ou Gagnant / Perdant
        self.user_input_control2(user_input)
        user_input = int(user_input)
        user_input2 = int(user_input2)
        self.db.add_score_to_players(user_input, user_input2)
        """Fonctionnalité qui control le nombre de joueurs qui se trouve dans le fichier RoundX.json"""
        numbers_players = self.controller.player_list_controller.control_number_player_in_list_round()
        if numbers_players == 8:
            self.view.end_of_game_message()
            """Crer le fichier des scores"""
            self.create_file_score_controller()
            """Créer le fichier du match suivant"""
            """Afficher Le match suivant"""
            """Retour au menu GESTIONNAIRE DU TOURNOI"""
            self.controller.menu_controller.run_tournament_menu()

        else:
            self.input_control_player_selection()

    def user_input_control2(self, user_input):
        user_input2 = True
        while user_input2:
            if user_input == "":
                self.view.empty_user_input()
                user_input2 = True
            else:
                user_input = int(user_input)
                if user_input > 2:
                    self.view.incorrect_entry()
                    user_input2 = True
                elif user_input <= 2:
                    user_input2 = False


    def user_input_control(self, user_input, list_match):
        """Control de la saisie utilisateur
            Control que la saisie correspond au nombre de joueurs dans la liste
        """
        numbers = len(list_match)  # Calcul le nombre de joueurs dans cette liste
        user_input2 = True
        while user_input2:

            if user_input == "":
                self.view.empty_user_input()
                user_input2 = True
            else:
                user_input = int(user_input)
                if user_input == 0:
                    self.view.incorrect_entry()
                    user_input2 = True
                elif user_input > numbers:
                    self.view.incorrect_entry()
                    user_input2 = True
                elif user_input <= numbers:
                    user_input2 = False


    def input_control_player_selection(self):
        """Control de la saisie utilisateur"""
        user_input2 = True
        while user_input2:
            user_input = self.view.ask_to_continue()  # Demander à l'utilisateur s'il souhaite enregistrer un autre score
            if user_input == "":
                self.view.empty_user_input()
                user_input2 = True
            elif user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o":
                self.player_selection()
            elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no":
                self.controller.menu_controller.run_tournament_menu()
            else:
                self.view.incorrect_entry()
                user_input2 = True

    def show_team_table_controller(self):
        """Méthode qui permet d'afficher les équipes"""
        self.view.print_message_team_table()
        list_match = self.db.get_player_list_match()
        self.view.print_start_match(list_match)
        self.controller.menu_controller.run_tournament_menu()


    def create_file_score_controller(self):
        """Récupérer les données du fichier RoundX.json"""
        list_round = self.db.get_list_round()
        """Trie des joueurs par ordre de joueurs"""
        player_sorted = self.db.sorted_by_player_order(list_round)
        """Ajouter les joueurs avec leurs score dans un fichier json"""
        self.db.add_scores_to_players_in_file_score(player_sorted)



