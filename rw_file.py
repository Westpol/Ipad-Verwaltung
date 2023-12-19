import json
import tkinter
import time

ipads = {}

with open("Data/Ipads.json", "r") as jsonfile:
    jsonstring: str = ""
    for i in jsonfile.readlines():
        jsonstring += str(i)
    ipads = json.loads(jsonstring)


