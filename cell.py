from tkinter import Button
import random
import math
import settings


class Cell:
    all = []
    
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
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
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
    
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