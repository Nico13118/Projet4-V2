class PlayerModel:
    def __init__(self, chess_id, name, first_name, birthday, number_player=0, rounds=0, score=0.0):
        self.chess_id = chess_id
        self.name = name
        self.first_name = first_name
        self.birthday = birthday
        self.number_player = number_player
        self.rounds = rounds
        self.score = score

    def player_registration(self):
        player = {
            "identifiant": self.chess_id,
            "nom": self.name,
            "prenom": self.first_name,
            "naissance": self.birthday,
            "joueur": self.number_player,
            "round": self.rounds,
            "score": self.score
        }
        return player
