from manager import Manager
import pytest


class TestManager:

    @pytest.fixture
    def setup_tests(self):
        self.test_manager = Manager()

    def test_if_handle_instruction_print_invalid_option_with_choice_out_of_option(self, setup_tests, capsys):
        self.test_manager.handle_instruction(choice=7)
        captured = capsys.readouterr()
        assert captured.out == 'Invalid option.\n'

    def test_if_manager_end_program(self, setup_tests, capsys):
        self.test_manager._Manager__end_app()
        captured = capsys.readouterr()
        assert captured.out == 'Program shutting down.\n'
