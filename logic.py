from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda : self.submit())

    def submit(self):
        csvfile="votes.csv"
        with open(csvfile, 'a', newline='') as file:
            file.write('Voter  Candidate  Total\n')
            name = self.input_id.text()

