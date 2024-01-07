import json
import tkinter as tk
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
        self.root.geometry("{}x{}".format(960, 540))
        self.root.minsize(960, 540)
        self.root.maxsize(960, 540)
        self.root.bind("<KeyPress>", self.keylogger)

        self.dropdown_menu()

        self.keyData = []

        self.welcome_screen()

    def dropdown_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        sub_menu = tk.Menu()

        menu.add_cascade(label="file", menu=sub_menu)

        sub_menu.add_cascade(label="Import Database")
        sub_menu.add_cascade(label="Export Database")
        sub_menu.add_cascade(label="New Database")
        sub_menu.add_cascade(label="Export .xlsx")

    def welcome_screen(self):
        welcome_screen = tk.Label(self.root, text="Scan Ipad to see Information...", font=("Arial", 30))
        welcome_screen.place(relx=.5, rely=.4, anchor=tk.CENTER)
        manual_search = tk.Button(self.root, text="Manual Search (in Progress...)", font=("Arial", 15))
        manual_search.pack(anchor="w", side="bottom")

    def keylogger(self, event):
        self.keyData.append((event.char, time.time()))

    def close(self):
        self.backend.close()

    def mainloop(self):
        self.root.mainloop()
        self.close()


if __name__ == "__main__":
    frontend = Frontend()
    frontend.mainloop()
