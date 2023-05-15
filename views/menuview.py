class MenuView:

    def club_name(self):
        print("\n******** Club Provence Échecs ********* ")

    def error_message_menuview1(self):
        print("Choix invalide !!!")

    def error_message_menuview2(self):
        print("La saisie ne peut pas être vide !!")

    def get_user_input(self):
        """
        Récupération de la saisie utilisateur
        :return: Retourne la saisie utilisateur
        """

        def print_menu():
            """
                    Affichage du menu

                    """
            print("\n|================== MENU ==================|")
            print("| 1 -Créer un tournoi.                      |")
            print("| 2 -Inscription des joueurs                |")
            print("| 3 -Gérer les joueurs                      |")
            print("| 4 -Gérer les tournois                     |")
            print("| 5 -Rapport de tournoi                     |")
            print("| 6 -Quitter l'application.                 |")
            print("|===========================================|")

        print_menu()
        user_input = input("Faite votre choix :")
        return user_input

    def get_user_input2(self):

        def print_menu_player():
            print("\n|============ Gérer les joueurs ===========|")
            print("| 1 -Voir la liste des joueurs              |")
            print("| 2 -Supprimer un joueur de la liste        |")
            print("| 3 -Retourner au menu principal            |")
            print("|===========================================|")

        print_menu_player()
        user_input = input("Faite votre choix :")
        return user_input

    def get_user_input3(self):

        def print_menu_tournament():
            print("\n|=========== Gérer les tournois ===========|")
            print("| 1 -Ajouter des joueurs au tournoi         |")
            print("| 2 -Supprimer des joueurs du tournoi       |")
            print("| 3 -Lancer le tournoi                      |")
            print("| 4 -Reprendre un tournoi                   |")
            print("| 5 -Supprimer un tournoi                   |")
            print("| 6 -Retourner au menu principal            |")
            print("|===========================================|")

        print_menu_tournament()
        user_input = input("Faite votre choix :")
        return user_input

    def get_user_input4(self):

        def print_menu_report():
            print("\n|=========== Rapport de tournoi ===========|")
            print("| 1 -Rapport du tournoi en cours            |")
            print("| 2 -Rapport des tournois précédents.       |")
            print("| 3 -Retourner au menu principal            |")
            print("|===========================================|")

        print_menu_report()
        user_input = input("Faite votre choix :")
        return user_input
