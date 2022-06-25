from cgitb import text
from tkinter import *



SIZE_X = 10
SIZE_Y = 10

#new window
class Minesweeper:
    
    
    def __init__(self):
        self.window = Tk()
        self.window.title("Minesweeper v.Sean.0")
        self.window.minsize(width=500, height=500)

        # Label
        self.label = Label()
        self.label.config(text="Careful where you click")
        self.label.pack()

        self.button_bootcamp = Button(text="Bootcamp", command=self.bootcamp)
        self.button_bootcamp.pack()
        self.button_infantry = Button(text="Infantry", command=self.infantry)
        self.button_infantry.pack()
        self.button_veteran = Button(text="Special Forces", command=self.special_forces)
        self.button_veteran.pack()



        self.window.mainloop()


    # Buttons
    def reveal():
        """
        On tile left click, reveal all blank tiles or explode if tile contains mine
        On tile right click, place a flag
        """

    def play_again():
        """
        remove all tiles and show play again button which could just run create_field() again
        """
        

    def bootcamp(self):
        """
        Create a field with x number of mines, surrounding tiles contain hidden number? 
        No tile can touch more than 3 mines?
        """
        pass
        self.label.config(text="Welcome to Bootcamp")
        self.label.pack()
        self.label2 = Label()
        self.label2.config(text="High Score: ")
        self.label2.pack()
            
        self.button_bootcamp.destroy()
        self.button_infantry.destroy()
        self.button_veteran.destroy()
            
        
        
    def infantry(self):
        pass
    
    def special_forces(self):
        pass

    def flag(self):
        self.label.configure(text="🏴‍☠️")

    def make_tiles(self, number):
        self.number = number
        self.count = 0
        self.column = 0
        self.row = 0
        for i in range(0, number):
            pass