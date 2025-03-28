from tkinter import *
import time

master=Tk()

listbox=Listbox(master)
listbox.pack()

def my_mainloop1():
    s1=time.asctime()
    print("Hello World")
    listbox.insert(END, "Hello"+s1)
    master.after(1000, my_mainloop1)

def my_mainloop2():
    s2=time.asctime()
    print("Esen")
    listbox.insert(END, "Esen"+s2)
    master.after(1000,my_mainloop2)

master.after(1000, my_mainloop1)
master.after(1000, my_mainloop2)
master.mainloop()