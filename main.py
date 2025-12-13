from logic import *

def main() -> None:
    """
    The main function for the PyQt6 application.
    """
    application = QApplication([])
    window = Logic()
    window.show()
    application.exec()


if __name__ == "__main__":
    main()