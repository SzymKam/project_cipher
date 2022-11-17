import buffer
from buffer.buffer_manager import BufferManager
from text import TextElements
import pytest


class TestBufferManagerOptions:
    def test_if_buffer_menu_print_right(self):
        assert BufferManager.buffer_menu() == print("BUFFER MENU: \n"
                                                    "Check buffer - 1\n"
                                                    "Clear buffer - 2\n")

    def test_if_program_choice_works_correctly_choose_1_when_buffer_is_empty(self, mocker):
        mocker.patch.object(buffer.Buffer, "program_buffer", [])
        assert BufferManager.program_choice(choice='1') == print("Buffer is empty!\n")

    def test_if_program_choice_works_correctly_choose_1_when_element_is_in_buffer(self, mocker):
        test_buffer = [TextElements(text='test_text', status="test_status", rot_type='test_rot_type')]
        mocker.patch.object(buffer.Buffer, "program_buffer", test_buffer)
        assert BufferManager.program_choice(choice='1') == print('Text: test_text\n'
                                                                 'Status: test_status\n'
                                                                 'Rot type: test_rot_type')

    def test_if_program_choice_works_correctly_choose_2(self, mocker):
        test_buffer = [TextElements(text='test_text', status="test_status", rot_type='test_rot_type')]
        mocker.patch.object(buffer.Buffer, "program_buffer", test_buffer)
        assert BufferManager.program_choice(choice='2') == print('Buffer empty!')

    @pytest.mark.parametrize("choice", ['0', '5'])
    def test_if_program_choice_raise_value_error_with_number_other_than_1_or_2(self, choice):
        with pytest.raises(ValueError):
            BufferManager.program_choice(choice=choice)

