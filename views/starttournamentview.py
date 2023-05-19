class StartTournamentView:
    def message_start_tournament(self):
        print("Lancement du tournoi")

    def message_start_tournament_missing_player(self):
        print("Action impossible, vous devez ajouter des joueurs dans le tournoi")

    def print_match(self, temporary_list):
        select1 = temporary_list[0]
        select2 = temporary_list[1]
        select3 = temporary_list[2]
        select4 = temporary_list[3]
        select5 = temporary_list[4]
        select6 = temporary_list[5]
        select7 = temporary_list[6]
        select8 = temporary_list[7]
        print(f"Équipe 1 :", select1["nom"], select1["prenom"], "(", select1["couleur"], ")", "VS",
              select2["nom"], select2["prenom"], "(", select2["couleur"], ")")
        print(f"Équipe 2 :", select3["nom"], select3["prenom"], "(", select3["couleur"], ")", "VS",
              select4["nom"], select4["prenom"], "(", select4["couleur"], ")")
        print(f"Équipe 3 :", select5["nom"], select5["prenom"], "(", select5["couleur"], ")", "VS",
              select6["nom"], select6["prenom"], "Couleur:", select6["couleur"])
        print(f"Équipe 4 :", select7["nom"], select7["prenom"], "(", select7["couleur"], ")", "VS",
              select8["nom"], select8["prenom"], "(", select8["couleur"], ")")