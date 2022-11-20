import os
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
from java.awt.event import ActionListener
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
    INITIAL_IMAGE = os.path.join(os.getcwd(), 'assets', 'slightly-smiling-face.png')
    VICTORY_IMAGE = os.path.join(os.getcwd(), 'assets', 'smiling-face-with-sunglasses.png')
    GAME_OVER_IMAGE = os.path.join(os.getcwd(), 'assets', 'face-with-head-bandage.png')

    def __init__(self):
        self.state = YET_TO_START

        self.frame = JFrame("Minesweeper")
        self.frame.setResizable(False)
        self.frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE)
        self.frame.setLayout(BorderLayout())


        topbar = TopbarWrapper()
        
        topbar.add(Label("MINES LEFT"), BorderLayout.WEST)

        self.restartBtn = JButton()
        
        restart_wrap = JPanel()
        self.restartBtn.setMargin(Insets(0,0,0,0))
        
        self.restartBtn.setIcon(ImageIcon(Game.INITIAL_IMAGE))
        self.restartBtn.setFocusPainted(False)
        self.restartBtn.setPreferredSize(Dimension(60, 60))
        self.restartBtn.setBackground(Color.WHITE)
        self.restartBtn.addActionListener(Game.restartBtnActionListener(self))
        restart_wrap.add(self.restartBtn)

        topbar.add(restart_wrap, BorderLayout.CENTER)

        topbar.add(Label("TIME TAKEN"), BorderLayout.EAST)

        self.frame.getContentPane().add(topbar, BorderLayout.NORTH)


        self.grid = Mines(self)
        self.frame.getContentPane().add(self.grid, BorderLayout.CENTER)

        
        self.frame.pack()
        self.frame.setVisible(True)
    
    class restartBtnActionListener(ActionListener):
        
        def __init__(self, game):
            super(ActionListener, self).__init__()
            self.game = game

        def actionPerformed(self, e):
            self.game.restart()

    
    def isGameEnded(self):
        return self.state == VICTORY or self.state == GAME_OVER
    
    def setState(self, state):
        if self.state == state:
            return

        self.state = state
        self.updateGame()
    
    def updateGame(self):
        if self.state == YET_TO_START:
            # print "new grid"
            self.frame.remove(self.grid)
            self.grid = Mines(self)
            self.frame.getContentPane().add(self.grid, BorderLayout.CENTER)
            self.frame.revalidate()
            self.frame.pack()
            print "two textbox reset"
            # print "restart button icon updated"
            self.restartBtn.setIcon(ImageIcon(Game.INITIAL_IMAGE))
        elif self.state == STARTED:
            print "timer started"
        elif self.state == VICTORY:
            print "timer stopped"
            # print "flag remaining mines"
            self.grid.onVictory()
            # print "restart button icon updated"
            self.restartBtn.setIcon(ImageIcon(Game.VICTORY_IMAGE))
        elif self.state == GAME_OVER:
            print "timer stopped"
            # print "reveal all mines"
            # print "falsely flagged cells color"
            self.grid.onGameOver()
            # print "restart button icon updated"
            self.restartBtn.setIcon(ImageIcon(Game.GAME_OVER_IMAGE))
    
    def restart(self):
        self.setState(YET_TO_START)