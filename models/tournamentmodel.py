class TournamentModel:
    def __init__(self, tournament_name, place, start_date, end_date, director_remark, number_rounds):
        self.tournament_name = tournament_name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.director_remark = director_remark
        self.number_rounds = number_rounds
        self.tournament = []

    def tournament_registration(self):
        tournament_information = {
            "nom": self.tournament_name,
            "lieu": self.place,
            "date1": self.start_date,
            "date2": self.end_date,
            "remarques": self.director_remark,
            "rounds": self.number_rounds
        }
        self.tournament.append(tournament_information)
        tournament = self.tournament
        return tournament
