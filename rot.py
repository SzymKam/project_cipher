from abc import ABC, abstractmethod
import string


class Encryptor:
    """This element of code, have to encode and decode text string."""
    def __init__(self) -> None:
        self.encrypted_txt: str = ""
        # if self.encrypted_txt:
        #     self.encrypted_txt
        # if self. encrypted_txt will exist, push them to the buffer

    def caesar_cipher_13(self, text_to_encrypt: str) -> None:
        text_to_encrypt = text_to_encrypt.lower()
        for char in text_to_encrypt:
            if char in string.ascii_lowercase:
                new_char = ord(char) + 13
                if new_char > 122:
                    new_char = 96 + (new_char - 122)
            self.encrypted_txt += new_char

    def caesar_cipher_47(self, text_to_encrypt: str) -> None:
        text_to_encrypt = text_to_encrypt.lower()
        for char in text_to_encrypt:
            if char in string.ascii_lowercase:
                new_char = ord(char) + 47
                if new_char > 122:
                    new_char = 96 + (new_char - 122)
            self.encrypted_txt += new_char


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
    def __init__(self):
        self._shift: int = 47
        self._type: str = "rot" + str(self._shift)

    def encode(self, text_to_encode: str):
        pass

    def decode(self, text_to_decode: str):
        pass

    def rot_type(self):
        pass


class Rot13(Rot):
    def __init__(self):
        self._shift: int = 13
        self._type: str = "rot" + str(self._shift)

    def encode(self, text_to_encode: str):
        pass

    def decode(self, text_to_decode: str):
        pass

    def rot_type(self):
        pass


class RotFactory:
    @classmethod
    def get_rot(cls, shift: str):
        if shift == "rot47":
            return Rot47()
        elif shift == "rot13":
            return Rot13()