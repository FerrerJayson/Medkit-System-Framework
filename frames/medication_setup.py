import tkinter as tk
from pySerialTransfer import pySerialTransfer as txfer
from tkcalendar import Calendar
import time
from pygame import mixer
from variables import login, pin

def play(name):
    sfx= mixer.Sound(f"./audios/{name}.wav")
    sfx.play()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        clicked_dose = tk.StringVar()
        clicked_meds = tk.StringVar()
        
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
        def medm(event):
            global flag5
            global flag
            if flag5 != 1:
                mednn.delete(0, tk.END)
                mednn.config(fg="black")
                
                flag5 = 1   
            flag = 0
            btnsel()

        camimg= tk.PhotoImage(file="cam.png")
        self.camimg=camimg
        camimg2= tk.PhotoImage(file="success.png")
        self.camimg2=camimg2
        campanel=tk.Label(self,image=camimg,borderwidth=0)
        wht= tk.PhotoImage(file="white bg.png")
        self.wht=wht
        whtp=tk.Label(self,image=wht,borderwidth=0)
        whtpt=tk.Label(self,text="",width=15,font=('Helvetica', 30),borderwidth=0,bg="white")
        medn=tk.StringVar()
        mednn=tk.Entry(self,fg="#D9D9D9", bg="white", width=30,textvariable=medn,borderwidth=0,font=('Helvetica', 20))
        mednn.insert(0,"   Type Here   ")
        mednn.bind("<1>", medm)
        def btnsel():
            global flag
            if flag == 0:
                campanel.config(image=camimg)
                campanel.place(x=440,y=1)
                btn_meds.config(image="cte.png")
                #mednn.place(x=50,y=320)
                btn_meds.place(x=41 ,y=373)
                whtp.place_forget()
                whtpt.place_forget()
                play("entermed")
                flag = 1
                
            else:
                campanel.place(x=440,y=1)
                #medname=medn.get()
                #mednn.delete(0, END)
                #whtpt.config(text=medname)
                btn_meds.place_forget()
                whtp.place(x=41 ,y=373)
                whtpt.place(x=55 ,y=410)
                #subprocess.call("barcoderead.py", shell=True)
                with open('barcode_result.txt') as f:
                    global line
                    line = f.readline()
                    f.close()
                    print("code is " + line)
                campanel.config(image=camimg2)
                campanel.place(x=440,y=1)
                whtpt.config(text=line)
                btn_meds.place_forget()
                whtp.place(x=41 ,y=373)
                whtpt.place(x=55 ,y=410)
                play("enterdose")

        def btnmeds():
            medsbtn.place_forget()
            meds.place(x=67,y=410)
            whtmeds.place(x=41,y=373)

        def btndose():
            dosebtn.place_forget()
            dose.place(x=470,y=410)
            whtdose.place(x=446,y=373)

        whtmeds=tk.Label(self,image=wht,borderwidth=0)
        btn_meds= tk.PhotoImage(file="inmed.png")
        self.btn_meds=btn_meds
        medsbtn=tk.Button(self,borderwidth=0,image=btn_meds,command=btnmeds)
        medsbtn.place(x=41 ,y=373)

        whtdose=tk.Label(self,image=wht,borderwidth=0)
        btn_dose= tk.PhotoImage(file="dday.png")
        self.btn_dose=btn_dose
        dosebtn=tk.Button(self,borderwidth=0,image=btn_dose,command=btndose)
        dosebtn.place(x=446 ,y=373)

        dose_options = [
            "1 dose a day",
            "2 dose a day",
            "3 dose a day",
            "4 dose a day",
            "5 dose a day"
        ]

        meds_options = [
            "Mefenamic Acid",
            "Paracetamol",
            "Amoxicillin",
            "Antihistamines",
            "Anti inflammatory"
        ]
        clicked_dose.set("Dose")
        dose = tk.OptionMenu( self , clicked_dose , *dose_options )
        meds = tk.OptionMenu( self , clicked_meds , *meds_options )
        global dosep
        dosep = clicked_meds.get()
        #dose.place(x=485,y=373)
        meds.config(text = "Medication",width=15,font=('Helvetica', 30),bg="white", borderwidth=0,direction="below")
        dose.config(text = "Dose",width=15,font=('Helvetica', 30),bg="white", borderwidth=0,direction="below")
        menudose = self.nametowidget(dose.menuname)
        menumeds = self.nametowidget(meds.menuname)
        menudose.config(font=('Helvetica', 30))
        menumeds.config(font=('Helvetica', 30))
        def change():
            clkpcd.config(text="Click to Finish",command=pg3)
            campanel.place_forget()
            controller.show_frame("PageThree")
        def pg3():
            controller.show_frame("PageFour")

        clkpcd=tk.Button(self,borderwidth=0,text="Click to Proceed",fg="#A6A6A6",bg="white",font=('Helvetica', 30),command=change)

        def dateiton():
            datebtn.place_forget()
            global dosep
            dosep=clicked_dose.get()
            whtdose2.place(x=854,y=373)
            global labelmore,labelmore2
            labelmore = tk.Label(self,text="7:00AM / 12:00PM / 7:00PM", font=('Helvetica', 30),bg="white")
            labelmore2 = tk.Label(self,text="", font=('Helvetica', 30),bg="white")
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
        btn_date= tk.PhotoImage(file="tsched.png")
        self.btn_date=btn_date
        datebtn=tk.Button(self,borderwidth=0,image=btn_date,command=dateiton)
        datebtn.place(x=854 ,y=373)
        whtdose2=tk.Label(self,image=wht,borderwidth=0)

        logout=tk.Button(self,borderwidth=0,text="LOGOUT",fg="#A6A6A6",bg="white",font=('Helvetica', 30),command=lambda:controller.show_frame("StartPage"))
        logout.place(x=1000,y=700)
    def on_show_frame(self, event):
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

class PageFour(tk.Frame):

    def __init__(self, parent, controller):
        clicked = tk.StringVar()
        
        tk.Frame.__init__(self, parent,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        owimg= tk.PhotoImage(file="ownum2.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=60,y=51)
        vico= tk.PhotoImage(file="vico.png")
        self.vico=vico
        #vicoT=Label(self,image=vico,borderwidth=0)
        #vicoT.place(x=72,y=157)
        

        global labe1,labe2,labe3,labe4,labe5,labe6,labe7,labe8,labe9,labe10
        labe1= tk.Label(self,bg="white",font=('Helvetica', 35))
        labe1.place(x=100,y=170)
        labe2= tk.Label(self,bg="white",font=('Helvetica', 35))
        labe2.place(x=100,y=270)
        labe3= tk.Label(self,bg="white",font=('Helvetica', 35))
        labe3.place(x=100,y=370)
        labe4= tk.Label(self,bg="white",font=('Helvetica', 35))
        labe4.place(x=100,y=470)
        labe5= tk.Label(self,bg="white",font=('Helvetica', 35))
        labe5.place(x=100,y=570)
        labe6= tk.Label(self,bg="white",font=('Helvetica', 30))
        labe6.place(x=100,y=250)
        labe7= tk.Label(self,bg="white",font=('Helvetica', 30))
        labe7.place(x=100,y=350)
        labe8= tk.Label(self,bg="white",font=('Helvetica', 30))
        labe8.place(x=100,y=450)
        labe9= tk.Label(self,bg="white",font=('Helvetica', 30))
        labe9.place(x=100,y=550)
        labe10= tk.Label(self,bg="white",font=('Helvetica', 30))
        labe10.place(x=100,y=650)
        global dose1,dose2,dose3,dose4,dose5,AMT
        dose1= tk.PhotoImage(file="1dose.png")
        self.dose1=dose1
        dose2= tk.PhotoImage(file="2dose.png")
        self.dose2=dose2
        dose3= tk.PhotoImage(file="3dose.png")
        self.dose3=dose3
        dose4= tk.PhotoImage(file="4dose.png")
        self.dose4=dose4
        dose5= tk.PhotoImage(file="5dose.png")
        self.dose5=dose5
        #AMT=Label(self,borderwidth=0)
        #AMT.place(x=830,y=160)
        global lb1,lb2,lb3,lb4,lb5
        
        lb1 = tk.Label(self , text = time1 ,font=('Helvetica', 35),bg= "white",borderwidth=0) 
        lb1.place(x=830,y=160)
        lb2=tk.Label(self,text= "",bg="white",font=('Helvetica', 35),borderwidth=0)
        lb2.place(x=830,y=270)
        lb3=tk.Label(self,text= "",bg="white",font=('Helvetica', 35),borderwidth=0)
        lb3.place(x=830,y=370)
        lb4=tk.Label(self,text= "",bg="white",font=('Helvetica', 35),borderwidth=0)
        lb4.place(x=830,y=470)
        lb5=tk.Label(self,text= "",bg="white",font=('Helvetica', 35),borderwidth=0)
        lb5.place(x=830,y=570)

        logout=tk.Button(self,borderwidth=0,text="LOGOUT",fg="#A6A6A6",bg="white",font=('Helvetica', 30),command=lambda:controller.show_frame("StartPage"))
        logout.place(x=1000,y=72)
        setup=tk.Button(self,borderwidth=0,text="Click to set up",fg="#A6A6A6",bg="white",font=('Helvetica', 30),command=lambda:controller.show_frame("PageOne"))
        setup.place(x=850,y=700)
    def on_show_frame(self, event):
        print(time1)
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