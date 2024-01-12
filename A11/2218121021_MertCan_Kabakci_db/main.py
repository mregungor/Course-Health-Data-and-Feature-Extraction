from main_gui import MainGUI
import sys
from PyQt5.QtWidgets import QApplication

def run_ui():
    app = QApplication(sys.argv)
    arayuz = MainGUI()
    arayuz.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    run_ui()