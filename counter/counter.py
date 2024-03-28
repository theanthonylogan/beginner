from tkinter import *
from tkinter import ttk


class Counter:
    def __init__(self, root):

        root.title("Counter")

        mainframe = ttk.Frame(root, padding="12 12 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.count = IntVar(value=0)
        print(self.count.get())
        ttk.Label(mainframe, textvariable=self.count).grid(
            column=2, row=1, sticky=(W, E)
        )
        ttk.Button(mainframe, text="Count", command=self.counter).grid(
            column=2, row=2, sticky=(W, E)
        )

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        root.bind("<Return>", self.counter)

    def counter(self, *args):
        value = self.count.get()
        self.count.set(value + 1)


root = Tk()
Counter(root)
root.mainloop()
