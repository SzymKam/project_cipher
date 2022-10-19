from menu import Menu
from rot import RotManager
import buffer


class Manager:
    def __init__(self) -> None:
        self.__option = None
        self.__is_running = True
        self.__menu = Menu()
        self.__rot_manager = RotManager()
        self.__options = {5: self.__end_app,
                          # 4: "save to file",
                          # 3: "load from file",
                          2: buffer.my_buffer.run_buffer,
                          1: self.__rot_manager.start,
                          }

    def run(self) -> None:
        while self.__is_running:
            self.__menu.print_main_menu()
            self.choose_option()
            self.execute(choice=self.__option)

    def choose_option(self) -> None:
        self.__option = int(input("Enter number of option: \n"))
        print(f"You choose {self.__option}\n")

    def execute(self, choice: int) -> None:
        self.__options.get(choice, "INVALID OPTION")()

    def __end_app(self) -> None:
        self.__is_running = False
