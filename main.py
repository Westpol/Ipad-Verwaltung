import json
import tkinter as tk
import time

''' 
TODO:
- sort variables (frontend / backend)
- assign every job to frontend / backend
- show the info in a useful way
'''


class Backend:
    def __init__(self):     # loading json file and converting it into a dict
        self.Ipads = {}
        with open("Data/Ipads.json", "r") as jsonfile:
            self.Ipads = json.load(jsonfile)
        self.Ipads["opendate"] = int(time.time())

        self.keyData = []
        self.itnum = ""
        self.accept_scan = False

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

    def get_scan(self):     # returns itnum
        self.itnum = ""

        time_delta = self.keyData[len(self.keyData) - 1][1]
        temp_string = ""

        for i in reversed(range(0, len(self.keyData) - 1)):
            if 0.005 < time_delta - self.keyData[i][1] < 0.025:
                temp_string += self.keyData[i][0]
            else:
                if time_delta - self.keyData[i][1] > 0.01:
                    break
                else:
                    if self.keyData[i][0] != "":
                        temp_string += self.keyData[i][0]
            time_delta = self.keyData[i][1]
        self.itnum = temp_string[::-1]

        return self.itnum


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
        self.accept_scan = False

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
        self.accept_scan = True

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def keylogger(self, event):
        if self.accept_scan:
            if event.keysym == "Return":
                self.backend.keyData.append(("\n", time.time()))
                itnum = self.backend.get_scan()
                if itnum is not None:
                    self.clear()
                    self.dropdown_menu()
                    print(itnum)
            else:
                self.backend.keyData.append((event.char, time.time()))

    def close(self):
        self.backend.close()

    def mainloop(self):
        self.root.mainloop()
        self.close()


if __name__ == "__main__":
    frontend = Frontend()
    frontend.mainloop()
