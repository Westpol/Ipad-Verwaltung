import json
import tkinter as tk
import tkinter.ttk as ttk
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

    def print_ipad(self, itnum: str):
        if self.inlist(itnum):
            return self.Ipads["Ipads"][itnum]
        raise "given IT-number not in system, bofore requesting directly, please check with inlist()"

    def delete_ipad(self, itnum: str):
        del self.Ipads["Ipads"][itnum]


class Frontend:
    def __init__(self):
        self.backend = Backend()
        self.data = self.backend.Ipads

    def close(self):
        self.backend.close()

    def dump(self):
        print(self.data)

    def add(self, itnum: str):
        version: str = str(input("Version: "))
        surname: str = input("Surname: ")
        name: str = input("Name: ")
        classNum = input("Class: ")
        subclass: str = input("Subclass: ")
        self.backend.addnew(itnum, version, surname, name, classNum, subclass)

    def get_num(self):
        itnum: str = str(input("Scan Barcode: "))
        if self.backend.inlist(itnum):
            print(self.backend.print_ipad(itnum))
            if input("Do you want to delete the entrance? [delete/n]") == "delete":
                self.backend.delete_ipad(itnum)
        else:
            if input("IT number not in system, want to add? [y/n]") == "y":
                self.add(itnum)
            else:
                print("mkayyyy")


if __name__ == "__main__":
    front = Frontend()
    front.get_num()
    front.close()
