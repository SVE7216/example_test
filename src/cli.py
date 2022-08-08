import sys
from .model import ConfigModel
from .controller import Controller


class Cli:
    """A class for working with the user interface"""

    interfaces = {
        'config_exists': {
            '1': 'Start',
            '2': 'Configure',
            '3': 'Exit',
        },
        'config_not_exits': {
            '1': 'Configure',
            '2': 'Exit',
        }
    }

    @classmethod
    def __init__(cls):
        cls.main()

    @classmethod
    def main(cls):
        """The main logic of the CLI."""
        interface = cls.get_interface()
        cls.print_interface(interface)
        user_action = cls.ask_user_action(interface)
        cls.user_action_v(user_action)

    @classmethod
    def print_text(cls, text: str):
        """Prints the transmitted text to the console"""
        print(text)

    @classmethod
    def print_interface(cls, interface: dict):
        """Outputs the interface to the console"""
        for number, action in interface.items():
            print(f"{number}: {action}")

    @classmethod
    def get_interface(cls) -> dict:
        """Return the interface in depending on the config."""
        if ConfigModel.is_config_exits():
            return cls.interfaces['config_exists']
        return cls.interfaces['config_not_exits']

    @classmethod
    def user_action_v(cls, user_action: str):
        if user_action == 'Start':
            Controller()
        elif user_action == 'Configure':
            cls.configure()
        elif user_action == 'Exit':
            cls.exit()

    @classmethod
    def check_language(cls, language: str) -> bool:
        """Checking the language for correctness"""
        if language == 'ru' or language == 'en':
            return True
        return False

    @classmethod
    def configure(cls):
        """Configure user data in the Database."""
        token = cls.ask_while_empty("Token: ")

        while True:
            language = input("Language(ru/en): ")
            if cls.check_language(language):
                ConfigModel.configure(token, language)
                break

    @classmethod
    def exit(cls):
        """Exiting the program"""
        cls.print_text('Goodbye!')
        sys.exit(0)

    @classmethod
    def ask_while_empty(cls, text: str) -> str:
        """Ask user while input is empty in loop."""
        while True:
            result = input(text)
            if result:
                return result

    @classmethod
    def ask_user_action(cls, interface: dict):
        """Returns the user's choice from the dictionary interface"""
        user_action = input('Your action: ')
        try:
            return interface[user_action]
        except KeyError:
            cls.print_text('Incorrect command!')

    @classmethod
    def ask_user_location(cls):
        """Returns the location that the user entered"""
        while True:
            print("For exit, enter: 'Exit'")
            select_user = input("Your location: ").lower()
            if select_user == 'exit':
                cls.exit()
            else:
                return select_user





