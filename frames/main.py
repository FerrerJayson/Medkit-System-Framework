import tkinter as tk
from registration import NamePage, PinPage, PinConfirmPage
from mainscreen import ActiveScreen, HomePage
from login import StartPage
from pySerialTransfer import pySerialTransfer as txfer

link = txfer.SerialTransfer('COM3', 9600) #chang port number accordingly
link.open()
send_size = 0
list_size = link.tx_obj(3)
send_size += list_size
link.send(send_size) #send Red led code
line=""
login="admin" #default login name
pin="1234"  #default pin
pas=""
flag3=0
flag4=0
flag5=0
flag6=0
flag7=0
flag8=0
flag9=0
medname="" #medicine name var
medname2=""
x=0
dosep=""
time1="" 
time2=""
time3="" 
time4=""
time5="" 

setpass = "1234"
setlog ="admin"

class MedkitUI(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry('1260x800')
        self.resizable(False, False)
        self.config(bg="white")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ActiveScreen, HomePage, StartPage, NamePage, PinPage, PinConfirmPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()



if __name__ == "__main__":
    app = MedkitUI()
    app.mainloop()