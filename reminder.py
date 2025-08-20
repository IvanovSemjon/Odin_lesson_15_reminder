from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание", font=("Arial Bold", 20))
label.pack(pady=10)
set_button = Button(text="Установить напоминание", font=("Arial Bold", 20), command=set)
set_button.pack(pady=10)

window.mainloop()