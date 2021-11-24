import numpy as np

from entities.SubjectScore import SubjectScore


class SubjectCalculator:

    @staticmethod
    def evaluate(subject):
        distance = 0
        cities = subject.get_cities().tolist()
        cities.append(cities[0])
        for city in cities:
            index = cities.index(city)
            next_city = cities[index + 1]
            for city_distance in city.get_distances():
                if city_distance.get_city().get_name() == next_city.get_name():
                    distance += city_distance.get_distance()
                    break
        return distance

    @staticmethod
    def get_best_subjects(subjects):
        subject_scores = []
        for subject in subjects:
            subject_scores.append(SubjectScore(subject, SubjectCalculator.evaluate(subject)))
        subject_scores.sort(key=lambda x: x.get_score())
        return subject_scores
