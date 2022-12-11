from view import View
from model import Model
from controller import Controller
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        model = Model("example.fimpp")

        view = View(self)

        controller = Controller(model, view)

        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
