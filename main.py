import PIL

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap,QFont
import sys, os
import sqlite3
from PIL import Image

conn = sqlite3.connect('employees.db') #creates db when first run if one does not exist
cur = conn.cursor()

defaultImg = "person.png"
def create_table():
    cur.execute()


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Employees")
        self.setGeometry(450,150,750,600)
        self.UI()
        self.show()
    
    def UI(self):
        self.mainDesign()
        self.layouts()
        self.getEmployees()
    
    def mainDesign(self):
        self.employeeList = QListWidget()
        self.btnNew = QPushButton("New")
        self.btnNew.clicked.connect(self.addEmployee)
        
        self.btnUpdate = QPushButton("Update")
        self.btnDelete = QPushButton("Delete")
    
    def layouts(self):
        #################Layouts##########################
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        ##################Adding child layouts to main layout############
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        self.mainLayout.addLayout(self.leftLayout,40) #using numbers allows for us to to set how much of the window we want our layout to take up. 
        self.mainLayout.addLayout(self.rightMainLayout,60)
        ##################adding widgets to layouts####################
        self.rightTopLayout.addWidget(self.employeeList)
        self.rightBottomLayout.addWidget(self.btnNew)
        self.rightBottomLayout.addWidget(self.btnUpdate)
        self.rightBottomLayout.addWidget(self.btnDelete)
        ##################setting main window layout##################
        self.setLayout(self.mainLayout)
    
    def addEmployee(self):
        self.newEmployee = AddEmployee()
        self.close()
    
    def getEmployees(self):
        query="SELECT id,name,surname FROM employees"
        employees=cur.execute(query).fetchall()
        for employee in employees:
            self.employeeList.addItem(str(employee[0]) + "-" + employee[1] + " " + employee[2])

class AddEmployee(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Employees")
        self.setGeometry(450,150,350,600)
        self.UI()
        self.show()
        
    def UI(self):
        self.mainDesign()
        self.layouts()
    
    def closeEvent(self,event):
        self.main = Main()
        

    def mainDesign(self):
        #######################top layout widgets##############################
        self.setStyleSheet("background-color:white;font-size:14pt;font-family:Times")
        self.title = QLabel("Add Person")
        self.title.setStyleSheet('font-size: 24pt;font-family:Arial Bold')
        self.imgAdd = QLabel()
        self.imgAdd.setPixmap(QPixmap("icons/person.png"))
        
        ########################bottom layout widgets###########################
        self.nameLbl = QLabel("Name :")
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter Employee Name")
        
        self.surnameLbl = QLabel("Surname :")
        self.surnameEntry = QLineEdit()
        self.surnameEntry.setPlaceholderText("Enter Employee Surname")
        
        self.phoneLbl = QLabel("Phone :")
        self.phoneEntry = QLineEdit()
        self.phoneEntry.setPlaceholderText("Enter Employee Phone Number")
        
        self.emailLbl = QLabel("Email :")
        self.emailEntry = QLineEdit()
        self.emailEntry.setPlaceholderText("Enter Employee Email")
        
        self.imgLbl = QLabel("Picture :")
        self.imgButton = QPushButton("Browse")
        self.imgButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.imgButton.clicked.connect(self.uploadImage)
        
        self.addressLbl = QLabel("Address :")
        self.addressEditor=QTextEdit()
        self.addButton = QPushButton("Add")
        self.addButton.setStyleSheet("background-color:orange;font-size:10pt")
        self.addButton.clicked.connect(self.addEmployee)
    
    def layouts(self):
        ##########################creating main layouts############################
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        
        ###########################adding child layouts to main layout##############
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        
        ############################adding widgets to layouts#######################
                #########top layout################
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.imgAdd)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110,20,10,30)
                ##########bottom layout############
        self.bottomLayout.addRow(self.nameLbl,self.nameEntry)
        self.bottomLayout.addRow(self.surnameLbl,self.surnameEntry)
        self.bottomLayout.addRow(self.phoneLbl, self.phoneEntry)
        self.bottomLayout.addRow(self.emailLbl, self.emailEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgButton)
        self.bottomLayout.addRow(self.addressLbl, self.addressEditor)
        self.bottomLayout.addRow("",self.addButton)
        
        ############################setting main layout for window##################
        self.setLayout(self.mainLayout)
    
    def uploadImage(self):
        global defaultImg
        size = (128,128)
        self.filename,ok = QFileDialog.getOpenFileName(self,'Upload Image','','image Files (*.jpg *.png)')
        
        if ok:
            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("images/{}".format(defaultImg))
    
    def addEmployee(self):
        global defaultImg
        name = self.nameEntry.text()
        surname = self.surnameEntry.text()
        phone = self.phoneEntry.text()
        email = self.emailEntry.text()
        img = defaultImg
        address = self.addressEditor.toPlainText()
        
        if (name and surname and phone !=""):
            try:
                query = "INSERT INTO employees (name,surname,phone,email,img,address) VALUES(?,?,?,?,?,?)"
                cur.execute(query,(name,surname,phone,email,img,address))
                con.commit()
                QMessageBox.information(self,"Success","Person has been added")
                self.close()
                self.main = Main()
            
            except:
                QMessageBox.information(self, "Warning", "Person has not been added")
        
        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")
        
        


def main():
    APP = QApplication(sys.argv)
    window=Main()
    sys.exit(APP.exec_())

if __name__ == '__main__':
    main()