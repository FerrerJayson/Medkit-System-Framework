import tkinter as tk
import pandas as pd
import csv
from pygame import mixer
from variables import login, pin

mixer.init()
name_entry_flag = 0
pin_entry_flag = 0

def play(name):
    sfx= mixer.Sound(f"./audios/{name}.wav")
    sfx.play()

class NamePage(tk.Frame):

    def __init__(self, parent, controller):
    
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.controller = controller
        self.bind("<<ShowFrame>>", self.on_show_frame)

        owimg= tk.PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        dtrimg= tk.PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=tk.Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
        btn_bg= tk.PhotoImage(file="./graphics/blank.png")
        self.btn_bg= btn_bg
        blank1=tk.Label(self,image=btn_bg,borderwidth=0)   
        blank1.place(x=365,y=237)
        btn_bg3= tk.PhotoImage(file="./graphics/reg.png")
        self.btn_bg3= btn_bg3
        username_entry = tk.Entry(self,fg="black", bg="white", width=16,borderwidth=0,font=('Helvetica', 40), justify='center')
        username_entry.insert(0, "Enter your name")
        username_entry.place( x=375,y=250)
        keys=['1','2','3','4','5','6','7','8','9','0','_',
            'Q','W','E','R','T','Y','U','I','O','P','DELETE',
            'A','S','D','F','G','H','J','K','L',':','"',
            'Z','X','C','V','B','N','M','<','>','?','ENTER']

        button=[]

        def back():
            controller.show_frame("HomePage")

        back_button = tk.Button(self, text="BACK", font= ('Helvetica', 20), command=back)
        back_button.place(x=10, y=10)

        def create_account():
            global login
            header = ['Medication', 'Dose', 'Start Date', 'End Date', 'First Dose', 'Second Dose', 'Third Dose', 'Fourth Dose', 'Fifth Dose', 'Pin']
            file = open(f"./accounts/{login}.csv", "w", newline='')
            writer = csv.writer(file)
            writer.writerow(header)
            
        def enter():
                global login
                login = username_entry.get()
                create_account()
                controller.show_frame("PinPage")

        def select(value):
            if value == "DELETE":
                username_entry.delete(len(username_entry.get())-1)

            elif value == "ENTER":
                enter()

            else:
                username_entry.insert(tk.END, value)

        def show_keyboard():
            index = 0
            varRow = 2
            varColumn = 0
            for letter in keys:
                command = lambda x=letter: select(x)
                button.append(tk.Button(self, text=letter, width=5, bg="#22272c", fg="#ffffff",
                    activebackground="#2a4158", activeforeground="#ffffff", relief="raised", padx=10,
                    pady=10, bd=4, font=("Helvetica", 20), justify="center", command=command))
                button[index].place(y=varRow+400, x=varColumn+20)
                index+=1

                varColumn += 110
                if varColumn > 1200:
                    varColumn = 0
                    varRow += 75

        def usrclicked(event):
            global name_entry_flag
            if name_entry_flag != 1:
                username_entry.delete(0, tk.END)
                username_entry.config(fg="black")
                play("entername")
            show_keyboard()

        username_entry.bind("<1>", usrclicked)
        
    def on_show_frame(self, event):
        pass

class PinPage(tk.Frame):

    def __init__(self, parent, controller):
    
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.bind("<<ShowFrame>>", self.on_show_frame)
        self.controller = controller

        global login
        owimg= tk.PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        dtrimg= tk.PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=tk.Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
        btn_bg= tk.PhotoImage(file="blank.png")
        self.btn_bg= btn_bg
        blank1=tk.Label(self,image=btn_bg,borderwidth=0)   
        blank1.place(x=365,y=237)
        btn_bg3= tk.PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        dtpanel4=tk.Label(self,text=f"Welcome {login}",fg="black", bg="white",borderwidth=0,font=('Helvetica',40), justify='center')
        dtpanel4.place(x=400,y=155)
        pin_entry = tk.Entry(self,fg="black", bg="white", width=15,borderwidth=0,font=('Helvetica',40), justify='center', show="*")
        pin_entry.insert(0, "Enter pin")
        pin_entry.place( x=375,y=250)
        keys=['1','2','3','4','5','6','7','8','9','DELETE','0','ENTER']

        button=[]
        
        def enter():
            global pin
            pin = pin_entry.get()
            file = open(f"./accounts/{login}.csv", "a", newline='')
            writer = csv.writer(file)
            writer.writerow(['','','','','','','','','',str(pin)+'x'])
            controller.show_frame("PinConfirmPage")

        def select(value):
                if value == "DELETE":
                    pin_entry.delete(len(pin_entry.get())-1)

                elif value == "ENTER":
                    enter()

                else:
                    pin_entry.insert(tk.END, value)

        def show_keyboard():
            index = 0
            varRow = 2
            varColumn = 0
            for letter in keys:
                command = lambda x=letter: select(x)
                button.append(tk.Button(self, text=letter, width=5, bg="#22272c", fg="#ffffff",
                    activebackground="#5ce1e6", activeforeground="#000000", relief="raised", padx=10,
                    pady=10, bd=4, font=("Helvetica", 20), justify="center", command=command))
                button[index].place(y=varRow+400, x=varColumn+450)
                index+=1

                varColumn += 110
                if varColumn > 220:
                    varColumn = 0
                    varRow += 75
        
        def usrclicked(event):
            global pin_entry_flag
            if pin_entry_flag != 1:
                pin_entry.delete(0, tk.END)
                pin_entry.config(fg="black")
                play("enterpin")
            show_keyboard()
        pin_entry.bind("<1>", usrclicked)

    def on_show_frame(self, event):
        pass

class PinConfirmPage(tk.Frame):

    def __init__(self, parent, controller):
    
        tk.Frame.__init__(self, parent,height=800,width=1260,bg="#ffffff")
        self.bind("<<ShowFrame>>", self.on_show_frame)
        self.controller = controller


        owimg= tk.PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=100,y=54)
        dtrimg= tk.PhotoImage(file="docdoc.png")
        self.dtrimg=dtrimg
        dtpanel=tk.Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=990,y=54)
        btn_bg= tk.PhotoImage(file="blank.png")
        self.btn_bg= btn_bg
        blank1=tk.Label(self,image=btn_bg,borderwidth=0)   
        blank1.place(x=365,y=237)
        btn_bg3= tk.PhotoImage(file="reg.png")
        self.btn_bg3= btn_bg3
        dtpanel4=tk.Label(self,text=f"Welcome {login}",fg="black", bg="white",borderwidth=0,font=('Helvetica',40), justify='center')
        dtpanel4.place(x=400,y=155)
        pin_entry = tk.Entry(self,fg="black", bg="white", width=15,borderwidth=0,font=('Helvetica',40), justify='center', show="*")
        pin_entry.insert(0, "Confirm pin")
        pin_entry.place( x=375,y=250)
        keys=['1','2','3','4','5','6','7','8','9','DELETE','0','ENTER']

        button=[]
        
        def enter():
            global pin
            pin_confirm = pin_entry.get()
            if pin != pin_confirm:
                play("wpin")
                controller.show_frame("PinPage")
            
            else:
                controller.show_frame("StartPage")

        def select(value):
            if value == "DELETE":
                pin_entry.delete(len(pin_entry.get())-1)

            elif value == "ENTER":
                enter()

            else:
                pin_entry.insert(tk.END, value)

        def show_keyboard():
            index = 0
            varRow = 2
            varColumn = 0
            for letter in keys:
                command = lambda x=letter: select(x)
                button.append(tk.Button(self, text=letter, width=5, bg="#22272c", fg="#ffffff",
                    activebackground="#5ce1e6", activeforeground="#000000", relief="raised", padx=10,
                    pady=10, bd=4, font=("Helvetica", 20), justify="center", command=command))
                button[index].place(y=varRow+400, x=varColumn+450)
                index+=1

                varColumn += 110
                if varColumn > 220:
                    varColumn = 0
                    varRow += 75
        
        def usrclicked(event):
            global pin_entry_flag
            if pin_entry_flag != 1:
                pin_entry.delete(0, tk.END)
                pin_entry.config(fg="black")
                play("enterpin")
            show_keyboard()
        pin_entry.bind("<1>", usrclicked)

    def on_show_frame(self, event):
        pass