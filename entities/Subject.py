class Subject:
    def __init__(self, cities):
        self._cities = cities

    def get_cities(self):
        return self._cities

    def get_city(self, index):
        return self._cities[index]

    def set_city(self, index, city):
        self._cities[index] = city

    def __str__(self):
        cities_names = []
        for city in self._cities:
            cities_names.append(str(city))
        return str(cities_names)

