from datetime import datetime
import os


class TournamentController:
    def __init__(self, view, controller):
        self.view = view
        self.controller = controller

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
            self.tournament_name_controller()
            self.tournament_place_controller()
            self.tournament_start_date_controller()
            self.tournament_end_date_controller()
            self.tournament_directore_remark_controller()
            self.controller.menu_controller.run()

    def tournament_name_controller(self):
        tournament_name = self.view.tournament_name()
        if tournament_name == "":
            self.view.tournament_error_message2()
            self.tournament_name_controller()
        else:
            return tournament_name

    def tournament_place_controller(self):
        place = self.view.tournament_place()
        if place == "":
            self.view.tournament_error_message2()
            self.tournament_place_controller()
        else:
            return place

    def tournament_start_date_controller(self):
        start_date = self.view.tournament_start_date()
        try :
            start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
            return start_date
        except ValueError:
            self.view.date_error_message()
            self.tournament_start_date_controller()

    def tournament_end_date_controller(self):
        end_date = self.view.tournament_end_date()
        try:
            end_date = datetime.strptime(end_date, "%d/%m/%Y").date()
            return end_date
        except ValueError:
            self.view.date_error_message()
            self.tournament_end_date_controller()

    def tournament_directore_remark_controller(self):
        directore_remark = self.view.tournament_directore_remark()
        if directore_remark == "":
            self.view.tournament_error_message2()
            self.tournament_directore_remark_controller()
        else:
            return directore_remark












