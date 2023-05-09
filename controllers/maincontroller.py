from controllers import MenuController
from views import MenuView


class MainController:
    def __init__(self):
        self.menu_controller = MenuController(MenuView(), self)

    def run(self):
        self.menu_controller.run()

