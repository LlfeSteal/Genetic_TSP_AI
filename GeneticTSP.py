import random

from entities.CityManager import CityManager
from entities.GraphGenerator import GraphGenerator
from entities.Subject import Subject
from entities.SubjectCalculator import SubjectCalculator
from entities.SubjectScoreManager import SubjectScoreManager
import numpy as np


class GeneticTSP:
    def __init__(self, population_number=40, population_to_cross=30, max_distance=900, mutation_rate=5,
                 city_number=13, save=None):
        self.city_number = city_number
        self.population_to_cross = population_to_cross
        self.population_number = population_number
        self.mutation_rate = mutation_rate
        self.city_manager = CityManager(max_distance, city_number, save)
        self.population = []
        self.generate_population()
        self.graph_generator = GraphGenerator(self.city_manager.get_cities(), max_distance)

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
            childs = self.generate_new_childs(subject1, subject2)
            new_generation = np.append(new_generation, childs)
        new_generation = np.append(new_generation, best_subjects[0].get_subject())
        missing_subject_number = self.population_number - len(new_generation)
        for i in range(missing_subject_number):
            #new_generation = np.append(new_generation, best_subjects[i].get_subject())
            new_generation = np.append(new_generation, subject_score_manager.pick_subject())
        self.population = new_generation

    def generate_new_childs(self, subject1, subject2):
        subject1_cities = subject1.get_cities()
        subject2_cities = subject2.get_cities()

        child1 = self.cross_childs(subject1_cities, subject2_cities)
        child2 = self.cross_childs(subject2_cities, subject1_cities)
        return [self.roll_mutation(Subject(child1)), self.roll_mutation(Subject(child2))]

    def cross_childs(self, child1, child2):
        cross_index = random.randint(0, self.city_number - 1)
        new_child = child1.tolist()[:cross_index]
        for city in child2[cross_index:]:
            if city not in new_child:
                new_child = np.append(new_child, city)
        missing_cities = self.city_manager.get_missing_cities(new_child)
        new_child = np.append(new_child, missing_cities)

        return new_child

    @staticmethod
    def display_child(child):
        cities = []
        for city in child:
            cities.append(city.get_name())
        print(cities)

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

    def get_graph_generator(self):
        return self.graph_generator

    def display_graph(self, subject):
        self.graph_generator.create_graph()
        self.graph_generator.display(subject)

    def roll_mutation(self, subject):
        rand = random.uniform(0.0, 100.0)
        if rand < self.mutation_rate:
            return self.apply_mutation(subject)
        return subject

    @staticmethod
    def apply_mutation(subject):
        index = random.randint(0, len(subject.get_cities()) - 1)
        next_index = index + 1
        if index == len(subject.get_cities()) - 1:
            next_index = 0
        city = subject.get_city(index)
        next_city = subject.get_city(next_index)
        subject.set_city(index, next_city)
        subject.set_city(next_index, city)
        return subject
