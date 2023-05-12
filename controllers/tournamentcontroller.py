from models import TournamentModel
from datetime import datetime
import os


class TournamentController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory


    def control(self):
        """
        Méthode qui contrôle si le répertoire tournament est vide ou non
        Si directory1 = True, alors il affiche un message d'erreur
        Sinon il procède à l'enregistrement du tournoi
        """
        data = os.getcwd()
        path = f"{data}/data/tournament/"
        directory1 = os.listdir(path)
        if directory1:
            self.view.tournament_error_message1()
            self.controller.menu_controller.run()

        else:
            """Création d'un tournoi"""
            self.view.start_tournament()


        def tournament_name_controller():
            tournament_name = self.view.tournament_name()
            if tournament_name == "":
                self.view.tournament_error_message2()
                tournament_name_controller()
            else:
                self.dm.make_directory_tournament(tournament_name)
                return tournament_name

        def tournament_place_controller():
            place = self.view.tournament_place()
            if place == "":
                self.view.tournament_error_message2()
                tournament_place_controller()
            else:
                return place

        def tournament_start_date_controller():
            try:
                date_string = self.view.tournament_start_date()
                date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
                start_date = date_object.strftime("%d/%m/%Y")
                return str(start_date)
            except ValueError:
                self.view.date_error_message()
                tournament_start_date_controller()

        def tournament_end_date_controller():
            try:
                date_string = self.view.tournament_end_date()
                date_object = datetime.strptime(date_string, "%d/%m/%Y").date()
                end_date = date_object.strftime("%d/%m/%Y")
                return str(end_date)
            except ValueError:
                self.view.date_error_message()
                tournament_end_date_controller()

        def tournament_directore_remark_controller():
            directore_remark = self.view.tournament_directore_remark()
            if directore_remark == "":
                self.view.tournament_error_message2()
                tournament_directore_remark_controller()
            else:
                return directore_remark

        tournamentmodel = TournamentModel(
            tournament_name_controller(),
            tournament_place_controller(),
            tournament_start_date_controller(),
            tournament_end_date_controller(),
            tournament_directore_remark_controller(),

        )
        self.db.add_tournament_in_json(tournamentmodel)
        self.controller.menu_controller()












