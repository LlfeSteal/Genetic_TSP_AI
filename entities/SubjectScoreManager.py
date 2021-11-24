import numpy as np
from functools import reduce


class SubjectScoreManager:
    def __init__(self, subject_scores):
        self._subject_scores = subject_scores
        self.probabilities = []
        self.generate_probabilities()

    def generate_probabilities(self):
        total = self.calculate_sum()
        for subject_score in self._subject_scores:
            self.probabilities.append((subject_score.get_score() / total))

    def calculate_sum(self):
        total = 0
        for subject_score in self._subject_scores:
            total += subject_score.get_score()
        return total

    def pick_subject(self):
        choice = np.random.choice(self._subject_scores, 1, p=self.probabilities)
        return choice[0].get_subject()
