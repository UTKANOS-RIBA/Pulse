from Occupation import Occupation


class DayInSchoolSchedule:
    def __init__(self, name):
        self.name = name
        self.lessons = []

    def sort_lessons(self):
        self.lessons.sort(key=lambda x: (x.start_hour, x.start_minute))

    def add_lesson(self, name, start, finish):
        self.lessons.append(Occupation(name, start, finish))
        self.sort_lessons()