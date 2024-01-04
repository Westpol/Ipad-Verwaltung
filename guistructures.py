import tkinter as tk
from tkinter import ttk
import time


class Frontend:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(960, 540))

    def choose(self, guiselect: str):

        match guiselect:
            case "1":
                self.welcome_screen()
            case _:
                pass

        self.root.mainloop()

    def destroy_wigets(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def welcome_screen(self):

        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        subMenu = tk.Menu()

        menu.add_cascade(label="file", menu=subMenu)

        subMenu.add_cascade(label="Import Database")
        subMenu.add_cascade(label="Export Database")
        subMenu.add_cascade(label="New Database")
        subMenu.add_cascade(label="Export .xlsx")

        style = ttk.Style()
        style.configure("style1.TFrame", background="green")
        style.configure("style1.welcome.TFrame", background="red")
        style.configure("style1.exit.TFrame", background="yellow")

        welcome_message = ttk.Frame(self.root, style="style1.TFrame")
        welcome_message.configure(width=960, height=500)
        welcome_message.grid()


frontend = Frontend()
frontend.choose(input("which gui to show?"))
print([ m for m in dir(frontend) if not m.startswith('__')])
