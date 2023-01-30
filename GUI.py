from tkinter import *
from tkinter import messagebox
import os

win = Tk()
win.title("Internship")
win.geometry('1920x1080')
win.maxsize(1920, 1080)
#win.configure(background='green')

def run():
    while(True):
        os.system('python captureAndDetect.py')
        os.system('python faceCompareLIB.py')
        os.system('python extractAndVerifyDetails.py')
        os.system("python result.py")
        os.system('del img1.jpg img2.jpg NewImg1.jpg NewImg2.jpg result.txt')


Label(win, text = "Automated Verification Of Air Travellers at Airport!", font= ('Helvetica 25 bold', 32)).place(relx=.5, rely=.2, anchor= CENTER)
btn = Button(win, text="Verify", bg="black", fg="white", height = 5, width = 15, command=run).place(relx=0.5, rely=0.8, anchor=CENTER)

win.mainloop()