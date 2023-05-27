import os

MAX_PLAYER = 8


class PlayerListController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def print_player_list_controller(self):
        """Méthode qui permet d'afficher la liste List_Registered_Players.json dans l'ordre alphabétique"""
        if self.control_player_list_controller(): # Si la présence du fichier est True
            list_player = self.db.get_player_list() # Extraire les données de la liste
            player_sorted = self.db.sort_player_list_db(list_player) # Tries la liste des joueurs par ordre alphabétique
            self.view.message_list_view()
            self.view.print_player_list_view(player_sorted) # Affiche la liste des joueurs
        else:
            self.controller.menu_controller.run_menu_player()

    def print_list_player_select(self):
        """Méthode qui permet d'afficher la liste List_Players_Select.json"""
        list_player_select = self.db.get_list_player_select_db()
        self.view.print_list_player_select()
        self.view.print_player_list_view(list_player_select)
        self.controller.menu_controller.run_tournament_menu()

    def del_player_in_list_controller(self):
        """Méthode qui permet d'afficher la liste List_Registered_Players.json
            dans l'ordre et de supprimer un joueur de cette liste
            """
        if self.control_player_list_controller(): # Si la présence du fichier est True
            self.view.message_del_player() # Demande à l'utilisateur s'il souhaite continuer
            self.control_user_input_del_player_in_list_controller()
            list_player = self.db.get_player_list()  # Extraire les données de la liste
            player_sorted = self.db.sort_player_list_db(list_player)  # Tries la liste des joueurs par ordre alphabétique
            self.view.message_list_view()  # Affiche le message - Liste des joueurs enregistrés -
            self.view.print_player_list_view(player_sorted)  # Affiche la liste des joueurs triés par ordre alphabétique
            self.view.message_del_player_in_list_view()  # Demander à l'utilisateur le joueur à supprimer
            return_user_input = self.control_user_input_del_player_list_player_select(player_sorted)
            self.db.del_player_in_list_db(return_user_input)  # Envoie le choix de l'utilisateur
            self.view.message_del_player_in_list_view2()  # Message qui confirme la suppression
        else:
            self.view.message_error_list_view()
            self.controller.menu_controller.run_menu_player()

    def del_player_in_list_player_select(self):
        """Méthode qui permet d'afficher la liste List_Players_Select.json
            dans l'ordre et de supprimer un joueur de cette liste
        """
        if self.control_player_select_controller():
            list_player_select = self.db.get_list_player_select_db() # Récupération de la liste des joueurs inscrits
            player_sorted = self.db.sort_player_list_db(list_player_select)  # Tries la liste des joueurs par ordre alphabétique
            self.view.print_list_player_select() # Affiche "Liste des joueurs inscrits au tournoi"
            self.view.print_player_list_view(player_sorted) # Affiche la liste des joueurs inscrits dans l'ordre alphabétique
            self.view.message_del_player_in_list_view()  # Demande à l'utilisateur de faire son choix
            return_user_input = self.control_user_input_del_player_list_player_select(player_sorted)
            self.db.del_player_in_list_player_select_db(return_user_input)
            self.view.message_del_player_in_list_view2()
            self.controller.menu_controller.run_tournament_menu()
        else:
            self.view.message_error_list_view()
            self.controller.menu_controller.run_tournament_menu()

    def control_user_input_del_player_in_list_controller(self):
        user_input2 = True
        while user_input2:
            user_input = self.view.repeat_message()
            if user_input == "":
                self.view.message_error_list_view3()
            if user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o":
                user_input2 = False
            if user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no":
                self.controller.menu_controller.run_menu_player()
            if user_input.isdigit():
                self.view.message_error_list_view2()

    def control_user_input_del_player_list_player_select(self, player_sorted):
        user_input2 = True
        while user_input2:
            user_input = self.view.repeat_message()
            if user_input == "":
                self.view.message_error_list_view3()
            if str(user_input).isalpha():
                self.view.message_error_list_view4()
            """Controle combien de joueur sont inscrits dans la liste """
            if user_input != "" and not str(user_input).isalpha():
                numbers = len(player_sorted)
                user_input = int(user_input)
                if user_input > numbers:
                    self.view.message_error_list_view4()
                elif user_input == 0:
                    self.view.message_error_list_view4()
                else:
                    return user_input


    def control_player_list_controller(self):
        """Controle si le fichier List_Registered_Players.json existe"""
        data = os.getcwd()
        path1 = f"{data}/data/players_list"
        directory1 = os.listdir(path1)
        if directory1:
            return True
        else:
            self.view.message_error_list_view()
            return False

    def control_player_select_controller(self):
        """Controle si le fichier List_Players_Select.json existe"""
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory = os.listdir(path)
        tournament_name = str(directory[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Player_Select"
        directory_player_select = os.listdir(path2)
        if directory_player_select:
            return True
        else:
            return False

    def control_number_player_in_list_players_select(self):
        temporary_list = []
        """Controle le nombre de joueurs inscrits dans List_Players_Select.json" """
        list_player_select = self.db.get_list_player_select_db()
        for list_player_select1 in list_player_select:
            temporary_list.append(list_player_select1)
        numbers_players = len(temporary_list)
        if numbers_players == MAX_PLAYER:
            return True

        else:
            return False

    def round_file_control(self):
        """Méthode qui controle la présence du fichier Round"""
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
        temporary_list = []
        list_round = self.db.get_list_round()
        for list_round1 in list_round:
            temporary_list.append(list_round1)
        numbers_players = len(temporary_list)
        numbers_players = int(numbers_players)
        return numbers_players

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

    def number_of_score_files(self):
        """Méthode qui controle le nombre de fichiers qu'il y a dans le répertoire Scores """
        data = os.getcwd()
        path1 = f"{data}/data/tournament/"
        directory1 = os.listdir(path1)
        tournament_name = str(directory1[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Scores"
        directory2 = os.listdir(path2)
        number_files = len(directory2)
        return number_files

    def get_score_file_names(self):
        data = os.getcwd()
        path1 = f"{data}/data/tournament/"
        directory1 = os.listdir(path1)
        tournament_name = str(directory1[0])
        path2 = f"{data}/data/tournament/{tournament_name}/Scores"
        score_files = os.listdir(path2)
        return score_files
