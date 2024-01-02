import tkinter as tk
from tkinter import ttk


class Frontend:
    def __init__(self):
        self.root = tk.Tk()

    def choose(self, guiselect: str):
        match guiselect:
            case "1":
                self.welcome_screen()
            case _:
                pass
        self.root.mainloop()

    def welcome_screen(self):

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        subMenu = tk.Menu()

        menu.add_cascade(label="file", menu=subMenu)

        subMenu.add_cascade(label="Import Database")
        subMenu.add_cascade(label="Export Database")
        subMenu.add_cascade(label="New Database")
        subMenu.add_cascade(label="Export .xlsx")

        content = ttk.Frame(self.root)
        onevar = tk.BooleanVar(value=True)
        twovar = tk.BooleanVar(value=False)
        threevar = tk.BooleanVar(value=True)

        onevar.set(True)
        twovar.set(False)
        threevar.set(True)

        one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
        ok = ttk.Button(content, text="Okay")
        cancel = ttk.Button(content, text="Cancel")

        content.grid(column=0, row=0)

        one.grid(column=0, row=1)
        two.grid(column=1, row=2)
        three.grid(column=2, row=3)
        ok.grid(column=3, row=4)
        cancel.grid(column=4, row=5)


frontend = Frontend()
frontend.choose(input("which gui to show?"))
