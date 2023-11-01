""" init """

import tkinter as tk

from controller import Controller
from model import Model
from view import View


class App(tk.Tk):
    """ init app """
    def __init__(self):
        super().__init__()

        model = Model("example.fimpp")

        view = View(self)

        controller = Controller(model, view)

        view.set_controller(controller)


if __name__ == '__main__':
    app = App()
    app.mainloop()
