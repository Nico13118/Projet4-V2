import os


class PlayerListController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def print_player_list_controller(self):
        if self.control_player_list_controller(): # Si la présence du fichier est True
            list_player = self.db.get_player_list() # Extraire les données de la liste
            player_sorted = self.db.sort_player_list_db(list_player) # Tries la liste des joueurs par ordre alphabétique
            self.view.message_list_view()
            self.view.print_player_list_view(player_sorted) # Affiche la liste des joueurs

    def del_player_in_list_controller(self):
        if self.control_player_list_controller(): # Si la présence du fichier est True
            user_input = self.view.message_del_player() # Demande à l'utilisateur s'il souhaite continuer
            if user_input == "Y" or user_input == "y" or user_input == "O" or user_input == "o":
                list_player = self.db.get_player_list() # Extraire les données de la liste
                player_sorted = self.db.sort_player_list_db(list_player)  # Tries la liste des joueur par ordre alphabétique
                self.view.message_list_view() # Affiche le message - Liste des joueurs enregistrés -
                self.view.print_player_list_view(player_sorted) # Affiche la liste des joueurs triés par ordre alphabétique
                user_input = self.view.message_del_player_in_list_view() # Demander à l'utilisateur le joueur à supprimer
                self.db.del_player_in_list_db(user_input) # Envoie le choix de l'utilisateur
                self.view.message_del_player_in_list_view2() # Message qui confirme la suppression
            elif user_input == "N" or user_input == "n" or user_input == "No" or user_input == "no":
                self.controller.menu_controller.run_menu_player()
            else:
                self.view.message_error_list_view2()
                self.del_player_in_list_controller()

    def control_player_list_controller(self):
        """Controle si le fichier existe"""
        data = os.getcwd()
        path = f"{data}/data/players_list"
        directory1 = os.listdir(path)
        if not directory1:
            self.view.message_error_list_view()
            self.controller.menu_controller.run_menu_player()
        else:
            return True

