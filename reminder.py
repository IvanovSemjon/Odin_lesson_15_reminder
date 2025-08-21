from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import datetime
import time
import pygame


t = 0

def set():
    global t
    rem = sd.askstring('Время напоминания', 'Введте время напоминания в формате ЧЧ:ММ (24 часовой формат)')
    if rem is None:
        try:
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute)
            t = dt.timestamp()
        except Exception as e:
            mb.showerror(f'Ошибка! Неверный формат времени --> {e}')


def check():
    global t
    if t != 0:
        now = time.time()
        if now >= t:
            play_sound()
            t = 0
    window.after(1000, check)


def play_sound():
    pygame.mixer.init()
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

window = Tk()
window.title("Напоминание")
label = Label(text="Установите напоминание", font=("Arial Bold", 20))
label.pack(pady=10)
set_button = Button(text="Установить напоминание", font=("Arial Bold", 20), command=set)
set_button.pack(pady=10)

window.mainloop()