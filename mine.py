import os
from javax.swing import (
    BorderFactory, JPanel, JLabel, ImageIcon, SwingUtilities,
)
from java.awt import (
    Color, Font,
)
from java.awt.event import MouseListener
from settings import *



class Mine(JPanel):
    PRESSED_COLOR = (184, 207, 229)

    INITIAL = 0
    FLAGGED = 1
    FALSE_POSITIVE = 2
    REVEALED = 3
    BLAST = 4

    WARNING_SIGN_IMAGE = os.path.join(os.getcwd(), 'assets', 'warning-sign.png')
    MINE_IMAGE = os.path.join(os.getcwd(), 'assets', 'mine.png')

    def __init__(self, id, data, mines):
        super(JPanel, self).__init__()
        self.id = id
        self.data = data
        self.state = Mine.INITIAL
        self.flagged = False
        self.pressed = False
        self.parent_ = mines
        self.label = JLabel()
        self.setBackground(Color.WHITE)
        self.setBorder(BorderFactory.createLineBorder(Color.BLACK, 1))
        self.label.setFont(Font("Arial", Font.BOLD, 30))
        self.add(self.label)
        self.addMouseListener(self.MineActionListener(self))

    class MineActionListener(MouseListener):
        
        def __init__(self, btn):
            super(MouseListener, self).__init__()
            self.btn = btn

        def mouseEntered(self, mouse_event): pass
        def mouseExited(self, mouse_event): pass
        def mousePressed(self, mouse_event): pass
        def mouseReleased(self, mouse_event): pass

        def mouseClicked(self, mouse_event):
            if SwingUtilities.isLeftMouseButton(mouse_event):
                self.btn.onLeftClick()
            if SwingUtilities.isRightMouseButton(mouse_event):
                self.btn.onRightClick()
    
    def updateDisplay(self):
        if self.state == Mine.INITIAL:
            self.label.setIcon(None)
        elif self.state == Mine.FLAGGED:
            self.label.setIcon(ImageIcon(Mine.WARNING_SIGN_IMAGE))
        elif self.state == Mine.FALSE_POSITIVE:
            pass
        elif self.state == Mine.REVEALED:
            self.setBackground(Color(*Mine.PRESSED_COLOR))
            if 0 < self.data < INF:
                self.label.setText(str(self.data))
            elif self.data == INF:
                self.label.setIcon(ImageIcon(Mine.MINE_IMAGE))
        elif self.state == Mine.BLAST:
            self.setBackground(Color.RED)
            self.label.setIcon(ImageIcon(Mine.MINE_IMAGE))

    def onRightClick(self):
        if self.state in [Mine.INITIAL, Mine.FLAGGED]:
            if self.state == Mine.INITIAL:
                self.state = Mine.FLAGGED
            elif self.state == Mine.FLAGGED:
                self.state = Mine.INITIAL
            self.updateDisplay()

    def onLeftClick(self):
        if self.state == Mine.INITIAL:
            if self.data == 0:
                self.state = Mine.REVEALED
                self.updateDisplay()
                self.parent_.bfs(self.id)
                return
            
            if self.data < INF:
                self.state = Mine.REVEALED
            else:
                self.state = Mine.BLAST
            self.updateDisplay()
    
    def bfsClick(self):
        if self.state != Mine.REVEALED:
            self.state = Mine.REVEALED
            self.updateDisplay()
    
    def gameOver(self):
        pass
    
    def __str__(self):
        return "Mine: " + str(self.id)
