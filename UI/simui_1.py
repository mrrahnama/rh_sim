# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\1.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 771, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_10.setGeometry(QtCore.QRect(120, 21, 31, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setGeometry(QtCore.QRect(160, 20, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_11.setGeometry(QtCore.QRect(120, 60, 31, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_43 = QtWidgets.QLabel(self.tab)
        self.label_43.setGeometry(QtCore.QRect(10, 59, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_12.setGeometry(QtCore.QRect(120, 141, 31, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setGeometry(QtCore.QRect(10, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_13.setGeometry(QtCore.QRect(120, 101, 31, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setGeometry(QtCore.QRect(10, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.comboBox_14 = QtWidgets.QComboBox(self.tab)
        self.comboBox_14.setGeometry(QtCore.QRect(610, 20, 131, 22))
        self.comboBox_14.setObjectName("comboBox_14")
        self.label_47 = QtWidgets.QLabel(self.tab)
        self.label_47.setGeometry(QtCore.QRect(470, 20, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.pushButton_23 = QtWidgets.QPushButton(self.tab)
        self.pushButton_23.setGeometry(QtCore.QRect(10, 190, 93, 28))
        self.pushButton_23.setObjectName("pushButton_23")
        self.tabWidget.addTab(self.tab, "")
        self.customer_tab = QtWidgets.QWidget()
        self.customer_tab.setToolTip("")
        self.customer_tab.setToolTipDuration(-1)
        self.customer_tab.setStatusTip("")
        self.customer_tab.setObjectName("customer_tab")
        self.comboBox = QtWidgets.QComboBox(self.customer_tab)
        self.comboBox.setGeometry(QtCore.QRect(310, 150, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.customer_tab)
        self.label.setGeometry(QtCore.QRect(10, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.customer_tab)
        self.frame.setGeometry(QtCore.QRect(10, 190, 741, 281))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(self.frame)
        self.listWidget.setGeometry(QtCore.QRect(0, 130, 121, 131))
        self.listWidget.setObjectName("listWidget")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(100, 60, 81, 31))
        self.label_5.setObjectName("label_5")
        self.listWidget_3 = QtWidgets.QListWidget(self.frame)
        self.listWidget_3.setGeometry(QtCore.QRect(150, 130, 121, 131))
        self.listWidget_3.setObjectName("listWidget_3")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(40, 90, 41, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(190, 90, 31, 31))
        self.label_9.setObjectName("label_9")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(460, 30, 74, 17))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(500, 90, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(400, 90, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_14.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_46 = QtWidgets.QLabel(self.frame)
        self.label_46.setGeometry(QtCore.QRect(20, 20, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(350, 180, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(460, 200, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 170, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(500, 200, 71, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(460, 170, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.pushButton = QtWidgets.QPushButton(self.customer_tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.customer_tab)
        self.pushButton_3.setGeometry(QtCore.QRect(540, 150, 61, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.customer_tab)
        self.pushButton_4.setGeometry(QtCore.QRect(630, 150, 71, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.customer_tab)
        self.pushButton_5.setGeometry(QtCore.QRect(90, 150, 71, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit = QtWidgets.QLineEdit(self.customer_tab)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 31, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_10 = QtWidgets.QLabel(self.customer_tab)
        self.label_10.setGeometry(QtCore.QRect(20, 18, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.customer_tab)
        self.label_11.setGeometry(QtCore.QRect(120, 19, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.comboBox_2 = QtWidgets.QComboBox(self.customer_tab)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 60, 73, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_2 = QtWidgets.QLabel(self.customer_tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 81, 21))
        self.label_2.setObjectName("label_2")
        self.tabWidget.addTab(self.customer_tab, "")
        self.seller_tab = QtWidgets.QWidget()
        self.seller_tab.setObjectName("seller_tab")
        self.pushButton_10 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_10.setGeometry(QtCore.QRect(540, 60, 61, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 60, 61, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_24 = QtWidgets.QLabel(self.seller_tab)
        self.label_24.setGeometry(QtCore.QRect(10, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton_12 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_12.setGeometry(QtCore.QRect(90, 60, 71, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.comboBox_8 = QtWidgets.QComboBox(self.seller_tab)
        self.comboBox_8.setGeometry(QtCore.QRect(370, 40, 141, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_13.setGeometry(QtCore.QRect(630, 60, 71, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.frame_4 = QtWidgets.QFrame(self.seller_tab)
        self.frame_4.setGeometry(QtCore.QRect(10, 130, 711, 251))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(120, 20, 31, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_48 = QtWidgets.QLabel(self.frame_4)
        self.label_48.setGeometry(QtCore.QRect(10, 19, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_48.setFont(font)
        self.label_48.setObjectName("label_48")
        self.label_49 = QtWidgets.QLabel(self.frame_4)
        self.label_49.setGeometry(QtCore.QRect(10, 60, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_49.setFont(font)
        self.label_49.setObjectName("label_49")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(120, 61, 31, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.comboBox_9 = QtWidgets.QComboBox(self.seller_tab)
        self.comboBox_9.setGeometry(QtCore.QRect(210, 40, 141, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.label_25 = QtWidgets.QLabel(self.seller_tab)
        self.label_25.setGeometry(QtCore.QRect(260, 10, 41, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.seller_tab)
        self.label_26.setGeometry(QtCore.QRect(420, 10, 41, 21))
        self.label_26.setObjectName("label_26")
        self.pushButton_22 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_22.setGeometry(QtCore.QRect(320, 70, 71, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.tabWidget.addTab(self.seller_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSave = QtWidgets.QMenu(self.menuFile)
        self.menuSave.setObjectName("menuSave")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionsave_seller_config = QtWidgets.QAction(MainWindow)
        self.actionsave_seller_config.setObjectName("actionsave_seller_config")
        self.actionsave_strategy = QtWidgets.QAction(MainWindow)
        self.actionsave_strategy.setObjectName("actionsave_strategy")
        self.menuSave.addAction(self.actionsave_seller_config)
        self.menuSave.addAction(self.actionsave_strategy)
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuSave.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RM Simulator"))
        self.label_23.setText(_translate("MainWindow", "simulatoin days"))
        self.label_42.setText(_translate("MainWindow", "days/nego"))
        self.label_43.setText(_translate("MainWindow", "NO customer"))
        self.label_44.setText(_translate("MainWindow", "NO simulation"))
        self.label_45.setText(_translate("MainWindow", "NO seller"))
        self.label_47.setText(_translate("MainWindow", "market mechanism"))
        self.pushButton_23.setText(_translate("MainWindow", "Run"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Senario"))
        self.label.setText(_translate("MainWindow", "customer type"))
        self.label_5.setText(_translate("MainWindow", "preference list"))
        self.label_8.setText(_translate("MainWindow", "product"))
        self.label_9.setText(_translate("MainWindow", "seller"))
        self.checkBox.setText(_translate("MainWindow", "force buy"))
        self.label_22.setText(_translate("MainWindow", "price variance"))
        self.label_46.setText(_translate("MainWindow", "% of all"))
        self.label_19.setText(_translate("MainWindow", "budget/price"))
        self.label_21.setText(_translate("MainWindow", "min"))
        self.label_20.setText(_translate("MainWindow", "max"))
        self.pushButton.setText(_translate("MainWindow", "new "))
        self.pushButton_3.setText(_translate("MainWindow", "delete "))
        self.pushButton_4.setText(_translate("MainWindow", "save"))
        self.pushButton_5.setText(_translate("MainWindow", "load"))
        self.label_10.setText(_translate("MainWindow", "life time"))
        self.label_11.setText(_translate("MainWindow", "days/nego"))
        self.label_2.setText(_translate("MainWindow", "distribution"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.customer_tab), _translate("MainWindow", "Customer"))
        self.pushButton_10.setText(_translate("MainWindow", "delete "))
        self.pushButton_11.setText(_translate("MainWindow", "new "))
        self.label_24.setText(_translate("MainWindow", "strategy"))
        self.pushButton_12.setText(_translate("MainWindow", "load"))
        self.pushButton_13.setText(_translate("MainWindow", "save"))
        self.label_48.setText(_translate("MainWindow", "NO product"))
        self.label_49.setText(_translate("MainWindow", "shop capasity"))
        self.label_25.setText(_translate("MainWindow", "seller"))
        self.label_26.setText(_translate("MainWindow", "strategy"))
        self.pushButton_22.setText(_translate("MainWindow", "set"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.seller_tab), _translate("MainWindow", "Seller"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSave.setTitle(_translate("MainWindow", "Save "))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionsave_seller_config.setText(_translate("MainWindow", "save seller config"))
        self.actionsave_strategy.setText(_translate("MainWindow", "save strategy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
