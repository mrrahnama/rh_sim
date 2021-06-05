import csv

from PyQt5.QtWidgets import *
from PyQt5 import QtGui, QtCore
import sys
class ListManage(QDialog):
    def __init__(self,name,proList = None,parent_listwidget=None):
        super(ListManage,self).__init__()
        self.name = name
        self.list = QListWidget()
        self.list.setDragEnabled(True)
        self.list.setDragDropOverwriteMode(False)
        self.list.setDragDropMode(QAbstractItemView.InternalMove)
        self.list.setDefaultDropAction(QtCore.Qt.MoveAction)
        if  parent_listwidget:
            for index in range(parent_listwidget.count()):
                m=QListWidgetItem(parent_listwidget.item(index).text())
                m.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
                self.list.addItem(m)
        if proList is not None:
            self.list.addItems(proList)
            self.list.setCurrentRow(0)

        vbox = QVBoxLayout()

        for text, slot in (("Add", self.add),
                           ("load", self.loadfile),
                           ("Remove", self.remove),
                           ("Apply", self.close)):
            button= QPushButton(text)
            vbox.addWidget(button)
            button.clicked.connect(slot)
        hbox = QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.setWindowTitle("Edit {0}  List".format(self.name))

        self.setWindowIcon(QtGui.QIcon("icon.png"))
        # self.show()
    def loadfile(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = QFileDialog.getOpenFileName(
            self, "select proper file ")

        if isinstance(fileName, tuple):
            fileName = fileName[0]
        else:
            fileName = str(fileName)
        print(fileName)
        if fileName:
            with open(fileName, newline='', encoding='utf-8') as f:
                self.list.clear()
                self.list.setDragEnabled(True)
                self.list.setDragDropOverwriteMode(False)
                self.list.setDragDropMode(QAbstractItemView.InternalMove)
                self.list.setDefaultDropAction(QtCore.Qt.MoveAction)
                infile = csv.reader(f)
                for row in infile:
                    m = QListWidgetItem(row[0])
                    m.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
                    self.list.addItem(m)
                    #self.tree.show()

    def add(self):
        row = self.list.currentRow()
        title = "Add {0}".format(self.name)
        string, ok = QInputDialog.getText(self, title, title)
        if ok and string is not None:
            self.list.insertItem(row, string)


    def edit(self):
        row = self.list.currentRow()
        item = self.list.item(row)
        if item is not None:
            title = "Edit {0}".format(self.name)
            string, ok = QInputDialog.getText(self, title, title,
                    QLineEdit.Normal, item.text())
            if ok and string is not None:
                item.setText(string)


    def remove(self):
        row = self.list.currentRow()
        item = self.list.item(row)
        if item is None:
            return
        reply = QMessageBox.question(self, "Remove {0}".format(
                self.name), "Remove {0} `{1}'?".format(
                self.name, str(item.text())),
                QMessageBox.Yes|QMessageBox.No)
        if reply == QMessageBox.Yes:
            item = self.list.takeItem(row)
            del item

    def sort(self):
        self.list.sortItems()


    def close(self):
        self.accept()






if __name__ == "__main__":

    programming = ["Python", "Java", "C#", "C++", "Ruby", "Kotlin"]

    app= QApplication(sys.argv)
    dialog = ListManage("Languages", programming)
    dialog.exec_()