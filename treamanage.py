from PyQt5.QtWidgets import QDialog, QListWidget,QTreeWidgetItem,QTreeWidget,QLineEdit ,QWidget, QMessageBox , QVBoxLayout,QPushButton, QHBoxLayout, QApplication,QInputDialog
from PyQt5 import QtGui,QtCore
import sys
# class myInputDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
        
#         self.first = QLineEdit(self)
#         self.second = QLineEdit(self)
#         buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

#         layout = QFormLayout(self)
#         layout.addRow("First text", self.first)
#         layout.addRow("Second text", self.second)
#         layout.addWidget(buttonBox)

#         buttonBox.accepted.connect(self.accept)
        # buttonBox.rejected.connect(self.reject)

    # def getInputs(self):
    #     return [self.first.text(), self.second.text()]
class TreeManage(QDialog):
    def __init__(self,name,proList = None,parent_treewidget=None):
        super(TreeManage,self).__init__()
        self.name = name
        # inputdialog=InputDialog(self)
        # self.list = QListWidget()
        self.tree = QTreeWidget()
        self.tree.setSortingEnabled(True)
        self.tree.setColumnCount(2)
        self.tree.setHeaderLabels(["name","max_budget"])
        # self.tree.itemAt()
        if   parent_treewidget:
            for index in range(parent_treewidget.topLevelItemCount()):
                m=parent_treewidget.topLevelItem(index).clone()
                # print(m.text(0))
                m.setFlags(QtCore.Qt.ItemIsSelectable  | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsEditable)
                self.tree.insertTopLevelItem(index,m)
            # print(self.tree.topLevelItemCount())
        # if proList is not None:
        #     self.list.addItems(proList)
        #     self.list.setCurrentRow(0)
        # self.tree=parent_treewidget
        vbox = QVBoxLayout()

        for text, slot in (("Add", self.add),

                        #    ("Edit", self.edit),
                           ("Remove", self.remove),
                        #    ("Sort", self.sort),
                           ("Apply", self.close)):
            button= QPushButton(text)
            vbox.addWidget(button)
            button.clicked.connect(slot)
        hbox = QHBoxLayout()
        hbox.addWidget(self.tree)
        hbox.addLayout(vbox)
        self.setLayout(hbox)
        self.setWindowTitle("Edit {0}  List".format(self.name))
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        # self.show()

    def add(self):
        row = self.tree.topLevelItemCount()
        title = "Add {0}".format(self.name)
        string, ok = QInputDialog.getText(self,title,title)
        if ok and string is not None:
            self.tree.insertTopLevelItem(row,QTreeWidgetItem(string.split()))


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
        root =self.tree.invisibleRootItem()
        for item in self.tree.selectedItems():
            reply = QMessageBox.question(self, "Remove {0}".format(
                    self.name), "Remove {0} `{1}'?".format(
                    self.name, str(item.text(0))),
                    QMessageBox.Yes|QMessageBox.No)
            if reply == QMessageBox.Yes:
                (item.parent() or root).removeChild(item)
                # item = self.list.takeItem(row)
                del item
        # row = self.list.currentRow()
        # item = self.list.item(row)
        # if item is None:
            # return

    def sort(self):
        pass

    def close(self):
        self.accept()






if __name__ == "__main__":

    # programming = ["Python", "Java", "C#", "C++", "Ruby", "Kotlin"]

    app= QApplication(sys.argv)
    l1 = QTreeWidgetItem(["String A", "String B"])
    l2 = QTreeWidgetItem(["String AA", "String BB"])

    # w = QWidget()
    # w.resize(510, 210)

    tw = QTreeWidget()
    tw.resize(500, 200)
    tw.setColumnCount(2)
    tw.setHeaderLabels(["product name ", "max budget"])
    tw.addTopLevelItem(l1)
    tw.addTopLevelItem(l2)
    if tw.topLevelItem(0)== l1:
        print(l1)
    print(l2.text(1))
    # l1.text()
    dialog = TreeManage("products",None,tw)

    print(dialog.tree.topLevelItemCount())
    dialog.show()
    # w.show()

    sys.exit(app.exec_())