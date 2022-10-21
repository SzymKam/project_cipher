from menu import Menu
from rot import RotManager
from buffer import BufferManager


class Manager:
    def __init__(self) -> None:
        self.__option = None
        self.__is_running = True
        self.__menu = Menu()
        self.__buffer_start = BufferManager()
        self.__rot_manager = RotManager()
        self.__options = {5: self.__end_app,
                          # 4: "save to file",
                          2: self.__buffer_start.buffer_run,
                          1: self.__rot_manager.rot_run,
                          }

    def run(self) -> None:
        while self.__is_running:
            self.__menu.print_main_menu()
            self.__option = int(input("Enter number of option: \n"))
            self.handle_instruction(choice=self.__option)

    def handle_instruction(self, choice: int) -> None:
        if choice in self.__options:
            self.__options.get(choice, "INVALID OPTION")()
        else:
            print("Invalid option.")

    def __end_app(self) -> None:
        print("Program shutting down.\n")
        self.__is_running = False
