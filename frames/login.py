import tkinter as tk
import time
import pandas as pd
from pygame import mixer
import os.path
from variables import link, login, pin, board, BayOne, BayTwo, BayThree, BayFour, BayFive, BaySix, BaySeven, BayEight, BayNine
name_entry_flag = 0
pin_entry_flag = 0

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
        wrgloh=tk.Label(self,text="Wrong Username or Password",font=('Helvetica', 20),bg="white",fg="#D9D9D9",borderwidth=0)
        userimg= tk.PhotoImage(file="user.png")
        self.userimg=userimg
        passimg= tk.PhotoImage(file="pass.png")
        self.passimg=passimg
        usrpanel=tk.Label(self,image=userimg,borderwidth=0)
        usrpanel.place(x=200,y=300)
        username_entry = tk.Entry(self,fg="#D9D9D9", bg="#F8F8F8", width=28,borderwidth=0,font=('Helvetica', 20))
        username_entry.insert(0, "  Username")
        username_entry.place( x=280,y=310)
        passpanel=tk.Label(self,image=passimg,borderwidth=0)
        passpanel.place(x=200,y=390)
        passnentry = tk.Entry(self,fg="#D9D9D9", bg="#F8F8F8", width=28,borderwidth=0,font=('Helvetica', 20),show="*")
        passnentry.insert(0, "  Password")
        passnentry.place( x=280,y=400)

        def back():
            controller.show_frame("HomePage")


        def printme():
            pass

        fingerprint_button=tk.Button(self,height=127,width=380,font=('Helvetica', 40),text="LOG IN  >",fg="white",bg="white",borderwidth=0,image=btn_bg3, command=printme )
        fingerprint_button.place(x=800,y=320)

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
                username_entry.delete(len(username_entry.get())-1)

            elif value == "ENTER":
                global login
                login = username_entry.get()
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
                button[index].place(y=varRow+480, x=varColumn+20)
                index+=1

                varColumn += 110
                if varColumn > 1200:
                    varColumn = 0
                    varRow += 75

        keypad=['1','2','3','4','5','6','7','8','9','DELETE','0','ENTER']

        keypad_buttons=[]
        
        def enter_keypad():
            for b in keypad_buttons:
                b.place_forget()
            name=username_entry.get()
            pas=passnentry.get()
            df = pd.read_csv(f'./accounts/{name}.csv')
            pin = str(df['Pin'][0])
            if os.path.exists(f'./accounts/{name}.csv'):
                if pin.rstrip(pin[-1]) == str(pas):
                    controller.show_frame("PageOne")
                    passnentry.delete(0, tk.END)
                    play('entersucess')
                else:
                    play('wpin')
                    passnentry.delete(0, tk.END)
            else:
                wrgloh.place(x=300,y=310)
                play('wrongme')

        def select_keypad(value):
                if value == "DELETE":
                    passnentry.delete(len(passnentry.get())-1)

                elif value == "ENTER":
                    enter_keypad()

                else:
                    passnentry.insert(tk.END, value)

        def show_keypad():
            index = 0
            varRow = 2
            varColumn = 0
            for letter in keypad:
                command = lambda x=letter: select_keypad(x)
                keypad_buttons.append(tk.Button(self, text=letter, width=5, bg="#22272c", fg="#ffffff",
                    activebackground="#5ce1e6", activeforeground="#000000", relief="raised", padx=10,
                    pady=10, bd=4, font=("Helvetica", 20), justify="center", command=command))
                keypad_buttons[index].place(y=varRow+480, x=varColumn+450)
                index+=1

                varColumn += 110
                if varColumn > 220:
                    varColumn = 0
                    varRow += 75

        #display logo
        owimg= tk.PhotoImage(file="ownum.png")
        self.owimg=owimg
        owpanel=tk.Label(self,image=owimg,borderwidth=0)
        owpanel.place(x=170,y=54)
        back_button = tk.Button(self, text="BACK", font= ('Helvetica', 20), command=back)
        back_button.place(x=10, y=10)
        
        #display additional designs
        ntimg= tk.PhotoImage(file="next.png")
        self.ntimg=ntimg
        ntpanel=tk.Label(self,image=ntimg,borderwidth=0)
        ntpanel.place(x=170,y=200)
        
        dtrimg= tk.PhotoImage(file="doctors.png")
        self.dtrimg=dtrimg
        dtpanel=tk.Label(self,image=dtrimg,borderwidth=0)
        dtpanel.place(x=770,y=0)

        def usrclicked(event):
            global name_entry_flag
            if name_entry_flag != 1:
                username_entry.delete(0, tk.END)
                username_entry.config(fg="black")
                name_entry_flag = 1
            try:
                for b in keypad_buttons:
                    b.place_forget()
            except:
                pass
            show_keyboard()

        def passclicked(event):
            global pin_entry_flag
            if pin_entry_flag != 1:
                passnentry.delete(0, tk.END)
                passnentry.config(fg="black")
                pin_entry_flag = 1
            try:
                for b in button:
                    b.place_forget()
            except:
                pass
            show_keypad()

        username_entry.bind("<1>", usrclicked)
        passnentry.bind("<1>", passclicked)

    def on_show_frame(self, event):
        BayOne.write(1)
        BayTwo.write(1)