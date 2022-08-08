import sys

from .service import Service


class Controller:
    """The Controller class to get and show some data."""
    @classmethod
    def __init__(cls):
        cls.main()

    @classmethod
    def main(cls):
        """The main logic controller"""
        while True:
            user_location_select = cls.ask_user_name_location()
            data_many_location = Service.dict_name_location(user_location_select)
            key_user_action = cls.dict_location(data_many_location)
            data = Service.get_list_location_data(select_user=user_location_select)
            user_location = data[key_user_action - 1]
            data_location = f"{user_location['unrestricted_value']}: {user_location['data']['geo_lat']} широта " \
                            f"{user_location['data']['geo_lon']} долгота"

            print(data_location)

    @classmethod
    def dict_location(cls, dict_location):
        """Print list of possible locations and asks the user for the desired one"""

        data = dict_location
        for number, location in data.items():
            print(f"{number}: {location}")

        while True:
            user_action = int(input("Your number location: "))
            return user_action

    @classmethod
    def ask_user_name_location(cls):
        """Returns the user's primary request"""
        while True:
            print("For exit, enter: 'Exit'")
            select_user = input("Your location: ").lower()
            if select_user == 'exit':
                cls.exit()
            else:
                return select_user

    @classmethod
    def exit(cls):
        """Exiting the program"""
        print('Goodbye!')
        sys.exit(0)
