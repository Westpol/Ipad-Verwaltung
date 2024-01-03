import tkinter as tk
from tkinter import ttk, scrolledtext


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Information")

        # Anmerkungen Section (Left Half)
        self.anmerkungen_frame = ttk.Frame(root)
        self.anmerkungen_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10)

        self.anmerkungen_label = ttk.Label(self.anmerkungen_frame, text="Anmerkungen:")
        self.anmerkungen_label.pack(anchor="w", padx=10)

        self.anmerkungen_entry = scrolledtext.ScrolledText(self.anmerkungen_frame, wrap=tk.WORD, width=40, height=10)
        self.anmerkungen_entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))

        # User Frame (Right Half)
        self.user_frame = ttk.Frame(root)
        self.user_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10)

        self.name_label = ttk.Label(self.user_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.name_entry = ttk.Entry(self.user_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        self.schoolclass_label = ttk.Label(self.user_frame, text="Schoolclass:")
        self.schoolclass_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.schoolclass_entry = ttk.Entry(self.user_frame)
        self.schoolclass_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.teacher_label = ttk.Label(self.user_frame, text="Teacher:")
        self.teacher_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.teacher_entry = ttk.Entry(self.user_frame)
        self.teacher_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.edit_button = ttk.Button(self.user_frame, text="Edit")
        self.edit_button.grid(row=3, column=0, columnspan=2, pady=10)

        # History Button
        self.history_button = ttk.Button(root, text="History")
        self.history_button.pack(side=tk.RIGHT, padx=10)

        # Save, Save and Exit, Exit buttons
        self.save_button = ttk.Button(root, text="Save")
        self.save_button.pack(side=tk.LEFT, padx=5)
        self.save_exit_button = ttk.Button(root, text="Save and Exit")
        self.save_exit_button.pack(side=tk.LEFT, padx=5)
        self.exit_button = ttk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(side=tk.LEFT, padx=5)


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
