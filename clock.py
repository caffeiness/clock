from tkinter import *
from time import strftime

root=Tk()
root.title("時計")

def time():
    clock=strftime("%H:%M:%S %p")
    label.config(text=clock)
    label.after(1000,time)

label = Label(root,font=("Impact",80,"bold"),bg="black",fg="blue")
label.pack(anchor="center")

time()

root.mainloop()