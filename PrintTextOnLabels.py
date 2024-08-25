from tkinter import *
import time

root=Tk() 
root.wm_title("TEXTS") 
root.config(background = "#FFFFFF")
root.geometry("1400x600")

leftFrame=Frame(root, width=900, height = 600, background="Yellow")
leftFrame.grid(row=0, column=0)

rightFrame=Frame(root, width=500, height = 600, background="Yellow")
rightFrame.grid(row=0, column=1)

text1=Label(rightFrame, text="READ TEXTS", font=('times', 20, 'bold'))
text1.config(bg='yellow', fg='black')
text1.grid(row=0, column=0, padx=2, pady=2)

text2=Label(rightFrame, text="SAVED TEXTS", font=('times', 20, 'bold'))
text2.config(bg='yellow', fg='black')
text2.grid(row=2, column=0, padx=2, pady=2)

colorLog=Text(rightFrame, width = 37, height = 10, takefocus=0, font=('times', 18))
colorLog.grid(row=1, column=0, padx=10, pady=10)

colorLog2=Text(rightFrame, width = 37, height= 5, takefocus=0, font=('times', 18))
colorLog2.grid(row=3, column=0, padx=10, pady=10)

def my_mainloop():
    s1=time.asctime()
    print("Text")
    colorLog.insert(0.0, "Text "+s1+"\n")
    root.after(1000, my_mainloop)

root.after(1000, my_mainloop)
root.mainloop() 