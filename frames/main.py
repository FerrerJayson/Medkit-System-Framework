import tkinter as tk
from registration import NamePage, PinPage, PinConfirmPage
from mainscreen import ActiveScreen, HomePage
from medication_setup import PageOne, PageTwo, PageThree, PageFour
from login import StartPage
from pySerialTransfer import pySerialTransfer as txfer

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
        for F in (ActiveScreen, HomePage, StartPage, NamePage, PinPage, PinConfirmPage, PageOne, PageTwo, PageThree, PageFour):
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