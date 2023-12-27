import json
import PySimpleGUI as psg
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
        self.welcome = [[psg.Text("Scan Barcode in this Textbox"), psg.Input(key="IT-num")],
                        [psg.Button('Submit', visible=False, bind_return_key=True)]]
        self.window = None
        self.event, self.values = None, None

    def begin(self):
        self.window = psg.Window('Ipad-Verwaltung', self.welcome)
        self.event, self.values = self.window.read()
        print(self.values["IT-num"])
        self.window.close()
        self.window = psg.Window('Ipad-Verwaltung', self.welcome)
        self.event, self.values = self.window.read()
        print(self.values["IT-num"])

    def close(self):
        self.backend.close()

    def add(self, itnum: str):
        version: str = str(input("Version: "))
        surname: str = input("Surname: ")
        name: str = input("Name: ")
        classNum = input("Class: ")
        subclass: str = input("Subclass: ")
        self.backend.addnew(itnum, version, surname, name, classNum, subclass)

    def show(self, itnum: str):
        print(self.backend.get_ipad(itnum))
        showStats = [[],
                     [],
                     [],
                     [],
                     []]

    def get_num(self):
        welcome = self.welcome
        self.window = psg.Window('Ipad-Verwaltung', welcome)
        event, values = self.window.read()
        self.window.close()
        if self.backend.inlist(values["IT-num"]):
            self.show(values["IT-num"])


if __name__ == "__main__":
    front = Frontend()
    front.get_num()
    front.close()
