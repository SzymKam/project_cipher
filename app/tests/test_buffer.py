import pytest
from buffer import buffer
from text import TextElements


class TestBufferOptions:

    @pytest.fixture
    def manager_test(self, mocker):
        self.test_program_buffer = []
        self.test_text_elements = TextElements(text="This is test text",
                                               status="This is test status",
                                               rot_type="This is test rot type")
        mocker.patch.object(buffer.Buffer, "program_buffer", self.test_program_buffer)
        buffer.Buffer.add_to_buffer(self.test_text_elements)

    def test_if_add_to_buffer_return_right_value_asserting_to_another_buffer(self, manager_test):
        self.test_program_buffer_to_assert = [self.test_text_elements]
        assert buffer.Buffer.program_buffer == self.test_program_buffer_to_assert

    def test_if_clear_buffer_return_empty_buffer(self, manager_test):
        buffer.Buffer.clear_buffer()
        assert buffer.Buffer.program_buffer == []

    def test_if_show_buffer_print_correct_text(self, manager_test, capsys):
        buffer.Buffer.show_buffer()
        captured = capsys.readouterr()
        assert captured.out == f"Element number: 1 \n"\
                               f"Text: This is test text \n"\
                               f"Status: This is test status \n" \
                               f"Rot type: This is test rot type \n" \
                               f"\n"

    def test_if_buffer_to_dict_return_right_value(self, manager_test):
        assert buffer.Buffer.buffer_to_dict() == {"element: 1": {"text": "This is test text",
                                                                 "status": "This is test status",
                                                                 "rot_type": "This is test rot type"
                                                                 }}

    def test_if_dict_to_buffer_return_right_value(self, manager_test):
        test_program_dict = {"element: 1": {"text": "This is test text",
                                            "status": "This is test status",
                                            "rot_type": "This is test rot type"
                                            }}
        assert buffer.Buffer.dict_to_buffer(dict_to_add=test_program_dict) == \
               TextElements(text="This is test text",
                            status="This is test status",
                            rot_type="This is test rot type")
