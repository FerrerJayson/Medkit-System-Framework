import tkinter as tk
import time
from pySerialTransfer import pySerialTransfer as txfer
from pygame import mixer

link = txfer.SerialTransfer('COM6', 9600) #chang port number accordingly
link.open()
name_entry_flag = 0
pin_entry_flag = 0
login = ""
pin = ""

def play(name):
    sfx= mixer.Sound(f"./audios/{name}.wav")
    sfx.play()

class StartPage(tk.Frame):

    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        btn_bg= tk.PhotoImage(file="btn_lg.png")
        self.btn_bg= btn_bg   
        btn_bg3= tk.PhotoImage(file="fing.png")
        self.btn_bg3= btn_bg3
        name_var=tk.StringVar()
        passw_var=tk.StringVar()
        wrgloh=tk.Label(self,text="Wrong Username or Password",font=('Helvetica', 40),bg="white",fg="#D9D9D9",borderwidth=0)
        def login():
            global login
            global pas
            name=name_var.get()
            pas=passw_var.get()
            usrnentry.delete(0, tk.END)
            passnentry.delete(0, tk.END)
            if name == login and pas == pas:
                controller.show_frame("PageOne")
                play('entersucess')
            else:
                wrgloh.place(x=300,y=310)
                play('wrongme')
        def printme():
            send_size = 0
            send_size = link.tx_obj(6)
            link.send(send_size)
            time.sleep(2)
            send_size = 0
            send_size = link.tx_obj(1)
            link.send(send_size)
            time.sleep(1)
            send_size = 0
            send_size = link.tx_obj(7)
            link.send(send_size)
            controller.show_frame("PageOne")

        def enter(event):
            global login
            global pas
            name=name_var.get()
            pas=passw_var.get()
            usrnentry.delete(0, tk.END)
            passnentry.delete(0, tk.END)
            if name == login and pas == pas:
                controller.show_frame("PageOne")
                play('entersucess')
            else:
                wrgloh.place(x=300,y=310)    
                play('wrongme')

        login=tk.Button(self,height=60,width=529,font=('Helvetica', 40),text="LOG IN  >",fg="white",bg="white",borderwidth=0,image=btn_bg, command=login )
        login.place(x=200,y=580)
        login2=tk.Button(self,height=127,width=380,font=('Helvetica', 40),text="LOG IN  >",fg="white",bg="white",borderwidth=0,image=btn_bg3, command=printme )
        login2.place(x=800,y=450)
        owimg= tk.PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=170,y=54)

        ntimg= tk.PhotoImage(file="next.png")
        self.ntimg=ntimg
        ntpanel=tk.Label(self,image=ntimg,borderwidth=0)
        ntpanel.place(x=170,y=245)
        
        dtrimg= tk.PhotoImage(file="doctors.png")
        self.dtrimg=dtrimg
        dtpanel=tk.Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=770,y=51)

        def usrclicked(event):
            global name_entry_flag
            if name_entry_flag != 1:
                usrnentry.delete(0, tk.END)
                usrnentry.config(fg="black")
                name_entry_flag = 1

        userimg= tk.PhotoImage(file="user.png")
        self.userimg=userimg
        usrpanel=tk.Label(self,image=userimg,borderwidth=0)
        usrpanel.place(x=200,y=360)
        usrnentry = tk.Entry(self,fg="#D9D9D9", bg="#F8F8F8",textvariable=name_var, width=30,borderwidth=0,font=('Helvetica', 20))
        usrnentry.insert(0, "  Username")
        usrnentry.bind("<1>", usrclicked)
        usrnentry.place( x=280,y=370)

        def passclicked(event):
            global pin_entry_flag
            if pin_entry_flag != 1:
                passnentry.delete(0, tk.END)
                passnentry.config(fg="black")
                pin_entry_flag = 1   


        passimg= tk.PhotoImage(file="pass.png")
        self.passimg=passimg
        passpanel=tk.Label(self,image=passimg,borderwidth=0)
        passpanel.place(x=200,y=440)
        passnentry = tk.Entry(self,fg="#D9D9D9", bg="#F8F8F8", width=30,textvariable=passw_var,borderwidth=0,font=('Helvetica', 20),show="*")
        passnentry.insert(0, "  Password")
        passnentry.bind("<1>", passclicked)
        passnentry.place( x=280,y=450)
    def on_show_frame(self, event):
        send_size = 0
        list_size = link.tx_obj(3)
        send_size += list_size
        link.send(send_size)