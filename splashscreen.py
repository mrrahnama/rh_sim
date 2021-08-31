import sys
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QApplication, QSplashScreen
from PyQt5.QtCore import QTimer

class Dialog(QDialog):
    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)
        self.splash = QSplashScreen(QPixmap('e.jpg'))

        self.b1 = QPushButton('Display screensaver')
        # self.b1.clicked.connect(self.flashSplash)

        # layout = QVBoxLayout()
        # self.setLayout(layout)
        # layout.addWidget(self.b1)

    def flashSplash(self):
        # By default, SplashScreen will be in the center of the screen.
        # You can move it to a specific location if you want:
        # self.splash.move(10,10)

        self.splash.show()

        # Close SplashScreen after 2 seconds (2000 ms)
        QTimer.singleShot(970, self.show)
        QTimer.singleShot(900, self.splash.close)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Dialog()
    main.flashSplash()
    sys.exit(app.exec_())