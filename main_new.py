import json
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import time

# TODO
'''
Backend is ONLY used as the json Interface
at the beninging, the data is stored in a dict variable, and saved when saved button is pressed 
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
        self.keyData = []
        self.accept_scan = False

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
        self.keyData = []

        if self.itnum != "":
            return self.itnum
        else:
            return None

    def begin(self):
        pass


if __name__ == "__main__":
    frontend = Frontend()
    frontend.begin()
