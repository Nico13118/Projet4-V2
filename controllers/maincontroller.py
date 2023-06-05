from controllers.menucontroller import MenuController
from controllers.playercontroller import PlayerController
from controllers.tournamentcontroller import TournamentController
from controllers.databasecontroller import DatabaseController
from controllers.playerlistcontroller import PlayerListController
from controllers.starttournamentcontroller import StartTournamentController
from controllers.matchcontroller import MatchController
from controllers.reportcontroller import ReportController
from views.menuview import MenuView
from views.tournamentview import TournamentView
from views.playerview import PlayerView
from views.playerlistview import PlayerListView
from views.starttournamentview import StartTournamentView
from views.reportview import ReportView
from models.directorymodel import DirectoryModel


class MainController:
    def __init__(self):
        self.dm = DirectoryModel()
        self.db = DatabaseController(self)
        self.mc = MatchController(self, self.db)
        self.menu_controller = MenuController(MenuView(), self, self.db, self.dm)
        self.tournament_controller = TournamentController(TournamentView(), self, self.db, self.dm)
        self.player_controller = PlayerController(PlayerView(), self, self.db, self.dm)
        self.player_list_controller = PlayerListController(PlayerListView(), self, self.db, self.dm)
        self.report_controller = ReportController(ReportView(), self, self.db, self.dm)
        self.start_tournament_controller = StartTournamentController(StartTournamentView(), self, self.db, self.dm,
                                                                     self.mc)

    def run(self):
        self.menu_controller.run_menu()
