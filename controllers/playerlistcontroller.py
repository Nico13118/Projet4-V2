import os
import re
MAX_PLAYER = 8


class PlayerListController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def print_player_list_controller(self):
        """Méthode qui permet d'afficher la liste List_Registered_Players.json dans l'ordre alphabétique"""
        """Si le fichier List_Registered_Players existe"""
        """"Si la présence du fichier est True"""
        if self.control_player_list_controller():
            """Extraire les données de la liste"""
            list_player = self.db.get_player_list()
            """Tries la liste des joueurs par ordre alphabétique"""
            player_sorted = self.db.sort_player_list_db(list_player)
            self.view.message_list_view()
            """Affiche la liste des joueurs"""
            self.view.print_player_list_view(player_sorted)
            self.controller.menu_controller.run_menu_player()
        else:
            self.view.message_no_list()
            self.controller.menu_controller.run_menu_player()

    def print_list_player_select(self):
        """Méthode qui permet d'afficher la liste List_Players_Select.json"""
        if not self.dm.control_tournament_directory():
            self.view.message_no_tournament_directory()
            self.controller.menu_controller.run_tournament_menu()

        if self.control_player_select_controller():
            number = self.control_number_player_in_list_players_select2()
            if number >= 1:
                list_player_select = self.db.get_list_player_select_db()
                self.view.print_list_player_select()
                self.view.print_player_list_view(list_player_select)
                self.controller.menu_controller.run_tournament_menu()
            else:
                self.view.message_error_list_view()
                self.controller.menu_controller.run_tournament_menu()
        else:
            self.view.message_error_list_view()
            self.controller.menu_controller.run_tournament_menu()

    def del_player_in_list_controller(self):
        """Méthode qui permet d'afficher la liste List_Registered_Players.json
            dans l'ordre et de supprimer un joueur de cette liste
            """
        """# Si la présence du fichier est True"""
        if self.control_player_list_controller():
            """Demande à l'utilisateur s'il souhaite continuer"""
            self.view.message_del_player()
            self.control_user_input_del_player_in_list_controller()
            """ Extraire les données de la liste"""
            list_player = self.db.get_player_list()
            """ Tries la liste des joueurs par ordre alphabétique"""
            player_sorted = self.db.sort_player_list_db(list_player)
            """# Affiche le message - Liste des joueurs enregistrés -"""
            self.view.message_list_view()
            """ Affiche la liste des joueurs triés par ordre alphabétique"""
            self.view.print_player_list_view(player_sorted)
            """ Demander à l'utilisateur le joueur à supprimer"""
            self.view.message_del_player_in_list_view()
            return_user_input = self.control_user_input_del_player_list_player_select(player_sorted)
            """ Envoie le choix de l'utilisateur"""
            self.db.del_player_in_list_db(return_user_input)
            """ Message qui confirme la suppression"""
            self.view.message_del_player_in_list_view2()
            self.controller.menu_controller.run_menu_player()
        else:
            self.view.message_no_list()
            self.controller.menu_controller.run_menu_player()

    def del_player_in_list_player_select(self):
        """Méthode qui permet d'afficher la liste List_Players_Select.json
            dans l'ordre et de supprimer un joueur de cette liste
        """
        if not self.list_match_file_control():
            if not self.dm.control_tournament_directory():
                self.view.message_no_tournament_directory()
                self.controller.menu_controller.run_tournament_menu()

            if self.control_player_select_controller():
                number = self.control_number_player_in_list_players_select2()
                if number >= 1:
                    """ Récupération de la liste des joueurs inscrits"""
                    list_player_select = self.db.get_list_player_select_db()
                    """ Tries la liste des joueurs par ordre alphabétique"""
                    player_sorted = self.db.sort_player_list_db(list_player_select)
                    """ Affiche "Liste des joueurs inscrits au tournoi"""
                    self.view.print_list_player_select()
                    """ Affiche la liste des joueurs inscrits dans l'ordre alphabétique"""
                    self.view.print_player_list_view(player_sorted)
                    """ Demande à l'utilisateur de faire son choix"""
                    self.view.message_del_player_in_list_view()
                    return_user_input = self.control_user_input_del_player_list_player_select(player_sorted)
                    self.db.del_player_in_list_player_select_db(return_user_input)
                    self.view.message_del_player_in_list_view2()
                    self.controller.menu_controller.run_tournament_menu()
                else:
                    self.view.message_error_list_view()
                    self.controller.menu_controller.run_tournament_menu()
            else:
                self.view.message_error_list_view()
                self.controller.menu_controller.run_tournament_menu()
        else:
            self.view.tournament_already_launched()
            self.controller.menu_controller.run_tournament_menu()

    def control_user_input_del_player_in_list_controller(self):
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.repeat_message()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if user_input.isdigit():
                        self.view.message_error_list_view2()
                    if not user_input.isdigit():
                        if user_input != "y" or user_input == "yes" or user_input == "oui" or user_input == "o":
                            self.view.message_error_list_view4()
                        if user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o":
                            user_input2 = False
                        if user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no":
                            self.controller.menu_controller.run_menu_player()
                else:
                    self.view.message_error_list_view4()
            except ValueError:
                self.view.message_error_list_view4()

    def control_user_input_del_player_list_player_select(self, player_sorted):
        user_input2 = True
        while user_input2:
            try:
                user_input = self.view.repeat_message()
                if re.match(r'^[a-zA-Z0-9]+$', user_input):
                    if str(user_input).isalpha():
                        self.view.message_error_list_view4()
                    """Controle combien de joueur sont inscrits dans la liste """
                    if not str(user_input).isalpha():
                        numbers = len(player_sorted)
                        user_input = int(user_input)
                        if user_input > numbers:
                            self.view.message_error_list_view4()
                        elif user_input == 0:
                            self.view.message_error_list_view4()
                        else:
                            return user_input
                else:
                    self.view.message_error_list_view4()
            except ValueError:
                self.view.message_error_list_view4()

    def control_player_list_controller(self):
        """Controle si le fichier List_Registered_Players.json existe"""
        data = os.getcwd()
        path1 = f"{data}/data/players_list"
        directory1 = os.listdir(path1)
        if directory1:
            return True
        else:
            return False

    def control_player_select_controller(self):
        """Controle si le fichier List_Players_Select.json existe"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Player_Select"
        list_player_select_file_in_directory = os.listdir(path2)
        if list_player_select_file_in_directory:
            return True
        else:
            return False

    def control_number_player_in_list_players_select(self):
        """Controle le nombre de joueurs inscrits dans List_Players_Select.json" """
        list_player_select = self.db.get_list_player_select_db()
        numbers_players = len(list_player_select)
        if numbers_players == MAX_PLAYER:
            return True

        else:
            return False

    def control_number_player_in_list_players_select2(self):
        """Permet de connaitre le nombre de joueurs dans la liste List_Players_Select.json"""
        list_player_select = self.db.get_list_player_select_db()
        numbers_players = len(list_player_select)
        return numbers_players

    def round_file_control(self):
        """Méthode qui controle la présence du fichier RoundX.json"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        directory_rounds = os.listdir(path2)
        if directory_rounds:
            return True
        else:
            return False

    def control_number_player_in_list_round(self):
        """Méthode qui controle combien de joueur se trouvent dans le fichier RoundX.json"""
        list_round = self.db.get_list_round()
        numbers_players = len(list_round)
        return numbers_players

    def list_scoreboard_file_control(self):
        """Méthode qui controle l'existance du fichier ScoreBoard.json"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/ScoreBoard"
        file_scoreboard = os.listdir(path2)
        if file_scoreboard:
            return True
        else:
            return False

    def list_match_file_control(self):
        """Méthode qui permet de controler l'existance du fichier List_MatchX.json"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        file_rounds = os.listdir(path2)
        if file_rounds:
            return True
        else:
            return False

    def number_files_round(self):
        """Méthode qui controle le nombre de fichiers qu'il y a dans le répertoire Rounds """
        data = os.getcwd()
        path1 = f"{data}/data/tournament/"
        directory1 = os.listdir(path1)
        tournament_name = str(directory1[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Rounds"
        directory2 = os.listdir(path2)
        number_files = len(directory2)
        return number_files

    def number_files_in_list_match(self):
        """Méthode qui controle le nombre de fichiers qu'il y a dans le répertoire Match """
        data = os.getcwd()
        path1 = f"{data}/data/tournament/"
        directory1 = os.listdir(path1)
        tournament_name = str(directory1[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Match"
        directory2 = os.listdir(path2)
        number_files = len(directory2)
        return number_files

    def nbr_files_in_list_match_old(self, tournament_name):
        """Méthode qui controle le nombre de fichiers qu'il y a dans le répertoire Match de tournament_old """
        data = os.getcwd()
        path1 = f"{data}/data/tournament_old/{tournament_name}/Match"
        directory2 = os.listdir(path1)
        number_files = len(directory2)
        return number_files

    def returns_filenames_list_match(self, tournament_name):
        data = os.getcwd()
        path = f"{data}/data/tournament/tournament_old/{tournament_name}/Match"
        names_list_match = os.listdir(path)
        return names_list_match
