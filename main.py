import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        ui_file = "main.ui"
        uic.loadUi(ui_file, self)
        self.con = sqlite3.connect("Coffee.sqlite")

        cur = self.con.cursor()
        que = "SELECT * FROM coffee"
        result = cur.execute(que).fetchall()

        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels(
            ['ИД', 'Сорт', 'Обжарка', 'Зерна',
             'Вкус', 'Цена', 'Упаковка'])

        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec())
