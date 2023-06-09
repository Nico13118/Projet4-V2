class MenuView:
    def club_name(self):
        print("\n*************** Club Provence Échecs *************** ")

    def get_user_input_main_menu(self):
        """
        Affichage du menu
        Récupération de la saisie utilisateur
        : return : Retourne la saisie utilisateur
        """
        print("\n|============= MENU PRINCIPAL ===============|")
        print("| 1 - Gestionnaire de joueurs                |")
        print("| 2 - Gestionnaire de tournoi                |")
        print("| 3 - Rapport de tournoi                     |")
        print("| 4 - Quitter l'application                  |")
        print("|============================================|")

    def get_user_input_player_menu(self):
        print("\n|======== GESTIONNAIRE DE JOUEURS ===========|")
        print("| 0 - Retourner au menu principal            |")
        print("| 1 - Enregistrement de joueurs              |")
        print("| 2 - Lister les joueurs enregistrés         |")
        print("| 3 - Supprimer un joueur enregistré         |")
        print("|============================================|")

    def get_user_input_tournament_menu(self):
        print("\n|========= GESTIONNAIRE DE TOURNOI ==========|")
        print("| 0 - Retourner au menu principal            |")
        print("| 1 - Créer un tournoi                       |")
        print("| 2 - Inscrire des joueurs au tournoi        |")
        print("| 3 - lister les joueurs inscrits au tournoi |")
        print("| 4 - Retirer un joueurs du tournoi          |")
        print("| 5 - Lancer le tournoi                      |")
        print("| 6 - Saisir les scores                      |")
        print("| 7 - Lister les équipes                     |")
        print("| 8 - Supprimer un tournoi                   |")
        print("|============================================|")

    def get_user_input4(self):
        print("\n|==================== RAPPORT DE TOURNOI ====================|")
        print("| 0 - Retourner au menu principal                            |")
        print("| 1 - Visualiser le rapport du tournoi en cours              |")
        print("| 2 - Visualiser le rapport des tournois précédents          |")
        print("| 3 - Éditer un rapport du tournoi en cours (format txt)     |")
        print("| 4 - Éditer un rapport des tournois précédents (format txt) |")
        print("|============================================================|")

    def error_message_menuview1(self):
        print("Choix invalide !!!")

    def error_message_menuview2(self):
        print("La saisie ne peut pas être vide !!")

    def repeat_message(self):
        user_input = input("Faite votre choix :")
        return user_input

    def incorrect_entry(self):
        print("Saisie incorrect !! Veuillez réessayer.")
