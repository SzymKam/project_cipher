import os
import pytest
import buffer
from file_handler import FilehandlerManager
from text import TextElements
import temporary_dir


class TestFilehandler:
    @pytest.fixture
    def setup_test(self):
        self.test_filehandler_manager = FilehandlerManager()

    def test_if_make_decision_print_invalid_option_with_choice_out_of_range(self, setup_test, capsys):
        self.test_filehandler_manager.make_decision(choice='some_option')
        capture = capsys.readouterr()
        assert capture.out == "Invalid option\n"

    def test_if_save_return_right_value(self, mocker, setup_test):
        mocker.patch(buffer.Buffer, 'program_buffer', TextElements(text="test_text",
                                                                   status="tet_status",
                                                                   rot_type="test_rot_type"))
        self.test_filehandler_manager.save(filename='test_file', save_option='w', directory='temporary_dir')
        with not pytest.raises(FileNotFoundError):
            assert open(temporary_dir.test_file.json, 'rb').read() == {'a': 'a'}
