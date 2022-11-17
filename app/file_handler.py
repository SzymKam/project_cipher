from typing import Optional
import json
import os

from buffer import Buffer


class FilehandlerManager:
    def __init__(self):
        self.__user_choice = None
        self.__file_name = None
        self.__write_option = None
        self.__filehandler_options = {
                                        "1": self.save_to_new_file,
                                        "2": self.save_to_existing_file,
                                        "3": self.load_file_to_buffer,
                                        "4": self.save_files
                                    }

    def filehandler_run(self):
        self.filehandler_menu()
        self.__user_choice = input("Enter number of filehandler option: ")
        self.make_decision(self.__user_choice)

    def make_decision(self, choice: str):
        if choice in self.__filehandler_options:
            self.__filehandler_options.get(choice)()
        else:
            print("Invalid option")

    def save_to_new_file(self):
        self.__file_name = input("Give name of file to save: ")
        if f"{self.__file_name}.json" in os.listdir('files'):
            print("This file already exist! \n")
        else:
            self.__write_option = "w"
            self.save(filename=self.__file_name, save_option=self.__write_option)

    def save_to_existing_file(self):
        print(f"List of existing files: \n")
        self.save_files()
        self.__file_name = input("Which one do you want to overwrite? ")
        if f"{self.__file_name}.json" not in os.listdir('files'):
            print("This file doesn't exist! \n")
        else:
            self.__write_option = "a"
            self.save(filename=self.__file_name, save_option=self.__write_option)

    @staticmethod
    def save(filename: str, save_option: str, directory: Optional[str] = 'files/'):
        with open(f"{directory}{filename}.json", save_option) as new_file:
            json.dump(Buffer.buffer_to_dict(), new_file)
            print(f"Buffer saved as {filename}.json")

    def load_file_to_buffer(self):
        self.save_files()
        file_to_load = input("Which one do you want to choose? ") + ".json"
        if file_to_load in os.listdir('files'):
            with open(f"files/{file_to_load}", "r") as load_file:
                translate_file = Buffer.dict_to_buffer(json.load(load_file))
                Buffer.add_to_buffer(translate_file)
                print(f"{file_to_load} added to buffer")
        else:
            print("File doesn't exist. Choose right file.")

    @staticmethod
    def save_files():
        print(f"\nList of existing files:")
        for element in os.listdir('files'):
            print(element)

    @staticmethod
    def filehandler_menu():
        print("FILEHANDLER MENU \n"
              "Save buffer to new file - 1 \n"
              "Save buffer to exist file - 2 \n"
              "Load file to buffer - 3\n"
              "Check save files - 4\n")
