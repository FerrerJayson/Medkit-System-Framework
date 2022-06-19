import cmd
from pickle import TRUE
import tkinter as tk
from tkinter import Canvas, Image, Label, PhotoImage, StringVar, filedialog, Text,ttk,Frame,OptionMenu,Spinbox
import os
import signal
from tkinter.constants import COMMAND, END, X, Y
import tkinter.font as font             
from tkinter import font as tkfont
from tokenize import String
from turtle import delay
from unittest import case  
from tkcalendar import Calendar
import subprocess
import keyboard
import time
from pySerialTransfer import pySerialTransfer as txfer
from pygame import mixer
#Make sure to install necessary modules

link = txfer.SerialTransfer('COM16', 9600) #chang port number accordingly
link.open()
time.sleep(2)
send_size = 0
list_size = link.tx_obj(3)
send_size += list_size
link.send(send_size) #send Red led code
# send_size = 0
# list_size = link.tx_obj(7)
# send_size += list_size
# link.send(send_size)
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
flag0=0
medname="" #medicine name var
medname2=""
x=0
dosep=""
time1="" 
time2=""
time3="" 
time4=""
time5="" 
mixer.init()

entername = mixer.Sound("entername.wav")
enterpin= mixer.Sound("enterpin.wav")
entersucess = mixer.Sound("entersucess.wav")
wpin= mixer.Sound("wpin.wav")
wrongme= mixer.Sound("wrongme.wav")
alarm= mixer.Sound("alarm.wav")
entermed= mixer.Sound("entermed.wav")
enterdose= mixer.Sound("enterdose.wav")
seldate= mixer.Sound("seldate.wav")
placemed= mixer.Sound("placemed.wav")
setdone= mixer.Sound("setdone.wav")
#def refresh(self): # code to refresh each page
  #  self.destroy()
 #   self.__init__()
setpass = "1234"
setlog ="admin"
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        calibri = font.Font(family="Calibri",size=20,weight="bold")
        self.geometry('1260x800')
        #self.resizable(False, False)
        self.config(bg="white")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo,PageThree,PageFour,pilipage,namepage,pinpage,pincpage,pintrypage,tatspage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("pilipage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.event_generate("<<ShowFrame>>")
        frame.tkraise()


class pilipage(tk.Frame):

    
    def __init__(self, parent, controller):
    
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller

        btn_bg= PhotoImage(file="login.png")
        self.btn_bg= btn_bg   
        btn_bg3= PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        calibri = font.Font(family="Calibri",size=25,weight="bold")
    

        label1=Label(self,text="Or",font=calibri,bg="white",fg="gray",borderwidth=0)
        label1.place(x=600,y=530)
        
        
        owimg= PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        
        dtrimg= PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
    
        sel2=tk.Button(self,borderwidth=0,image=btn_bg3,command=lambda:controller.show_frame("namepage"))
        sel2.place(x=377 ,y=348)
        sel=tk.Button(self,borderwidth=0,image=btn_bg,command=lambda:controller.show_frame("StartPage"))
        sel.place(x=516 ,y=600)

class namepage(tk.Frame):

    
    def __init__(self, parent, controller):
    
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        name_var= tk.StringVar()
        btn_bg= PhotoImage(file="blank.png")
        self.btn_bg= btn_bg
        blank1=Label(self,image=btn_bg,borderwidth=0)   
        blank1.place(x=365,y=237)
        btn_bg3= PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        
        def usrclicked(event):
            def enter(event):
                global setlog
                setlog = name_var.get()
                print(setlog)
                controller.show_frame("pinpage")
            global flag0
            if flag0 != 1:
                usrnentry.delete(0, END)
                usrnentry.config(fg="black")
                entername.play()
                flag0 = 1
            
            subprocess.Popen("./On-ScreenKeyboardPortable/On-ScreenKeyboardPortable.exe")
            keyboard.on_press_key("ENTER", enter)

        calibri = font.Font(family="Calibri",size=40,weight="bold")
        usrnentry = tk.Entry(self,fg="black", bg="white",textvariable=name_var, width=18,borderwidth=0,font=calibri)
        usrnentry.insert(0, "    Enter your name")
        usrnentry.bind("<1>", usrclicked)
        usrnentry.place( x=375,y=250)
        
        
        owimg= PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        
        dtrimg= PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
    def on_show_frame(self, event):
        send_size = 0
        list_size = link.tx_obj(2)
        send_size += list_size
        link.send(send_size)

class pinpage(tk.Frame):

    
    def __init__(self, parent, controller):
    
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.bind("<<ShowFrame>>", self.on_show_frame)
        self.controller = controller
        name_var= tk.StringVar()
        btn_bg= PhotoImage(file="blank.png")
        self.btn_bg= btn_bg
        blank1=Label(self,image=btn_bg,borderwidth=0)   
        blank1.place(x=365,y=237)
        btn_bg3= PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        def usrclicked(event):
            def enter(event):
                global setpass
                setpass=name_var.get()
                controller.show_frame("pintrypage")
            global flag8
            if flag8 != 1:
                usrnentry.delete(0, END)
                usrnentry.config(fg="black")  

            subprocess.Popen("./On-ScreenKeyboardPortable/On-ScreenKeyboardPortable.exe")
            keyboard.on_press_key("Enter", enter)

        calibri = font.Font(family="Calibri",size=40,weight="bold")
        calibri1 = font.Font(family="Calibri",size=30,weight="bold")
        global dtpanel4
        dtpanel4=Label(self,text="Welcome "+login,fg="black", bg="white",borderwidth=0,font=calibri1)
        dtpanel4.place(x=460,y=155)
        usrnentry = tk.Entry(self,fg="black", bg="white",textvariable=name_var, width=18,borderwidth=0,font=calibri)
        usrnentry.insert(0, "           Enter pin")
        usrnentry.bind("<1>", usrclicked)
        usrnentry.place( x=375,y=250)
        
        
        owimg= PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        
        dtrimg= PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
    def on_show_frame(self, event):
            print ("Welcome " + login)
            dtpanel4.config(text="Welcome " + login)
            enterpin.play()
class pincpage(tk.Frame):

    
    def __init__(self, parent, controller):
    
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        name_var= tk.StringVar()
        btn_bg= PhotoImage(file="blank.png")
        self.btn_bg= btn_bg
        blank1=Label(self,image=btn_bg,borderwidth=0)   
        blank1.place(x=365,y=237)
        btn_bg3= PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        def usrclicked(event):
            global flag7
            if flag7 != 1:
                usrnentry.delete(0, END)
                usrnentry.config(fg="black")
                flag7 = 1   

            subprocess.Popen("D:\Work\medkit\med\On-ScreenKeyboardPortable.\On-ScreenKeyboardPortable.exe")
            keyboard.on_press_key("ENTER", lambda _:controller.show_frame("tatspage"))
        
        calibri = font.Font(family="Calibri",size=40,weight="bold")
        calibri1 = font.Font(family="Calibri",size=30,weight="bold")
        dtpanel1=Label(self,text="Welcome Admin",fg="black", bg="white",borderwidth=0,font=calibri1)
        dtpanel1.place(x=460,y=155)
        usrnentry = tk.Entry(self,fg="black", bg="white",textvariable=name_var, width=18,borderwidth=0,font=calibri)
        usrnentry.insert(0, "         Confirm pin")
        usrnentry.bind("<1>", usrclicked)
        usrnentry.place( x=375,y=250)
        
        
        owimg= PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        
        dtrimg= PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)

class pintrypage(tk.Frame):

    
    def __init__(self, parent, controller):
    
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        name_var= tk.StringVar()
        btn_bg= PhotoImage(file="blank.png")
        self.btn_bg= btn_bg
        blank1=Label(self,image=btn_bg,borderwidth=0)   
        btn_bg3= PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        calibri = font.Font(family="Calibri",size=40,weight="bold")
        calibri1 = font.Font(family="Calibri",size=30,weight="bold")
        global dtpanel1
        dtpanel1=Label(self,text="Welcome " + login,fg="black", bg="white",borderwidth=0,font=calibri1)
        def refresh():
            print ("Welcome " + login)
            dtpanel1.config(text="Welcome " + login)
        

        def usrclicked(event):
            global flag7
            #if flag7 != 1:
            usrnentry.delete(0, END)
            usrnentry.config(fg="black")
                #flag7 = 1   
            global pro
            pro=subprocess.Popen("D:\Work\medkit\med\On-ScreenKeyboardPortable.\On-ScreenKeyboardPortable.exe")
            keyboard.on_press_key("ENTER", enter)
            
        
        
        
        usrnentry = tk.Entry(self,fg="black", bg="white",textvariable=name_var, width=18,borderwidth=0,font=calibri)
        usrnentry.insert(0, "         Confirm pin")
        usrnentry.bind("<1>", usrclicked)
        global flag9
        if flag9 == 0:
            blank1.place(x=365,y=237)
            dtpanel1.place(x=460,y=155)
            usrnentry.place( x=375,y=250)
            flag9 = 1
        #arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)
        def enter(event):
            curpin=name_var.get()
            print(curpin)
            global pas
            print(pas)
            global pin
            if pas == curpin:
                pin = pas
                send_size = 0
                list_size = link.tx_obj(2)
                send_size += list_size
                link.send(send_size)
                global x
                if x==0:
                    arr= 0.0
                    id =0.0
                    dtpanel1.place_forget()
                    usrnentry.place_forget()
                    blank1.place_forget()
                    btn_bg= PhotoImage(file="fblu.png")
                    self.btn_bg= btn_bg
                    blank12=Label(self,image=btn_bg,borderwidth=0) 
                    blank12.place(x=500,y=260)
                    dtpanel31=Label(self,text="Now press and hold ",fg="gray", bg="white",borderwidth=0,font=calibri1)
                    dtpanel31.place(x=460,y=550)
                    dtpanel21=Label(self,text="the fingerprint button below",fg="gray", bg="white",borderwidth=0,font=calibri1)
                    dtpanel21.place(x=400,y=600)
                    send_size = 0
                    list_size = link.tx_obj(6)
                    send_size += list_size
                    link.send(send_size)
                    send_size = 0
                    list_size = link.tx_obj(8)
                    send_size += list_size
                    link.send(send_size)
                    while not link.available():rc=0
                    arr = link.rx_obj(obj_type='i')
                    print(arr)
                    while arr == 1093664768:
                        print("fail")
                        send_size = 0
                        list_size = link.tx_obj(3)
                        send_size += list_size
                        link.send(send_size)
                        send_size = 0
                        list_size = link.tx_obj(9)
                        send_size += list_size
                        link.send(send_size)
                        while not link.available():rc=0
                        arr = link.rx_obj(obj_type='i')
                    if arr == 1092616192:
                        print("enrolled")
                        send_size = 0
                        list_size = link.tx_obj(1)
                        send_size += list_size
                        link.send(send_size)
                        send_size = 0
                        list_size = link.tx_obj(9)
                        send_size += list_size
                        link.send(send_size)
                    while not link.available():rc=0
                    id = link.rx_obj(obj_type='i')
                    print(id)
                    btn_bg.config(file="fblk.png")
                    dtpanel21.config(text="lift finger a few times")
                    dtpanel31.config(text="wait for a few seconds and")
                    dtpanel31.place(x=440,y=550)
                    dtpanel21.place(x=470,y=600)
                    time.sleep(5)
                    #arduino.write(bytes('100/n', 'utf-8'))
                    time.sleep(.5)
                    #arduino.write(bytes('100/n', 'utf-8')) 
                    btn_bg.config(file="fgren.png")
                    dtpanel31.config(text="            Success!")
                    send_size = 0
                    list_size = link.tx_obj(1)
                    send_size += list_size
                    link.send(send_size)
                    dtpanel31.place(x=440,y=550)
                    dtpanel21.place_forget()
                    time.sleep(3)
                    dtpanel31.config(text="Registration complete!",fg="#2196F3",font=calibri)
                    dtpanel31.place(x=400,y=450)
                    blank12.place_forget()
                    time.sleep(1)
                    dtpanel21.config(text="Welcome to Ownum",font=calibri,fg="black")
                    dtpanel31.config(text=login,font=calibri,fg="black")
                    dtpanel21.place(x=440,y=300)
                    dtpanel31.place(x=600,y=355)
                    pros=tk.Button(self,borderwidth=0,text="Click to proceed to Medication set-up",fg="#2196F3",bg="white",font=calibri,command=lambda:controller.show_frame("PageOne"))
                    pros.place(x=200,y=420)
                    send_size = 0
                    list_size = link.tx_obj(7)
                    send_size += list_size
                    link.send(send_size)
                    x=1

            else: 
                usrnentry.delete(0, END)
                usrnentry.config(fg="black")
                usrnentry.insert(0, "         Wrong  pin")
                send_size = 0
                list_size = link.tx_obj(3)
                send_size += list_size
                link.send(send_size)
                wpin.play()
             
        
        owimg= PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        
        dtrimg= PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)

    def on_show_frame(self, event):
            print ("Welcome " + login)
            dtpanel1.config(text="Welcome " + login)
            #dtpanel1.config(text="Welcome " + login)

class tatspage(tk.Frame):

    
    def __init__(self, parent, controller):
    
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        btn_bg= PhotoImage(file="fblk.png")
        self.btn_bg= btn_bg
        blank1=Label(self,image=btn_bg,borderwidth=0)   
        blank1.place(x=500,y=260)
        btn_bg3= PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        

        calibri = font.Font(family="Calibri",size=40,weight="bold")
        calibri1 = font.Font(family="Calibri",size=30,weight="bold")
        dtpanel1=Label(self,text="Now press and hold ",fg="gray", bg="white",borderwidth=0,font=calibri1)
        dtpanel1.place(x=460,y=550)
        dtpanel21=Label(self,text="the fingerprint button below",fg="gray", bg="white",borderwidth=0,font=calibri1)
        dtpanel21.place(x=400,y=600)
        
        owimg= PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        
        dtrimg= PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
        

class StartPage(tk.Frame):

    
    def __init__(self, parent, controller):
    
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        btn_bg= PhotoImage(file="btn_lg.png")
        self.btn_bg= btn_bg   
        btn_bg3= PhotoImage(file="fing.png")
        self.btn_bg3= btn_bg3
        calibri = font.Font(family="Calibri",size=20,weight="bold")
        name_var=tk.StringVar()
        passw_var=tk.StringVar()
        wrgloh=Label(self,text="Wrong Username or Password",font=calibri,bg="white",fg="#D9D9D9",borderwidth=0)
        def login():
            global login
            global pas
            name=name_var.get()
            pas=passw_var.get()
            usrnentry.delete(0, END)
            passnentry.delete(0, END)
            if name == login and pas == pas:
                controller.show_frame("PageOne")
                entersucess.play()
            elif name == setlog and pas == setlog:
                controller.show_frame("PageOne")
                entersucess.play()
            else:
                wrgloh.place(x=300,y=310)
                wrongme.play()
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
            #while not link.available():rc=0
            #arr = link.rx_obj(obj_type='i')
            #print(arr)
            #while arr != 1093664768:
            #    wg=Label(self,text="Fingerprint Not Recognized",font=calibri,bg="white",fg="#D9D9D9",borderwidth=0)
            #    wg.place(x=522,y=310)
        def enter(event):
            global login
            global pas
            name=name_var.get()
            pas=passw_var.get()
            usrnentry.delete(0, END)
            passnentry.delete(0, END)
            if name == login and pas == pas:
                controller.show_frame("PageOne")
                entersucess.play()
            elif name == setlog and pas == setpass:
                controller.show_frame("PageOne")
                entersucess.play()
            else:
                wrgloh.place(x=300,y=310)    
                wrongme.play()

        login=tk.Button(self,height=60,width=529,font=calibri,text="LOG IN  >",fg="white",bg="white",borderwidth=0,image=btn_bg, command=login )
        login.place(x=200,y=580)
        login2=tk.Button(self,height=127,width=380,font=calibri,text="LOG IN  >",fg="white",bg="white",borderwidth=0,image=btn_bg3, command=printme )
        login2.place(x=800,y=450)
        owimg= PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=170,y=54)

        ntimg= PhotoImage(file="next.png")
        self.ntimg=ntimg
        ntpanel=Label(self,image=ntimg,borderwidth=0)
        ntpanel.place(x=170,y=245)
        
        dtrimg= PhotoImage(file="doctors.png")
        self.dtrimg=dtrimg
        dtpanel=Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=770,y=51)

        def usrclicked(event):
            global flag4
            if flag4 != 1:
                usrnentry.delete(0, END)
                usrnentry.config(fg="black")
                flag4 = 1   

            subprocess.Popen("D:\Work\medkit\med\On-ScreenKeyboardPortable.\On-ScreenKeyboardPortable.exe")
            keyboard.on_press_key("ENTER", enter)

        userimg= PhotoImage(file="user.png")
        self.userimg=userimg
        usrpanel=Label(self,image=userimg,borderwidth=0)
        usrpanel.place(x=200,y=360)
        usrnentry = tk.Entry(self,fg="#D9D9D9", bg="#F8F8F8",textvariable=name_var, width=30,borderwidth=0,font=calibri)
        usrnentry.insert(0, "  Username")
        usrnentry.bind("<1>", usrclicked)
        usrnentry.place( x=280,y=370)

        def passclicked(event):
            global flag3
            if flag3 != 1:
                passnentry.delete(0, END)
                passnentry.config(fg="black")
                flag3 = 1   

            subprocess.Popen("D:\Work\medkit\med\On-ScreenKeyboardPortable.\On-ScreenKeyboardPortable.exe")
            keyboard.on_press_key("ENTER", enter)


        passimg= PhotoImage(file="pass.png")
        self.passimg=passimg
        passpanel=Label(self,image=passimg,borderwidth=0)
        passpanel.place(x=200,y=440)
        passnentry = tk.Entry(self,fg="#D9D9D9", bg="#F8F8F8", width=30,textvariable=passw_var,borderwidth=0,font=calibri,show="*")
        passnentry.insert(0, "  Password")
        passnentry.bind("<1>", passclicked)
        passnentry.place( x=280,y=450)
    def on_show_frame(self, event):
        send_size = 0
        list_size = link.tx_obj(3)
        send_size += list_size
        link.send(send_size)
    

flag = 0
flag2 = 0
date1 = ""
date2 = ""

class PageOne(tk.Frame):

            


    def __init__(self, parent, controller):
        clicked = StringVar()
        
        tk.Frame.__init__(self, parent,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        calibri2 = font.Font(self,family="Calibri",size=30,weight="bold")
        calibri = font.Font(family="Calibri",size=20,weight="bold")
        owimg= PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)

        medimg= PhotoImage(file="medcalen.png")
        self.medimg=medimg
        medpanel=Label(self,image=medimg,borderwidth=0)
        medpanel.place(x=40,y=200)
        def medm(event):
            global flag5
            global flag
            if flag5 != 1:
                mednn.delete(0, END)
                mednn.config(fg="black")
                
                flag5 = 1   
            flag = 0
            btnsel()
            subprocess.Popen("D:\Work\medkit\med\On-ScreenKeyboardPortable.\On-ScreenKeyboardPortable.exe")

        camimg= PhotoImage(file="cam.png")
        self.camimg=camimg
        camimg2= PhotoImage(file="success.png")
        self.camimg2=camimg2
        campanel=Label(self,image=camimg,borderwidth=0)
        wht= PhotoImage(file="white bg.png")
        self.wht=wht
        whtp=Label(self,image=wht,borderwidth=0)
        whtpt=Label(self,text="",width=15,font=calibri2,borderwidth=0,bg="white")
        medn=tk.StringVar()
        mednn=tk.Entry(self,fg="#D9D9D9", bg="white", width=30,textvariable=medn,borderwidth=0,font=calibri)
        mednn.insert(0,"   Type Here   ")
        mednn.bind("<1>", medm)
        def btnsel():
            global flag
            global medname
            global medname2
            if flag == 0:
                campanel.config(image=camimg)
                campanel.place(x=440,y=1)
                sel.config(image=btn_sel3)
                #mednn.place(x=50,y=320)
                sel.place(x=41 ,y=373)
                whtp.place_forget()
                whtpt.place_forget()
                entermed.play()
                flag = 1
                
            else:
                campanel.place(x=440,y=1)
                #medname=medn.get()
                #mednn.delete(0, END)
                #whtpt.config(text=medname)
                send_size = 0
                list_size = link.tx_obj(5)
                send_size += list_size
                link.send(send_size)
                sel.place_forget()
                whtp.place(x=41 ,y=373)
                whtpt.place(x=55 ,y=410)
                #subprocess.call("barcoderead.py", shell=True)
                with open('barcode_result.txt') as f:
                    global line
                    line = f.readline()
                    f.close()
                    print("code is " + line)
                send_size = 0
                list_size = link.tx_obj(1)
                send_size += list_size
                link.send(send_size)
                campanel.config(image=camimg2)
                campanel.place(x=440,y=1)
                whtpt.config(text=line)
                sel.place_forget()
                whtp.place(x=41 ,y=373)
                whtpt.place(x=55 ,y=410)
                enterdose.play()
        

        #keyboard.on_press_key("escape", btnsel2)
        btn_sel= PhotoImage(file="inmed.png")
        self.btn_sel=btn_sel
        btn_sel2= PhotoImage(file="white bg.png")
        self.btn_sel2=btn_sel2
        btn_sel3= PhotoImage(file="cte.png")
        self.btn_sel3=btn_sel3
        sel=tk.Button(self,borderwidth=0,image=btn_sel,command=btnsel)
        sel.place(x=41 ,y=373)

        def btndose():
            dosebtn.place_forget()
            dose.place(x=470,y=410)
            whtdose.place(x=446,y=373)

        whtdose=Label(self,image=wht,borderwidth=0)
        btn_dose= PhotoImage(file="dday.png")
        self.btn_dose=btn_dose
        dosebtn=tk.Button(self,borderwidth=0,image=btn_dose,command=btndose)
        dosebtn.place(x=446 ,y=373)

        options = [
            "1 dose a day",
            "2 dose a day",
            "3 dose a day",
            "4 dose a day",
            "5 dose a day"
        ]
        clicked.set("Dose")
        dose = OptionMenu( self , clicked , *options )
        global dosep
        dosep = clicked.get()
        #dose.place(x=485,y=373)
        dose.config(text = "Dose",width=15,font=calibri2,bg="white", borderwidth=0,direction="below")
        menu = self.nametowidget(dose.menuname)
        menu.config(font=calibri2)
        def change():
            clkpcd.config(text="Click to Finish",command=pg3)
            campanel.place_forget()
            controller.show_frame("PageThree")
        def pg3():
            controller.show_frame("PageFour")

        clkpcd=tk.Button(self,borderwidth=0,text="Click to Proceed",fg="#A6A6A6",bg="white",font=calibri2,command=change)


        

        def dateiton():
            datebtn.place_forget()
            global dosep
            dosep=clicked.get()
            whtdose2.place(x=854,y=373)
            global labelmore,labelmore2
            labelmore = Label(self,text="7:00AM / 12:00PM / 7:00PM", font=calibri,bg="white")
            labelmore2 = Label(self,text="", font=calibri,bg="white")
            global pilidose
            print (dosep)
            # if dosep=="1 dose a day":
            #     labelmore.config(text="         7:00AM       ")
            #     pilidose =1
            # elif dosep=="2 dose a day":
            #     labelmore.config(text="   7:00AM / 7:00PM    ")
            #     pilidose =2
            # elif dosep=="3 dose a day":
            #     labelmore.config(text="7:00AM / 12:00PM / 7:00PM")
            #     pilidose =3
            # elif dosep=="4 dose a day":
            #     labelmore.config(text="7:00AM / 11:00AM / 3:00PM")
            #     labelmore2.config(text="         7:00PM         ")
            #     labelmore2.place(x=880,y=440)
            #     pilidose =4
            # elif dosep=="5 dose a day":
            #     labelmore.config(text="7:00AM / 10:00AM / 1:00PM")
            #     labelmore2.config(text="     4:00PM / 7:00PM     ")
            #     labelmore2.place(x=880,y=440)
            #     pilidose =5
            # labelmore.place(x=880,y=400)
            controller.show_frame("PageTwo")
            clkpcd.place(x=500 ,y=600)
            global flag6
            flag6 =1


        global date2
        global date1  
        btn_date= PhotoImage(file="tsched.png")
        self.btn_date=btn_date
        datebtn=tk.Button(self,borderwidth=0,image=btn_date,command=dateiton)
        datebtn.place(x=854 ,y=373)
        whtdose2=Label(self,image=wht,borderwidth=0)

        logout=tk.Button(self,borderwidth=0,text="LOGOUT",fg="#A6A6A6",bg="white",font=calibri2,command=lambda:controller.show_frame("StartPage"))
        logout.place(x=1000,y=700)
    def on_show_frame(self, event):
        send_size = 0
        list_size = link.tx_obj(1)
        send_size += list_size
        link.send(send_size)
        global pilidose,time1,time2,time3,time4,time5
        time1= hr +":"+mins+pm
        time2= hr1 +":"+mins1+pm1
        time3= hr2 +":"+mins2+pm2
        time4= hr3 +":"+mins3+pm3
        time5= hr4 +":"+mins4+pm4
        with open("alarm1.txt", mode ='w') as file1:
            if int(hr) < 10 and int(mins) < 10 :
                file1.write("0"+hr +":00 "+pm)
            elif int(hr) < 10 :
                file1.write("0"+hr +":"+mins+" "+pm)
            else:
                file1.write(hr +":"+mins+" "+pm)
        with open("alarm2.txt", mode ='w') as file2:
            if int(hr1) < 10 and int(mins1) < 10 :
                file2.write("0"+hr1 +":00 "+pm1)
            elif int(hr1) < 10 :
                file2.write("0"+hr1 +":"+mins1+" "+pm1)
            else:
                file2.write(hr1 +":"+mins1+" "+pm1)
        with open("alarm3.txt", mode ='w') as file3:
            if int(hr2) < 10 and int(mins2) < 10 :
                file3.write("0"+hr2 +":00 "+pm2)
            elif int(hr2) < 10 :
                file3.write("0"+hr2 +":"+mins2+" "+pm2)
            else:
                file3.write(hr2 +":"+mins2+" "+pm2)
        with open("alarm4.txt", mode ='w') as file4:
            if int(hr3) < 10 and int(mins3) < 10 :
                file4.write("0"+hr3 +":00 "+pm3)
            elif int(hr1) < 10 :
                file4.write("0"+hr3 +":"+mins3+" "+pm3)
            else:
                file4.write(hr3 +":"+mins3+" "+pm3)
        with open("alarm5.txt", mode ='w') as file5:
            if int(hr4) < 10 and int(mins4) < 10 :
                file5.write("0"+hr4 +":00 "+pm4)
            elif int(hr4) < 10 :
                file5.write("0"+hr4 +":"+mins4+" "+pm4)
            else:
                file5.write(hr4 +":"+mins4+" "+pm4)
        if dosep=="1 dose a day":
            labelmore.config(text="              "+ hr2 +":"+mins2+pm2)
            pilidose =1
        elif dosep=="2 dose a day":
            labelmore.config(text="   "+hr +":"+mins+pm+" / "+hr2 +":"+ mins2 +pm2)
            pilidose =2
        elif dosep=="3 dose a day":
            labelmore.config(text=hr +":"+mins+pm+" / "+hr2 +":"+ mins2 +pm2+" / "+hr4 +":"+ mins4 +pm4)
            pilidose =3
        elif dosep=="4 dose a day":
            labelmore.config(text=hr +":"+mins+pm+" / "+hr1 +":"+ mins1 +pm1+" / "+hr2 +":"+ mins2 +pm2)
            labelmore2.config(text="              "+ hr3 +":"+mins3+pm3)
            pilidose =4
            labelmore2.place(x=880,y=440)
        elif dosep=="5 dose a day":
            labelmore.config(text=hr +":"+mins+pm+" / "+hr1 +":"+ mins1 +pm1+" / "+hr2 +":"+ mins2 +pm2)
            labelmore2.config(text="   "+hr3 +":"+mins3+pm3+" / "+hr4 +":"+ mins4 +pm4)
            pilidose =5
            labelmore2.place(x=880,y=440)
        labelmore.place(x=880,y=400)
        send_size = 0
        list_size = link.tx_obj(1)
        send_size += list_size
        link.send(send_size)


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="white")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        #self.bind("<<ShowFrame>>", showpicked)
        calibri3 = font.Font(family="Calibri",size=35,weight="bold")
        calibri = font.Font(family="Calibri",size=20,weight="bold")
        calibri4 = font.Font(family="Calibri",size=15,weight="bold")
        calibri5 = font.Font(family="Calibri",size=25,weight="bold")
        # Set geometry

        owimg= PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)
        # Add Calendar
        cal = Calendar(self, selectmode = 'day',
			year = 2022, month = 1,
			day = 10)
        cal.config(background="#ffffff",foreground="black",headersbackground="#ffffff",othermonthbackground="white",othermonthwebackground="white",firstweekday="sunday",showweeknumbers=0,
				borderwidth=0,font=calibri3,weekendbackground="white",weekendforeground="black",bordercolor="white",selectbackground="#2196F3")
        cal.place(x=500,y=85)

        def data():
            global day1
            date1 = cal.get_date()
            day1=date1.split("/")

        def getdate():
	        date.config(text = cal.get_date()),data()
            # Add Button and Labe

        strdate= PhotoImage(file="strdate.png")
        self.strdate=strdate
        strsel=tk.Button(self,borderwidth=0,image=strdate,command=getdate)
        strsel.place(x=580,y=600)
        
        def data1():
            global day2
            date2 = cal.get_date()
            day2=date2.split("/")
            

        def getdate1():
	        date1.config(text = cal.get_date()),data1()
        
        endate= PhotoImage(file="endate.png")
        self.endate=endate
        endsel=tk.Button(self,borderwidth=0,image=endate,command=getdate1)
        endsel.place(x=900 ,y=600)

        date=Label(self,text=" ",font=calibri,bg="white")
        dashy=Label(self,text="-",font=calibri,bg="white")
        date1=Label(self,text=" ",font=calibri,bg="white")
        date.place(x=720,y=700)
        date1.place(x=900,y=700)
        dashy.place(x=850,y=700)
        
        wht1= PhotoImage(file="1.png")
        self.wht1=wht1
        wht1panel=Label(self,image=wht1,borderwidth=0)#gray #A6A6A6
        #wht1panel.place(x=150,y=250)
        wht2panel=Label(self,image=wht1,borderwidth=0)
        #wht2panel.place(x=150,y=400)
        wht3panel=Label(self,image=wht1,borderwidth=0)
        #wht3panel.place(x=150,y=550)
        sts=Label(self,text="Select Time Schedule",font=calibri5,bg="white",fg="#A6A6A6")
        sts.place(x=100,y=140)
        global dpd
        print (dosep)
        dpd=Label(self,text=dosep,font=calibri4,bg="white",fg="#A6A6A6")
        dpd.place(x=100,y=185)
        #ds1=Label(self,text=" 7 : 00 AM ",font=calibri3,bg="white")
        #ds2=Label(self,text="12 : 00 PM",font=calibri3,bg="white")
        #ds3=Label(self,text=" 7 : 00 PM ",font=calibri3,bg="white")
        global  min_sb,sec_hour,sec,min_sb1,sec_hour1,sec1,min_sb2,sec_hour2,sec2,min_sb3,sec_hour3,sec3,min_sb4,sec_hour4,sec4
        global hour_string,min_string,hour_string1,min_string1,hour_string2,min_string2,hour_string3,min_string3,hour_string4,min_string4
        options = ["AM","PM"]
        global am,am1,am2,am3,am4
        am=StringVar()
        am1=StringVar()
        am2=StringVar()
        am3=StringVar()
        am4=StringVar()
        hour_string=StringVar()
        min_string=StringVar()
        min_sb = Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string,width=2,state="readonly",font=calibri3)
        sec_hour = Spinbox(self,from_=0,to=50,increment=10,wrap=True,textvariable=min_string,font=calibri3,width=2,)
        am.set("AM")
        sec = OptionMenu( self , am , *options)
        sec.config(text="AM",width=4,font=calibri3,bg="white", borderwidth=0,direction="below")
        menu = self.nametowidget(sec.menuname)
        menu.config(font=calibri3)
        min_sb.place(x=165,y=260)
        sec_hour.place(x=240,y=260)
        sec.place(x=315,y=260)

        hour_string1=StringVar()
        min_string1=StringVar()
        min_sb1 = Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string1,width=2,state="readonly",font=calibri3)
        sec_hour1 = Spinbox(self,from_=0,to=50,increment=10,wrap=True,textvariable=min_string1,font=calibri3,width=2,)
        am1.set("AM")
        sec1 = OptionMenu( self , am1 , *options)
        sec1.config(text="AM",width=4,font=calibri3,bg="white", borderwidth=0,direction="below")
        menu1 = self.nametowidget(sec1.menuname)
        menu1.config(font=calibri3)
        min_sb1.place(x=165,y=330)
        sec_hour1.place(x=240,y=330)
        sec1.place(x=315,y=330)

        hour_string2=StringVar()
        min_string2=StringVar()
        min_sb2 = Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string2,width=2,state="readonly",font=calibri3)
        sec_hour2 = Spinbox(self,from_=00,to=50,wrap=True,increment=10,textvariable=min_string2,font=calibri3,width=2,)
        am2.set("AM")
        sec2 = OptionMenu( self , am2 , *options)
        sec2.config(text="AM",width=4,font=calibri3,bg="white", borderwidth=0,direction="below")
        menu2 = self.nametowidget(sec2.menuname)
        menu2.config(font=calibri3)
        min_sb2.place(x=165,y=410)
        sec_hour2.place(x=240,y=410)
        sec2.place(x=315,y=410)

        hour_string3=StringVar()
        min_string3=StringVar()
        min_sb3 = Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string3,width=2,state="readonly",font=calibri3)
        sec_hour3 = Spinbox(self,from_=0,to=50,wrap=True,increment=10,textvariable=min_string3,font=calibri3,width=2,)
        am3.set("AM")
        sec3 = OptionMenu( self , am3 , *options)
        sec3.config(text="AM",width=4,font=calibri3,bg="white", borderwidth=0,direction="below")
        menu3 = self.nametowidget(sec3.menuname)
        menu3.config(font=calibri3)
        min_sb3.place(x=165,y=480)
        sec_hour3.place(x=240,y=480)
        sec3.place(x=315,y=480)


        hour_string4=StringVar()
        min_string4=StringVar()
        min_sb4 = Spinbox(self,from_=0,to=23,wrap=True,textvariable=hour_string4,width=2,state="readonly",font=calibri3)
        sec_hour4 = Spinbox(self,from_=0,to=50,wrap=True,increment=10,textvariable=min_string4,font=calibri3,width=2,)
        am4.set("AM")
        sec4 = OptionMenu( self , am4 , *options)
        sec4.config(text="AM",width=4,font=calibri3,bg="white", borderwidth=0,direction="below")
        menu4 = self.nametowidget(sec4.menuname)
        menu4.config(font=calibri3)
        min_sb4.place(x=165,y=560)
        sec_hour4.place(x=240,y=560)
        sec4.place(x=315,y=560)
        def getmoredata():
            global hr,mins,hr1,mins1,hr2,mins2,hr3,mins3,hr4,mins4,pm,pm1,pm2,pm3,pm4
            hr=hour_string.get()
            mins=min_string.get()
            pm=am.get()
            hr1=hour_string1.get()
            mins1=min_string1.get()
            pm1=am1.get()
            hr2=hour_string2.get()
            mins2=min_string2.get()
            pm2=am2.get()
            hr3=hour_string3.get()
            mins3=min_string3.get()
            pm3=am3.get()
            hr4=hour_string4.get()
            mins4=min_string4.get()
            pm4=am4.get()
            print (hr+mins)
            controller.show_frame("PageOne")
        clkpcd=tk.Button(self,borderwidth=0,text="Click to Proceed",fg="#A6A6A6",bg="white",font=calibri5,command=getmoredata)
        clkpcd.place(x=130 ,y=675)
    def on_show_frame(self, event):
        seldate.play()
        dpd.config(text=dosep)
        if dosep=="1 dose a day":
            min_sb.place_forget() 
            sec_hour.place_forget() 
            sec.place_forget() 
            min_sb1.place_forget() 
            sec_hour1.place_forget() 
            sec1.place_forget() 
            min_sb2.place(x=150,y=410)
            sec_hour2.place(x=240,y=410)
            sec2.place(x=315,y=410)  
            min_sb3.place_forget() 
            sec_hour3.place_forget() 
            sec3.place_forget() 
            min_sb4.place_forget() 
            sec_hour4.place_forget() 
            sec4.place_forget()   
        elif dosep=="2 dose a day":
            min_sb.place(x=150,y=260)
            sec_hour.place(x=240,y=260)
            sec.place(x=315,y=260)
            min_sb1.place_forget() 
            sec_hour1.place_forget() 
            sec1.place_forget() 
            min_sb2.place(x=150,y=410)
            sec_hour2.place(x=240,y=410)
            sec2.place(x=315,y=410)  
            min_sb3.place_forget() 
            sec_hour3.place_forget() 
            sec3.place_forget() 
            min_sb4.place_forget() 
            sec_hour4.place_forget() 
            sec4.place_forget()  
        elif dosep=="3 dose a day":
            min_sb.place(x=150,y=260)
            sec_hour.place(x=240,y=260)
            sec.place(x=315,y=260)
            min_sb1.place_forget() 
            sec_hour1.place_forget() 
            sec1.place_forget()  
            min_sb2.place(x=150,y=410)
            sec_hour2.place(x=240,y=410)
            sec2.place(x=315,y=410)  
            min_sb3.place_forget() 
            sec_hour3.place_forget() 
            sec3.place_forget() 
            min_sb4.place(x=150,y=560)
            sec_hour4.place(x=240,y=560)
            sec4.place(x=315,y=560)
        elif dosep=="4 dose a day":
            min_sb.place(x=150,y=260)
            sec_hour.place(x=240,y=260)
            sec.place(x=315,y=260)
            min_sb1.place(x=150,y=330)
            sec_hour1.place(x=240,y=330)
            sec1.place(x=315,y=330)
            min_sb2.place(x=150,y=410)
            sec_hour2.place(x=240,y=410)
            sec2.place(x=315,y=410)  
            min_sb3.place(x=150,y=480)
            sec_hour3.place(x=240,y=480)
            sec3.place(x=315,y=480)
            min_sb4.place_forget() 
            sec_hour4.place_forget() 
            sec4.place_forget()             
        elif dosep=="5 dose a day":
            min_sb.place(x=150,y=260)
            sec_hour.place(x=240,y=260)
            sec.place(x=315,y=260)
            min_sb1.place(x=150,y=330)
            sec_hour1.place(x=240,y=330)
            sec1.place(x=315,y=330)
            min_sb2.place(x=150,y=410)
            sec_hour2.place(x=240,y=410)
            sec2.place(x=315,y=410)  
            min_sb3.place(x=150,y=480)
            sec_hour3.place(x=240,y=480)
            sec3.place(x=315,y=480)
            min_sb4.place(x=150,y=560)
            sec_hour4.place(x=240,y=560)
            sec4.place(x=315,y=560)
        send_size = 0
        list_size = link.tx_obj(1)
        send_size += list_size
        link.send(send_size)
        #ds1.place(x=165,y=260)
        #ds2.place(x=165,y=410)
        #ds3.place(x=165,y=560)
class PageThree(tk.Frame):

    def __init__(self, parent=None, controller=""):
        
        clicked = StringVar()
        tk.Frame.__init__(self, parent,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        global medname2
        owimg= PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)
        calibri1 = font.Font(self,family="Calibri",size=20,weight="bold") 
        calibri2 = font.Font(self,family="Calibri",size=40,weight="bold")
        calibri3 = font.Font(self,family="Calibri",size=60,weight="bold")      
        global date1
        #label1= Label(self,text="Place "+ medname2 + " at any Medicine Bay",bg="white",font=calibri2)
        print(medname2)

        
        label2= Label(self,text="Medicine Bay will light up once sensor detected the medicine",fg="#A6A6A6",bg="white",font=calibri1)
        label2.place(x=220,y=500)
        global label1
        label1= Label(self,text="",bg="white",font=calibri2)
        print(medname2) 
        label1.place(x=260,y=350)

        def updategg(x):
            label1.config(text="Place "+ x + " at any Medicine Bay")

        def gg():
            label1.place_forget()
            label2.place_forget()
            label3= Label(self,text="Set Up All Done!",bg="white",font=calibri3)
            setdone.play()
            label3.place(x=370,y=350)
            time.sleep(3)
            controller.show_frame("PageOne")

        def key(event):
            gg()

        clkpcd=tk.Button(self,borderwidth=0,text="                         ",fg="#A6A6A6",bg="white",font=calibri2,command=gg)
        clkpcd.place(x=490 ,y=600)
        keyboard.on_press_key("q", key)

    def on_show_frame(self, event):
        print ("Welcome " + login)
        print("hey")
        label1.config(text="Place "+   line + " at lit up Medicine Bay")
        placemed.play()
        send_size = 0
        list_size = link.tx_obj(11)
        send_size += list_size
        link.send(send_size)
        while not link.available():
            arr = link.rx_obj(obj_type='i')
            print(arr)
            # while arr == 1093664768:
            #     print("fail")
            #     send_size = 0
            #     list_size = link.tx_obj(3)
            #     send_size += list_size
            #     link.send(send_size)
            #     send_size = 0
            #     list_size = link.tx_obj(9)
            #     send_size += list_size
            #     link.send(send_size)
            #     while not link.available():rc=0
            #     arr = link.rx_obj(obj_type='i')
            # if arr == 1092616192:
            #     print("enrolled")
            #     send_size = 0
            #     list_size = link.tx_obj(1)
            #     send_size += list_size
            #     link.send(send_size)
            #     send_size = 0
            #     list_size = link.tx_obj(9)
            #     send_size += list_size
            #     link.send(send_size)
            # while not link.available():rc=0
            # id = link.rx_obj(obj_type='i')
            # print(id)
        # while True:
        #     if link.available():
        #         y = link.rx_obj(obj_type='i')
        #         print(y)

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        clicked = StringVar()
        
        tk.Frame.__init__(self, parent,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        calibri1 = font.Font(self,family="Calibri",size=20,weight="bold")
        calibri3 = font.Font(self,family="Calibri",size=45,weight="bold")  
        calibri2 = font.Font(self,family="Calibri",size=30,weight="bold")
        calibri = font.Font(family="Calibri",size=20,weight="bold")
        owimg= PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)
        vico= PhotoImage(file="vico.png")
        self.vico=vico
        #vicoT=Label(self,image=vico,borderwidth=0)
        #vicoT.place(x=72,y=157)
        

        global labe1,labe2,labe3,labe4,labe5,labe6,labe7,labe8,labe9,labe10
        labe1= Label(self,bg="white",font=calibri3)
        labe1.place(x=100,y=170)
        labe2= Label(self,bg="white",font=calibri3)
        labe2.place(x=100,y=270)
        labe3= Label(self,bg="white",font=calibri3)
        labe3.place(x=100,y=370)
        labe4= Label(self,bg="white",font=calibri3)
        labe4.place(x=100,y=470)
        labe5= Label(self,bg="white",font=calibri3)
        labe5.place(x=100,y=570)
        labe6= Label(self,bg="white",font=calibri1)
        labe6.place(x=100,y=250)
        labe7= Label(self,bg="white",font=calibri1)
        labe7.place(x=100,y=350)
        labe8= Label(self,bg="white",font=calibri1)
        labe8.place(x=100,y=450)
        labe9= Label(self,bg="white",font=calibri1)
        labe9.place(x=100,y=550)
        labe10= Label(self,bg="white",font=calibri1)
        labe10.place(x=100,y=650)
        global dose1,dose2,dose3,dose4,dose5,AMT
        dose1= PhotoImage(file="1dose.png")
        self.dose1=dose1
        dose2= PhotoImage(file="2dose.png")
        self.dose2=dose2
        dose3= PhotoImage(file="3dose.png")
        self.dose3=dose3
        dose4= PhotoImage(file="4dose.png")
        self.dose4=dose4
        dose5= PhotoImage(file="5dose.png")
        self.dose5=dose5
        #AMT=Label(self,borderwidth=0)
        #AMT.place(x=830,y=160)
        global lb1,lb2,lb3,lb4,lb5
        
        lb1 = Label(self , text = time1 ,font=calibri3,bg= "white",borderwidth=0) 
        lb1.place(x=830,y=160)
        lb2=Label(self,text= "",bg="white",font=calibri3,borderwidth=0)
        lb2.place(x=830,y=270)
        lb3=Label(self,text= "",bg="white",font=calibri3,borderwidth=0)
        lb3.place(x=830,y=370)
        lb4=Label(self,text= "",bg="white",font=calibri3,borderwidth=0)
        lb4.place(x=830,y=470)
        lb5=Label(self,text= "",bg="white",font=calibri3,borderwidth=0)
        lb5.place(x=830,y=570)

        logout=tk.Button(self,borderwidth=0,text="LOGOUT",fg="#A6A6A6",bg="white",font=calibri2,command=lambda:controller.show_frame("StartPage"))
        logout.place(x=1000,y=72)
        setup=tk.Button(self,borderwidth=0,text="Click to set up",fg="#A6A6A6",bg="white",font=calibri2,command=lambda:controller.show_frame("PageOne"))
        setup.place(x=850,y=700)
    def on_show_frame(self, event):
        print(time1)
        
        send_size = 0
        list_size = link.tx_obj(1)
        send_size += list_size
        link.send(send_size)
        def month(x):
            switcher = {
            '1': "JAN",
            '2': "FEB",
            '3': "MAR",
            '4': "APR",
            '5': "MAY",
            '6': "JUN",
            '7': "JUL",
            '8': "AUG",
            '9': "SEP",
            '10': "OCT",
            '11': "NOV",
            '12': "DEC",
            }
            return switcher.get(x, "")
        if pilidose ==1: 
            #AMT.config(image=dose1)
            labe3.config(text=line)
            labe8.config(text="till "+ month(day2[0])+" "+ day2[1])
            lb3.config(text=time3)
        if pilidose ==2: 
            #AMT.config(image=dose2)
            labe2.config(text=line)
            labe7.config(text="till "+ month(day2[0])+" "+ day2[1])
            labe4.config(text=line)
            labe9.config(text="till "+ month(day2[0])+" "+ day2[1])
            lb2.config(text=time1)
            lb4.config(text=time3)
        if pilidose ==3: 
            #AMT.config(image=dose3)
            labe1.config(text=line)
            labe6.config(text="till "+ month(day2[0])+" "+ day2[1])
            labe3.config(text=line)
            labe8.config(text="till "+ month(day2[0])+" "+ day2[1])
            labe5.config(text=line)
            labe10.config(text="till "+ month(day2[0])+" "+ day2[1])
            lb1.config(text=time1)
            lb2.config(text="")
            lb3.config(text=time3)
            lb4.config(text="")
            lb5.config(text=time5)
        if pilidose ==4: 
            #AMT.config(image=dose4)
            labe1.config(text=line)
            labe6.config(text="till "+ month(day2[0])+" "+ day2[1])
            labe2.config(text=line)
            labe7.config(text="till "+ month(day2[0])+" "+ day2[1])
            labe3.config(text=line)
            labe8.config(text="till "+ month(day2[0])+" "+day2[1])
            labe4.config(text=line)
            labe9.config(text="till "+ month(day2[0])+" "+day2[1])
            lb1.config(text=time1)
            lb2.config(text=time2)
            lb3.config(text=time3)
            lb4.config(text=time4)

        if pilidose ==5: 
            #AMT.config(image=dose5)
            labe1.config(text=line)
            labe6.config(text="till "+ month(day2[0])+" "+day2[1])
            labe2.config(text=line)
            labe7.config(text="till "+ month(day2[0])+" "+day2[1])
            labe3.config(text=line)
            labe8.config(text="till "+ month(day2[0])+" "+day2[1])
            labe4.config(text=line)
            labe9.config(text="till "+ month(day2[0])+" "+day2[1])
            labe5.config(text=line)
            labe10.config(text="till "+ month(day2[0])+" "+day2[1])
            lb1.config(text=time1)
            lb2.config(text=time2)
            lb3.config(text=time3)
            lb4.config(text=time4)
            lb5.config(text=time5)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
    