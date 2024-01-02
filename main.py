import json
import tkinter as tk
from tkinter import ttk
import time


class Backend:
    def __init__(self):     # loading json file and converting it into a dict
        self.Ipads = {}
        with open("Data/Ipads.json", "r") as jsonfile:
            self.Ipads = json.load(jsonfile)
        self.Ipads["opendate"] = int(time.time())

    def addnew(self, itnum: str, version: str, surname: str, name: str, class_num, subclass: str):      # creating a dict with new info and adding it to the existing dict
        data = {itnum: {"moddate": int(time.time()), "version": version, "surname": surname, "name": name, "class": class_num, "subclass": subclass, 'repair': False, 'repairdate': 0, 'dosys': False, 'comments': ''}}
        self.Ipads["Ipads"].update(data)

    def close(self):
        with open("Data/Ipads.json", "w") as file:
            json.dump(self.Ipads, file, indent=4)

    def inlist(self, itnum: str):
        if itnum in self.Ipads["Ipads"]:
            return True
        return False

    def get_ipad(self, itnum: str):
        if self.inlist(itnum):
            return self.Ipads["Ipads"][itnum]
        raise "given IT-number not in system, bofore requesting directly, please check with inlist()"

    def delete_ipad(self, itnum: str):
        del self.Ipads["Ipads"][itnum]


class Frontend:
    def __init__(self):
        self.backend = Backend()
        self.root = tk.Tk()
        self.content = ttk.Frame(self.root)

        onevar = tk.BooleanVar(value=True)
        twovar = tk.BooleanVar(value=False)
        threevar = tk.BooleanVar(value=True)

        onevar.set(True)
        twovar.set(False)
        threevar.set(True)

        one = ttk.Checkbutton(self.content, text="One", variable=onevar, onvalue=True)
        two = ttk.Checkbutton(self.content, text="Two", variable=twovar, onvalue=True)
        three = ttk.Checkbutton(self.content, text="Three", variable=threevar, onvalue=True)
        ok = ttk.Button(self.content, text="Okay")
        cancel = ttk.Button(self.content, text="Cancel")

        self.content.grid(column=0, row=0)

        one.grid(column=0, row=1)
        two.grid(column=1, row=2)
        three.grid(column=2, row=3)
        ok.grid(column=3, row=4)
        cancel.grid(column=4, row=5)

    def close(self):
        self.backend.close()

    def mainloop(self):
        self.root.mainloop()
        self.close()


if __name__ == "__main__":
    frontend = Frontend()
    frontend.mainloop()
