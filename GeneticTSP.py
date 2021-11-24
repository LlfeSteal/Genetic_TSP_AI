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
        return random.shuffle(self.city_manager.get_cities())

    def generate_new_population(self):
        new_generation = []
        best_subjects = SubjectCalculator.get_best_subjects(self.population)
        subject_score_manager = SubjectScoreManager(best_subjects)
        for i in range(int(self.population_to_cross / 2)):
            subject1 = subject_score_manager.pick_subject()
            subject2 = subject_score_manager.pick_subject()

    @staticmethod
    def generate_new_childs(subject1, subject2):
        cross_index = random.randint(3, 7)
        child1 = np.append(subject1[:cross_index], subject2[cross_index:])
        child2 = np.append(subject2[:cross_index], subject1[cross_index:])
        return [child1, child2]
