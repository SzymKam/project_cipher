class Buffer:
    def __init__(self):
        self.choice = None
        self.__buffer = []

    def add_to_buffer(self, new_element):
        self.__buffer.append(new_element)

    def clear_buffer(self):
        self.__buffer.clear()

    def show_buffer(self):
        for element in self.__buffer:
            print(element)

    @staticmethod
    def buffer_menu():
        print("You are in buffer.\n"
              "If you want check buffer enter: 1\n"
              "If you want clear buffer enter: 2\n")

    def user_choice(self):
        self.choice = int(input("What you want to do? \n"))

    def program_choice(self, choice: int) -> None:
        if choice == 1:
            if self.__buffer:
                self.show_buffer()
            else:
                print("Buffer is empty!\n")
        elif choice == 2:
            self.clear_buffer()
            print("Buffer clear!\n")
        else:
            raise ValueError

    def run_buffer(self):
        self.buffer_menu()
        self.user_choice()
        self.program_choice(choice=self.choice)


my_buffer = Buffer()

