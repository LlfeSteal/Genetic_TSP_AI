import random

from City import City
from entities.CityDistance import CityDistance


class CityFactory:

    @staticmethod
    def init_cities(cities_number):
        cities = []
        for city in range(cities_number):
            cities.append(City(str(city)))
        CityFactory.generate_city_distances(cities)
        return cities

    @staticmethod
    def generate_city_distances(cities):
        cities_set = cities[:]
        cities_set.remove(cities_set.getItem(0))
        for first_city in cities:
            for second_city in cities_set:
                distance = random.randint(0, 1000)
                first_city.add_distance(CityDistance(second_city, distance))
                second_city.add_distance(CityDistance(first_city, distance))
        cities_set.remove(cities_set.getItem(0))

