import tkinter as tk
import tkinter.ttk as ttk


class Window:
    def __init__(self):
        self.window = tk.Tk()

    def setup(self):
        self.window.geometry("1000x500")
        self.window.title("Ipad Verwaltung GeS-Scharnhorst")

    def mainloop(self):
        self.window.mainloop()


if __name__ == "__main__":
    window = Window()
    window.setup()
    window.mainloop()

