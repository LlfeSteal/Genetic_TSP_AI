import math
import random

from entities.City import City
from entities.CityDistance import CityDistance


class CityFactory:

    def __init__(self, max_distance):
        self._max_distance = max_distance

    def init_cities(self, cities_number):
        cities = []
        for city in range(cities_number):
            cities.append(City(str(city), self.get_random_coordinates_coordinates()))
        CityFactory.generate_city_distances(cities)
        return cities

    def generate_city_distances(self, cities):
        cities_set = cities[:]
        cities_set.remove(cities_set[0])
        for first_city in cities:
            for second_city in cities_set:
                distance = random.randint(0, 1000)
                first_city.add_distance(CityDistance(second_city, distance))
                second_city.add_distance(CityDistance(first_city, distance))
        cities_set.remove(cities_set[0])

    def get_random_coordinates_coordinates(self):
        random_x = random.randint(0, self._max_distance)
        random_y = random.randint(0, self._max_distance)
        return random_x, random_y

    def get_distance_between_two_cities(self, city1, city2):
        dist = math.sqrt((city2.get_x() - city1.get_x()) ** 2 + (city2.get_y() - city1.get_y()) ** 2)
        return dist




