from tkinter import *
import speedtest

sp = Tk()
sp.title("Internet Speed Test") 
sp.geometry("300x500")
sp.config(bg = "Blue")

lab = Label(sp,text="Internet Speed Test",bg="Blue",fg="White",font=("Arial",20,"bold"))
lab.place(x=40, y= 40)
sp.mainloop()
