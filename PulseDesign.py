# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Pulse_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(599, 538)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("LogoPulse.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.schoolDiaryTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.schoolDiaryTabWidget.setEnabled(True)
        self.schoolDiaryTabWidget.setAutoFillBackground(False)
        self.schoolDiaryTabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.schoolDiaryTabWidget.setObjectName("schoolDiaryTabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setAccessibleName("")
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.schoolScheduleTreeWidget = QtWidgets.QTreeWidget(self.tab)
        self.schoolScheduleTreeWidget.setObjectName("schoolScheduleTreeWidget")
        self.schoolScheduleTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout.addWidget(self.schoolScheduleTreeWidget)
        self.addLessonInSchoolScheduleButton = QtWidgets.QPushButton(self.tab)
        self.addLessonInSchoolScheduleButton.setObjectName("addLessonInSchoolScheduleButton")
        self.verticalLayout.addWidget(self.addLessonInSchoolScheduleButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.freeScheduleTreeWidget = QtWidgets.QTreeWidget(self.tab)
        self.freeScheduleTreeWidget.setObjectName("freeScheduleTreeWidget")
        self.freeScheduleTreeWidget.headerItem().setText(0, "1")
        self.verticalLayout_2.addWidget(self.freeScheduleTreeWidget)
        self.addOccupationButton = QtWidgets.QPushButton(self.tab)
        self.addOccupationButton.setObjectName("addOccupationButton")
        self.verticalLayout_2.addWidget(self.addOccupationButton)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.schoolDiaryTabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftScreen2Layout = QtWidgets.QVBoxLayout()
        self.leftScreen2Layout.setObjectName("leftScreen2Layout")
        self.listOfLessonsListWidget = QtWidgets.QListWidget(self.tab_2)
        self.listOfLessonsListWidget.setObjectName("listOfLessonsListWidget")
        self.leftScreen2Layout.addWidget(self.listOfLessonsListWidget)
        self.addLessonInListButton = QtWidgets.QPushButton(self.tab_2)
        self.addLessonInListButton.setAutoFillBackground(False)
        self.addLessonInListButton.setObjectName("addLessonInListButton")
        self.leftScreen2Layout.addWidget(self.addLessonInListButton)
        self.horizontalLayout_2.addLayout(self.leftScreen2Layout)
        self.rightScreen2Layout = QtWidgets.QVBoxLayout()
        self.rightScreen2Layout.setContentsMargins(0, 10, 0, 0)
        self.rightScreen2Layout.setObjectName("rightScreen2Layout")
        self.lessonInformationLayout = QtWidgets.QHBoxLayout()
        self.lessonInformationLayout.setObjectName("lessonInformationLayout")
        self.lessonInformationLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lessonInformationLabel.sizePolicy().hasHeightForWidth())
        self.lessonInformationLabel.setSizePolicy(sizePolicy)
        self.lessonInformationLabel.setObjectName("lessonInformationLabel")
        self.lessonInformationLayout.addWidget(self.lessonInformationLabel)
        self.nameOfCurrentLessonLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameOfCurrentLessonLabel.sizePolicy().hasHeightForWidth())
        self.nameOfCurrentLessonLabel.setSizePolicy(sizePolicy)
        self.nameOfCurrentLessonLabel.setText("")
        self.nameOfCurrentLessonLabel.setObjectName("nameOfCurrentLessonLabel")
        self.lessonInformationLayout.addWidget(self.nameOfCurrentLessonLabel)
        self.rightScreen2Layout.addLayout(self.lessonInformationLayout)
        self.homeworkLayout = QtWidgets.QVBoxLayout()
        self.homeworkLayout.setObjectName("homeworkLayout")
        self.homeworkLabel = QtWidgets.QLabel(self.tab_2)
        self.homeworkLabel.setObjectName("homeworkLabel")
        self.homeworkLayout.addWidget(self.homeworkLabel)
        self.changeHomeworkLabel = QtWidgets.QLabel(self.tab_2)
        self.changeHomeworkLabel.setIndent(0)
        self.changeHomeworkLabel.setObjectName("changeHomeworkLabel")
        self.homeworkLayout.addWidget(self.changeHomeworkLabel)
        self.changeHomeworkPushButton = QtWidgets.QPushButton(self.tab_2)
        self.changeHomeworkPushButton.setObjectName("changeHomeworkPushButton")
        self.homeworkLayout.addWidget(self.changeHomeworkPushButton)
        self.rightScreen2Layout.addLayout(self.homeworkLayout)
        self.averageScoreLayout = QtWidgets.QHBoxLayout()
        self.averageScoreLayout.setObjectName("averageScoreLayout")
        self.averageScoreConstantLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.averageScoreConstantLabel.sizePolicy().hasHeightForWidth())
        self.averageScoreConstantLabel.setSizePolicy(sizePolicy)
        self.averageScoreConstantLabel.setObjectName("averageScoreConstantLabel")
        self.averageScoreLayout.addWidget(self.averageScoreConstantLabel)
        self.averageScoreLabel = QtWidgets.QLabel(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.averageScoreLabel.sizePolicy().hasHeightForWidth())
        self.averageScoreLabel.setSizePolicy(sizePolicy)
        self.averageScoreLabel.setText("")
        self.averageScoreLabel.setObjectName("averageScoreLabel")
        self.averageScoreLayout.addWidget(self.averageScoreLabel)
        self.rightScreen2Layout.addLayout(self.averageScoreLayout)
        self.marksLabel = QtWidgets.QLabel(self.tab_2)
        self.marksLabel.setObjectName("marksLabel")
        self.rightScreen2Layout.addWidget(self.marksLabel)
        self.marksListWidget = QtWidgets.QListWidget(self.tab_2)
        self.marksListWidget.setObjectName("marksListWidget")
        self.rightScreen2Layout.addWidget(self.marksListWidget)
        self.addMarkPushButton = QtWidgets.QPushButton(self.tab_2)
        self.addMarkPushButton.setObjectName("addMarkPushButton")
        self.rightScreen2Layout.addWidget(self.addMarkPushButton)
        self.horizontalLayout_2.addLayout(self.rightScreen2Layout)
        self.schoolDiaryTabWidget.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.schoolDiaryTabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.schoolDiaryTabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pulse"))
        self.addLessonInSchoolScheduleButton.setText(_translate("MainWindow", "Добавить урок"))
        self.addOccupationButton.setText(_translate("MainWindow", "Добавить задачу"))
        self.schoolDiaryTabWidget.setTabText(self.schoolDiaryTabWidget.indexOf(self.tab), _translate("MainWindow", "      Расписание      "))
        self.addLessonInListButton.setText(_translate("MainWindow", "Добавить урок"))
        self.lessonInformationLabel.setText(_translate("MainWindow", "Сведения об уроке:"))
        self.homeworkLabel.setText(_translate("MainWindow", "Домашнее задание:"))
        self.changeHomeworkLabel.setText(_translate("MainWindow", "Нет"))
        self.changeHomeworkPushButton.setText(_translate("MainWindow", "Изменить домашнее задание"))
        self.averageScoreConstantLabel.setText(_translate("MainWindow", "Средний балл:"))
        self.marksLabel.setText(_translate("MainWindow", "Оценки:"))
        self.addMarkPushButton.setText(_translate("MainWindow", "Добавить оценку"))
        self.schoolDiaryTabWidget.setTabText(self.schoolDiaryTabWidget.indexOf(self.tab_2), _translate("MainWindow", "      Дневник      "))
