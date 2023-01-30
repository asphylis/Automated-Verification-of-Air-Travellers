from tkinter import *
from tkinter import messagebox


f = open("result.txt", "r")
content = f.read()
if content == "TrueVerified":
    messagebox.showinfo("Result", "Please Proceed")
else:
    messagebox.showerror("Result", "Please Try Again")
f.close()