from controllers.maincontroller import MainController
from models.directorymodel import DirectoryModel


def main():
    main_controller = MainController()
    directory_model = DirectoryModel()
    directory_model.make_directory1()
    main_controller.run()


if __name__ == "__main__":
    main()
