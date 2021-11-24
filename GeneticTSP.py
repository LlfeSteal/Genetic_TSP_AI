import random

from entities.CityManager import CityManager
from entities.Subject import Subject
from entities.SubjectCalculator import SubjectCalculator
from entities.SubjectScoreManager import SubjectScoreManager
import numpy as np


class GeneticTSP:
    def __init__(self, population_number=40, population_to_cross=30):
        self.population_number = population_number
        self.population_to_cross = population_to_cross
        self.city_manager = CityManager()
        self.population = []
        self.generate_population()

    def generate_population(self):
        for subject_number in range(self.population_number):
            self.population.append(Subject(self.get_random_cities()))

    def get_random_cities(self):
        new_cities = []
        new_cities = np.append(new_cities, self.city_manager.get_cities())
        np.random.shuffle(new_cities)
        return new_cities

    def generate_new_population(self):
        new_generation = []
        best_subjects = SubjectCalculator.get_best_subjects(self.population)
        subject_score_manager = SubjectScoreManager(best_subjects)
        for i in range(int(self.population_to_cross / 2)):
            subject1 = subject_score_manager.pick_subject()
            subject2 = subject_score_manager.pick_subject()
            np.append(new_generation, self.generate_new_childs(subject1, subject2))
        missing_subject_number = self.population_number - len(new_generation)
        for i in range(missing_subject_number):
            new_generation.append(best_subjects[i].get_subject())
        self.population = new_generation

    @staticmethod
    def generate_new_childs(subject1, subject2):
        cross_index = random.randint(3, 7)
        subject1_cities = subject1.get_cities()
        subject2_citites = subject2.get_cities()
        child1 = np.append(subject1_cities[:cross_index], subject2_citites[cross_index:])
        child2 = np.append(subject2_citites[:cross_index], subject1_cities[cross_index:])
        return [child1, child2]

    def display_population_status(self):
        for subject in self.population:
            subject_cities = []
            for city in subject.get_cities():
                subject_cities.append(str(city))
            print("SUBJECT", subject_cities)

    def display_population_score(self):
        best_subjects = SubjectCalculator.get_best_subjects(self.population)
        for subject_score in best_subjects:
            subject_cities = []
            for city in subject_score.get_subject().get_cities():
                subject_cities.append(str(city))
            print("SUBJECT", subject_cities, subject_score.get_score())

    def get_best_subjects(self, limit=5):
        best_subjects = SubjectCalculator.get_best_subjects(self.population)
        return best_subjects[:limit][0].get_subject()
