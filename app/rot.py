from abc import ABC, abstractmethod
import string
from buffer import Buffer
from text import TextElements


class Rot(ABC):
    @abstractmethod
    def encode(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def decode(self, text: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def rot_type(self) -> str:
        raise NotImplementedError


class Rot47(Rot):
    def __init__(self) -> None:
        self._shift: int = 47
        self._type: str = "rot" + str(self._shift)
        self._encoded = ""
        self._decoded = ""
        self._rot_status = ""

    def encode(self, text_to_encode: str) -> list:
        text_to_encode = text_to_encode.lower()
        for char in text_to_encode:
            if char in string.ascii_lowercase:
                new_char = ord(char) + self._shift
                if new_char > 122:
                    new_char = 96 + (new_char - 122)
            self._encoded += chr(new_char)
            self._rot_status = "encoded"
        return [self._encoded, self._rot_status]

    def decode(self, text_to_decode: str) -> list:
        text_to_decode = text_to_decode.lower()
        for char in text_to_decode:
            if char in string.ascii_lowercase:
                new_char = ord(char) - self._shift
                if new_char < 97:
                    new_char = 123 - (97 - new_char)
            self._decoded += chr(new_char)
            self._rot_status = "decoded"
        return [self._decoded, self._rot_status]

    def rot_type(self) -> str:
        return f"{self._type}"


class Rot13(Rot):
    def __init__(self) -> None:
        self._shift: int = 13
        self._type: str = "rot" + str(self._shift)
        self._encoded = ""
        self._decoded = ""
        self._rot_status = ""

    def encode(self, text_to_encode: str) -> list:
        text_to_encode = text_to_encode.lower()
        for char in text_to_encode:
            if char in string.ascii_lowercase:
                new_char = ord(char) + self._shift
                if new_char > 122:
                    new_char = 96 + (new_char - 122)
            self._encoded += chr(new_char)
            self._rot_status = "encoded"
        return [self._encoded, self._rot_status]

    def decode(self, text_to_decode: str) -> list:
        text_to_decode = text_to_decode.lower()
        for char in text_to_decode:
            if char in string.ascii_lowercase:
                new_char = ord(char) - self._shift
                if new_char < 97:
                    new_char = 123 - (97 - new_char)
            self._decoded += chr(new_char)
            self._rot_status = "decoded"
        return [self._decoded, self._rot_status]

    def rot_type(self) -> str:
        return f"{self._type}"


class RotFactory:
    @classmethod
    def get_rot(cls, shift: str):
        if shift == "47":
            return Rot47()
        elif shift == "13":
            return Rot13()


class RotManager:
    def __init__(self) -> None:
        self.__result = None
        self.__code = None
        self.__option = None
        self.__text = ""

    def rot_run(self) -> None:
        self.rot_menu()
        self.__option = input("Enter number of rot option: \n")
        self.rot_working(self.__option)
        Buffer.add_to_buffer(self.text_return())
        print("Added to buffer!\n")

    @staticmethod
    def rot_menu() -> None:
        print("ROT MENU: \n"
              "For encrypt own text in Rot13 enter - 1 \n"
              "For decrypt own text in Rot13 enter - 2 \n"
              "For encrypt own text in Rot47 enter - 3 \n"
              "For decrypt own text in Rot47 enter - 4 \n"
              "For use element from buffer enter - 5\n")

    def rot_working(self, decision: str) -> None:
        if decision in ("1", "2", "3", "4"):
            print(f"You choose option {self.__option}")
            self.__text = input("Enter text: \n")
            self.make_coding(decision=decision)
        # added option load form buffer
        elif decision == "5":
            if Buffer.program_buffer:
                print("Buffer elements:")
                Buffer.show_buffer()
                buffer_choice = int(input("Enter number you want to choose: ")) - 1  # add limit for len of buffer
                buffer_element = Buffer.program_buffer[buffer_choice]
                self.__text = buffer_element.return_text()
                print("For encrypt in Rot13 enter - 1 \n"
                      "For decrypt in Rot13 enter - 2 \n"
                      "For encrypt in Rot47 enter - 3 \n"
                      "For decrypt in Rot47 enter - 4 \n")
                self.__option = input("Which rot you want to use? ")  # add limit for 4 options
                self.make_coding(decision=self.__option)
            else:
                print("Buffer is empty")
        else:
            print("Invalid Value")

    def make_coding(self, decision: str) -> None:
        if int(decision) in range(1, 2):
            self.__code = RotFactory.get_rot(shift="13")
            if decision == "1":
                self.__result = (self.__code.encode(self.__text))
            elif decision == "2":
                self.__result = self.__code.decode(self.__text)
        elif decision == "3" or decision == "4":
            self.__code = RotFactory.get_rot(shift="47")
            if decision == "3":
                self.__result = self.__code.encode(self.__text)
            elif decision == "4":
                self.__result = self.__code.decode(self.__text)
        print("Task done")

    def text_return(self) -> TextElements:
        return TextElements(text=self.__result[0], status=self.__result[1], rot_type=self.__code.rot_type())
