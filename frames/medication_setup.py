import tkinter as tk
from pySerialTransfer import pySerialTransfer as txfer
from tkcalendar import Calendar
import time
from pygame import mixer
from variables import login, pin, time1, time2, time3, time4, time5

def play(name):
    sfx= mixer.Sound(f"./audios/{name}.wav")
    sfx.play()

flag = 0
flag2 = 0
date1 = ""
date2 = ""

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        clicked = tk.StringVar()
        
        tk.Frame.__init__(self, parent,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        owimg= tk.PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)
        medimg= tk.PhotoImage(file="medcalen.png")
        self.medimg=medimg
        medpanel=tk.Label(self,image=medimg,borderwidth=0)
        medpanel.place(x=40,y=200)
        wht= tk.PhotoImage(file="white bg.png")
        self.wht=wht
        whtp=tk.Label(self,image=wht,borderwidth=0)
        whtpt=tk.Label(self,text="",width=15,font=('Helvetica', 20),borderwidth=0,bg="white")
        mednn=tk.Entry(self, bg="white", width=13,borderwidth=0,font=('Helvetica', 35), justify='center')
        btn_sel= tk.PhotoImage(file="inmed.png")
        self.btn_sel=btn_sel
        whtdose=tk.Label(self,image=wht,borderwidth=0)
        btn_dose= tk.PhotoImage(file="dday.png")
        self.btn_dose=btn_dose

        keys=['1','2','3','4','5','6','7','8','9','0','_',
            'Q','W','E','R','T','Y','U','I','O','P','DELETE',
            'A','S','D','F','G','H','J','K','L',':','"',
            'Z','X','C','V','B','N','M','<','>','?','ENTER']

        button=[]
            
        def enter():
            for b in button:
                b.place_forget()

        def select(value):
            if value == "DELETE":
                mednn.delete(len(mednn.get())-1)

            elif value == "ENTER":
                enter()

            else:
                mednn.insert(tk.END, value)

        def show_keyboard():
            index = 0
            varRow = 2
            varColumn = 0
            for letter in keys:
                command = lambda x=letter: select(x)
                button.append(tk.Button(self, text=letter, width=5, bg="#22272c", fg="#ffffff",
                    activebackground="#2a4158", activeforeground="#ffffff", relief="raised", padx=10,
                    pady=10, bd=4, font=("Helvetica", 20), justify="center", command=command))
                button[index].place(y=varRow+480, x=varColumn+20)
                index+=1

                varColumn += 110
                if varColumn > 1200:
                    varColumn = 0
                    varRow += 75

        def medm(event):
            global flag5
            global flag
            if flag5 != 1:
                mednn.delete(0, tk.END)
                mednn.config(fg="black")
                
                flag5 = 1   
            flag = 0
            btnsel()

        mednn.bind("<1>", medm)

        def btnsel():
            global flag
            if flag == 0:
                show_keyboard()
                sel.place_forget()
                whtp.place(x=41 ,y=323)
                # whtpt.place(x=41 ,y=323)
                mednn.place(x=51 ,y=363)
                play('entermed')
                flag = 1
                
            else:
                #medname=medn.get()
                #mednn.delete(0, END)
                #whtpt.config(text=medname)
                sel.place_forget()
                whtp.place(x=41 ,y=323)
                whtpt.place(x=55 ,y=410)
                #subprocess.call("barcoderead.py", shell=True)
                with open('barcode_result.txt') as f:
                    global line
                    line = f.readline()
                    f.close()
                    print("code is " + line)
                whtpt.config(text=line)
                sel.place_forget()
                whtp.place(x=41 ,y=323)
                whtpt.place(x=55 ,y=410)
                play('enterdose')

        def btndose():
            dosebtn.place_forget()
            dose.place(x=470,y=353)
            whtdose.place(x=446,y=323)

        dosebtn=tk.Button(self,borderwidth=0,image=btn_dose,command=btndose)
        dosebtn.place(x=446 ,y=323)
        sel=tk.Button(self,borderwidth=0,image=btn_sel,command=btnsel)
        sel.place(x=41 ,y=323)

        options = [
            "1 dose a day",
            "2 dose a day",
            "3 dose a day",
            "4 dose a day",
            "5 dose a day"
        ]
        clicked.set("Dose")
        dose = tk.OptionMenu( self , clicked , *options )
        global dosep
        dosep = clicked.get()
        #dose.place(x=485,y=373)
        dose.config(text = "Dose",width=10,font=('Helvetica', 40),bg="white", borderwidth=0,direction="below")
        menu = self.nametowidget(dose.menuname)
        menu.config(font=('Helvetica', 40))

        def change():
            clkpcd.config(text="Click to Finish",command=pg3)
            controller.show_frame("PageThree")

        def pg3():
            controller.show_frame("PageFour")

        clkpcd=tk.Button(self,borderwidth=0,text="Click to Proceed",fg="#A6A6A6",bg="white",font=('Helvetica', 20),command=change)

        def dateiton():
            datebtn.place_forget()
            global dosep
            dosep=clicked.get()
            whtdose2.place(x=854,y=323)
            global labelmore,labelmore2
            labelmore = tk.Label(self,text="7:00AM / 12:00PM / 7:00PM", font=('Helvetica', 20),bg="white")
            labelmore2 = tk.Label(self,text="", font=('Helvetica', 20),bg="white")
            global pilidose
            print (dosep)
            controller.show_frame("PageTwo")
            clkpcd.place(x=500 ,y=600)
            global flag6
            flag6 =1

        btn_date= tk.PhotoImage(file="tsched.png")
        self.btn_date=btn_date
        datebtn=tk.Button(self,borderwidth=0,image=btn_date,command=dateiton)
        datebtn.place(x=854 ,y=323)
        whtdose2=tk.Label(self,image=wht,borderwidth=0)

        logout=tk.Button(self,borderwidth=0,text="LOGOUT",fg="#000000",bg="white",font=('Helvetica', 20),command=lambda:controller.show_frame("StartPage"))
        logout.place(x=1000,y=50)
    
    def on_show_frame(self, event):
        pass

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,bg="white")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        #self.bind("<<ShowFrame>>", showpicked)
        # Set geometry

        owimg= tk.PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)
        # Add Calendar
        cal = Calendar(self, selectmode = 'day',
			year = 2022, month = 1,
			day = 10)
        cal.config(background="#ffffff",foreground="black",headersbackground="#ffffff",othermonthbackground="white",othermonthwebackground="white",firstweekday="sunday",showweeknumbers=0,
				borderwidth=0,font=('Helvetica', 35),weekendbackground="white",weekendforeground="black",bordercolor="white",selectbackground="#2196F3")
        cal.place(x=500,y=85)

        def data():
            global day1
            date1 = cal.get_date()
            day1=date1.split("/")

        def getdate():
            date.config(text = cal.get_date()),data()
        
        # Add Button and Label
        strdate= tk.PhotoImage(file="strdate.png")
        self.strdate=strdate
        strsel=tk.Button(self,borderwidth=0,image=strdate,command=getdate)
        strsel.place(x=580,y=600)
        
        def data1():
            global day2
            date2 = cal.get_date()
            day2=date2.split("/")
            
        def getdate1():
            date1.config(text = cal.get_date()),data1()
        
        endate= tk.PhotoImage(file="endate.png")
        self.endate=endate
        endsel=tk.Button(self,borderwidth=0,image=endate,command=getdate1)
        endsel.place(x=900 ,y=600)

        date=tk.Label(self,text=" ",font=('Helvetica', 30),bg="white")
        dashy=tk.Label(self,text="-",font=('Helvetica', 30),bg="white")
        date1=tk.Label(self,text=" ",font=('Helvetica', 30),bg="white")
        date.place(x=720,y=700)
        date1.place(x=900,y=700)
        dashy.place(x=850,y=700)
        
        wht1= tk.PhotoImage(file="1.png")
        self.wht1=wht1
        wht1panel=tk.Label(self,image=wht1,borderwidth=0)#gray #A6A6A6
        #wht1panel.place(x=150,y=250)
        wht2panel=tk.Label(self,image=wht1,borderwidth=0)
        #wht2panel.place(x=150,y=400)
        wht3panel=tk.Label(self,image=wht1,borderwidth=0)
        #wht3panel.place(x=150,y=550)
        sts=tk.Label(self,text="Select Time Schedule",font=('Helvetica', 30),bg="white",fg="#A6A6A6")
        sts.place(x=100,y=140)
        global dpd
        print (dosep)
        dpd=tk.Label(self,text=dosep,font=('Helvetica', 30),bg="white",fg="#A6A6A6")
        dpd.place(x=100,y=185)
        #ds1=Label(self,text=" 7 : 00 AM ",font=calibri3,bg="white")
        #ds2=Label(self,text="12 : 00 PM",font=calibri3,bg="white")
        #ds3=Label(self,text=" 7 : 00 PM ",font=calibri3,bg="white")
        global  min_sb,sec_hour,sec,min_sb1,sec_hour1,sec1,min_sb2,sec_hour2,sec2,min_sb3,sec_hour3,sec3,min_sb4,sec_hour4,sec4
        global hour_string,min_string,hour_string1,min_string1,hour_string2,min_string2,hour_string3,min_string3,hour_string4,min_string4
        options = ["AM","PM"]
        global am,am1,am2,am3,am4
        am=tk.StringVar()
        am1=tk.StringVar()
        am2=tk.StringVar()
        am3=tk.StringVar()
        am4=tk.StringVar()
        hour_string=tk.StringVar()
        min_string=tk.StringVar()
        min_sb = tk.Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string,width=2,state="readonly",font=('Helvetica', 35))
        sec_hour = tk.Spinbox(self,from_=0,to=50,increment=10,wrap=True,textvariable=min_string,font=('Helvetica', 35),width=2,)
        am.set("AM")
        sec = tk.OptionMenu( self , am , *options)
        sec.config(text="AM",width=4,font=('Helvetica', 35),bg="white", borderwidth=0,direction="below")
        menu = self.nametowidget(sec.menuname)
        menu.config(font=('Helvetica', 35))
        min_sb.place(x=165,y=260)
        sec_hour.place(x=240,y=260)
        sec.place(x=315,y=260)

        hour_string1=tk.StringVar()
        min_string1=tk.StringVar()
        min_sb1 = tk.Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string1,width=2,state="readonly",font=('Helvetica', 35))
        sec_hour1 = tk.Spinbox(self,from_=0,to=50,increment=10,wrap=True,textvariable=min_string1,font=('Helvetica', 35),width=2,)
        am1.set("AM")
        sec1 = tk.OptionMenu( self , am1 , *options)
        sec1.config(text="AM",width=4,font=('Helvetica', 35),bg="white", borderwidth=0,direction="below")
        menu1 = self.nametowidget(sec1.menuname)
        menu1.config(font=('Helvetica', 35))
        min_sb1.place(x=165,y=330)
        sec_hour1.place(x=240,y=330)
        sec1.place(x=315,y=330)

        hour_string2=tk.StringVar()
        min_string2=tk.StringVar()
        min_sb2 = tk.Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string2,width=2,state="readonly",font=('Helvetica', 35))
        sec_hour2 = tk.Spinbox(self,from_=00,to=50,wrap=True,increment=10,textvariable=min_string2,font=('Helvetica', 35),width=2,)
        am2.set("AM")
        sec2 = tk.OptionMenu( self , am2 , *options)
        sec2.config(text="AM",width=4,font=('Helvetica', 35),bg="white", borderwidth=0,direction="below")
        menu2 = self.nametowidget(sec2.menuname)
        menu2.config(font=('Helvetica', 35))
        min_sb2.place(x=165,y=410)
        sec_hour2.place(x=240,y=410)
        sec2.place(x=315,y=410)

        hour_string3=tk.StringVar()
        min_string3=tk.StringVar()
        min_sb3 = tk.Spinbox(self,from_=0,to=12,wrap=True,textvariable=hour_string3,width=2,state="readonly",font=('Helvetica', 35))
        sec_hour3 = tk.Spinbox(self,from_=0,to=50,wrap=True,increment=10,textvariable=min_string3,font=('Helvetica', 35),width=2,)
        am3.set("AM")
        sec3 = tk.OptionMenu( self , am3 , *options)
        sec3.config(text="AM",width=4,font=('Helvetica', 35),bg="white", borderwidth=0,direction="below")
        menu3 = self.nametowidget(sec3.menuname)
        menu3.config(font=('Helvetica', 35))
        min_sb3.place(x=165,y=480)
        sec_hour3.place(x=240,y=480)
        sec3.place(x=315,y=480)


        hour_string4=tk.StringVar()
        min_string4=tk.StringVar()
        min_sb4 = tk.Spinbox(self,from_=0,to=23,wrap=True,textvariable=hour_string4,width=2,state="readonly",font=('Helvetica', 35))
        sec_hour4 = tk.Spinbox(self,from_=0,to=50,wrap=True,increment=10,textvariable=min_string4,font=('Helvetica', 35),width=2,)
        am4.set("AM")
        sec4 = tk.OptionMenu( self , am4 , *options)
        sec4.config(text="AM",width=4,font=('Helvetica', 35),bg="white", borderwidth=0,direction="below")
        menu4 = self.nametowidget(sec4.menuname)
        menu4.config(font=('Helvetica', 35))
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
        clkpcd=tk.Button(self,borderwidth=0,text="Click to Proceed",fg="#A6A6A6",bg="white",font=('Helvetica', 30),command=getmoredata)
        clkpcd.place(x=130 ,y=675)
    def on_show_frame(self, event):
        play('seldate')
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

class PageThree(tk.Frame):

    def __init__(self, parent=None, controller=""):
        
        clicked = tk.StringVar()
        tk.Frame.__init__(self, parent,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        global medname2
        owimg= tk.PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)      
        global date1
        #label1= Label(self,text="Place "+ medname2 + " at any Medicine Bay",bg="white",font=calibri2)

        
        label2= tk.Label(self,text="Medicine Bay will light up once sensor detected the medicine",fg="#A6A6A6",bg="white",font=('Helvetica', 30))
        label2.place(x=220,y=500)
        global label1
        label1= tk.Label(self,text="",bg="white",font=('Helvetica', 30)) 
        label1.place(x=260,y=350)

        def updategg(x):
            label1.config(text="Place "+ x + " at any Medicine Bay")

        def gg():
            label1.place_forget()
            label2.place_forget()
            label3= tk.Label(self,text="Set Up All Done!",bg="white",font=('Helvetica', 30))
            play('setdone')
            label3.place(x=370,y=350)
            time.sleep(3)
            controller.show_frame("PageOne")

        def key(event):
            gg()

        clkpcd=tk.Button(self,borderwidth=0,text="                         ",fg="#A6A6A6",bg="white",font=('Helvetica', 40),command=gg)
        clkpcd.place(x=490 ,y=600)

    def on_show_frame(self, event):
        label1.config(text="Place "+   line + " at lit up Medicine Bay")
        play("placemed")
