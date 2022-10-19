from abc import ABC, abstractmethod
import string
import buffer


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

    def encode(self, text_to_encode: str) -> str:
        text_to_encode = text_to_encode.lower()
        for char in text_to_encode:
            if char in string.ascii_lowercase:
                new_char = ord(char) + self._shift
                if new_char > 122:
                    new_char = 96 + (new_char - 122)
            self._encoded += chr(new_char)
        return self._encoded

    def decode(self, text_to_decode: str):
        text_to_decode = text_to_decode.lower()
        for char in text_to_decode:
            if char in string.ascii_lowercase:
                new_char = ord(char) - self._shift
                if new_char < 97:
                    new_char = 123 - (97 - new_char)
            self._decoded += chr(new_char)
        return self._decoded

    def rot_type(self) -> str:
        return f"{self._type}"


class Rot13(Rot):
    def __init__(self) -> None:
        self._shift: int = 13
        self._type: str = "rot" + str(self._shift)
        self._encoded = ""
        self._decoded = ""

    def encode(self, text_to_encode: str) -> str:
        text_to_encode = text_to_encode.lower()
        for char in text_to_encode:
            if char in string.ascii_lowercase:
                new_char = ord(char) + self._shift
                if new_char > 122:
                    new_char = 96 + (new_char - 122)
            self._encoded += chr(new_char)
        return self._encoded

    def decode(self, text_to_decode: str):
        text_to_decode = text_to_decode.lower()
        for char in text_to_decode:
            if char in string.ascii_lowercase:
                new_char = ord(char) - self._shift
                if new_char < 97:
                    new_char = 123 - (97 - new_char)
            self._decoded += chr(new_char)
        return self._decoded

    def rot_type(self) -> str:
        return f"{self._type}"


class RotFactory:
    @classmethod
    def get_rot(cls, shift: str):
        if shift == "47":
            return Rot47()
        elif shift == "13":
            return Rot13()


class RotManager(RotFactory):

    def __init__(self) -> None:
        self.result = None
        self.done = None
        self.__selected_method = None
        self.__choose = None
        self.__working_rot = None
        self.__text: str = ""
        # self.my_buffer = buffer.Buffer

    def start(self) -> None:
        self.menu()
        self.choose_cipher()
        self.input_text()
        self.__working_rot = self.get_rot(shift=self.__choose)
        self.choose_method()
        self.result = self.encrypt(method=self.__selected_method)
        buffer.my_buffer.add_to_buffer(self.result)

    @staticmethod
    def menu() -> None:
        print("You are in rot menu\n"
              "Choose rod type:\n"
              "For use Cezar cipher 13 - enter 13\n"
              "For use Cezar cipher 47 - enter 47\n")

    def choose_cipher(self) -> None:
        self.__choose = input("What type of cipher do you want? \n")
        print(f"You choose Cipher{self.__choose}\n")

    def input_text(self) -> None:
        self.__text = input("Enter text: \n")

    def choose_method(self) -> None:
        print("If you want encode enter: 1 \n"
              "If you want decode enter: 2 \n")
        self.__selected_method = int(input("Do you want do decode or encode? \n"))

    def encrypt(self, method: int) -> dict:
        if method == 1:
            self.done = self.__working_rot.encode(text_to_encode=self.__text)
            return {"cipher": self.__working_rot.rot_type(), "text": self.done, "status": "encrypted"}
        elif method == 2:
            self.done = self.__working_rot.decode(text_to_decode=self.__text)
            return {"cipher": self.__working_rot.rot_type(), "text": self.done, "status": "decrypted"}
