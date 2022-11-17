class TextElements:
    def __init__(self, text, status, rot_type) -> None:
        self.text = text
        self.status = status
        self.rot_type = rot_type

    def return_text(self) -> str:
        return self.text
