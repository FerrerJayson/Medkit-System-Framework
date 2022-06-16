import tkinter as tk
import pandas as pd

class ActiveScreen(tk.Frame):

    def __init__(self,parent,controller):
        
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)
        owimg= tk.PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)

        df = pd.read_csv("./accounts/admin.csv")
        meds = [med for med in df['Medication']]
        doses = [int(dose) for dose in df['Dose']]
        end_dates = [end for end in df['End Date']]
        times = [df['First Dose'][0],df['Second Dose'][0],df['Third Dose'][0],df['Fourth Dose'][0],df['Fifth Dose'][0]]
        y_increment = 0
        count = len(meds)

        med_label = []
        dose_label = []
        end_label = []
        time_label = []

        for i in range(doses[0]):
            med_label.append(tk.Label(self, text=meds[0], font=('Helvetica', 40), bg="#ffffff"))
            time_label.append(tk.Label(self, text=times[i].upper(),font=('Helvetica', 40), bg="#ffffff"))
            dose_label.append(tk.Label(self, text=f"{doses[0]} Doses", font=('Helvetica', 20), bg="#ffffff"))
            end_label.append(tk.Label(self, text=f"Til {end_dates[0][:6]}", font=('Helvetica',20), bg="#ffffff"))
            med_label[i].place(y=y_increment+200, x= 100)
            time_label[i].place(y=y_increment+230, x= 800)
            dose_label[i].place(y=y_increment+270, x = 110)
            end_label[i].place(y=y_increment+300, x = 110)
            y_increment+=200

    def on_show_frame(self, event):
        pass


class HomePage(tk.Frame):

    def __init__(self, parent, controller):
    
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller

        btn_bg= tk.PhotoImage(file="login.png")
        self.btn_bg= btn_bg   
        btn_bg3= tk.PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3

        label1=tk.Label(self,text="Or",font=('Helvetica', 30),bg="white",fg="gray",borderwidth=0)
        label1.place(x=600,y=530)
        
        
        owimg= tk.PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        
        dtrimg= tk.PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=tk.Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
    
        sel2=tk.Button(self,borderwidth=0,image=btn_bg3,command=lambda:controller.show_frame("NamePage"))
        sel2.place(x=377 ,y=348)
        sel=tk.Button(self,borderwidth=0,image=btn_bg,command=lambda:controller.show_frame("StartPage"))
        sel.place(x=516 ,y=600)