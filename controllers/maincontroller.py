from controllers import MenuController, PlayerController, TournamentController
from views import MenuView, TournamentView


class MainController:
    def __init__(self):
        self.menu_controller = MenuController(MenuView(), self)
        self.tournament_controller = TournamentController(TournamentView(), self)
        self.player_controller = PlayerController()

    def run(self):
        self.menu_controller.run()

