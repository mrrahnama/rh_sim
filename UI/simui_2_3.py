# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\2.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(566, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 561, 481))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_23 = QtWidgets.QLabel(self.tab)
        self.label_23.setGeometry(QtCore.QRect(10, 20, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.lineEdit_simdays = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_simdays.setGeometry(QtCore.QRect(120, 21, 31, 20))
        self.lineEdit_simdays.setObjectName("lineEdit_simdays")
        self.label_42 = QtWidgets.QLabel(self.tab)
        self.label_42.setGeometry(QtCore.QRect(160, 20, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.lineEdit_customerNo = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_customerNo.setGeometry(QtCore.QRect(120, 60, 31, 20))
        self.lineEdit_customerNo.setObjectName("lineEdit_customerNo")
        self.label_43 = QtWidgets.QLabel(self.tab)
        self.label_43.setGeometry(QtCore.QRect(10, 59, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.lineEdit_simNo = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_simNo.setEnabled(False)
        self.lineEdit_simNo.setGeometry(QtCore.QRect(270, 150, 31, 20))
        self.lineEdit_simNo.setReadOnly(False)
        self.lineEdit_simNo.setObjectName("lineEdit_simNo")
        self.label_44 = QtWidgets.QLabel(self.tab)
        self.label_44.setGeometry(QtCore.QRect(160, 149, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.lineEdit_sellerNo = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_sellerNo.setGeometry(QtCore.QRect(120, 101, 31, 20))
        self.lineEdit_sellerNo.setObjectName("lineEdit_sellerNo")
        self.label_45 = QtWidgets.QLabel(self.tab)
        self.label_45.setGeometry(QtCore.QRect(10, 100, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.comboBox_14 = QtWidgets.QComboBox(self.tab)
        self.comboBox_14.setGeometry(QtCore.QRect(370, 60, 131, 22))
        self.comboBox_14.setObjectName("comboBox_14")
        self.label_47 = QtWidgets.QLabel(self.tab)
        self.label_47.setGeometry(QtCore.QRect(230, 53, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_47.setFont(font)
        self.label_47.setObjectName("label_47")
        self.button_Run = QtWidgets.QPushButton(self.tab)
        self.button_Run.setGeometry(QtCore.QRect(10, 190, 93, 28))
        self.button_Run.setObjectName("button_Run")
        self.pushButton_reportaddress = QtWidgets.QPushButton(self.tab)
        self.pushButton_reportaddress.setGeometry(QtCore.QRect(420, 210, 111, 31))
        self.pushButton_reportaddress.setObjectName("pushButton_reportaddress")
        self.lineEdit_reportAddress = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_reportAddress.setGeometry(QtCore.QRect(160, 190, 341, 20))
        self.lineEdit_reportAddress.setObjectName("lineEdit_reportAddress")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(190, 90, 221, 21))
        font = QtGui.QFont()
        font.setFamily("MS Sans Serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab)
        self.comboBox_2.setGeometry(QtCore.QRect(430, 90, 73, 22))
        self.comboBox_2.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.comboBox_2.setObjectName("comboBox_2")
        self.label_50 = QtWidgets.QLabel(self.tab)
        self.label_50.setGeometry(QtCore.QRect(10, 140, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label_50.setFont(font)
        self.label_50.setText("")
        self.label_50.setObjectName("label_50")
        self.checkbox_batchsimulation = QtWidgets.QCheckBox(self.tab)
        self.checkbox_batchsimulation.setGeometry(QtCore.QRect(10, 144, 141, 31))
        self.checkbox_batchsimulation.setObjectName("checkbox_batchsimulation")
        self.tabWidget.addTab(self.tab, "")
        self.customer_tab = QtWidgets.QWidget()
        self.customer_tab.setToolTip("")
        self.customer_tab.setToolTipDuration(-1)
        self.customer_tab.setStatusTip("")
        self.customer_tab.setObjectName("customer_tab")
        self.comboBox_customertypes = QtWidgets.QComboBox(self.customer_tab)
        self.comboBox_customertypes.setGeometry(QtCore.QRect(180, 90, 141, 22))
        self.comboBox_customertypes.setEditable(True)
        self.comboBox_customertypes.setObjectName("comboBox_customertypes")
        self.label = QtWidgets.QLabel(self.customer_tab)
        self.label.setGeometry(QtCore.QRect(10, 50, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.frame = QtWidgets.QFrame(self.customer_tab)
        self.frame.setGeometry(QtCore.QRect(10, 170, 531, 301))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(90, 40, 81, 31))
        self.label_5.setObjectName("label_5")
        self.listWidget_sellerpreferencelist = QtWidgets.QListWidget(self.frame)
        self.listWidget_sellerpreferencelist.setGeometry(QtCore.QRect(150, 100, 121, 131))
        self.listWidget_sellerpreferencelist.setDragEnabled(True)
        self.listWidget_sellerpreferencelist.setDragDropOverwriteMode(False)
        self.listWidget_sellerpreferencelist.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.listWidget_sellerpreferencelist.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.listWidget_sellerpreferencelist.setMovement(QtWidgets.QListView.Free)
        self.listWidget_sellerpreferencelist.setProperty("isWrapping", False)
        self.listWidget_sellerpreferencelist.setModelColumn(0)
        self.listWidget_sellerpreferencelist.setObjectName("listWidget_sellerpreferencelist")
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget_sellerpreferencelist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget_sellerpreferencelist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.listWidget_sellerpreferencelist.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_sellerpreferencelist.addItem(item)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(20, 60, 41, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(200, 60, 31, 31))
        self.label_9.setObjectName("label_9")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(390, 30, 74, 17))
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(430, 90, 71, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_22 = QtWidgets.QLabel(self.frame)
        self.label_22.setGeometry(QtCore.QRect(330, 90, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.lineEdit_percentofall = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_percentofall.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.lineEdit_percentofall.setObjectName("lineEdit_percentofall")
        self.label_46 = QtWidgets.QLabel(self.frame)
        self.label_46.setGeometry(QtCore.QRect(20, 20, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.label_19 = QtWidgets.QLabel(self.frame)
        self.label_19.setGeometry(QtCore.QRect(300, 180, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_21 = QtWidgets.QLabel(self.frame)
        self.label_21.setGeometry(QtCore.QRect(390, 200, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(430, 170, 71, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(430, 200, 71, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_20 = QtWidgets.QLabel(self.frame)
        self.label_20.setGeometry(QtCore.QRect(390, 170, 31, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.button_pr_preferencelist = QtWidgets.QPushButton(self.frame)
        self.button_pr_preferencelist.setGeometry(QtCore.QRect(120, 80, 21, 21))
        self.button_pr_preferencelist.setObjectName("button_pr_preferencelist")
        self.button_seller_preferencelist = QtWidgets.QPushButton(self.frame)
        self.button_seller_preferencelist.setGeometry(QtCore.QRect(250, 80, 21, 21))
        self.button_seller_preferencelist.setObjectName("button_seller_preferencelist")
        self.treeWidget_productpreference = QtWidgets.QTreeWidget(self.frame)
        self.treeWidget_productpreference.setGeometry(QtCore.QRect(0, 100, 141, 131))
        self.treeWidget_productpreference.setDragEnabled(True)
        self.treeWidget_productpreference.setDragDropOverwriteMode(False)
        self.treeWidget_productpreference.setDragDropMode(QtWidgets.QAbstractItemView.InternalMove)
        self.treeWidget_productpreference.setDefaultDropAction(QtCore.Qt.MoveAction)
        self.treeWidget_productpreference.setRootIsDecorated(False)
        self.treeWidget_productpreference.setColumnCount(2)
        self.treeWidget_productpreference.setObjectName("treeWidget_productpreference")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_productpreference)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_productpreference)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_productpreference)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_productpreference)
        self.lineEdit_sellerfile = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_sellerfile.setGeometry(QtCore.QRect(150, 260, 113, 20))
        self.lineEdit_sellerfile.setObjectName("lineEdit_sellerfile")
        self.lineEdit_productlistfile = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_productlistfile.setGeometry(QtCore.QRect(0, 260, 113, 20))
        self.lineEdit_productlistfile.setObjectName("lineEdit_productlistfile")
        self.checkBox_productlistfile = QtWidgets.QCheckBox(self.frame)
        self.checkBox_productlistfile.setGeometry(QtCore.QRect(10, 237, 71, 20))
        self.checkBox_productlistfile.setObjectName("checkBox_productlistfile")
        self.button_product_listfile = QtWidgets.QPushButton(self.frame)
        self.button_product_listfile.setEnabled(False)
        self.button_product_listfile.setGeometry(QtCore.QRect(89, 239, 21, 21))
        self.button_product_listfile.setObjectName("button_product_listfile")
        self.button_seller_listfile = QtWidgets.QPushButton(self.frame)
        self.button_seller_listfile.setEnabled(False)
        self.button_seller_listfile.setGeometry(QtCore.QRect(230, 240, 21, 21))
        self.button_seller_listfile.setObjectName("button_seller_listfile")
        self.checkBox_sellerlistfile = QtWidgets.QCheckBox(self.frame)
        self.checkBox_sellerlistfile.setGeometry(QtCore.QRect(151, 241, 70, 17))
        self.checkBox_sellerlistfile.setObjectName("checkBox_sellerlistfile")
        self.pushButton = QtWidgets.QPushButton(self.customer_tab)
        self.pushButton.setGeometry(QtCore.QRect(10, 90, 61, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.customer_tab)
        self.pushButton_3.setGeometry(QtCore.QRect(350, 90, 61, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.button_savecustomertype = QtWidgets.QPushButton(self.customer_tab)
        self.button_savecustomertype.setGeometry(QtCore.QRect(420, 90, 71, 31))
        self.button_savecustomertype.setObjectName("button_savecustomertype")
        self.button_loadcustomertype = QtWidgets.QPushButton(self.customer_tab)
        self.button_loadcustomertype.setGeometry(QtCore.QRect(90, 90, 71, 31))
        self.button_loadcustomertype.setObjectName("button_loadcustomertype")
        self.lineEdit_lifetime = QtWidgets.QLineEdit(self.customer_tab)
        self.lineEdit_lifetime.setGeometry(QtCore.QRect(70, 22, 31, 20))
        self.lineEdit_lifetime.setObjectName("lineEdit_lifetime")
        self.label_10 = QtWidgets.QLabel(self.customer_tab)
        self.label_10.setGeometry(QtCore.QRect(10, 20, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.customer_tab)
        self.label_11.setGeometry(QtCore.QRect(110, 21, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.customer_tab, "")
        self.seller_tab = QtWidgets.QWidget()
        self.seller_tab.setObjectName("seller_tab")
        self.pushButton_10 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_10.setGeometry(QtCore.QRect(290, 70, 61, 31))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 70, 61, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.label_24 = QtWidgets.QLabel(self.seller_tab)
        self.label_24.setGeometry(QtCore.QRect(10, 110, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.pushButton_12 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_12.setGeometry(QtCore.QRect(80, 70, 71, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.comboBox_8 = QtWidgets.QComboBox(self.seller_tab)
        self.comboBox_8.setGeometry(QtCore.QRect(240, 40, 141, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.pushButton_13 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_13.setGeometry(QtCore.QRect(360, 70, 71, 31))
        self.pushButton_13.setObjectName("pushButton_13")
        self.frame_4 = QtWidgets.QFrame(self.seller_tab)
        self.frame_4.setGeometry(QtCore.QRect(10, 140, 421, 101))
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
        self.comboBox_9.setGeometry(QtCore.QRect(80, 40, 141, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.label_25 = QtWidgets.QLabel(self.seller_tab)
        self.label_25.setGeometry(QtCore.QRect(130, 10, 41, 21))
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.seller_tab)
        self.label_26.setGeometry(QtCore.QRect(290, 10, 41, 21))
        self.label_26.setObjectName("label_26")
        self.pushButton_22 = QtWidgets.QPushButton(self.seller_tab)
        self.pushButton_22.setGeometry(QtCore.QRect(180, 70, 71, 31))
        self.pushButton_22.setObjectName("pushButton_22")
        self.tabWidget.addTab(self.seller_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 566, 26))
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
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RM Simulator"))
        self.label_23.setText(_translate("MainWindow", "simulatoin days"))
        self.lineEdit_simdays.setText(_translate("MainWindow", "1000"))
        self.label_42.setText(_translate("MainWindow", "days/nego"))
        self.lineEdit_customerNo.setText(_translate("MainWindow", "50"))
        self.label_43.setText(_translate("MainWindow", "NO customer"))
        self.lineEdit_simNo.setText(_translate("MainWindow", "1"))
        self.label_44.setText(_translate("MainWindow", "NO simulation"))
        self.lineEdit_sellerNo.setText(_translate("MainWindow", "4"))
        self.label_45.setText(_translate("MainWindow", "NO seller"))
        self.label_47.setText(_translate("MainWindow", "market mechanism"))
        self.button_Run.setText(_translate("MainWindow", "Run"))
        self.pushButton_reportaddress.setText(_translate("MainWindow", "set report address"))
        self.lineEdit_reportAddress.setText(_translate("MainWindow", "C:/SSD/Uni/Thesis/Source/main/simulator/"))
        self.label_2.setText(_translate("MainWindow", "customer arival distribution"))
        self.checkbox_batchsimulation.setText(_translate("MainWindow", "batch run simulation"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Senario"))
        self.label.setText(_translate("MainWindow", "customer type"))
        self.label_5.setText(_translate("MainWindow", "preference list"))
        self.listWidget_sellerpreferencelist.setSortingEnabled(False)
        __sortingEnabled = self.listWidget_sellerpreferencelist.isSortingEnabled()
        self.listWidget_sellerpreferencelist.setSortingEnabled(False)
        item = self.listWidget_sellerpreferencelist.item(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.listWidget_sellerpreferencelist.item(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.listWidget_sellerpreferencelist.item(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.listWidget_sellerpreferencelist.item(3)
        item.setText(_translate("MainWindow", "New Item"))
        self.listWidget_sellerpreferencelist.setSortingEnabled(__sortingEnabled)
        self.label_8.setText(_translate("MainWindow", "product"))
        self.label_9.setText(_translate("MainWindow", "seller"))
        self.checkBox.setText(_translate("MainWindow", "force buy"))
        self.label_22.setText(_translate("MainWindow", "price variance"))
        self.label_46.setText(_translate("MainWindow", "% of all"))
        self.label_19.setText(_translate("MainWindow", "budget/price"))
        self.label_21.setText(_translate("MainWindow", "min"))
        self.label_20.setText(_translate("MainWindow", "max"))
        self.button_pr_preferencelist.setText(_translate("MainWindow", "+"))
        self.button_seller_preferencelist.setText(_translate("MainWindow", "+"))
        self.treeWidget_productpreference.setSortingEnabled(False)
        self.treeWidget_productpreference.headerItem().setText(0, _translate("MainWindow", "product name"))
        self.treeWidget_productpreference.headerItem().setText(1, _translate("MainWindow", "max budget"))
        __sortingEnabled = self.treeWidget_productpreference.isSortingEnabled()
        self.treeWidget_productpreference.setSortingEnabled(False)
        self.treeWidget_productpreference.topLevelItem(0).setText(0, _translate("MainWindow", "p1"))
        self.treeWidget_productpreference.topLevelItem(0).setText(1, _translate("MainWindow", "120"))
        self.treeWidget_productpreference.topLevelItem(1).setText(0, _translate("MainWindow", "p2"))
        self.treeWidget_productpreference.topLevelItem(1).setText(1, _translate("MainWindow", "200"))
        self.treeWidget_productpreference.topLevelItem(2).setText(0, _translate("MainWindow", "p3"))
        self.treeWidget_productpreference.topLevelItem(2).setText(1, _translate("MainWindow", "300"))
        self.treeWidget_productpreference.topLevelItem(3).setText(0, _translate("MainWindow", "p4"))
        self.treeWidget_productpreference.topLevelItem(3).setText(1, _translate("MainWindow", "380"))
        self.treeWidget_productpreference.setSortingEnabled(__sortingEnabled)
        self.checkBox_productlistfile.setText(_translate("MainWindow", "product file"))
        self.button_product_listfile.setText(_translate("MainWindow", "+"))
        self.button_seller_listfile.setText(_translate("MainWindow", "+"))
        self.checkBox_sellerlistfile.setText(_translate("MainWindow", "seller file"))
        self.pushButton.setText(_translate("MainWindow", "new "))
        self.pushButton_3.setText(_translate("MainWindow", "delete "))
        self.button_savecustomertype.setText(_translate("MainWindow", "save"))
        self.button_loadcustomertype.setText(_translate("MainWindow", "load"))
        self.lineEdit_lifetime.setText(_translate("MainWindow", "3"))
        self.label_10.setText(_translate("MainWindow", "life time"))
        self.label_11.setText(_translate("MainWindow", "days/nego"))
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
