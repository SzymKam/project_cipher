from menu import Menu


def test_if_menu_print_correctly():
    assert Menu.print_main_menu() == print("MAIN MENU: \n"
                                           "1. Encode / decode \n"
                                           "2. Buffer options \n"
                                           "3. Filehandler options\n"
                                           "4. Exit program\n")
