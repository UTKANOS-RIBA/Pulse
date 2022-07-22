class TheLesson:
    def __init__(self, name, marks=None, homework=' '):
        if marks is None:
            marks = []
        self.name = name
        self.marks = marks
        self.homework = homework
