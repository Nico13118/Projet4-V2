class MatchController:
    def __init__(self, controller, database):
        self.controller = controller
        self.db = database

    def make_team_list_match(self, temporary_list_match):
        """Création des équipes depuis list_MatchX.json """
        match_list = []
        for i in range(0, len(temporary_list_match), 2):
            player1 = temporary_list_match[i]
            player2 = temporary_list_match[i + 1]
            team_match = player1, player2
            match_list.append(team_match)
        return match_list

    def make_team_list_round(self, list_round_sorted):
        """Création des équipes depuis RoundX.json """
        round_list = []
        for i in range(0, len(list_round_sorted), 2):
            player1 = list_round_sorted[i]
            player2 = list_round_sorted[i + 1]
            team_round = player1, player2
            round_list.append(team_round)
        return round_list

    def extract_player_number_from_list_match(self, match_list):
        """Récupération du numéro de joueur de list_MatchX.json"""
        numbers_player = []
        for i in range(0, len(match_list), 1):
            equipe_list_match = match_list[i]
            joueur1_equipe_match1, joueur2_equipe_match1 = equipe_list_match[0], equipe_list_match[1]
            nbrs_joueur1_match, nbrs_joueur2_match = joueur1_equipe_match1["joueur"], joueur2_equipe_match1["joueur"]
            equipe_match = nbrs_joueur1_match, nbrs_joueur2_match
            numbers_player.append(equipe_match)
        return numbers_player

    def extract_player_number_from_list_round(self, round_list):
        """Récupération du numéro de joueur de list_MatchX.json"""
        numbers_player = []
        for i in range(0, len(round_list), 1):
            equipe2_list_round = round_list[i]
            joueur1_equipe_round1, joueur2_equipe_round1 = equipe2_list_round[0], equipe2_list_round[1]
            nbrs_joueur1_round, nbrs_joueur2_round = joueur1_equipe_round1["joueur"], joueur2_equipe_round1["joueur"]
            equipe1_round = nbrs_joueur1_round, nbrs_joueur2_round
            numbers_player.append(equipe1_round)
        return numbers_player

    def sorted_match_list_and_round(self, numbers_player_match, number_player_round):
        """Méthode qui sépare les joueurs qui ont joués ensemble dans une liste et
            les autres dans une autre liste
        """
        player_list_no_ok = []
        player_list_ok = []
        final_list = []

        for number_player_round1 in number_player_round:
            if number_player_round1 in numbers_player_match:
                player_list_no_ok.append(number_player_round1)
            else:
                player_list_ok.append(number_player_round1)
        info_list = len(player_list_no_ok)
        if info_list == 4:
            """Ajout des joueurs dans final_list"""
            for player_list_no_ok1 in player_list_no_ok:
                player1 = player_list_no_ok1[0]
                player2 = player_list_no_ok1[1]
                final_list.append(player1)
                final_list.append(player2)
            return final_list
        else:
            for player_list_ok1 in player_list_ok:
                player1 = player_list_ok1[0]
                player2 = player_list_ok1[1]
                final_list.append(player1)
                final_list.append(player2)

            if info_list == 1:
                team1_select = player_list_no_ok[0]
                player_select1, player_select2 = team1_select[0], team1_select[1]
                final_list.append(player_select2)
                final_list.append(player_select1)

            if info_list == 2:
                team1_select = player_list_no_ok[0]
                team2_select = player_list_no_ok[1]
                player_select1, player_select2 = team1_select[0], team2_select[0]
                final_list.append(player_select1)
                final_list.append(player_select2)
                player_select3, player_select4 = team1_select[1], team2_select[1]
                final_list.append(player_select3)
                final_list.append(player_select4)

            if info_list == 3:
                team1_select = player_list_no_ok[0]
                team2_select = player_list_no_ok[1]
                team3_select = player_list_no_ok[2]
                player_select1, player_select2 = team1_select[0], team2_select[3]
                player_select3, player_select4 = team1_select[1], team3_select[4]
                player_select5, player_select6 = team2_select[2], team3_select[5]
                final_list.append(player_select1)
                final_list.append(player_select2)
                final_list.append(player_select3)
                final_list.append(player_select4)
                final_list.append(player_select5)
                final_list.append(player_select6)

            return final_list

    def player_selection_from_list_match(self, final_list):
        new_list_match = []
        number_player = self.controller.player_list_controller.control_number_player_in_list_round()
        list_match = self.db.get_player_list_match()
        for i in final_list:
            i -= 1
            player_select = list_match[i]
            new_list_match.append(player_select)
            info_list = len(new_list_match)
            if info_list == number_player:
                return new_list_match
