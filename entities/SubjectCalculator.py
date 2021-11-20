class SubjectCalculator:

    @staticmethod
    def evaluate(subject):
        distance = 0
        cities = subject.get_cities()
        cities.append(cities[0])
        for index, city in cities:
            next_city = cities[index + 1]
            for city_distance in city.get_distances():
                if city_distance.get_city().get_name() == next_city.get_name():
                    distance += city_distance.get_distance()
                    break
        return distance
