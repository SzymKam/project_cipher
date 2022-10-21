class Buffer:
    program_buffer = []

    @staticmethod
    def add_to_buffer(new_element):
        Buffer.program_buffer.append(new_element)

    @staticmethod
    def clear_buffer():
        Buffer.program_buffer.clear()
        print("Buffer empty!\n")

    @staticmethod
    def show_buffer():
        for counter, element in enumerate(Buffer.program_buffer):
            print(f"Element number: {counter + 1} \n"
                  f"Text: {element.text} \n"
                  f"Status: {element.status} \n"
                  f"Rot type: {element.rot_type} \n")


class BufferManager:
    def __init__(self):
        self.__choice = None

    def buffer_run(self):
        self.buffer_menu()
        self.user_choice()
        self.program_choice(choice=self.__choice)

    @staticmethod
    def buffer_menu():
        print("BUFFER MENU: \n"
              "Check buffer - 1\n"
              "Clear buffer - 2\n")

    def user_choice(self):
        self.__choice = input("What you want to do? \n")

    @staticmethod
    def program_choice(choice: str):
        if choice == "1":
            if Buffer.program_buffer:
                Buffer.show_buffer()
            else:
                print("Buffer is empty!\n")
        elif choice == "2":
            Buffer.clear_buffer()
        else:
            raise ValueError
