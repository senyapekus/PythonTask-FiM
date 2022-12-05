from tkinter import *
import tkinter as tk


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.entry_text = ""

    def start_program(self):
        result_window = Tk()
        result_window.geometry('460x300')
        result_window.title('Ответ')
        answer_greeting = Label(result_window,
                                text="\nПришел ответ на ваше письмо:\n",
                                font=('Arial Bold', 16),
                                anchor=CENTER)

        self.entry_text = self.view.entry.get('1.0', tk.END)

        answer = Label(result_window,
                       font=('Arial Bold', 14),
                       text=self.entry_text,
                       justify=LEFT,
                       relief=SUNKEN,
                       padx=10,
                       pady=10)

        answer_greeting.pack()
        answer.pack()

        print(self.entry_text)
