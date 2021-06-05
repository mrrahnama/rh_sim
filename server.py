import asyncio
import math
import os
import pickle
import sys
import csv
from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTreeWidgetItem ,QListWidgetItem
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
import numpy as np
from Model import Market, Seller, Customer, CustomerType,Product
from UI.simui3_1 import Ui_MainWindow
from listmange import ListManage
from treamanage import TreeManage


# from UI.styles import breeze_resources

# from UI.UI_uibased import Ui
# width = 20
# height     = 20


def market_portrayal(agent):
    if agent is None:
        return
    portrayal = {"Shape": "UI/icon/store_color.png", "Filled":
        "true", "w": 1, "h": 1, "Layer": 0}
    if type(agent) is Seller:
        portrayal["Color"] = "cornflowerblue"
    elif type(agent) is Customer:
        portrayal["Shape"] = "UI/icon/customer4.png"
        portrayal["Color"] = "tomato"
        portrayal["r"] = 1
        portrayal["scale"] = 0.6
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
        # self.run()
        self.updatewidgets()
        self.widgetactions()
        self.MainWindow.show()
        self.customerTypes = {}
        self.sellerTypes = {}
        # self.thread.start()
        sys.exit(app.exec_())

    def updatewidgets(self):
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        self.MainWindow.setWindowIcon(
            QtGui.QIcon(scriptDir + r"\UI\icon\title.png"))

    def widgetactions(self):
        self.ui.button_pr_preferencelist.clicked.connect(
            lambda: self.newpreferencelist("product"))
        self.ui.button_seller_preferencelist.clicked.connect(
            lambda: self.newpreferencelist("seller"))
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
        self.ui.pushButton_reportaddress.clicked.connect(self.saveFileDialog)
        # self.ui.button_product_listfile.clicked.connect(
        #     lambda: self.openFileDialog(self.ui.lineEdit_productlistfile))
        # self.ui.button_seller_listfile.clicked.connect(
        #     lambda: self.openFileDialog(self.ui.lineEdit_sellerfile))

    def saveFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getExistingDirectory(
            self.MainWindow, "Set reports address")
        if fileName:
            fileName = fileName + "/"
            self.ui.lineEdit_reportAddress.setText(fileName)
            print(fileName)

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
        # simulation_batch_run = self.ui.checkbox_batchsimulation.isChecked()
        # batch_run_number=int(self.ui.lineEdit_simNo.text())
        self.load3testcustomertype()
        self.model_param = {
            "height": height,
            "width": width,
            "sellers": int(self.ui.lineEdit_sellerNo.text()),
            "report_address": self.ui.lineEdit_reportAddress.text(),
            "max_steps": simulatin_max_days,
            "customerTypes": self.customerTypes,
        }
        self.thread = RunThread(parent=None, model_param=self.model_param)
        self.thread.start()
        return self.model_param
        # server = ModularServer(Market, [canvas,chart_count], name="Market simulation",model_params=self.model_param)
        # server.launch()

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
        if name == "product":
            self.treemanagedialog = TreeManage(
                name, None, parent_treewidget=self.ui.treeWidget_productpreference)
            self.treemanagedialog.accepted.connect(
                lambda: self.closelistdialog("product"))
            self.treemanagedialog.exec_()
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

        elif name == "seller":
            self.ui.listWidget_sellerpreferencelist.clear()
            for index in range(self.ListManagedialog.list.count()):
                m = QListWidgetItem( self.ListManagedialog.list.item(index).text())
                m.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
                self.ui.listWidget_sellerpreferencelist.addItem(m)

        print("close dialoag")

    def saveCustomerType(self):
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
        user_customer.percentofall = int(self.ui.lineEdit_percentofall.text())
        user_customer.seller_preferencelist = seller_preferenceList
        user_customer.lifetime = int(self.ui.lineEdit_lifetime.text())
        type_name = self.ui.comboBox_customertypes.currentText()
        user_customer.type_name = type_name
        with open("customertypes\\customer_type_" + type_name + '.txt', 'wb') as file1:
            pickle.dump(user_customer, file1)
        self.customerTypes[type_name] = user_customer

        # print(self.ui.comboBox_customertypes.currentText())
        # print(product_preferencelist )
        # print(sellerpreferenceList)

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
        with open(fileName, 'rb') as filehandler:
            user_customer = pickle.load(filehandler)
            self.fill_preferencelist(user_customer.preference_list)
            self.fill_sellerpreferencelist(user_customer.seller_preferencelist)
            self.ui.comboBox_customertypes.addItem(user_customer.type_name)
            self.ui.comboBox_customertypes.setCurrentText(
                user_customer.type_name)
            self.ui.lineEdit_lifetime.setText(str(user_customer.lifetime))
            self.ui.lineEdit_percentofall.setText(
                str(user_customer.percentofall))
            self.customerTypes[user_customer.type_name] = user_customer

            print(user_customer.__dict__)

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

    def saveSellerType(self):
        pass

    def fill_preferencelist(self, preferenc_dict={}):
        self.ui.treeWidget_productpreference.clear()
        for key, val in preferenc_dict.items():
            self.ui.treeWidget_productpreference.addTopLevelItem(
                QTreeWidgetItem(self.ui.treeWidget_productpreference, [key, str(val)]))

    def fill_sellerpreferencelist(self, preferenc_list=[]):
        self.ui.listWidget_sellerpreferencelist.clear()
        self.ui.listWidget_sellerpreferencelist.addItems(preferenc_list)

    def setup_fromfile(self):
        pass

    # def update_customertypeui()

    def batchmodesetup(self):
        pass

def load3testcustomertype():
    custypes={}
    with open("customertypes/customer_type_customerpoor.txt", 'rb') as filehandler:
        custypes["customerpoor"] = pickle.load(filehandler)
    with open("customertypes/customer_type_customerrich.txt", 'rb') as filehandler:
        custypes["customerrrich"] = pickle.load(filehandler)
    with open("customertypes/customer_type_customernormal.txt", 'rb') as filehandler:
        custypes["customernormal"] = pickle.load(filehandler)
    return custypes

class MarketSimulation():
    def __init__(self):
        self.customer_types={}
        self.seller_list={}
        self.product_list={}
        self.custome_scheduler=None
        self.simulation_time=0
        self.grid_size=20
    #customer

    def add_customer_type(self, customer_type):
        if isinstance(customer_type,CustomerType):
            self.customer_types[customer_type.typeName] = customer_type

    def remove_customer_type(self,customer_type):
        if isinstance(customer_type,str):
            self.customer_types.pop(customer_type)
        elif isinstance(customer_type,CustomerType):
            self.customer_types.pop(customer_type.typeName)

    def create_customer_type(self,name ,lifetime , preferenclist, generationlambda, forcebuyprob ):
        samplecus = Customer(1,Market(),None,lifetime=lifetime)
        samplecus.preference_list=preferenclist
        samplecus.type_name=name
        samplecus.ignorShopping=forcebuyprob
        custyp = CustomerType(samplecustomer=samplecus)
        if callable(generationlambda):
            print("use custom function generation ratio")
            custyp.getLambda=generationlambda
        elif isinstance(generationlambda,str):
            print("use filepath for generation ratio")
            custyp.setlambda(generationlambda)
        elif isinstance(generationlambda,int):
            print("use fix generation ratio")
            custyp.getLambda=lambda step: generationlambda
        elif isinstance(generationlambda,list):
            print("use polynomial generation ratio")
            custyp.getLambda=lambda step:np.polyval(generationlambda,step)
        if callable(forcebuyprob):
            print("use custom function generation ratio")
            custyp.getcontprob = forcebuyprob
        elif isinstance(forcebuyprob, str):
            print("use filepath for generation ratio")
            custyp.setcontprob(forcebuyprob)
        elif isinstance(forcebuyprob, float):
            print("use fix generation ratio")
            custyp.getcontprob = lambda tryNo: forcebuyprob
        elif isinstance(forcebuyprob, list):
            print("use polynomial generation ratio")
            custyp.getcontprob = lambda tryNo: np.polyval(forcebuyprob, tryNo)
        return  custyp

    #seller

    def create_seller(self,strategy=None,inventory=None):
        seller = Seller(len(self.seller_list),Market())
        seller.inventory=inventory
        if strategy is not None:
            seller.strategy=strategy
        seller.inventory_available()
        return seller

    def create_inventory(self,products):
        inventory={}
        if isinstance(products,str):
            with open(products, newline='', encoding='utf-8') as f:
                infile = csv.DictReader(f,fieldnames=["name", "minvalue", "count"])
                for row in infile:
                    inventory[row["name"]] = Product(name=row["name"], minvalue=float(row["minvalue"]),available=row["count"])
        elif isinstance(products,dict):
            for row in products:
                inventory[row["name"]] = Product(name=row["name"], minvalue=float(row["minvalue"]),
                                                 available=row["count"])
        return inventory

    def add_seller(self,seller):
        if isinstance(seller,Seller):
            self.seller_list[seller.unique_id]=seller

    def remove_seller(self,seller):
        if isinstance(seller, int):
            self.seller_list.pop(seller)
        elif isinstance(seller, Seller):
            self.seller_list.pop(seller.unique_id)

    def set_product_list(self,p_list):
        if(isinstance(p_list,dict)):
            self.product_list=p_list
        elif(isinstance(p_list,str)):
            self.product_list=self.readproductfile(p_list)

    def readproductfile(self,filepath):
        d={}
        with open(filepath, newline='', encoding='utf-8') as f:
            infile = csv.reader(f)
            d = dict(filter(None, infile))
        return d

    def set_strategy(self,sellerid,strategy):
        if hasattr(strategy, "__call__"):
            self.seller_list[sellerid].strategy=strategy
    #model

    def set_max_days(self,simul_time):
        self.simulation_time=simul_time

    def set_callerscheduler(self,schedulfunction):
        self.custome_scheduler = schedulfunction

    def set_market_capacity(self,gridsize):
        self.grid_size=gridsize

    #server

    def run(self):
        print("server is running ...")
        # self, width=20, height=20, num_customer=50,num_seller=4

        height = self.grid_size
        width = height
        #self.load3testcustomertype()
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
        chart_count = ChartModule([customer, seller])
        self.server = ModularServer(Market, [
            canvas, chart_count], name="Market simulation", model_params=self.model_param)
        # self.server.signalobj.closesignal.connect(self.stop)
        self.server.launch()  # emit new Signal with value



    def setup_gui(self):
        sim = SetupGui()

    def console_run(self):
        pass

    def batch_run(self):
        pass
#reports
    def set_report_path(self,dirPath):
        self.report_path=dirPath

    def set_how_report(self,report_type="minimal"):
        if report_type in ["all","minimal","seller","periodic transaction"]:
            self.reports = report_type
        else:
            print('report option should be in "all","minimal","seller","periodic transaction" ')


if __name__ == "__main__":
    print("choose run mode")
    print("1 --> setup window")
    print("2 --> visual run ")
    print("3 --> single run console")
    print("4 --> batch mode run")
    mode =int( input())
    sim = MarketSimulation()
    if mode==1:
        sim.setup_gui()
    if mode==2:

        sim.set_market_capacity(20)
        sim.set_max_days(30)
        sim.report_path="C:/SSD/Uni/Thesis/Source/main/simulator/reports/"

        # sim.create_customer_type('poorcus',1,)
        # sim.customer_types=load3testcustomertype()
        sim.add_customer_type(sim.create_customer_type("poortype",1,{"p1":300,"p3":390,"p2":320},10,0.6))
        sim.add_customer_type(sim.create_customer_type("normaltype",1,{"p3":400,"p2":350,"p1":300},40,0.5))
        sim.add_customer_type(sim.create_customer_type("richtype",1,{"p4":800,"p3":800},5,0.2))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory1.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory2.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory3.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory3.csv")))
        sim.add_seller(sim.create_seller(inventory=sim.create_inventory("inventory1.csv")))
        sim.run()
    if mode==3:
        sim.console_run();
    if mode==4:
        sim.batch_run();

# server = ModularServer(Market, [canvas,chart_count], name="Market simulation")
# server.launch()
