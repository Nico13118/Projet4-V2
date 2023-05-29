class ReportController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def current_tournament_report(self):
        """Pour afficher les informations du tournoi en cours"""
        if self.dm.control_tournament_directory():
            tournament_info = self.db.get_tournament_information()
            self.view.report_message()
            self.view.print_tournament_info(tournament_info)
            """Appel des autres méthodes pour afficher :
                La liste des joueurs inscrits au tournoi 
                Le tableau des équipes
                Le round en cours
             """
            self.current_player_report()
            self.match_in_progress()
            self.round_in_progress()
            self.controller.menu_controller.run_menu_report()
        else:
            self.view.message_no_tournament_directory()
            self.controller.menu_controller.run_menu_report()

    def current_player_report(self):
        """Pour afficher la liste des joueurs inscrits au tournoi"""
        if self.controller.player_list_controller.control_player_select_controller():
            list_player_select = self.db.get_list_player_select_db()
            list_player_select = self.db.sort_player_list_db(list_player_select)
            self.view.message_list_of_players_selected()
            self.view.show_selected_players(list_player_select)
        else:
            self.view.no_list_of_players_selected()
            self.controller.menu_controller.run_menu_report()

    def match_in_progress(self):
        """Pour afficher le tableau des équipes """
        if self.controller.player_list_controller.list_match_file_control():
            number_files = self.controller.player_list_controller.number_files_in_list_match()
            number_files1 = 1
            while not number_files1 > number_files:
                match_list = self.db.get_player_list_match()
                self.view.table_of_teams(match_list, number_files1)
                number_files1 += 1
        else:
            self.view.no_match_list_to_display()

    def round_in_progress(self):
        """Pour afficher le résultat du round en cours"""
        if self.controller.player_list_controller.round_file_control():
            number_files = self.controller.player_list_controller.number_files_round()
            number_files1 = 1
            while not number_files1 > number_files:
                round_list = self.db.get_round_list_for_report(number_files1)
                self.view.show_round_list(round_list, number_files1)
                number_files1 += 1
            self.controller.menu_controller.run_menu_report()
        else:
            self.view.no_round_list_to_display()

    def score_in_progress(self):
        pass

