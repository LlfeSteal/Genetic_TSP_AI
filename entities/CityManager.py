import pickle
import random

from entities.CityFactory import CityFactory


class CityManager:
    def __init__(self, max_distance, city_number, save=None):
        self.city_factory = CityFactory(max_distance)
        if save is not None:
            self.load(save)
        else:
            self._cities = self.city_factory.init_cities(city_number)

    def get_cities(self):
        return self._cities

    def get_missing_cities(self, cities):
        missing_cities = []
        for city in self._cities:
            if city not in cities:
                missing_cities.append(city)
        random.shuffle(missing_cities)
        return missing_cities

    def save(self, name):
        with open('saved_state_'+name, 'wb') as file:
            pickle.dump(self._cities, file)

    def load(self, name):
        print("load")
        self._cities = []
        with open('saved_state_'+name, 'rb') as file:
            self._cities = pickle.load(file)
