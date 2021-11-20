class SubjectScore:
    def __init__(self, subject, score):
        self._subject = subject
        self._score = score

    def get_subject(self):
        return self._subject

    def get_score(self):
        return self._score