# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\黄翰林\Desktop\数据库大作业\前端制作\GaoKao\ChildrenForm2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import*
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*
from ConnectDB import*
from functools import partial
from Ui_ChildrenForm3 import*

class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(1200, 1000)
        font = QtGui.QFont()
        font.setPointSize(11)
        ChildrenForm.setFont(font)
        self.lineEdit = QtWidgets.QLineEdit(ChildrenForm)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayoutWidget = QtWidgets.QWidget(ChildrenForm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(200, 120, 300, 150))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.label_3)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_5)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_8)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        
        self.pushButton = QtWidgets.QPushButton(ChildrenForm)
        self.pushButton.setGeometry(QtCore.QRect(150, 170, 131, 41))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        
        self.tableWidget = QtWidgets.QTableWidget(ChildrenForm)
        self.tableWidget.setGeometry(QtCore.QRect(150, 400, 950, 500))
        self.tableWidget.setObjectName("tableWidget")

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
        self.lineEdit.setText(_translate("ChildrenForm", "您查询的录取的考生名单如下"))
        self.label_2.setText(_translate("ChildrenForm", "本科一批"))
        self.label_6.setText(_translate("ChildrenForm", "       院校名称："))
        self.label_3.setText(_translate("ChildrenForm", "南开大学"))
        self.label_7.setText(_translate("ChildrenForm", "           科类：   "))
        self.label_5.setText(_translate("ChildrenForm", "理科"))
        self.label.setText(_translate("ChildrenForm", "       专业名称："))
        self.label_8.setText(_translate("ChildrenForm", "金融学"))
        self.label_4.setText(_translate("ChildrenForm", "           批次："))
        self.pushButton.setText(_translate("ChildrenForm", "查询考生信息"))
        
    def SearchStudent(self, str):
        db=connectDB('127.0.0.1', 'hhlschema', 'HHL', '12345' )
        a, col, row=dataset1("section", db, str)
        db.close()
        self.tableWidget.setColumnCount(col)
        self.tableWidget.setRowCount(row)
        self.tableWidget.setHorizontalHeaderLabels(['course_id','sec_id','semester',  'year','building' 'room_number'])
        for i in range(row):
            for j in range(col):
                if j==0:
                    searchBtn=QPushButton(a[i][j])
                    searchBtn.setObjectName("pushButtonx")
                    searchBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
                    searchBtn.setStyleSheet('''background-color:QColor(192,192,192);''')
                    searchBtn.clicked.connect(partial(self.showSon2, a[i][j]))
                    self.tableWidget.setCellWidget(i, j, searchBtn)
                else:
                    self.tableWidget.setItem(i, j, QTableWidgetItem(a[i][j]))
        self.tableWidget.show()
    
    def showSon2(self, text):
        self.child2=ChildrenForm3()
        palette=QPalette()
        palette.setColor(QPalette.Background, QColor(202, 216, 235))
        self.child2.setPalette(palette)
        #self.child.SearchStudent(text)
        self.child2.show()
        print(text)

class ChildrenForm3(QWidget, Ui_ChildrenFrom3):
     def __init__(self):
        super(ChildrenForm3, self).__init__()
        self.setupUi(self)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    palette=QPalette()
    palette.setColor(QPalette.Background, QColor(202, 216, 235))
    ChildrenForm = QtWidgets.QWidget()
    ChildrenForm.setPalette(palette)
    ui = Ui_ChildrenForm()
    ui.setupUi(ChildrenForm)
    ChildrenForm.show()
    sys.exit(app.exec_())

