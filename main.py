import ctypes
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from The_lesson import TheLesson
from Day_in_school_schedule import DayInSchoolSchedule
from Day_in_free_schedule import DayInFreeSchedule
from Add_lesson_to_schedule_dialog import MyDialog
from Add_occupation_to_schedule_dialog import MyDialog2
import csv
from os import path as op, name as osname
from PulseDesign import Ui_MainWindow

INDEXING = {'Понедельник': 0, 'Вторник': 1, 'Среда': 2, 'Четверг': 3, 'Пятница': 4, 'Суббота': 5, 'Воскресение': 6}


def check(result):
    if 0 <= int(result[2]) <= 23:
        if 0 <= int(result[4]) <= 23:
            if 0 <= int(result[3]) <= 59:
                if 0 <= int(result[5]) <= 59:
                    return True


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('Pulse_design.ui', self)
        self.setupUi(self)
        if osname == 'nt':
            my_app_id = 'mycompany.myproduct.subproduct.version'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
        self.list_of_lessons = list()
        self.list_of_lessons_list_widget = self.findChild(QListWidget, 'listOfLessonsListWidget')
        self.list_of_lessons_list_widget.setSortingEnabled(True)
        self.school_schedule_tree_widget = self.findChild(QTreeWidget, 'schoolScheduleTreeWidget')
        self.free_schedule_tree_widget = self.findChild(QTreeWidget, 'freeScheduleTreeWidget')
        self.add_lesson_in_list_button = self.findChild(QPushButton, 'addLessonInListButton')
        self.name_of_current_lesson_label = self.findChild(QLabel, 'nameOfCurrentLessonLabel')
        self.average_score_label = self.findChild(QLabel, 'averageScoreLabel')
        self.add_mark_button = self.findChild(QPushButton, 'addMarkPushButton')
        self.change_homework_button = self.findChild(QPushButton, 'changeHomeworkPushButton')
        self.marks_list_widget = self.findChild(QListWidget, 'marksListWidget')
        self.homework_label = self.findChild(QLabel, 'changeHomeworkLabel')
        self.school_schedule_tree_widget.setHeaderLabels(['День недели'])
        self.free_schedule_tree_widget.setHeaderLabels(['День недели'])
        self.add_lesson_in_school_schedule_button = self.findChild(QPushButton, 'addLessonInSchoolScheduleButton')
        self.add_occupation_button = self.findChild(QPushButton, 'addOccupationButton')
        self.school_schedule = [DayInSchoolSchedule(name) for name in
                                ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']]
        self.school_schedule_days = [QTreeWidgetItem(self.school_schedule_tree_widget, [elem.name]) for elem in
                                     self.school_schedule]
        self.free_schedule = [DayInFreeSchedule(name) for name in
                              ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресение']]
        self.free_schedule_days = [QTreeWidgetItem(self.free_schedule_tree_widget, [elem.name]) for elem in
                                   self.free_schedule]

    def run(self):
        if op.exists('data_diary.csv'):
            with open('data_diary.csv', 'r') as data:
                cr = csv.reader(data)
                for row in cr:
                    if len(row) == 3:
                        marks = list()
                        for i in range(1, len(row[1]) - 1, 3):
                            marks.append(int(row[1][i]))
                        self.list_of_lessons.append(TheLesson(row[0], marks, row[2]))
                        self.list_of_lessons.sort(key=lambda x: x.name)
                        current_item = QListWidgetItem(row[0])
                        self.list_of_lessons_list_widget.addItem(current_item)
                        self.list_of_lessons_list_widget.setCurrentItem(current_item)
                        self.item_in_list_of_lessons_clicked()
            data.close()
        if op.exists('data_school_schedule.csv'):
            with open('data_school_schedule.csv', 'r', encoding='utf-8') as data:
                cr = csv.reader(data)
                for row in cr:
                    if len(row) == 6:
                        result = [row[1], row[0], int(row[2]), int(row[3]), int(row[4]), int(row[5])]
                        index = INDEXING[result[1]]
                        self.school_schedule[index].add_lesson(result[0], [result[2], result[3]],
                                                               [result[4], result[5]])
                        for i in reversed(range(self.school_schedule_days[index].childCount())):
                            self.school_schedule_days[index].removeChild(self.school_schedule_days[index].child(i))
                        for elem in self.school_schedule[index].lessons:
                            start = [str(elem.start_hour), str(elem.start_minute)]
                            finish = [str(elem.finish_hour), str(elem.finish_minute)]
                            if start[1] == '0':
                                start[1] = '00'
                            elif len(start[1]) == 1:
                                start[1] = '0' + start[1]
                            if finish[1] == '0':
                                finish[1] = '00'
                            elif len(finish[1]) == 1:
                                finish[1] = '0' + finish[1]
                            QTreeWidgetItem(self.school_schedule_days[index], [start[0] + ':' + start[1]
                                                                               + ' - ' + finish[0] + ':'
                                                                               + finish[1] + ' | ' + elem.name])
            data.close()
        if op.exists('data_free_schedule.csv'):
            with open('data_free_schedule.csv', 'r', encoding='utf-8') as data:
                cr = csv.reader(data)
                for row in cr:
                    if len(row) == 6:
                        result = [row[1], row[0], int(row[2]), int(row[3]), int(row[4]), int(row[5])]
                        index = INDEXING[result[1]]
                        self.free_schedule[index].add_occupation(result[0], [result[2], result[3]],
                                                                 [result[4], result[5]])
                        for i in reversed(range(self.free_schedule_days[index].childCount())):
                            self.free_schedule_days[index].removeChild(self.free_schedule_days[index].child(i))
                        for elem in self.free_schedule[index].occupations:
                            start = [str(elem.start_hour), str(elem.start_minute)]
                            finish = [str(elem.finish_hour), str(elem.finish_minute)]
                            if start[1] == '0':
                                start[1] = '00'
                            elif len(start[1]) == 1:
                                start[1] = '0' + start[1]
                            if finish[1] == '0':
                                finish[1] = '00'
                            elif len(finish[1]) == 1:
                                finish[1] = '0' + finish[1]
                            QTreeWidgetItem(self.free_schedule_days[index], [start[0] + ':' + start[1]
                                                                             + ' - ' + finish[0] + ':'
                                                                             + finish[1] + ' | ' + elem.name])
            data.close()
        self.add_lesson_in_list_button.clicked.connect(self.add_lesson_in_list_button_clicked)
        self.list_of_lessons_list_widget.itemClicked.connect(self.item_in_list_of_lessons_clicked)
        self.add_mark_button.clicked.connect(self.add_mark_button_clicked)
        self.change_homework_button.clicked.connect(self.change_homework_button_clicked)
        self.add_lesson_in_school_schedule_button.clicked.connect(self.add_lesson_to_schedule_button_clicked)
        self.add_occupation_button.clicked.connect(self.add_occupation_button_clicked)

    def add_lesson_in_list_button_clicked(self):
        name_of_lesson, ok_pressed = QInputDialog.getText(self, "Добавление урока", "Введите название урока")
        if ok_pressed:
            if name_of_lesson.rstrip() != '':
                self.list_of_lessons.append(TheLesson(name_of_lesson))
                self.list_of_lessons.sort(key=lambda x: x.name)
                current_item = QListWidgetItem(name_of_lesson)
                self.list_of_lessons_list_widget.addItem(current_item)
                self.list_of_lessons_list_widget.setCurrentItem(current_item)
                self.item_in_list_of_lessons_clicked()
            else:
                QMessageBox.information(self, 'Info', 'Неверный ввод')

    def item_in_list_of_lessons_clicked(self):
        self.name_of_current_lesson_label.setText(self.list_of_lessons_list_widget.currentItem().text())
        self.marks_list_widget.clear()
        for elem in self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].marks:
            self.marks_list_widget.addItem(QListWidgetItem(str(elem)))
        self.homework_label.setText(self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].homework)
        if len(self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].marks) != 0:
            self.average_score_label.setText(
                str(sum(self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].marks)
                    / len(self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].marks)))
        else:
            self.average_score_label.setText('0')

    def add_mark_button_clicked(self):
        mark, ok_pressed = QInputDialog.getText(self, 'Добавление оценки', 'Введите оценку')
        if ok_pressed:
            if mark in ['0', '1', '2', '3', '4', '5']:
                self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].marks.append(int(mark))
                self.marks_list_widget.addItem(QListWidgetItem(mark))
                self.marks_list_widget.show()
                self.average_score_label.setText(
                    str(sum(self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].marks)
                        / len(self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].marks)))
            else:
                QMessageBox.information(self, 'Info', 'Неверный ввод')

    def change_homework_button_clicked(self):
        homework, ok_pressed = QInputDialog.getText(self, 'Домашнее задание', 'Введите домашнее задание')
        if ok_pressed:
            self.list_of_lessons[self.list_of_lessons_list_widget.currentRow()].homework = homework
            self.homework_label.setText(homework.rstrip())

    def add_lesson_to_schedule_button_clicked(self):
        dialog = MyDialog(self)
        if dialog.exec_():
            result = dialog.get_inputs()
            if check(result):
                index = INDEXING[result[1]]
                self.school_schedule[index].add_lesson(result[0], [result[2], result[3]], [result[4], result[5]])
                for i in reversed(range(self.school_schedule_days[index].childCount())):
                    self.school_schedule_days[index].removeChild(self.school_schedule_days[index].child(i))
                for elem in self.school_schedule[index].lessons:
                    start = [str(elem.start_hour), str(elem.start_minute)]
                    finish = [str(elem.finish_hour), str(elem.finish_minute)]
                    if start[1] == '0':
                        start[1] = '00'
                    elif len(start[1]) == 1:
                        start[1] = '0' + start[1]
                    if finish[1] == '0':
                        finish[1] = '00'
                    elif len(finish[1]) == 1:
                        finish[1] = '0' + finish[1]
                    QTreeWidgetItem(self.school_schedule_days[index], [start[0] + ':' + start[1]
                                                                       + ' - ' + finish[0] + ':'
                                                                       + finish[1] + ' | ' + elem.name])
            else:
                QMessageBox.information(self, 'Info', 'Неверный ввод')

    def add_occupation_button_clicked(self):
        dialog = MyDialog2()
        if dialog.exec_():
            result = dialog.get_inputs()
            if check(result):
                index = INDEXING[result[1]]
                self.free_schedule[index].add_occupation(result[0], [result[2], result[3]], [result[4], result[5]])
                for i in reversed(range(self.free_schedule_days[index].childCount())):
                    self.free_schedule_days[index].removeChild(self.free_schedule_days[index].child(i))
                for elem in self.free_schedule[index].occupations:
                    start = [str(elem.start_hour), str(elem.start_minute)]
                    finish = [str(elem.finish_hour), str(elem.finish_minute)]
                    if start[1] == '0':
                        start[1] = '00'
                    elif len(start[1]) == 1:
                        start[1] = '0' + start[1]
                    if finish[1] == '0':
                        finish[1] = '00'
                    elif len(finish[1]) == 1:
                        finish[1] = '0' + finish[1]
                    QTreeWidgetItem(self.free_schedule_days[index], [start[0] + ':' + start[1]
                                                                     + ' - ' + finish[0] + ':'
                                                                     + finish[1] + ' | ' + elem.name])
            else:
                QMessageBox.information(self, 'Info', 'Неверный ввод')

    def save(self):
        with open('data_diary.csv', 'w+') as data:
            cw = csv.writer(data)
            for i in range(len(self.list_of_lessons)):
                cw.writerow([self.list_of_lessons[i].name, self.list_of_lessons[i].marks,
                             self.list_of_lessons[i].homework])
            data.close()
        with open('data_school_schedule.csv', 'w+', encoding='utf-8') as data:
            cw = csv.writer(data)
            for elem in self.school_schedule:
                for lesson in elem.lessons:
                    cw.writerow([elem.name, lesson.name, lesson.start_hour, lesson.start_minute, lesson.finish_hour,
                                 lesson.finish_minute])
        data.close()
        with open('data_free_schedule.csv', 'w+', encoding='utf-8') as data:
            cw = csv.writer(data)
            for elem in self.free_schedule:
                for occupation in elem.occupations:
                    cw.writerow([elem.name, occupation.name, occupation.start_hour, occupation.start_minute,
                                 occupation.finish_hour, occupation.finish_minute])
        data.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.run()
    ex.show()
    if not app.exec_():
        ex.save()
    sys.exit(app.exec_())
