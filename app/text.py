from dataclasses import dataclass


@dataclass
class TextElements:
    text: str
    status: str
    rot_type: str

    def return_text(self) -> str:
        return self.text
