from dadata import Dadata
from .model import ConfigModel


class Service:
    """A class for working with data"""

    @classmethod
    def get_list_location_data(cls, select_user) -> list:
        """Returns a list of data based on a user request"""
        configure = ConfigModel.get_configure_user()
        token = configure[0][0]
        language = configure[0][1]
        dadata = Dadata(token)
        result = dadata.suggest("address", f"{select_user}", language=f"{language}")
        return result

    @classmethod
    def dict_name_location(cls, select_user) -> dict:
        """Generates and return dictionary with possible location options"""
        dict_location = {}
        data = cls.get_list_location_data(select_user)
        if len(data) != 0:
            item = 1
            for i in data:
                dict_location[item] = i.get('value')
                item = item+1
            return dict_location
        else:
            print('No data!')
