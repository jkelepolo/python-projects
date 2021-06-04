# Jothan Kelepolo
# 021
# 12-9-2020

from UI import *
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets

def customer_submit():
    
 
    
    if ui.firstNameText.toPlainText() == "" or ui.lastNameText.toPlainText() == "" or ui.addressText.toPlainText() == "" or ui.cityText.toPlainText() == "" or ui.stateText.toPlainText() == "" or ui.zipText.toPlainText() == "" or ui.phoneText.toPlainText() == "" or ui.emailText.toPlainText() == "" :
        ui.statusLabel.setText("One or more fields are empty!")
        return
    
    # Create database or connect to one
    conn = sqlite3.connect("DGS_DATA.db")
    
    # Create cursor
    c = conn.cursor()
    
    # Create table
    try:
        c.execute("""CREATE TABLE customers (
                  name text,
                  address text,
                  city text,
                  state text,
                  zip integer,
                  phone text,
                  email text,
                  customer_id integer
                  )
                  """)
        print("Creating Database")
    except:
        print("Adding to Database")
    
    c.execute("SELECT *, oid FROM customers")
    records = c.fetchall()

    ID = 0
    
    for record in records:
        # print(record)
        if str(record[7]) == str(ID):
            ID += 1
    
    # Insert Into Table
    c.execute("INSERT INTO customers VALUES (:name, :address, :city, :state, :zip, :phone, :email, :customer_id) ",
              
              {
                  "name": ui.firstNameText.toPlainText() + " " + ui.lastNameText.toPlainText(),
                  "customer_id": ID,
                  "address": ui.addressText.toPlainText(),
                  "city": ui.cityText.toPlainText(),
                  "state": ui.stateText.toPlainText(),
                  "zip": ui.zipText.toPlainText(),
                  "phone": ui.phoneText.toPlainText(),
                  "email": ui.emailText.toPlainText(),
                  
                  } )
    
    
    # Commit Changes
    conn.commit()
    
    # Close Connection
    conn.close()
    
    
    ui.statusLabel.setText("Added new customer " + ui.firstNameText.toPlainText() + " " + ui.lastNameText.toPlainText() + " with id " + str(ID) + "!")
    



def query():
    # Create database or connect to one
    conn = sqlite3.connect("DGS_DATA.db")
    
    # Create cursor
    c = conn.cursor()
    
    
    # Query the database
    c.execute("SELECT *, oid FROM customers")
    records = c.fetchall()
    
    ui.ListWidget.clear()
    
    ui.statusLabel2.setText("Failed to retrieve data for customer ID: " + ui.customerByIDText.toPlainText() )

    for index, record in enumerate(records):
        if ui.customerByIDText.toPlainText() == "":
            pass
        elif str(record[7]) == ui.customerByIDText.toPlainText():
            # ui.ListWidget.addItem(str(record))
            
            ui.ListWidget.addItem("________________")
            ui.ListWidget.addItem("Name: "+record[0])
            ui.ListWidget.addItem("Address: "+record[1])
            ui.ListWidget.addItem("City: "+record[2])
            ui.ListWidget.addItem("State: "+record[3])
            ui.ListWidget.addItem("ZIP: "+record[4])
            ui.ListWidget.addItem("Phone: "+record[5])
            ui.ListWidget.addItem("Email: "+record[6])
            ui.ListWidget.addItem("Customer ID: "+str(record[7]))
            
            
            ui.statusLabel2.setText("Retrieved customer data \nCheck output tab")
    

    
    
    
    # Commit Changes
    conn.commit()
    
    # Close Connection
    conn.close()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)    
    
    # Connections
    ui.addCustomerBtn.pressed.connect(customer_submit)
    ui.retrieveDataBtn.pressed.connect(query)
    

    
    
    MainWindow.show()
    sys.exit(app.exec_())
    


