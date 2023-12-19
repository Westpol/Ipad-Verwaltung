import json
import tkinter
import time

ipads = {}

with open("Data/Ipads.json", "r") as jsonfile:
    Ipads = json.load(jsonfile)

Ipads["opendate"] = int(time.time())
print(Ipads)

with open("Data/Ipads.json", "w") as file:
    json.dump(Ipads, file, indent=4)
