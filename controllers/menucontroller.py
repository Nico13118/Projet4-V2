
class MenuController:
    def __init__(self, view, controller):
        self.view = view
        self.controller = controller

    def run(self):
        self.view.club_name()
        user_input = self.view.get_user_input()
        if user_input == 1:
            print("Test1")
        elif user_input == 2:
            print("Test2")
        elif user_input == 3:
            print("Test3")
        elif user_input == 4:
            print("Test4")
        elif user_input == 5:
            quit()
        else:
            self.run()





