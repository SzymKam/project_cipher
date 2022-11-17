from menu import Menu
MAIN_MENU = ("MAIN MENU: \n"
             "1. Encode / decode \n"
             "2. Buffer options \n"
             "3. Filehandler options\n"
             "4. Exit program\n"
             "\n")


def test_if_menu_print_correctly(capsys):
    Menu.print_main_menu()
    capture = capsys.readouterr()
    assert capture.out == MAIN_MENU
