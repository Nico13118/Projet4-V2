class MenuView:

    def club_name(self):
        print("\n******** Club Provence Échecs ********* ")


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
            print("|1 -Créer un tournoi.                      |")
            print("|2 -Démarrer un tournoi.                   |")
            print("|3 -Reprendre un tournoi.                  |")
            print("|4 -Visualiser le rapport d'un tournoi.    |")
            print("|5 -Quitter l'application.                 |")
            print("|==========================================|")

        print_menu()
        user_input = input("Faite votre choix :")
        if user_input > "5":
            print("Choix invalide !!!")
        else:
            return user_input in ["1", "2", "3", "4", "5"]
