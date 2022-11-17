from .buffer import Buffer


class BufferManager:
    def __init__(self) -> None:
        self.__choice = None

    def buffer_run(self) -> None:
        self.buffer_menu()
        self.user_choice()
        self.program_choice(choice=self.__choice)

    @staticmethod
    def buffer_menu() -> None:
        print("BUFFER MENU: \n"
              "Check buffer - 1\n"
              "Clear buffer - 2\n")

    def user_choice(self) -> None:
        self.__choice = input("Enter number of buffer option: \n")

    @staticmethod
    def program_choice(choice: str) -> None:
        if choice == "1":
            if Buffer.program_buffer:
                Buffer.show_buffer()
            else:
                print("Buffer is empty!\n")
        elif choice == "2":
            Buffer.clear_buffer()
        else:
            raise ValueError
