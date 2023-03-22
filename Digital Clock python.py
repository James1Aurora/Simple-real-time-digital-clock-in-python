#PROJECT AURORA Digital Clock
from tkinter import *
from tkinter.ttk import *

from time import strftime

main = Tk()
main.title('Jam Digital Akbar')

def jam():
    tick = strftime('%H:%M:%S %p')

    jam_label .config(text=tick)

    jam_label .after(1000, jam)

jam_label = Label(main, font=('times',80), background = 'red', foreground = 'white')

jam_label.pack(anchor='center')

jam()
mainloop()