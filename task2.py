from tkinter import *
import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1",
                                    database="tkinterdata",
                                    user="vadim",
                                    password="vadim")
root = Tk()
Fr_lab = Label(text="Please print id:")
Fr_fra = Frame()
Fr_lab.pack()
Fr_fra.pack()

label_id = Label(text="Values id: ", master=Fr_fra)
entry_id = Entry(master=Fr_fra)

label_id.grid(row=1, column=0)
entry_id.grid(row=1, column=1)
cursor=connection.cursor()

def send_id():
    get_id = entry_id.get()
    cursor.execute("SELECT name, password, city FROM customers where id = '{}'"
    .format(get_id))

    finish_data.config(text="{}"
    .format(cursor.fetchall()))
     
finish_data = Label()
finish_data.pack()
entry_id.grid(row=1, column=1)

def input():
  Last_but = Frame()
  Last_but.pack()
  button = Button(text="Show", master=Last_but,  command=send_id)
  button.pack()

  mainloop()
  cursor.close()

input()