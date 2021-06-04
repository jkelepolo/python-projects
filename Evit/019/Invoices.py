# Jothan Kelepolo
# 019.1
# 11/3/2020



from tkinter import *
import sqlite3

root = Tk()
root.title("Invoice")
root.geometry("450x450")
# root.iconbitmap("")



# List
scrollbar = Scrollbar(root)
scrollbar.grid( row=12,column=1,sticky="E")

mylist = Listbox(root, yscrollcommand = scrollbar.set )

mylist.grid(row=12,column=0,columnspan=2, ipadx=110 )
scrollbar.config( command = mylist.yview )

#Quit
def Quit():
    root.destroy()

# Create Function to Delete A Record
def delete_oid():
        # Create database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    # Create cursor
    c = conn.cursor()
    
    
    # Delete a record
    c.execute("DELETE from addresses WHERE oid ="+ delete_box.get())
    
    
    # Commit Changes
    conn.commit()
    
    # Close Connection
    conn.close()
    
    delete_box.delete(0,END)
    query()


# Create Function to Delete A Record
def delete_cid():
        # Create database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    # Create cursor
    c = conn.cursor()
    
    
    # Delete a record
    c.execute("DELETE from addresses WHERE customer_id ="+ delete_box.get())
    
    
    # Commit Changes
    conn.commit()
    
    # Close Connection
    conn.close()
    
    delete_box.delete(0,END)
    query()
    

# Create Submit Function for database
def submit():
    
    if customer_id.get() == "" or name.get() == "" or invoice_date.get()=="" or invoice_amount.get() == "":
        mylist.delete(0,END)
        mylist.insert(END, "One or more fields are empty!")
        return
    
    # Create database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    # Create cursor
    c = conn.cursor()
    
    # Create table
    try:
        c.execute("""CREATE TABLE addresses (
                  name text,
                  customer_id integer,
                  invoice_number integer,
                  invoice_date text,
                  invoice_amount real
                  )
                  """)
        print("Creating Database")
    except:
        print("Adding to Database")
    
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    invoices = 0
    
    for record in records:
        if str(record[1]) == str(customer_id.get()):
            if record[2] > invoices:
                invoices = record[2]
    
    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:name, :customer_id, :invoice_number, :invoice_date, :invoice_amount) ",
              
              {
                  "name": name.get(),
                  "customer_id": customer_id.get(),
                  "invoice_number": invoices+1,
                  "invoice_date": invoice_date.get(),
                  "invoice_amount": invoice_amount.get()
                  
                  } )
    
    
    # Commit Changes
    conn.commit()
    
    # Close Connection
    conn.close()
    
    
     
     
    
    # Clear the Text Boxes
    # name.delete(0,END)
    # customer_id.delete(0,END)
    # invoice_number.delete(0,END)
    # invoice_date.delete(0,END)
    # invoice_amount.delete(0,END)
    
    query()

    
def query():
    global mylist
    # Create database or connect to one
    conn = sqlite3.connect("address_book.db")
    
    # Create cursor
    c = conn.cursor()
    
    
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()
    
    mylist.delete(0,END)
    
    unique_customers = []
    
    # Display all current customers and their CID's
    if delete_box.get() == "":
        for record in records:
            if record[1] not in unique_customers:
                mylist.insert(END, str(record[0]) + " CID:" + str(record[1]))
                unique_customers.append(record[1])
    else:
        
        # Display all records under CID
        for record in records:
            if str(record[1]) == str(delete_box.get()):
                mylist.insert(END,"------------------------------------------" )
                mylist.insert(END, str(record[0]))
                mylist.insert(END, "Item ID: "+str(record[5]))
                mylist.insert(END, "Invoice Number: "+str(record[2]))
                mylist.insert(END, "Date: "+str(record[3]))
                mylist.insert(END, "Amount Owed: "+str(record[4]))



    # Commit Changes
    conn.commit()
    
    # Close Connection
    conn.close()
    
    
# Create edit boxes
name = Entry(root,width=30)
name.grid(row=0, column=1, padx=20)
customer_id = Entry(root,width=30)
customer_id.grid(row=1, column=1, padx=20)
invoice_date = Entry(root,width=30)
invoice_date.grid(row=3, column=1, padx=20)
invoice_amount = Entry(root,width=30)
invoice_amount.grid(row=4, column=1, padx=20)


delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1)

# Create labels
name_label = Label(root, text="Customer Name")
name_label.grid(row=0, column=0)
customer_id_label = Label(root, text="Customer ID")
customer_id_label.grid(row=1, column=0)
invoice_date_label = Label(root, text="MM/DD/YY")
invoice_date_label.grid(row=3, column=0)
invoice_amount_label = Label(root, text="Amount Total")
invoice_amount_label.grid(row=4, column=0)


delete_label = Label(root, text="ID Number")
delete_label.grid(row=9, column=0)

# Create Submit Button
submit_btn = Button(root, text="Add Record To Database", command=submit)
submit_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=96)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=116)

# Create a delete button
delete_btn = Button(root, text="Delete CID Records", command=delete_cid)
delete_btn.grid(row=10,column=0,columnspan=2,pady=10,padx=10,ipadx=110)

# Create a delete button
delete_OID_btn = Button(root, text="Delete Item ID", command=delete_oid)
delete_OID_btn.grid(row=11,column=0,columnspan=2,pady=10,padx=10,ipadx=122)

# Quit Button
quit_btn = Button(root, text="Quit", command=Quit)
quit_btn.grid(row=13,column=0,columnspan=2,pady=10,padx=10,ipadx=136)


while True:
    
    
    if delete_box.get() == "":
        query_btn['text'] = "Show ALL Records"
    else:
        query_btn['text'] = "Show CID Records"
    
    

    root.update_idletasks()
    root.update()
root.mainloop()