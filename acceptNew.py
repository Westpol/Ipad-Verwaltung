import json
import pygame
import tkinter
import time

Ipads = {"moddate": int(time.time()), "Ipads": {"IT18563": {"name": "Benno Schörmann", "Klasse": 13},
                                                "IT18363": {"name": "Benno Schörmann", "Klasse": 13}}}

Ipads["Ipads"].update({"IT16563": {"name": "Benno Schörmann", "Klasse": 13}})

inpt: str = str(input("Scan IPad:"))

if inpt in Ipads["Ipads"]:
    print(Ipads["Ipads"][inpt])
else:
    print("Neu anlegen? [y/n]")
    if input() == "y":
        Ipads["Ipads"].update({inpt: {"name": "Benno Schörmann", "Klasse": 13}})
print(Ipads)
