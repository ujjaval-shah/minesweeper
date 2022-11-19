import random
from javax.swing import (
    JFrame, JPanel, 
    JButton, JToggleButton, BorderFactory,
    ImageIcon, Box, BoxLayout,
    SwingUtilities,
)
from java.awt import (
    GridLayout, BorderLayout, FlowLayout,
    Label, Image, Dimension, Color, Font, Insets,
    Component,
)
from java.awt.event import MouseListener
from mine import Mine
from settings import *



class Mines(JPanel):
    
    def __init__(self):
        super(JPanel, self).__init__()
        self.setLayout(GridLayout(GRID_SIZE, GRID_SIZE))
        self.setBorder(BorderFactory.createEmptyBorder(MARGIN, MARGIN, MARGIN, MARGIN))

        self.arrangeMines()
        self.buttons = [[Mine(i*GRID_SIZE+j, self.cells[i][j]) for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                self.add(self.buttons[i][j])

    def getPreferredSize(self):
        return Dimension(LENGTH, LENGTH)

    def is_valid(self, x):
        return 0 <= x[0] < GRID_SIZE and 0 <= x[1] < GRID_SIZE
    
    def arrangeMines(self):
        self.cells = [[0 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]

        mines_set = set()
        while len(mines_set) < TOTAL_MINES:
            mine = random.randrange(GRID_SIZE*GRID_SIZE)
            mines_set.add(mine)
        
        for mine in mines_set:
            cell = (mine // GRID_SIZE, mine % GRID_SIZE)

            neighbours = [
                (cell[0]-1, cell[1]-1),
                (cell[0]-1, cell[1]),
                (cell[0]-1, cell[1]+1),
                (cell[0], cell[1]-1),
                (cell[0], cell[1]+1),
                (cell[0]+1, cell[1]-1),
                (cell[0]+1, cell[1]),
                (cell[0]+1, cell[1]+1),
            ]

            self.cells[cell[0]][cell[1]] = INF

            for ncell in neighbours:
                if self.is_valid(ncell):
                    self.cells[ncell[0]][ncell[1]] += 1
        
        for row in self.cells:
            print(row)
