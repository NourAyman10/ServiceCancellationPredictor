import background as background
import pandas as pd
from tkinter import ttk
from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title("Service cancellation predictor")
root.iconbitmap()
root.geometry("700x500")

style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="orange", background="red", foreground='blue', selectbackground='black')

value = StringVar()
combobox = ttk.Combobox(root, values=["hi", "hello", "bye"])
combobox.config()
combobox.current(0)


def action(event):
    value = combobox.get()
    print(value)


combobox.bind("<<ComboboxSelected>>", action)
combobox.pack()

root.mainloop()
