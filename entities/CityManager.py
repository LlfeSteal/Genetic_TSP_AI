from entities.CityFactory import CityFactory


class CityManager:
    def __init__(self):
        self._cities = CityFactory.init_cities(13)

    def get_cities(self):
        return self._cities
