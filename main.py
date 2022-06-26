from tkinter import *
from turtle import left
import settings
import utils
from cell import Cell


root = Tk()
# Override window settings
root.configure(bg=settings.BG)
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper v.Sean.0")
root.resizable(False, False)

top_frame = Frame(
    root, 
    bg=settings.BG,
    width=settings.WIDTH,
    height=utils.height_pct(25)
    )
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='green',
    fg='white',
    text='Watch your step',
    font=('American Typewriter', 30)
)
game_title.place(
    x=utils.width_pct(35),
    y=utils.height_pct(10)
)

left_frame = Frame(
    root,
    bg=settings.BG,
    width=utils.width_pct(25),
    height=utils.height_pct(75)
)
left_frame.place(x=0, y=utils.height_pct(25))

center_frame = Frame(
    root,
    bg=settings.BG,
    width=utils.width_pct(75),
    height=utils.height_pct(75)
)
center_frame.place(
    x=utils.width_pct(25),
    y=utils.height_pct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )
        
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()
for cell in Cell.all:
    print(cell.is_mine)

# Run Window
root.mainloop()