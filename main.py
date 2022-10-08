#!/usr/bin/env python
import tkinter as tk
from tkinter import messagebox as mb
from time import strftime
from math import ceil, floor

time1 = strftime("%S")


def average(list):
    result = 0
    for i in list:
        result += int(i)
    return result / len(list)


def deleteSpaces(data):
    result = ''
    for i in range(len(data)):
        if not (data[i] == ' ' and data[i + 1]) == ' ':
            result += data[i]
    return result


class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('Калькулятор оценок 😎')
        self.master.iconbitmap(r"icon.ico")
        self.master.geometry("475x300+550+245")
        self["bg"] = "white"
        self.createLabel1 = None
        self.outputLabel = None
        self.inputField = None
        self.quitButton = None
        self.okButton = None
        self.continuePass = False
        self.inputs = 0
        self.grid(sticky=tk.N + tk.S + tk.E + tk.W)
        self.createWidgets()
        self.drawImages()
        self.inputList = []

    def finalResult(self):
        self.inputList = deleteSpaces(self.inputField.get(1.0, tk.END)[:-1]).split(' ')
        print(self.inputList, len(self.inputList))
        print(self.inputs)
        if self.inputList == ['0', '2', '1', '2', '2'] and self.inputs == 5:
            mb.showwarning(title="Дождь из тако!!! :0", message="Внимание! Вы нашли пасхалку с тако, вы - молодец!\n🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮🌮 😋")

        if len(self.inputList) != self.inputs:
            if mb.askyesno(title="Ошибка!",
                           message="Вы ввели неверное количество аргументов,\nвы можете продолжить с текущими данными нажав 'Да'\nили повторить ввод, нажав кнопку 'Нет'"):
                self.continuePass = True

            else:
                self.inputField.delete(1.0, tk.END)
                self.createLabel1.destroy()
                self.createWidgets()
        else:
            self.continuePass = True

        if self.continuePass:
            self.continuePass = False
            result = average(self.inputList)

            if result % 1.0 >= 0.65:
                finalResult = ceil(result)
            else:
                finalResult = floor(result)

            self.outputLabel = tk.Label(
                text=f"Средний балл - {round(result, 3)}, финальная оценка - '{finalResult}'",
                bg="white")
            self.outputLabel.grid(row=0, column=0, sticky=tk.S, pady=50)

    def gotoNextStep(self):
        self.inputs = 0
        self.inputs = int(self.inputField.get(1.0, tk.END))
        self.okButton["command"] = self.finalResult
        self.createLabel1["text"] = "А теперь введите оценки ученика,\nв указанном ранее количестве (или нет)"
        self.inputField.delete(1.0, tk.END)
        self.continuePass = True

    def createWidgets(self):
        top = self.winfo_toplevel()  # создание ссылки на самое верхнее окно на экране

        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)  # делает колонки и строки верхнего окна растяжимыми

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)  # делает колонки и строки приложения растяжимыми

        self.createLabel1 = tk.Label(anchor="center", text="Введите число оценок ученика", bg="white", fg="#31409F",
                                     font=("TimesNewRoman", 11))
        self.quitButton = tk.Button(self, text='Выход', command=self.quit, width=10)
        self.okButton = tk.Button(self, text='OK', width=10, state=tk.DISABLED, command=self.gotoNextStep)
        self.inputField = tk.Text(bg="white", height=1, width=45)

        self.createLabel1.grid(row=0, column=0, sticky=tk.NW, pady=7)
        self.inputField.grid(row=0, column=0)
        self.quitButton.grid(row=2, column=2, sticky=tk.SW, padx=3, pady=4)
        self.okButton.grid(row=2, column=3, sticky=tk.SW, padx=3, pady=4)

    def checkInput(self):
        fromField = self.inputField.get(1.0)
        if fromField != '\n' and fromField.isdigit():
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

    def drawImages(self):
        global backpackimage, logoimage
        backpackimage = tk.PhotoImage(file="backpack.png")
        backpacklabel = tk.Label(self.master, image=backpackimage, bg="white")
        backpacklabel.grid(row=0, column=0, sticky=tk.SW)

        logoimage = tk.PhotoImage(file="logo.png")
        logolabel = tk.Label(self.master, image=logoimage, bg="white")
        logolabel.grid(row=0, column=0, sticky=tk.NE)

    def deleteErrorMessage(self):

        pass

app = App()
app.onTick()
app.mainloop()
