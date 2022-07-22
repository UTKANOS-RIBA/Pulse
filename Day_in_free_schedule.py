from Occupation import Occupation


class DayInFreeSchedule:
    def __init__(self, name):
        self.name = name
        self.occupations = []

    def sort_occupations(self):
        self.occupations.sort(key=lambda x: (x.start_hour, x.start_minute))

    def add_occupation(self, name, start, finish):
        self.occupations.append(Occupation(name, start, finish))
        self.sort_occupations()