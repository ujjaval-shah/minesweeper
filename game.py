import os
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
from mines import Mines
from settings import *


class TopbarWrapper(JPanel):
    
    def __init__(self):
        super(JPanel, self).__init__()
        self.setLayout(BorderLayout())
        self.setBorder(BorderFactory.createEmptyBorder(MARGIN, MARGIN, MARGIN, MARGIN))

    def getPreferredSize(self):
        return Dimension(LENGTH, 100)


class Game:

    def __init__(self):
        frame = JFrame("Minesweeper")
        frame.setResizable(False)
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        frame.setLayout(BorderLayout())


        topbar = TopbarWrapper()
        
        topbar.add(Label("MINES LEFT"), BorderLayout.WEST)

        restart = JButton()
        
        restart_wrap = JPanel()
        restart.setMargin(Insets(0,0,0,0))
        
        img = os.path.join(os.getcwd(), 'assets', 'slightly-smiling-face.png')
        restart.setIcon(ImageIcon(img))
        restart.setFocusPainted(False)
        restart.setPreferredSize(Dimension(60, 60))
        restart.setBackground(Color.WHITE)
        restart_wrap.add(restart)

        topbar.add(restart_wrap, BorderLayout.CENTER)

        topbar.add(Label("TIME TAKEN"), BorderLayout.EAST)

        frame.getContentPane().add(topbar, BorderLayout.NORTH)


        minus_grid = Mines()
        frame.getContentPane().add(minus_grid, BorderLayout.CENTER)

        
        frame.pack()
        frame.setVisible(True)
