class City:
    def __init__(self, name, coordinates):
        self._name = name
        self.coordinates = coordinates
        self._distances = []

    def add_distance(self, city_distance):
        self._distances.append(city_distance)

    def get_name(self):
        return self._name

    def get_distances(self):
        return self._distances

    def get_x(self):
        return self.coordinates[0]

    def get_y(self):
        return self.coordinates[1]

    def __str__(self):
        return self._name