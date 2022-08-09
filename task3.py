from tkinter import *
from tkinter import messagebox
import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1",
                                    database="tkinterdata",
                                    user="vadim",
                                    password="vadim")
root = Tk()


Fr_lab = Label(text="Please print id:")
Fr_lab.pack()

cursor=connection.cursor()
def display_on():
    cursor.execute("SELECT * from customers")
    messagebox.showinfo('',cursor.fetchall())

def input():

  Last_but = Frame()
  Last_but.pack()

  button = Button(text="Show", master=Last_but,  command=display_on)
  button.pack()

  mainloop()
  cursor.close()

input()
