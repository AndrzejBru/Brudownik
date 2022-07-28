import tkinter as tk

import datetime as dt # dla obsługi daty i czasu

class Application:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("300x40")
        
        self.lb_clock = tk.Label(self.window, font = ("Times New Roman", 20))
        self.lb_clock.pack()
        
        self.timer() # pierwsze wywołanie metody timer
        
        self.window.mainloop()
        
    def timer(self):
        self.lb_clock.config(text = str(dt.datetime.now().time()).split(".")[0]) # poberanie czasu
        self.window.after(1000, self.timer) # ustawienie kolejnego wywołania metody timer

apl = Application()
