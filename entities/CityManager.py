from entities.CityFactory import CityFactory


class CityManager:
    def __init__(self, max_distance, city_number):
        self.city_factory = CityFactory(max_distance)
        self._cities = self.city_factory.init_cities(city_number)

    def get_cities(self):
        return self._cities
