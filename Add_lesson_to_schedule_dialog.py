from PyQt5.QtWidgets import *


class MyDialog(QDialog):
    def __init__(self, main_window=None):
        super().__init__()
        self.parent = main_window
        self.choose_lesson = QComboBox(self)
        self.choose_day = QComboBox(self)
        self.choose_lesson.addItems(elem.name for elem in self.parent.list_of_lessons)
        self.choose_day.addItems(['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение'])
        self.start_hour = QLineEdit()
        self.start_minute = QLineEdit()
        self.finish_hour = QLineEdit()
        self.finish_minute = QLineEdit()
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self)
        self.horizontal_start_layout = QHBoxLayout()
        self.horizontal_finish_layout = QHBoxLayout()
        self.general_layout = QFormLayout(self)
        self.start_layout = QFormLayout()
        self.finish_layout = QFormLayout()
        self.start_layout.addRow(self.start_hour, self.start_minute)
        self.finish_layout.addRow(self.finish_hour, self.finish_minute)
        self.horizontal_start_layout.addItem(self.start_layout)
        self.horizontal_finish_layout.addItem(self.finish_layout)
        self.general_layout.addRow("Выберите урок", self.choose_lesson)
        self.general_layout.addRow("Выберите день", self.choose_day)
        self.general_layout.addRow("Начало:", self.horizontal_start_layout)
        self.general_layout.addRow("Конец:", self.horizontal_finish_layout)
        self.general_layout.addWidget(self.button_box)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

    def get_inputs(self):
        return (self.choose_lesson.currentText(), self.choose_day.currentText(), self.start_hour.text(),
                self.start_minute.text(), self.finish_hour.text(), self.finish_minute.text())
