from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.v = StringVar()
        self.window = parent
        self.window.geometry('750x600')
        self.window.title('FiM++')
        self.greeting = Label(self.window,
                              text='\nНапишите свою программу на языке FiM++!\n',
                              font=('Arial Bold', 20),
                              anchor=CENTER)
        self.entry = ScrolledText(self.window,
                                  bd=5,
                                  font="Arial 16",
                                  width=50,
                                  wrap=NONE,
                                  height=15)
        self.button_space = Label(self.window,
                                  text='\n')
        self.do_work_button = Button(self.window,
                                     text="Отослать письмо",
                                     font=('Arial Bold', 16),
                                     pady=5,
                                     anchor=CENTER)

        self.greeting.pack()
        self.entry.pack(anchor=CENTER)
        self.button_space.pack()
        self.do_work_button.pack()

        self.controller = None

    def set_controller(self, controller):
        self.controller = controller

        self.do_work_button.configure(command=self.controller.start_program)
        self.entry.bind('<Double-Button-1>', self.controller.set_breakpoint)
        self.entry.bind('<Button-3>', self.controller.delete_breakpoint)
