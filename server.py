import asyncio
import math
import os
import pickle
import sys
import csv
from builtins import set
from numpy.polynomial.polynomial import polyval2d

import dill
from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTreeWidgetItem, QListWidgetItem
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
import numpy as np
from Model import Market, Seller, Customer, CustomerType, Product
from UI.simui_3_4 import Ui_MainWindow
from listmange import ListManage
from treamanage import TreeManage


# from UI.styles import breeze_resources

# from UI.UI_uibased import Ui
# width = 20
# height     = 20


def market_portrayal(agent):
    if agent is None:
        return
    portrayal = {"Shape": "circle",
    # portrayal = {"Shape": "UI/icon/store_color.png",
                 "Filled":"true",
                 # "w": 1,
                 # "h": 1,
                 "r":1,
                 "Layer": 0}
    if type(agent) is Seller:
        portrayal["Color"] = "cornflowerblue"
    elif type(agent) is Customer:
        # portrayal["Shape"] = "UI/icon/customer4.png"
        # portrayal["Shape"] = "circle"

        portrayal["Color"] = "tomato"
        portrayal["r"] = 1
        # portrayal["scale"] = 0.6
        portrayal["Layer"] = 1
    return portrayal


class RunThread(QtCore.QThread):
    def __init__(self, parent=None, model_param={}):
        super(RunThread, self).__init__(parent)
        self.is_running = True
        self.model_param = model_param
        height = self.model_param.get("height")
        width = self.model_param.get("width")
        customer = {"Label": "Customer", "Color": "cornflowerblue"}
        seller = {"Label": "Seller", "Color": "blueviolet"}
        canvas = CanvasGrid(market_portrayal, width, height)
        chart_count = ChartModule([customer, seller])
        self.server = ModularServer(Market, [
            canvas, chart_count], name="Market simulation", model_params=self.model_param)
        self.server.signalobj.closesignal.connect(self.stop)

    def run(self):
        print("run thread")
        # self.counter_value.emit()
        print("server is running ...")
        # self, width=20, height=20, num_customer=50,num_seller=4
        asyncio.set_event_loop(asyncio.new_event_loop())

        self.server.launch()  # emit new Signal with value

    def stop(self):
        self.is_running = False
        print('stopping thread...')
        self.terminate()


class SetupGui():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.model_param = {}
        # file = QFile(":/light.qss")
        # file.open(QFile.ReadOnly | QFile.Text)
        # stream = QTextStream(file)
        # app.setStyleSheet(stream.readAll())
        self.ListManagedialog = ListManage(
            "seller", [], self.ui.listWidget_sellerpreferencelist)
        self.treemanagedialog = TreeManage(
            "product", [], self.ui.treeWidget_productpreference)
        self.treemanagedialoginventory = TreeManage(
            "inventory", [], self.ui.treeWidget_inventory, columns=3)
        # self.run()
        self.lastcustomertype = ""
        self.lastseller = ""
        self.updatewidgets()
        self.widgetactions()
        self.MainWindow.show()
        self.customerTypes = {}
        self.sellerTypes = {}
        self.simobj=MarketSimulation()
        # self.thread.start()
        sys.exit(app.exec_())

    def updatewidgets(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.MainWindow.setWindowIcon(
            QtGui.QIcon(scriptDir + r"\UI\icon\title.png"))
        self.ui.comboBox_customertypes.addItem("<new>")
        self.ui.Button_newcustomer.hide()
        self.ui.button_newseller.hide()

    def widgetactions(self):
        self.ui.button_pr_preferencelist.clicked.connect(
            lambda: self.newpreferencelist("product"))
        self.ui.button_seller_preferencelist.clicked.connect(
            lambda: self.newpreferencelist("seller"))
        self.ui.button_inventory.clicked.connect(
            lambda: self.newpreferencelist("inventory"))
        self.ui.checkbox_batchsimulation.stateChanged.connect(lambda: self.state_changed(
            self.ui.checkbox_batchsimulation, self.ui.lineEdit_simNo))
        # self.ui.checkBox_sellerlistfile.stateChanged.connect(lambda: self.state_changed(
        #     self.ui.checkBox_sellerlistfile, self.ui.button_seller_listfile))
        # self.ui.checkBox_productlistfile.stateChanged.connect(lambda: self.state_changed(
        #     self.ui.checkBox_productlistfile, self.ui.button_product_listfile))
        self.ListManagedialog.accepted.connect(self.closelistdialog)
        self.ui.actionExit.triggered.connect(self.close_GUI)
        self.ui.actionExit.setShortcut("ctrl+Q")
        self.ui.button_savecustomertype.clicked.connect(self.saveCustomerType)
        self.ui.button_loadcustomertype.clicked.connect(self.load_customerType)
        # self.ui.button_Run.clicked.connect(self.thread.start)
        self.ui.button_Run.clicked.connect(self.run)
        self.ui.pushButton_reportaddress.clicked.connect(lambda: self.openFileDialog(self.ui.lineEdit_reportAddress))
        self.ui.button_lamdafile.clicked.connect(lambda: self.openFileDialog(self.ui.lineEdit_lambdafile))
        self.ui.button_probfile.clicked.connect(lambda: self.openFileDialog(self.ui.lineEdit_probfile))
        self.ui.button_strategyfile.clicked.connect(lambda: self.openFileDialog(self.ui.lineEdit_stratefyfile))
        # self.ui.button_product_listfile.clicked.connect(
        #     lambda: self.openFileDialog(self.ui.lineEdit_productlistfile))
        # self.ui.button_seller_listfile.clicked.connect(
        #     lambda: self.openFileDialog(self.ui.lineEdit_sellerfile))
        self.ui.lineEdit_stratefyfile.setDisabled(self.ui.radioButton_strategyfile.isChecked() is not True)
        self.ui.radioButton_strategyfile.toggled.connect(
            lambda: self.ui.lineEdit_stratefyfile.setDisabled(self.ui.radioButton_strategyfile.isChecked() is not True))
        self.ui.lineEdit_strategypoly.setDisabled(self.ui.radioButton_strategypoly.isChecked() is not True)
        self.ui.radioButton_strategypoly.toggled.connect(
            lambda: self.ui.lineEdit_strategypoly.setDisabled(self.ui.radioButton_strategypoly.isChecked() is not True))
        self.ui.lineEdit_probfile.setDisabled(self.ui.radioButton_probabilityfile.isChecked() is not True)
        self.ui.radioButton_probabilityfile.toggled.connect(
            lambda: self.ui.lineEdit_probfile.setDisabled(self.ui.radioButton_probabilityfile.isChecked() is not True))
        self.ui.lineEdit_probfixval.setDisabled(self.ui.radioButton_probabilityfixed.isChecked() is not True)
        self.ui.radioButton_probabilityfixed.toggled.connect(
            lambda: self.ui.lineEdit_probfixval.setDisabled(self.ui.radioButton_probabilityfixed.isChecked() is not True))
        self.ui.lineEdit_probpoly.setDisabled(self.ui.radioButton_probabilitypoly.isChecked() is not True)
        self.ui.radioButton_probabilitypoly.toggled.connect(
            lambda: self.ui.lineEdit_probpoly.setDisabled(self.ui.radioButton_probabilitypoly.isChecked() is not True))
        self.ui.lineEdit_lambdafile.setDisabled(self.ui.radioButton_lamdafile.isChecked() is not True)
        self.ui.radioButton_lamdafile.toggled.connect(
            lambda: self.ui.lineEdit_lambdafile.setDisabled(self.ui.radioButton_lamdafile.isChecked() is not True))
        self.ui.lineEdit_lambdafixval.setDisabled(self.ui.radioButton_lamdafixed.isChecked() is not True)
        self.ui.radioButton_lamdafixed.toggled.connect(
            lambda: self.ui.lineEdit_lambdafixval.setDisabled(self.ui.radioButton_lamdafixed.isChecked() is not True))
        self.ui.lineEdit_lambdapoly.setDisabled(self.ui.radioButton_polylamda.isChecked() is not True)
        self.ui.radioButton_polylamda.toggled.connect(
            lambda: self.ui.lineEdit_lambdapoly.setDisabled(self.ui.radioButton_polylamda.isChecked() is not True))
        # self.ui.radioButton_probabilityfile.toggled.connect(lambda : print("toggled"))
        self.ui.comboBox_customertypes.textActivated.connect(self.setCustomerType)
        # self.ui.comboBox_customertypes.currentTextChanged[str].connect(self.setCustomerType)
        self.ui.Button_newcustomer.clicked.connect(self.newcustomerType)
        self.ui.button_removecusType.clicked.connect(self.removecustomerType)
        #------------------------------------------------------------------
        self.ui.button_removeseller.clicked.connect(self.removeSellerType)
        self.ui.button_newseller.clicked.connect(self.newSellerType)
        self.ui.button_saveseller.clicked.connect(self.saveSellerType)
        self.ui.button_loadseller.clicked.connect(self.loadSellerType)
        self.ui.combo_seller.textActivated.connect(self.setSellerType)

        #--------------------------------------------------------------------

    def saveFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getExistingDirectory(
            self.MainWindow, "Set reports address")
        if fileName:
            fileName = fileName + "/"
            return fileName

    def openFileDialog(self, target_lineedit):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "select proper file ")
        if isinstance(fileName, tuple):
            fileName = fileName[0]
        else:
            fileName = str(fileName)
        if fileName:
            fileName = fileName
            target_lineedit.setText(fileName)
            print(fileName)

    def run(self):
        print("server is running ...")
        # self, width=20, height=20, num_customer=50,num_seller=4
        height = int(math.sqrt(int(self.ui.lineEdit_customerNo.text())) * 2)
        width = height
        simulatin_max_days = int(self.ui.lineEdit_simdays.text())
        for key,val in self.customerTypes.items():
            if isinstance(val ,CustomerType):
                self.customerTypes[key]=self.simobj.create_customer_type(val.typeName,
                val.sampleCustomer.lifetime,val.sampleCustomer.preference_list,val.lambdafile,val.contprobfile)
        i=1
        for key ,val in self.sellerTypes.items():
            if isinstance(val, Seller):
                val=self.simobj.create_seller(val.strategy,val.inventory,val.name)
                val.unique_id=i
                self.sellerTypes[key]=val
                i = i + 1
        # simulation_batch_run = self.ui.checkbox_batchsimulation.isChecked()
        # batch_run_number=int(self.ui.lineEdit_simNo.text())
        # self.load3testcustomertype()
        self.model_param = {
            "height": height,
            "width": width,
            "sellers": self.sellerTypes if len(self.sellerTypes) > 0 else int(self.ui.lineEdit_sellerNo.text()),
            "report_address": self.ui.lineEdit_reportAddress.text(),
            "max_steps": simulatin_max_days,
            "customerTypes": self.customerTypes,
        }
        #self.model_param = {
        #     "height": height,
        #     "width": width,
        #     "sellers": int(self.ui.lineEdit_sellerNo.text()),
        #     "report_address": self.ui.lineEdit_reportAddress.text(),
        #     "max_steps": simulatin_max_days,
        #     "customerTypes": self.customerTypes,
        # }
        self.thread = RunThread(parent=None, model_param=self.model_param)
        self.thread.start()
        return self.model_param
        # server = ModularServer(Market, [canvas,chart_count], name="Market simulation",model_params=self.model_param)
        # server.launch()

    def update_customer(self,custyp_name):
        if custyp_name in self.customerTypes.keys():
            self.setCustomerType(self.customerTypes[custyp_name])

    def close_GUI(self):
        self.MainWindow.close()

    def closeEvent(self, event):
        print("window closed")

    def state_changed(self, source, target_btn):
        if source.isChecked():
            target_btn.setDisabled(False)
        else:
            target_btn.setDisabled(True)

    def newpreferencelist(self, name):
        self.ListManagedialog = None
        self.treemanagedialog = None
        self.treemanagedialoginventory = None
        if name == "product":
            self.treemanagedialog = TreeManage(
                name, None, parent_treewidget=self.ui.treeWidget_productpreference)
            self.treemanagedialog.accepted.connect(
                lambda: self.closelistdialog("product"))
            self.treemanagedialog.exec_()
        if name == "inventory":
            self.treemanagedialoginventory = TreeManage(
                name, None, parent_treewidget=self.ui.treeWidget_inventory, columns=3)
            self.treemanagedialoginventory.accepted.connect(
                lambda: self.closelistdialog("inventory"))
            self.treemanagedialoginventory.exec_()
            # self.treemanagedialog.show()

        elif name == "seller":
            self.ListManagedialog = ListManage(
                name, [], parent_listwidget=self.ui.listWidget_sellerpreferencelist)
            self.ListManagedialog.accepted.connect(
                lambda: self.closelistdialog("seller"))
            self.ListManagedialog.exec_()

    def closelistdialog(self, name):
        if name == "product":
            self.ui.treeWidget_productpreference.clear()
            for index in range(self.treemanagedialog.tree.topLevelItemCount()):
                m = self.treemanagedialog.tree.topLevelItem(index).clone()
                # print(m.text(0))
                m.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled |
                           QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
                self.ui.treeWidget_productpreference.insertTopLevelItem(
                    index, m)
        elif name == "inventory":
            self.ui.treeWidget_inventory.clear()
            for index in range(self.treemanagedialoginventory.tree.topLevelItemCount()):
                m = self.treemanagedialoginventory.tree.topLevelItem(index).clone()
                # print(m.text(0))
                m.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled |
                           QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
                self.ui.treeWidget_inventory.insertTopLevelItem(
                    index, m)
        elif name == "seller":
            self.ui.listWidget_sellerpreferencelist.clear()
            for index in range(self.ListManagedialog.list.count()):
                m = QListWidgetItem(self.ListManagedialog.list.item(index).text())
                m.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
                self.ui.listWidget_sellerpreferencelist.addItem(m)

        print("close dialog")

    # ---------------------------------------------------------------------

    def getCustomerTypeFromUi(self):
        seller_preferenceList = [str(self.ui.listWidget_sellerpreferencelist.item(
            i).text()) for i in range(self.ui.listWidget_sellerpreferencelist.count())]
        root = self.ui.treeWidget_productpreference.invisibleRootItem()
        child_count = root.childCount()
        product_preferencelist = {}
        for i in range(child_count):
            item = root.child(i)
            product_preferencelist[item.text(0)] = int(item.text(1))
        user_customer = Customer(1, Market)
        user_customer.preference_list = product_preferencelist
        # user_customer.percentofall = int(self.ui.lineEdit_percentofall.text())
        user_customer.seller_preferencelist = seller_preferenceList
        user_customer.lifetime = int(self.ui.lineEdit_lifetime.text())
        type_name = self.ui.comboBox_customertypes.currentText()
        user_customer.type_name = type_name
        prob= 0.5
        lamda= 10
        if self.ui.radioButton_probabilityfixed.isChecked() is True:
            prob = float(self.ui.lineEdit_probfixval.text())
        elif self.ui.radioButton_probabilityfile.isChecked() is True:
            prob = str(self.ui.lineEdit_probfile.text())
        elif self.ui.radioButton_probabilitypoly.isChecked() is True:
            prob = [self.ui.lineEdit_probpoly.text()]
            # prob = [float(p) for p in self.ui.lineEdit_probpoly.text().split()]
        if self.ui.radioButton_lamdafixed.isChecked() is True:
            lamda = int(self.ui.lineEdit_lambdafixval.text())
        elif self.ui.radioButton_lamdafile.isChecked() is True:
            lamda = str(self.ui.lineEdit_lambdafile.text())
        elif self.ui.radioButton_polylamda.isChecked() is True:
            # lamda = [float(p) for p in self.ui.lineEdit_lambdapoly.text().split()]
            lamda = [self.ui.lineEdit_lambdapoly.text()]
        # custyp=self.simobj.create_customer_type(type_name,user_customer.lifetime,user_customer.preference_list,lamda,prob)
        custyp = CustomerType(samplecustomer=user_customer, typeName=type_name, contprobfile=prob,lambdafile=lamda)
        return custyp

    def setCustomerType(self,customertyp):

        if customertyp == "<new>" :
            self.ui.comboBox_customertypes.setEditable(True)
            self.lastcustomertype = "<new>"
            self.ui.Button_newcustomer.show()
            return
        elif self.lastcustomertype == "<new>" :
            self.ui.comboBox_customertypes.setEditable(False)
            self.ui.Button_newcustomer.hide()

        self.ui.comboBox_customertypes.setCurrentText(self.lastcustomertype)
        if self.lastcustomertype != "" and self.lastcustomertype != "<new>":
            self.customerTypes[self.lastcustomertype]=self.getCustomerTypeFromUi()

        mm = self.ui.comboBox_customertypes.currentIndex()

        # self.lastcustomertype=self.ui.comboBox_customertypes.currentText()
        self.ui.comboBox_customertypes.setCurrentText(self.lastcustomertype)
        if customertyp == self.lastcustomertype:
            return

        if isinstance(customertyp,str) and str(customertyp) in self.customerTypes.keys() :
            customertyp=self.customerTypes[customertyp]
        if isinstance(customertyp,Customer):
            user_customer = customertyp
            self.fill_preferencelist(user_customer.preference_list)
            self.fill_sellerpreferencelist(user_customer.seller_preferencelist)
            # self.ui.comboBox_customertypes.addItem(user_customer.type_name)
            self.ui.comboBox_customertypes.setCurrentText(user_customer.type_name)
            self.ui.lineEdit_lifetime.setText(str(user_customer.lifetime))
            self.lastcustomertype = user_customer.type_name
        elif isinstance(customertyp,CustomerType):
            self.fill_preferencelist(customertyp.sampleCustomer.preference_list)
            self.fill_sellerpreferencelist(customertyp.sampleCustomer.seller_preferencelist)
            # self.ui.comboBox_customertypes.addItem(user_customer.type_name)
            self.ui.comboBox_customertypes.setCurrentText(customertyp.typeName)
            self.ui.lineEdit_lifetime.setText(str(customertyp.sampleCustomer.lifetime))
            self.lastcustomertype = customertyp.typeName
            if isinstance(customertyp.lambdafile, str):
                print("use filepath for generation ratio")
                self.ui.radioButton_lamdafile.click()
                self.ui.lineEdit_lambdafile.setText(str(customertyp.lambdafile))
            elif isinstance(customertyp.lambdafile, int):
                print("use fix generation ratio")
                self.ui.radioButton_lamdafixed.click()
                self.ui.lineEdit_lambdafixval.setText(str(customertyp.lambdafile))
            elif isinstance(customertyp.lambdafile, list):
                print("use polynomial generation ratio")
                self.ui.radioButton_polylamda.click()
                # plist=""
                # for cell in customertyp.lambdafile:
                #     plist+=str(cell)+" "
                self.ui.lineEdit_lambdapoly.setText(customertyp.lambdafile[0])
            if isinstance(customertyp.contprobfile, str):
                print("use filepath for generation ratio")
                self.ui.radioButton_probabilityfile.click()
                self.ui.lineEdit_probfile.setText(str(customertyp.contprobfile))
            elif isinstance(customertyp.contprobfile, float):
                print("use fix generation ratio")
                self.ui.radioButton_probabilityfixed.click()
                self.ui.lineEdit_probfixval.setText(str(customertyp.contprobfile))
            elif isinstance(customertyp.contprobfile, list):
                self.ui.radioButton_probabilitypoly.click()
                print("use polynomial generation ratio")
                # for cell in customertyp.contprobfile:
                #     plist+=str(cell)+" "
                self.ui.lineEdit_probpoly.setText(customertyp.contprobfile[0])
        self.ui.comboBox_customertypes.show()

        # self.ui.lineEdit_percentofall.setText(str(user_customer.percentofall))
        # self.customerTypes[user_customer.type_name] = user_customer
        # print(user_customer.__dict__)

    def saveCustomerType(self):
        custype=self.getCustomerTypeFromUi()
        with open("customertypes\\customer_type_" + custype.typeName + '.txt', 'wb') as file1:
            dill.dump(custype, file1)
        self.customerTypes[custype.typeName] = custype

    def load_customerType(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "select proper file ")
        if isinstance(fileName, tuple):
            fileName = fileName[0]
        else:
            fileName = str(fileName)
        print(fileName)
        if not fileName:
            return
        with open(fileName, 'rb') as filehandler:
            user_customer = dill.load(filehandler)
        if isinstance(user_customer,CustomerType):
            self.ui.comboBox_customertypes.addItem(user_customer.typeName)
            self.setCustomerType(user_customer)
            self.customerTypes[user_customer.typeName]=user_customer
            self.ui.comboBox_customertypes.show()

    def newcustomerType(self):
        typname=self.ui.comboBox_customertypes.lineEdit().text()
        self.ui.comboBox_customertypes.setEditable(False)

        self.ui.comboBox_customertypes.addItem(typname)
        custyp=self.getCustomerTypeFromUi()
        custyp.typeName=typname
        custyp.sampleCustomer.type_name=typname
        self.customerTypes[typname]=custyp
        self.ui.Button_newcustomer.hide()

        # self.ui.comboBox_customertypes.addItem(str(self.ui.comboBox_customertypes.count()))

    def removecustomerType(self):
        typename=self.ui.comboBox_customertypes.currentText()
        if typename !="<new>":
            self.ui.comboBox_customertypes.removeItem(self.ui.comboBox_customertypes.findText(typename))
            self.customerTypes.pop(typename)

    # ---------------------------------------------------------------------

    def getSellerTypeFromUi(self):
        root = self.ui.treeWidget_inventory.invisibleRootItem()
        child_count = root.childCount()
        inventory = {}
        strategy=""
        for i in range(child_count):
            item = root.child(i)
            inventory[item.text(0)] = Product(name=item.text(0),minvalue=item.text(1),available=int(item.text(2)))
        sellerName = self.ui.combo_seller.currentText()
        if self.ui.radioButton_strategyfile.isChecked() is True:
            strategy = str(self.ui.lineEdit_stratefyfile.text())
        elif self.ui.radioButton_strategypoly.isChecked() is True:
            strategy = [self.ui.lineEdit_strategypoly.text()]
            # strategy = [float(p) for p in self.ui.lineEdit_strategypoly.text().split()]
        elif self.ui.radioButton_strategyfixed.isChecked() is True:
            strategy = float(self.ui.lineEdit_strategyfixval.text())
        seller = self.simobj.create_seller(inventory=inventory, strategy=None, name=sellerName)
        seller.strategy=strategy
        if self.ui.combo_seller.findText(sellerName) > -1:
            seller.unique_id=self.ui.combo_seller.findText(sellerName)
        else:
            seller.unique_id=self.ui.combo_seller.count()
        seller.name=sellerName
        return seller

    def setSellerType(self,sellertyp):

        m=self.ui.combo_seller.currentText()

        self.ui.combo_seller.setCurrentText(self.lastseller)
        m=self.ui.combo_seller.currentText()
        if self.lastseller != "" and self.lastseller != "<new>":
            self.sellerTypes[self.lastseller]=self.getSellerTypeFromUi()

        if sellertyp == "<new>" :
            self.ui.combo_seller.setEditable(True)
            self.lastseller = "<new>"
            self.ui.button_newseller.show()
            return
        elif self.lastseller == "<new>" :
            self.ui.combo_seller.setEditable(False)
            self.ui.button_newseller.hide()


        if sellertyp == self.lastseller:
            return

        if isinstance(sellertyp,str) and str(sellertyp) in self.sellerTypes.keys():
            sellertyp=self.sellerTypes[sellertyp]
        if isinstance(sellertyp,Seller):
            self.fill_inventory(sellertyp.inventory)
            self.ui.combo_seller.setCurrentText(sellertyp.name)
            self.lastseller = sellertyp.name
            if isinstance(sellertyp.strategy, str):
                print("use filepath for generation ratio")
                self.ui.radioButton_strategyfile.click()
                self.ui.lineEdit_stratefyfile.setText(str(sellertyp.strategy))
            elif isinstance(sellertyp.strategy, list):
                print("use polynomial generation ratio")
                self.ui.radioButton_strategypoly.click()
                plist=""
                for cell in sellertyp.strategy:
                    plist+=str(cell)+" "
                self.ui.lineEdit_strategypoly.setText(plist)
            elif isinstance(sellertyp.strategy,float):
                self.ui.radioButton_strategyfixed.click()
                self.ui.lineEdit_strategyfixval.setText(str(sellertyp.strategy))
        self.ui.combo_seller.show()

    def saveSellerType(self):
        sellertyp=self.getSellerTypeFromUi()
        with open("sellerTypes\\seller_type_" + sellertyp.name + '.txt', 'wb') as file1:
            dill.dump(sellertyp, file1)
        self.sellerTypes[sellertyp.name] = sellertyp

    def loadSellerType(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getOpenFileName(
            self.MainWindow, "select proper file ")
        if isinstance(fileName, tuple):
            fileName = fileName[0]
        else:
            fileName = str(fileName)
        print(fileName)
        if not fileName:
            return
        with open(fileName, 'rb') as filehandler:
            sellertype = dill.load(filehandler)
        if isinstance(sellertype,Seller):
            self.ui.combo_seller.addItem(sellertype.name)
            self.setSellerType(sellertype)
            self.sellerTypes[sellertype.name]=sellertype
            self.ui.combo_seller.show()

    def newSellerType(self):
        typname=self.ui.combo_seller.lineEdit().text()
        self.ui.combo_seller.setEditable(False)
        self.ui.combo_seller.addItem(typname)
        sellertyp=self.getSellerTypeFromUi()
        self.lastseller=typname
        sellertyp.name=typname
        self.sellerTypes[typname]=sellertyp
        self.ui.button_newseller.hide()
        self.ui.combo_seller.setCurrentText(typname)
        self.ui.combo_seller.show()


    def removeSellerType(self):
        typename=self.ui.combo_seller.currentText()
        if typename !="<new>":
            self.ui.combo_seller.removeItem(self.ui.combo_seller.findText(typename))
            self.sellerTypes.pop(typename)
    # -----------------------------------------------------------------------------
    def load3testcustomertype(self):
        # c = CustomerType(samplecustomer=typ, typeName=typ.type_name, lambdafile="lambda.csv",
        #                  contprobfile="contprob.csv")
        # c.setlambda()
        # c.setcontprob()
        with open("customertypes/customer_type_customerpoor.txt", 'rb') as filehandler:
            self.customerTypes["customerpoor"] = pickle.load(filehandler)
        with open("customertypes/customer_type_customerrich.txt", 'rb') as filehandler:
            self.customerTypes["customerrrich"] = pickle.load(filehandler)
        with open("customertypes/customer_type_customernormal.txt", 'rb') as filehandler:
            self.customerTypes["customernormal"] = pickle.load(filehandler)


    def fill_preferencelist(self, preferenc_dict={}):
        self.ui.treeWidget_productpreference.clear()
        for key, val in preferenc_dict.items():
            self.ui.treeWidget_productpreference.addTopLevelItem(
                QTreeWidgetItem(self.ui.treeWidget_productpreference, [key, str(val)]))

    def fill_inventory(self, inventory={}):
        self.ui.treeWidget_inventory.clear()
        for key, val in inventory.items():
            if isinstance(val ,Product):
                self.ui.treeWidget_inventory.addTopLevelItem(
                    QTreeWidgetItem(self.ui.treeWidget_inventory, [key, str(val.minvalue),str(val.available)]))
            else:
                self.ui.treeWidget_inventory.addTopLevelItem(
                QTreeWidgetItem(self.ui.treeWidget_inventory, [key, str(val)]))

    def fill_sellerpreferencelist(self, preferenc_list=[]):
        self.ui.listWidget_sellerpreferencelist.clear()
        self.ui.listWidget_sellerpreferencelist.addItems(preferenc_list)

    def setup_fromfile(self):
        pass

    # def update_customertypeui()

    def batchmodesetup(self):
        pass

def load3testcustomertype():
    custypes = {}
    with open("customertypes/customer_type_customerpoor.txt", 'rb') as filehandler:
        custypes["customerpoor"] = pickle.load(filehandler)
    with open("customertypes/customer_type_customerrich.txt", 'rb') as filehandler:
        custypes["customerrrich"] = pickle.load(filehandler)
    with open("customertypes/customer_type_customernormal.txt", 'rb') as filehandler:
        custypes["customernormal"] = pickle.load(filehandler)
    return custypes


class MarketSimulation():
    def __init__(self):
        self.customer_types = {}
        self.seller_list = {}
        self.product_list = {}
        self.custome_scheduler = None
        self.simulation_time = 0
        self.grid_size = 20

    def fix_power_sign(self,equation):
        return equation.replace("^", "**")

    def eval_polynomial(self,equation, x_value, y_value=None):
        fixed_equation = self.fix_power_sign(equation.strip())
        parts = fixed_equation.split("+")
        x_str_value = str(x_value)
        parts_with_values = (part.replace("x", x_str_value) for part in parts)
        if y_value is not None:
            y_str_value = str(y_value)
            parts_with_values = (part.replace("y", y_str_value) for part in parts_with_values)
        partial_values = (eval(part) for part in parts_with_values)
        return sum(partial_values)
    # customer

    def add_customer_type(self, customer_type):
        if isinstance(customer_type, CustomerType):
            self.customer_types[customer_type.typeName] = customer_type

    def remove_customer_type(self, customer_type):
        if isinstance(customer_type, str):
            self.customer_types.pop(customer_type)
        elif isinstance(customer_type, CustomerType):
            self.customer_types.pop(customer_type.typeName)

    def create_customer_type(self, name, lifetime, preferenclist, generationlambda, forcebuyprob):
        samplecus = Customer(1, Market(), None, lifetime=lifetime)
        samplecus.preference_list = preferenclist
        samplecus.type_name = name
        # samplecus.ignorShopping = forcebuyprob
        custyp = CustomerType(samplecustomer=samplecus)
        if callable(generationlambda):
            print("use custom function generation ratio")
            custyp.getLambda = generationlambda
        elif isinstance(generationlambda, str):
            print("use filepath for generation ratio")
            custyp.setlambda(generationlambda)
        elif isinstance(generationlambda, int):
            print("use fix generation ratio")
            custyp.getLambda = lambda step: generationlambda
            custyp.lambdafixval=generationlambda
        elif isinstance(generationlambda, list):
            print("use polynomial generation ratio")
            # custyp.getLambda = lambda step: np.polyval(generationlambda, int(step))
            custyp.getLambda= lambda step: self.eval_polynomial(str(generationlambda[0]),step)
        if callable(forcebuyprob):
            print("use custom function generation ratio")
            custyp.getcontprob = forcebuyprob
        elif isinstance(forcebuyprob, str):
            print("use filepath for generation ratio")
            custyp.setcontprob(forcebuyprob)
        elif isinstance(forcebuyprob, float):
            print("use fix generation ratio")
            custyp.getcontprob = lambda tryNo: forcebuyprob
            custyp.contprobfixval=forcebuyprob
        elif isinstance(forcebuyprob, list):
            print("use polynomial generation ratio")
            # custyp.getcontprob = lambda tryNo: np.polyval(forcebuyprob, int(tryNo))
            custyp.getcontprob= lambda tryNo: self.eval_polynomial(str(forcebuyprob[0]), int(tryNo))

        custyp.typeName=name
        return custyp

    # seller
    def create_seller(self, strategy=None, inventory=None,name=None):
        seller = Seller(len(self.seller_list), Market())
        seller.inventory = inventory
        if strategy is not None:
            if isinstance(strategy,list):
                seller.strategy=lambda product,step,:self.eval_polynomial(strategy[0],step,product.minvalue)
                # seller.strategy=lambda product,step,:polyval2d(step,product.minvalue,strategy)
            elif callable(strategy):
                seller.strategy=strategy
            elif isinstance(strategy,float):
                seller.strategy = lambda product,step,:seller.strategy15(product,step,strategy)
        if name is None:
            seller.name=str(seller.unique_id)
        else :
            seller.name=name
        seller.inventory_available()
        return seller

    def create_inventory(self, products):
        inventory = {}
        if isinstance(products, str):
            with open(products, newline='', encoding='utf-8') as f:
                infile = csv.DictReader(f, fieldnames=["name", "minvalue", "count"])
                for row in infile:
                    inventory[row["name"]] = Product(name=row["name"], minvalue=float(row["minvalue"]),
                                                     available=row["count"])
        elif isinstance(products, list):
            for row in products:
                inventory[row["name"]] = Product(name=row["name"], minvalue=float(row["minvalue"]),
                                                 available=row["count"])
        return inventory

    def add_seller(self, seller):
        if isinstance(seller, Seller):
            self.seller_list[seller.unique_id] = seller

    def remove_seller(self, seller):
        if isinstance(seller, int):
            self.seller_list.pop(seller)
        elif isinstance(seller, Seller):
            self.seller_list.pop(seller.unique_id)

    def set_product_list(self, p_list):
        if (isinstance(p_list, dict)):
            self.product_list = p_list
        elif (isinstance(p_list, str)):
            self.product_list = self.readproductfile(p_list)

    def readproductfile(self, filepath):
        d = {}
        with open(filepath, newline='', encoding='utf-8') as f:
            infile = csv.reader(f)
            d = dict(filter(None, infile))
        return d

    def set_strategy(self, sellerid, strategy):
        if hasattr(strategy, "__call__"):
            self.seller_list[sellerid].strategy = strategy

    # model

    def set_max_days(self, simul_time):
        self.simulation_time = simul_time

    def set_callerscheduler(self, schedulfunction):
        self.custome_scheduler = schedulfunction

    def set_market_capacity(self, gridsize):
        self.grid_size = gridsize

    # server

    def run(self,visual=True):
        print("server is running ...")
        # self, width=20, height=20, num_customer=50,num_seller=4

        height = self.grid_size
        width = height
        # self.load3testcustomertype()
        self.model_param = {
            "height": height,
            "width": width,
            # "grid_size": int(self.gridsize),#change to gridsize
            "report_address": self.report_path,
            "max_steps": self.simulation_time,
            "customerTypes": self.customer_types,
            "sellers": self.seller_list,
        }
        self.is_running = True

        customer = {"Label": "Customer", "Color": "cornflowerblue"}
        seller = {"Label": "Seller", "Color": "blueviolet"}
        canvas = CanvasGrid(market_portrayal, width, height)
        chart_count = ChartModule([customer, seller,])
        if visual:
            self.server = ModularServer(Market, [
            canvas, chart_count], name="Market simulation", model_params=self.model_param)
        else:
            self.server = ModularServer(Market, [chart_count], name="Market simulation", model_params=self.model_param)
        # self.server.signalobj.closesignal.connect(self.stop)
        self.server.launch()  # emit new Signal with value

    def setup_gui(self):
        sim = SetupGui()

    def console_run(self):
        height = self.grid_size
        width = height
        # self.load3testcustomertype()
        self.model_param = {
            "height": height,
            "width": width,
            # "grid_size": int(self.gridsize),#change to gridsize
            "report_address": self.report_path,
            "max_steps": self.simulation_time,
            "customerTypes": self.customer_types,
            "sellers": self.seller_list,
        }
        self.is_running = True

    def batch_run(self):
        pass

    # reports
    def set_report_path(self, dirPath):
        self.report_path = dirPath

    def set_how_report(self, report_type="minimal"):
        if report_type in ["all", "minimal", "seller", "periodic transaction"]:
            self.reports = report_type
        else:
            print('report option should be in "all","minimal","seller","periodic transaction" ')


if __name__ == "__main__":

    print("choose run mode")
    print("1 --> setup window")
    print("2 --> visual run ")
    print("3 --> single run console")
    print("4 --> batch mode run")
    mode = int(input())
    sim = MarketSimulation()
    if mode == 1:
        sim.setup_gui()
    if mode == 2:
        sim.set_market_capacity(20)
        sim.set_max_days(30)
        sim.report_path = "C:/SSD/Uni/Thesis/Source/main/simulator/reports/"

        # sim.create_customer_type('poorcus',1,)
        # sim.customer_types=load3testcustomertype()
        sim.add_customer_type(sim.create_customer_type("poortype", 1, {"p1": 300, "p3": 390, "p2": 320}, 10, 0.6))
        sim.add_customer_type(sim.create_customer_type("normaltype", 1, {"p3": 400, "p2": 350, "p1": 300}, 40, 0.5))
        sim.add_customer_type(sim.create_customer_type("richtype", 1, {"p4": 800, "p3": 800}, 5, 0.2))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory/inventory1.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory/inventory2.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory/inventory3.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory/inventory3.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory/inventory1.csv")))
        sim.run()
    if mode == 3:
        sim.console_run();
    if mode == 4:
        sim.batch_run();

# server = ModularServer(Market, [canvas,chart_count], name="Market simulation")
# server.launch()
