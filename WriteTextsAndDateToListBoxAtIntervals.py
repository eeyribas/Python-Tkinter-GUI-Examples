from tkinter import *
import time

master=Tk()

listbox=Listbox(master)
listbox.pack()

def my_mainloop():
    s1=time.asctime()
    print("Hello World")
    listbox.insert(END, "Hello"+s1)
    master.after(1000, my_mainloop)

def my_mainloop2():
    s2=time.asctime()
    print("Esen")
    listbox.insert(END, "Esen"+s2)
    master.after(1000,my_mainloop2)

master.after(1000, my_mainloop)
master.after(1000, my_mainloop2)
master.mainloop()