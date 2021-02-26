
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from Model import Market, Seller, Customer
from PyQt5 import QtCore
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QTreeWidgetItem
from PyQt5.QtCore import QFile, QTextStream
from UI.simui_2_4 import Ui_MainWindow
import sys
import math
import asyncio
import os
import pickle
from listmange import ListManage
from treamanage import TreeManage
#from UI.styles import breeze_resources

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

        self.server.launch()     # emit new Signal with value

    def stop(self):
        self.is_running = False
        print('stopping thread...')
        self.terminate()
        


class Run_handler():
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.model_param = {}
        #file = QFile(":/light.qss")
        #file.open(QFile.ReadOnly | QFile.Text)
        #stream = QTextStream(file)
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
        self.ui.checkBox_sellerlistfile.stateChanged.connect(lambda: self.state_changed(
            self.ui.checkBox_sellerlistfile, self.ui.button_seller_listfile))
        self.ui.checkBox_productlistfile.stateChanged.connect(lambda: self.state_changed(
            self.ui.checkBox_productlistfile, self.ui.button_product_listfile))
        self.ListManagedialog.accepted.connect(self.closelistdialog)
        self.ui.actionExit.triggered.connect(self.close_GUI)
        self.ui.actionExit.setShortcut("ctrl+Q")
        self.ui.button_savecustomertype.clicked.connect(self.saveCustomerType)
        self.ui.button_loadcustomertype.clicked.connect(self.load_customerType)
        # self.ui.button_Run.clicked.connect(self.thread.start)
        self.ui.button_Run.clicked.connect(self.run)
        self.ui.pushButton_reportaddress.clicked.connect(self.saveFileDialog)
        self.ui.button_product_listfile.clicked.connect(
            lambda: self.openFileDialog(self.ui.lineEdit_productlistfile))
        self.ui.button_seller_listfile.clicked.connect(
            lambda: self.openFileDialog(self.ui.lineEdit_sellerfile))

    def saveFileDialog(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getExistingDirectory(
            self.MainWindow, "Set reports address")
        if fileName:
            fileName = fileName+"/"
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
        height = int(math.sqrt(int(self.ui.lineEdit_customerNo.text()))*2)
        width = height
        simulatin_max_days = int(self.ui.lineEdit_simdays.text())
        #simulation_batch_run = self.ui.checkbox_batchsimulation.isChecked()
        # batch_run_number=int(self.ui.lineEdit_simNo.text())
        self.load3testcustomertype()
        self.model_param = {
            "height": height,
            "width": width,
            "num_customer": int(self.ui.lineEdit_customerNo.text()),
            "num_seller": int(self.ui.lineEdit_sellerNo.text()),
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
                self.ui.listWidget_sellerpreferencelist.addItem(
                    self.ListManagedialog.list.item(index).text())
            self.ui.listWidget_sellerpreferencelist.openPersistentEditor(
                self.ui.listWidget_sellerpreferencelist.item(0))
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
        with open("customertypes\\customer_type_"+type_name+'.txt', 'wb') as file1:
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
        with open("customertypes/customer_type_customerpoor.txt", 'rb') as filehandler:
            self.customerTypes["customerpoor"]=pickle.load(filehandler)
        with open("customertypes/customer_type_customerrich.txt", 'rb') as filehandler:
            self.customerTypes["customerrrich"]=pickle.load(filehandler)
        with open("customertypes/customer_type_customernormal.txt", 'rb') as filehandler:
            self.customerTypes["customernormal"]=pickle.load(filehandler)
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


if __name__ == "__main__":
    sim = Run_handler()


# server = ModularServer(Market, [canvas,chart_count], name="Market simulation")
# server.launch()
