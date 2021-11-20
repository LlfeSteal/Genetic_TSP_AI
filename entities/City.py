class City:
    def __init__(self, name):
        self._name = name
        self._distances = []

    def add_distance(self, city_distance):
        self._distances.append(city_distance)

    def get_name(self):
        return self._name

    def get_distance(self):
        return self._distances
