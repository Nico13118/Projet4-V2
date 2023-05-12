from controllers import MenuController, PlayerController, TournamentController, DatabaseController
from views import MenuView, TournamentView, PlayerView
from models import DirectoryModel


class MainController:
    def __init__(self):
        self.dm = DirectoryModel()
        self.db = DatabaseController()
        self.menu_controller = MenuController(MenuView(), self, self.db, self.dm)
        self.tournament_controller = TournamentController(TournamentView(), self, self.db, self.dm)
        self.player_controller = PlayerController(PlayerView(), self, self.db, self.dm)

    def run(self):
        self.menu_controller.run()

