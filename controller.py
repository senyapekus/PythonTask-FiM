import os
from tkinter import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import compiler

breakpoint_count = 0


class Controller:
    def __init__(self, model, view):
        self.answ = ""
        self.model = model
        self.view = view

        self.entry_text = ""

    def start_program(self):
        self._py_window = Tk()
        self._py_window.geometry('600x500')
        self._py_window.title('Отправить в таком виде?')
        answer_greeting = Label(self._py_window,
                                text="\nПринцесса увидит ваше письмо следующим образом:\n",
                                font=('Arial Bold', 16),
                                anchor=CENTER)

        self.entry_text = self.view.entry.get('1.0', tk.END)

        with open(self.model.text_file, "w", encoding='utf8') as fimpp_file:
            fimpp_file.write(self.entry_text)

        try:
            compiler.Compiler(self.model.text_file)
        except Exception as e:
            self.answ = e

        answer_greeting.pack()

        if compiler.has_breakpoint:
            self.print_py_program("py_program/example_debug.py")
        else:
            self.print_py_program("py_program/example.py")
            
    def print_py_program(self, py_file):
        with open(py_file, "r", encoding='utf8') as p_file:
            text = p_file.readlines()
        for i in text:
            self.answ += i

        py_program = ScrolledText(self._py_window,
                                  font=('Arial Bold', 14),
                                  width=50,
                                  height=15,

                                  relief=SUNKEN,
                                  padx=10,
                                  pady=10)
        py_program['text'] = py_program.insert(1.0, self.answ)

        get_answer_button = Button(self._py_window,
                                   text="Отослать письмо",
                                   command=self.print_answer,
                                   font=('Arial Bold', 16),
                                   pady=5,
                                   anchor=CENTER)

        py_program.pack()
        get_answer_button.pack()

    def print_answer(self):
        global breakpoint_count
        result_window = Tk()
        result_window.geometry('460x300')
        result_window.title('Ответ')

        try:
            if breakpoint_count != 0:
                pipe = os.popen("python py_program/example_debug.py")
                res = pipe.read()
            else:
                pipe = os.popen("python py_program/example.py")
                res = pipe.read()
        except Exception:
            res = "Ошибка выполнения"

        answer_greeting = Label(result_window,
                                text="\nПришел ответ на ваше письмо:\n",
                                font=('Arial Bold', 16),
                                anchor=CENTER)
        py_answer = Label(result_window,
                          font=('Arial Bold', 14),
                          text=res,
                          justify=LEFT,
                          relief=SUNKEN,
                          padx=10,
                          pady=10)

        answer_greeting.pack()
        py_answer.pack()

    def set_breakpoint(self, event):
        global breakpoint_count

        breakpoint_count += 1
        line = self.view.entry.index("insert").partition(".")[0]
        self.view.entry.insert(f"{line}.end", "    b")
        self.view.entry.tag_add('breakpoint', f"{line}.0", f"{line}.end")
        self.view.entry.tag_config('breakpoint', background='#B22222')

    def delete_breakpoint(self, event):
        global breakpoint_count

        line = self.view.entry.index("insert").partition(".")[0]
        text = self.view.entry.get(f"{line}.0", f"{line}.end")
        if text[-5:] == "    b":
            breakpoint_count -= 1
            self.view.entry.tag_delete('sel')
            self.view.entry.delete(f"{line}.{len(text) - 5}", f"{line}.end")
            self.view.entry.tag_add('del_breakpoint', f"{line}.0", f"{line}.end")
            self.view.entry.tag_config('del_breakpoint', background='white')
            
