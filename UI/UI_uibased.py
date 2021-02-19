from PyQt5 import QtWidgets, uic
import sys,os
class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        ui_path = os.path.dirname(os.path.abspath(__file__))
        # print(ui_path)
        uic.loadUi(os.path.join(ui_path, "2.ui"), self) # Load the .ui file
        # self.show() # Show the GUI/
# app = QtWidgets.QApplication(sys.argv)
# window = Ui()
# app.exec_()