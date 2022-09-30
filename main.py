#!/usr/bin/env python
import tkinter as tk
from time import strftime

time1 = strftime("%S")


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Калькулятор оценок 😎')
        self.master.iconbitmap(r"icon.ico")
        self.master.geometry("400x250+550+245")
        self["bg"] = "white"
        self.createLabel1 = None
        self.inputField = None
        self.quitButton = None
        self.okButton = None
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.createWidgets()

    def createWidgets(self):
        top = self.winfo_toplevel()  # создание ссылки на самое верхнее окно на экране

        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)  # делает колонки и строки верхнего окна растяжимыми

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)  # делает колонки и строки приложения растяжимыми

        self.createLabel1 = tk.Label(anchor="center", text="Введите число оценок ученика", bg="white", fg="#31409F",
                                     font=("TimesNewRoman", 11))
        self.quitButton = tk.Button(self, text='Отмена', command=self.quit, width=10)
        self.okButton = tk.Button(self, text='OK', width=10, state=tk.DISABLED)
        self.inputField = tk.Text(bg="white", height=1, width=45)

        self.createLabel1.grid(row=0, column=0, sticky=tk.NW, pady=7)
        self.inputField.grid(row=0, column=0)
        self.quitButton.grid(row=2, column=2, sticky=tk.SW, padx=3, pady=4)
        self.okButton.grid(row=2, column=3, sticky=tk.SW, padx=3, pady=4)

    def checkInput(self):
        fromField = self.inputField.get(1.0)
        if fromField != '\n' and fromField.isdigit():
            print(self.inputField.get(1.0))
            self.okButton["state"] = tk.ACTIVE
        else:
            self.okButton["state"] = tk.DISABLED

    def onTick(self):
        global time1
        time2 = strftime("%S")
        if time2 != time1:
            time1 = time2
            self.checkInput()
        self.inputField.after(200, self.onTick)

app = App()
app.onTick()
app.mainloop()
