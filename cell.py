from tkinter import Button, Label
import random
import math
import settings


class Cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None
    
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.cell_btn_object = None
        self.x = x
        self.y = y
        # Append the object to the Cell.all list
        Cell.all.append(self)
        
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=settings.GRID_SIZE//4,
            height=settings.GRID_SIZE//4
        )
        btn.bind('<Button-1>', self.left_click)
        btn.bind('<Button-2>', self.right_click)
        self.cell_btn_object = btn
        
    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location, 
            text=f"Cells Left: {Cell.cell_count}",
            bg="black",
            fg="white",
            font=("Typewriter", 26)
            )
        Cell.cell_count_label_object = lbl
        
    def left_click(self, event):
        print(self.is_mine)
        # print("Left Click")
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell in self.surrounded_cells:
                    cell.show_cell()
            self.show_cell()
        
    def show_cell(self):
        if not self.is_opened:
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            # Replace cell count label with updated cell count
            Cell.cell_count -= 1
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f"Cells Remaining: {Cell.cell_count}"
                    )
        # Mark the cell as opened now that it's open
        self.is_opened = True
    
    @property
    def surrounded_cells_mines_length(self):
        count = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                count += 1
        return count
    
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell != None]
        return cells
        
    def show_mine(self):
        self.cell_btn_object.configure(text="🏴‍☠️")
    
    def get_cell_by_axis(self, x, y):
        # Return a cell object base on value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    def right_click(self, event):
        print(event)
        print("Right Click")
        
    @staticmethod
    def randomize_mines():
        mines = random.sample(Cell.all, 
                              math.floor(len(Cell.all)/4))
        for mine in mines:
            mine.is_mine = True
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"