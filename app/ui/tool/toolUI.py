# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'toolUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(590, 547)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setMaximumSize(QtCore.QSize(80, 80))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setMinimumSize(QtCore.QSize(100, 80))
        self.listWidget.setMaximumSize(QtCore.QSize(500, 80))
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.listWidget.setLineWidth(0)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setFlow(QtWidgets.QListView.LeftToRight)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.horizontalLayout.addWidget(self.listWidget)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setMaximumSize(QtCore.QSize(80, 80))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setObjectName("stackedWidget")
        self.verticalLayout.addWidget(self.stackedWidget)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "新建项目"))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "新建项目"))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "新建项目"))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "新建项目"))
        item = self.listWidget.item(4)
        item.setText(_translate("Dialog", "新建项目"))
        self.listWidget.setSortingEnabled(__sortingEnabled)