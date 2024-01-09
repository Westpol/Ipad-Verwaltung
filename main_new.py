import json
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import time

# TODO
'''
Backend is ONLY used as the json Interface
at the beninging, the data is stored in a dict variable, and saved when saved button is pressed 

- Status label in frontend.showData über tk.stringVar ändern und nicht durch reset und call von showData
- textbox and state shouldn't be saved by changing the status
'''


class Backend:

    def __init__(self):
        self.device_dict = {}
        with open("Data/Ipads.json", "r") as jsonfile:      # loading json file and storing it globally, to save in the end
            self.device_dict = json.load(jsonfile)
        self.device_dict["opendate"] = int(time.time())

    def addNew(self, itnum: str, version: str, surname: str, name: str, classNum, subClass: str):      # creating a dict with new info and adding it to the existing dict
        data = {itnum: {"moddate": int(time.time()), "version": version, "surname": surname, "name": name, "class": classNum, "subclass": subClass, 'repair': False, 'repairdate': 0, 'dosys': False, 'comments': ''}}
        self.device_dict["Ipads"].update(data)

    def save(self):
        with open("Data/Ipads.json", "w") as file:
            json.dump(self.device_dict, file, indent=4)

    def inList(self, itnum: str):       # returns true or false if the given IT number is in dict or not
        if itnum in self.device_dict["Ipads"]:
            return True
        return False

    def getIpad(self, itnum: str):      # returns dict with the Information stored about the Ipad
        if self.inList(itnum):
            return self.device_dict["Ipads"][itnum]
        raise "given IT-number not in system, bofore requesting directly, please check with inlist()"

    def delete_ipad(self, itnum: str):
        del self.device_dict["Ipads"][itnum]


class Frontend:

    def __init__(self):
        self.backend = Backend()

        self.keyData = []
        self.accept_scan = False
        self.itnum = ""

        self.root = tk.Tk()
        self.root.geometry("{}x{}".format(960, 540))
        self.root.minsize(960, 540)
        self.root.maxsize(960, 540)
        self.root.bind("<KeyPress>", self.keylogger)

        self.dropdownMenu()
        self.welcomeScreen()

    def begin(self):
        self.root.mainloop()
        self.backend.save()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.dropdownMenu()

    def dropdownMenu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        sub_menu = tk.Menu()

        menu.add_cascade(label="file", menu=sub_menu)

        sub_menu.add_cascade(label="Import Database")
        sub_menu.add_cascade(label="Export Database")
        sub_menu.add_cascade(label="New Database")
        sub_menu.add_cascade(label="Export .xlsx")

    def welcomeScreen(self):
        self.accept_scan = True
        welcome_screen = tk.Label(self.root, text="Scan Ipad to see Information...", font=("Arial", 30))
        welcome_screen.place(relx=.5, rely=.4, anchor=tk.CENTER)
        manual_search = tk.Button(self.root, text="Manual Search (in Progress...)", font=("Arial", 15))
        manual_search.pack(anchor="w", side="bottom")

    def showData(self, infos: dict, itnum: str):

        def changeStatus():
            if infos["status"] == 0:
                infos["status"] = 1
            elif infos["status"] == 1:
                infos["status"] = 2
            else:
                infos["status"] = 0
            setStatus()

        def setStatus():
            if infos["status"] == 1:
                statusVar.set("Status:  In Reperatur")
            elif infos["status"] == 2:
                statusVar.set("Status:  Bei Dosys eingesendet")
            else:
                statusVar.set("Status:  Standard")

        def editUserWindow():
            childWindow = tk.Toplevel(self.root)

        self.accept_scan = False

        self.root.columnconfigure(0, weight=2)
        self.root.columnconfigure((1, 2, 3), weight=1)

        notes = tk.Label(self.root, text="Anmerkungen:", font=("Arial", 15))
        textfield = ScrolledText(self.root)
        textfield.insert("1.0", str(infos["comments"]))

        user = tk.Label(self.root, text="Besitzer:", font=("Arial", 15))
        name = tk.Label(self.root, text=str("Name:  " + infos["surname"] + " " + infos["name"]))

        if infos["subclass"] is not None:
            classs = tk.Label(self.root, text=str("Klasse:  " + str(infos["class"]) + "." + str(infos["subclass"])))
        else:
            classs = tk.Label(self.root, text=str("Klasse:  " + str(infos["class"])))

        teacher = tk.Label(self.root, text=str("Lehrer:  " + infos["teacher"]))

        besitzer_bearbeiten = tk.Button(self.root, text="Bearbeiten", command=editUserWindow)

        device = tk.Label(self.root, text="Gerät:", font=("Arial", 15))

        statusVar = tk.StringVar(self.root, "")
        setStatus()

        status = tk.Label(self.root, textvariable=statusVar)

        history = tk.Button(self.root, text="Status ändern", command=changeStatus)

        save_button = tk.Button(self.root, text="Save", command=lambda: self.saveData(infos, textfield.get("1.0", "end"), itnum))
        save_exit_button = tk.Button(self.root, text="Save + Exit", command=lambda: self.saveAndExit(infos, textfield.get("1.0", "end"), itnum))
        exit_button = tk.Button(self.root, text="Exit", command=lambda: self.exitShowData())

        textfield.grid(row=1, column=0, rowspan=7, padx="20")
        notes.grid(row=0, column=0, sticky="w")
        user.grid(row=0, column=1, columnspan=3, sticky="w")
        name.grid(row=1, column=1, columnspan=3, sticky="w")
        classs.grid(row=2, column=1, columnspan=3, sticky="w")
        teacher.grid(row=3, column=1, columnspan=2, sticky="w")
        besitzer_bearbeiten.grid(row=3, column=3, sticky="w")
        device.grid(row=4, column=1, columnspan=3, sticky="w")
        status.grid(row=5, column=1, columnspan=3, sticky="w")
        history.grid(row=6, column=1, columnspan=3, sticky="w")
        save_button.grid(row=8, column=1)
        save_exit_button.grid(row=8, column=2)
        exit_button.grid(row=8, column=3)

    def exitShowData(self):
        self.clear()
        self.welcomeScreen()

    def saveAndExit(self, infos: dict, textbox: str, itnum: str):
        self.saveData(infos, textbox, itnum)
        self.exitShowData()

    def saveData(self, infos: dict, textbox: str, itnum: str):
        infos["comments"] = textbox[0:len(textbox)-1:1]
        self.backend.device_dict["Ipads"][itnum] = infos
        self.backend.save()

    def getScan(self):     # returns itnum
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
        self.keyData = []

        if self.itnum != "":
            return self.itnum
        else:
            return None

    def keylogger(self, event):
        if self.accept_scan:
            if event.keysym == "Return":
                self.keyData.append(("\n", time.time()))
                itnum = self.getScan()
                if itnum is not None:
                    self.clear()
                    print(itnum)
                    self.showData(self.backend.getIpad(itnum), itnum)
            else:
                self.keyData.append((event.char, time.time()))


if __name__ == "__main__":
    frontend = Frontend()
    frontend.begin()
