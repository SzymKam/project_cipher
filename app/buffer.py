from text import Text


class Buffer:
    program_buffer = []
    dict_buffer = {}

    @staticmethod
    def add_to_buffer(new_element: Text) -> None:
        Buffer.program_buffer.append(new_element)

    @staticmethod
    def clear_buffer() -> None:
        Buffer.program_buffer.clear()
        print("Buffer empty!\n")

    @staticmethod
    def show_buffer() -> None:
        for counter, element in enumerate(Buffer.program_buffer):
            print(f"Element number: {counter + 1} \n"
                  f"Text: {element.text} \n"
                  f"Status: {element.status} \n"
                  f"Rot type: {element.rot_type} \n")

    @staticmethod
    def buffer_to_dict():
        for counter, element in enumerate(Buffer.program_buffer):
            add_to_dict = {"element: " + str(counter + 1): {"text": element.text,
                                                            "status": element.status,
                                                            "rot_type": element.rot_type
                                                            }}
            Buffer.dict_buffer.update(add_to_dict)
        return Buffer.dict_buffer

    @staticmethod
    def dict_to_buffer(dict_to_add: dict) -> Text:
        for element in dict_to_add:
            add_text = dict_to_add[element]["text"]
            add_status = dict_to_add[element]["status"]
            add_rot_type = dict_to_add[element]["rot_type"]
            return Text(text=add_text, status=add_status, rot_type=add_rot_type)


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
