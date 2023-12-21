import json
import tkinter as tk
import tkinter.ttk as ttk
import time


class Backend:
    def __init__(self):
        self.Ipads = {}
        with open("Data/Ipads.json", "r") as jsonfile:
            self.Ipads = json.load(jsonfile)
        self.Ipads["opendate"] = int(time.time())

    def addnew(self):
        itnum: str = str(input("Scan Barcode: "))
        version: str = str(input("Version: "))
        surname: str = input("Surname: ")
        name: str = input("Name: ")
        classNum = input("Class: ")
        subclass: str = input("Subclass: ")
        Data = {itnum: {"moddate": int(time.time()), "version": version, "surname": surname, "name": name, "class": classNum, "subclass": subclass, 'repair': False, 'repairdate': 0, 'dosys': False, 'comments': ''}}
        self.Ipads["Ipads"].update(Data)

    def close(self):
        with open("Data/Ipads.json", "w") as file:
            json.dump(self.Ipads, file, indent=4)


class Frontend:
    def __init__(self):
        self.backend = Backend()
        self.data = self.backend.Ipads

    def close(self):
        self.backend.close()

    def dump(self):
        print(self.data)

    def add(self):
        self.backend.addnew()


if __name__ == "__main__":
    front = Frontend()
    front.add()
    front.dump()
    front.close()
