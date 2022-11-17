import buffer
from buffer.buffer_manager import BufferManager
from text import TextElements
import pytest


class TestBufferManagerOptions:
    def test_if_buffer_menu_print_right(self, capsys):
        BufferManager.buffer_menu()
        capture = capsys.readouterr()
        assert capture.out == "BUFFER MENU: \n" \
                              "Check buffer - 1\n" \
                              "Clear buffer - 2\n" \
                              "\n"

    def test_if_program_choice_works_correctly_choose_1_when_buffer_is_empty(self, mocker, capsys):
        mocker.patch.object(buffer.Buffer, "program_buffer", [])
        BufferManager.program_choice(choice='1')
        capture = capsys.readouterr()
        assert capture.out == "Buffer is empty!\n" \
                              "\n"

    def test_if_program_choice_works_correctly_choose_1_when_element_is_in_buffer(self, mocker, capsys):
        test_buffer = [TextElements(text='test_text', status="test_status", rot_type='test_rot_type')]
        mocker.patch.object(buffer.Buffer, "program_buffer", test_buffer)
        BufferManager.program_choice(choice='1')
        capture = capsys.readouterr()
        assert capture.out == 'Element number: 1 \n' \
                              'Text: test_text \n' \
                              'Status: test_status \n' \
                              'Rot type: test_rot_type \n' \
                              '\n'
    def test_if_program_choice_works_correctly_choose_2(self, mocker, capsys):
        test_buffer = [TextElements(text='test_text', status="test_status", rot_type='test_rot_type')]
        mocker.patch.object(buffer.Buffer, "program_buffer", test_buffer)
        BufferManager.program_choice(choice='2')
        capture = capsys.readouterr()
        assert capture.out == "Buffer empty!\n\n"

    @pytest.mark.parametrize("choice", ['0', '5'])
    def test_if_program_choice_raise_value_error_with_number_other_than_1_or_2(self, choice):
        with pytest.raises(ValueError):
            BufferManager.program_choice(choice=choice)
