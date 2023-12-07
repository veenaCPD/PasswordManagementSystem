#importing Libraries

from tkinter import *
import random, string
import pyperclip
import sqlite3
from tkinter import ttk
from PIL import ImageTk, Image  

credname_g = ""
url_g = ""
username_g = ""
password_g = ""

# Create Database
def create_db():
    # create connection to database 
    sqliteConnection = sqlite3.connect('password_db.db') 
    
    # Drop table, if exists
    sqliteConnection.execute('''DROP TABLE IF EXISTS password_tbl;''')
    
    # Create a table
    sqliteConnection.execute('''CREATE TABLE password_tbl(CredName TEXT NOT NULL,Url TEXT,UserName YEXT NOT NULL, Password TEXT NOT NULL);''')
    sqliteConnection.close()
    
# To generate password
def generatePwd():
    password = ''
    
    for y in range(pass_len.get()):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    password_str.set(password)
    
# Copy password on Clipboard    
def Copy_password():
    pyperclip.copy(password_str.get()) 

# Restrieve data from DB
def get_db():   
    credname_g = credname_str.get()
    url_g = url_str.get()
    username_g = username_str.get()
    
    # create connection to database 
    sqliteConnection = sqlite3.connect('password_db.db')  
    
    query = "SELECT CredName, Url, UserName, Password from password_tbl where " 
    param = ""
    
    if credname_g !="":
        param = "CredName like '%" + credname_g + "%' OR "
        query = query + param
        
    if url_g !="":
        param = "Url like '%" + url_g + "%' OR "
        query = query + param
        
    if username_g !="":
        param = "UserName like '%" + username_g + "%'"
        query = query + param
        
    length = len(query)
    temp = query[length-3:]
    if temp=="OR ":
        query = query[:length-3]
        
    temp = query[length-6:]
    if temp=="where ":
        query = query[:length-6]
    
    cursor = sqliteConnection.execute(query)
 
    # display all data from FOOD1 table
    for row in cursor:
        print(row)     
    sqliteConnection.close()

# To save data in DataBase
def save_db():
    # create connection to database 
    sqliteConnection = sqlite3.connect('password_db.db')  
    
    # Collect data
    credname_g = credname_str.get()
    url_g = url_str.get()
    username_g = username_str.get()
    password_g = password_str.get()    
    
    sqlite_insert_with_param = """INSERT INTO password_tbl (CredName, Url, UserName, Password ) VALUES(?,?,?,?);"""
    data_tuple = (credname_g, url_g, username_g, password_g)
    sqliteConnection.execute(sqlite_insert_with_param, data_tuple)
    
    sqliteConnection.commit()    
    sqliteConnection.close()  
    
    
    
###initialize window
root =Tk()

root.geometry("700x600")
root.resizable(0,0)
root.title("Rani Software Technologies - Password Management System")

# Credential Name
credname_lbl = Label(root, text = 'Credential Name', font = 'arial 10 bold')
credname_lbl.place(x=10, y=40)

credname_str = StringVar()
credname_entry = Entry(root , textvariable = credname_str, width = 35)  
credname_entry.place(x=130, y=40)

# Url
url_lbl = Label(root, text = 'Url', font = 'arial 10 bold')
url_lbl.place(x=365, y=40)

url_str = StringVar()
url_entry = Entry(root , textvariable = url_str, width = 35)  
url_entry.place(x=440, y=40) 

# Username
username_lbl = Label(root, text = 'Username', font = 'arial 10 bold')
username_lbl.place(x=10, y=80) 

username_str = StringVar()
username_entry = Entry(root , textvariable = username_str, width = 35) 
username_entry.place(x=130, y=80) 

# Password
password_lbl = Label(root, text = 'Password', font = 'arial 10 bold')
password_lbl.place(x=365, y=80)

password_str = StringVar()
password_entry = Entry(root , textvariable = password_str, width = 35)
password_entry.place(x=440, y=80)

# Select password length
pass_label = Label(root, text = 'Password Length', font = 'arial 10 bold')
pass_len = IntVar()
pass_label.place(x=10, y=120) 

length_box = Spinbox(root, from_ = 8, to_ = 20 , textvariable = pass_len , width = 34)
length_box.place(x=130, y=120) 

# Copy to clipboard button
copy_button = Button(root, text = 'Copy to clipboard', bg="PaleTurquoise",fg="black", command = Copy_password, font = 'arial 10 bold') 
copy_button.place(x=150, y=160)

# Generate Password button
generatePwd_button = Button(root, text = "Generate Password" , bg="PaleTurquoise",fg="black",command = generatePwd, font = 'arial 10 bold' )
generatePwd_button.place(x=450, y=160) 

# Create DataBase button
generatePwd_button = Button(root, text = "Create Database" , bg="tomato",fg="black",command = create_db, font = 'arial 10 bold' )
generatePwd_button.place(x=300, y=200)

# Save to DB button
saveDb_button = Button(root, text = 'Save to DataBase', bg="wheat", fg="black", command = save_db, font = 'arial 10 bold')   
saveDb_button.place(x=150, y=240)

# Get information from DB button
getDb_button = Button(root, text = 'Get info from DataBase', bg="wheat", fg="black", command = get_db, font = 'arial 10 bold')   
getDb_button.place(x=450, y=240)

# Display Lock image
frame = Frame(root, width=600, height=100)
frame.place(x=0, y=100,anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("Lock.jpeg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

# loop to run program
root.mainloop()      
