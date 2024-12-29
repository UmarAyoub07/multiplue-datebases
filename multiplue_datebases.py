from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtSql
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle("Multiplue DateBases")
        self.show()

    def createConnection(self, dbName):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(dbName)

        if not db.open():
            print("Cannot establish a database connection to: " + dbName)
            return False
        return True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.createConnection("test_db.sqlite")
    sys.exit(app.exec_())