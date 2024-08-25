from tkinter import *

master=Tk()

listbox=Listbox(master)
listbox.pack()

def my_mainloop():
    print("Hello World")
    listbox.insert(END, "Hello World")
    master.after(1000, my_mainloop)

master.after(1000, my_mainloop)
master.mainloop()