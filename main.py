import json
import pygame
import tkinter
import time

Ipads = {"moddate": int(time.time()), "Ipads": {"IT18563": {"name": "Benno Schörmann", "Klasse": 13}, "IT18363": {"name": "Benno Schörmann", "Klasse": 13}}}

Ipads["Ipads"].update({"IT16563": {"name": "Benno Schörmann", "Klasse": 13}})

for i in Ipads["Ipads"]:
    print(i)
    print(Ipads["Ipads"][i])
 