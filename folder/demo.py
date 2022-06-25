from tkinter import *
from tkinter import ttk

rows = 20
columns = 20


window = Tk()
window.title("Minesweeper v.Sean.0")
window.minsize(width=500, height=500)

mainframe = ttk.Frame(window, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

# Label
label = Label()
label.config(text="Careful where you click")
label.pack()


def make_grid(num):
    l_list = []
    count = 0
    column = 0
    row = 0
    for i in range(num):
        if num == columns:
            column = 0
            row += 1
        l_list.append(ttk.Label(mainframe, text=" ", relief="raised", width=2))
        l_list[i].grid(column=column, row=row)
        column += 1
        count += 1
        

make_grid(20)
        