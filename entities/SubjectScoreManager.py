import numpy as np
from functools import reduce


class SubjectScoreManager:
    def __init__(self, subject_scores):
        self._subject_scores = subject_scores
        self.probabilities = []
        self.generate_probabilities()

    def generate_probabilities(self):
        sum = reduce(lambda a, b: a.get_score() + b.get_score(), self._subject_scores)
        for subject_score in self._subject_scores:
            self.probabilities.append((subject_score.get_score() / sum))

    def pick_subject(self):
        return np.random.choice(self._subject_scores, 1, p=self.probabilities)
