import csv
from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):
    """
    This class handles Logic and interacts with the PyQt6 application.
    It inherits from QMainWindow to help getting the main window structure.
    It also helps in accessing the GUI elements which are defined in the gui.py file.
    """


    def __init__(self):
        """
        This method initializes the application window.
        This method sets up the UI.
        """
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(lambda : self.submit())

        self.jane_total = 0
        self.john_total = 0

        my_file = 'votes.csv'
        with open(my_file, 'w') as file:
            file.write('Voter           Candidate           Total\n')


    def submit(self):
        """
        This method retrieves the user input, performs validation checks, and then processes the data.
        """
        csvfile = "votes.csv"
        already_voted = False
        name = self.input_id.text().strip()
        is_number = False
        with open(csvfile, 'a', newline='') as file:
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
                        with open('votes.csv', 'r') as f:
                            csv_reader = csv.reader(f)
                            for row in csv_reader:
                                if row and str(number) in row[0]:
                                    already_voted = True
                                    self.label_message.setStyleSheet("color: red;")
                                    self.label_message.setText(f'Already voted')
                        if self.radioButton_jane.isChecked() and already_voted == False:
                            self.jane_total += 1
                            self.label_message.setText(f'Voted Jane')
                            file.write(f'Voter - {number}  Candidate - Jane  Total - {self.jane_total}\n')
                        elif self.radioButton_john.isChecked() and already_voted == False:
                            self.john_total += 1
                            self.label_message.setText(f'Voted John')
                            file.write(f'Voter - {number}  Candidate - John  Total - {self.john_total}\n')
                    else:
                        self.label_message.setStyleSheet("color: red;")
                        self.label_message.setText('Invalid ID. Please enter your correct ID.')
                except NameError:
                    self.label_message.setStyleSheet("color: red;")
                    self.label_message.setText('Invalid ID. Please enter your correct ID.')
            else:
                self.label_message.setStyleSheet("color: red;")
                self.label_message.setText('Invalid ID. Please enter your correct ID.')