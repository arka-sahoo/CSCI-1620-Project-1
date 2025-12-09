from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda : self.submit())

    def submit(self):
        jane_total = 0
        john_total = 0
        csvfile="votes.csv"
        with open(csvfile, 'a', newline='') as file:
            file.write('Voter           Candidate           Total\n')
            name = self.input_id.text().strip()
            is_number = False
            try:
                number = int(name)
                is_number = True
            except ValueError:
                self.label_message.setText('Invalid ID. Please enter your correct ID.')
            if is_number:
                try:
                    if (number >= 10000) and (number <= 99999):
                        self.label_message.setStyleSheet("color: black;")
                        self.label_message.setText('ID is valid. Please vote any one candidate.')
                        if self.radioButton_jane.isChecked():
                            jane_total += 1
                            self.label_message.setText(f'Voted Jane, Total - {jane_total}')
                            file.write(f'Voter - {number}  Candidate - Jane  Total - {jane_total}\n')
                        elif self.radioButton_john.isChecked():
                            john_total += 1
                            self.label_message.setText(f'Voted John, Total - {john_total}')
                            file.write(f'Voter - {number}  Candidate - John  Total - {john_total}\n')
                    else:
                        self.label_message.setStyleSheet("color: red;")
                        self.label_message.setText('Invalid ID. Please enter your correct ID.')
                except NameError:
                    self.label_message.setStyleSheet("color: red;")
                    self.label_message.setText('Invalid ID. Please enter your correct ID.')
            else:
                self.label_message.setStyleSheet("color: red;")
                self.label_message.setText('Invalid ID. Please enter your correct ID.')