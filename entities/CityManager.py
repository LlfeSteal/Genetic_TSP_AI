from entities.CityFactory import CityFactory


class CityManager:
    def __init__(self, max_distance):
        self.city_factory = CityFactory(max_distance)
        self._cities = self.city_factory.init_cities(13)

    def get_cities(self):
        return self._cities
