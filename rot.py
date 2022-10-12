from abc import ABC, abstractmethod
import string


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
        pass

    def rot_type(self) -> None:
        print(f"Rot type is: {self._type}")


class Rot13(Rot):
    def __init__(self) -> None:
        self._shift: int = 13
        self._type: str = "rot" + str(self._shift)
        self._encoded = ""

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
        pass

    def rot_type(self) -> None:
        print(f"Rot type is: {self._type}")


class RotFactory:
    @classmethod
    def get_rot(cls, shift: str):
        if shift == "47":
            return Rot47()
        elif shift == "13":
            return Rot13()
