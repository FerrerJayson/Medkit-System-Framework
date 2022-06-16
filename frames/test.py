#Import the Tkinter library
from tkinter import *
#Create an instance of Tkinter frame
win= Tk()
#Define the geometry
win.geometry("750x250")
#Define Event handlers for different Operations
def event_show(event):
   label.config(text="Hello World")
   e.focus_set()
   print("focus is:" ,e.focus_get)
#Create a Label
label= Label(win, text="Press Enter",font=('Helvetica 15 underline'))
label.pack()
#Create an entry widget
e= Entry(win, width= 25)
e.pack(pady=20)
#Bind the function
win.bind('<Return>',lambda event:event_show(event))
win.mainloop()