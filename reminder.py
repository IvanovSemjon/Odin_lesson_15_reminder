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
    if rem is not None:
        try:
            if ':' not in rem:
                mb.showerror('Ошибка!', 'Время должно содержать двоеточие между часами и минутами')
                set()
                return
            hour = int(rem.split(':')[0])
            minute = int(rem.split(':')[1])
            if hour < 0 or hour > 23:
                mb.showerror('Ошибка!', 'Часы должны быть в диапазоне от 0 до 23')
                set()
                return
            if minute < 0 or minute > 59:
                mb.showerror('Ошибка!', 'Минуты должны быть в диапазоне от 0 до 59')
                set()
                return
            now = datetime.datetime.now()
            dt = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            t = dt.timestamp()
            text = sd.askstring('Текст напоминания', 'Введите текст напоминания')
            label.config(text=f'Напоминание установлено на {hour:02}:{minute:02} с текстом "{text}"')
        except Exception as e:
            mb.showerror('Ошибка!', f'Неверный формат времени: {e}')
            set()


def check():
    global t
    if t != 0:
        now = time.time()
        if now >= t:
            play_sound()
            t = 0
    window.after(1000, check)


def play_sound():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()


def stop_music():
    global music
    if music:
        pygame.mixer.music.stop()
        music = False
    pygame.mixer.music.stop()
    label.config(text='Установить новое напоминание')


window = Tk()
window.title("Напоминание")
window.geometry("300x200")
label = Label(text="Установите напоминание", font=("Arial Bold", 10))
label.pack(pady=10)
set_button = Button(text="Установить напоминание", font=("Arial Bold", 10), command=set)
set_button.pack(pady=10)

stop_button = Button(text="Остановить музыку", font=("Arial Bold", 10), command=stop_music)
stop_button.pack(pady=10)

check()
window.mainloop()