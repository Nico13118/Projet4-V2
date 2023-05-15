class PlayerListController:
    def __init__(self, view, controller, database, directory):
        self.view = view
        self.controller = controller
        self.db = database
        self.dm = directory

    def print_player_list_controller(self):
        list_player = self.db.get_player_list()

        if not self.db.get_player_list():
            self.view.message_error_list_view()
            self.controller.menu_controller.run()
        else:
            self.view.message_list_view()
            self.sort_player_list_controller(list_player)

    def sort_player_list_controller(self, list_player):
        player_sorted = sorted(list_player, key=lambda x: (x["nom"], x["prenom"]))
        self.view.print_player_list_view(player_sorted)
