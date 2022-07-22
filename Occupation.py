class Occupation:
    def __init__(self, name, start, finish):
        self.name = name
        self.start_hour = int(start[0])
        self.start_minute = int(start[1])
        self.finish_hour = int(finish[0])
        self.finish_minute = int(finish[1])
