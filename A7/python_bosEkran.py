from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import sqlite3 as sql

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 565)
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 30, 550, 500))
        self.label.setStyleSheet("QPushButton#pushButton{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
            "    color:rgba(255, 255, 255, 210);\n"
            "    border-radius:5px;\n"
            "}\n"
            "\n"
            "QPushButton#pushButton:hover{\n"
            "    background-color: qlineargradient(spread:pad, x1:0, y1:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
            "}\n"
            "\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(150, 123, 111, 255);\n"
            "}")

        self.label.setText("")
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 60, 491, 431))
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.clicked.connect(Form.close)
        self.pushButton_5.setGeometry(QtCore.QRect(243, 447, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.398, y1:0.409091, x2:1, y2:1, stop:0 rgba(255, 115, 176, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "border-radius;")
        self.pushButton_5.setObjectName("pushButton_5")

        self.db_connection = sql.connect('Breast-Cancer.db')
        self.cursor = self.db_connection.cursor()

        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 100, 500, 300))

        self.show_data()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def show_data(self):
        query = "SELECT * FROM BreastCancer_Data_Hastalar"
        self.cursor.execute(query)
        data = self.cursor.fetchall()

        column_names = [desc[0] for desc in self.cursor.description]

        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setHorizontalHeaderLabels(column_names)

        for row_num, row_data in enumerate(data):
            self.tableWidget.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                item = QtWidgets.QTableWidgetItem(str(col_data))
                self.tableWidget.setItem(row_num, col_num, item)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_5.setText(_translate("Form", "Çıkış"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
