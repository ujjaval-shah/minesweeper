import os
from javax.swing import (
    JToggleButton, ImageIcon, SwingUtilities,
)
from java.awt import (
    Color, Font, Insets,
)
from java.awt.event import MouseListener
from settings import *



class Mine(JToggleButton):

    def __init__(self, id, data, mines):
        super(JToggleButton, self).__init__()
        self.id = id
        self.data = data
        self.flagged = False
        self.pressed = False
        self.parent_ = mines
        self.setBackground(Color.WHITE)
        self.setMargin(Insets(0,0,0,0))
        self.setFocusPainted(False)
        self.setFont(Font("Arial", Font.BOLD, 30))
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
    
    def onRightClick(self):
        if not self.pressed:
            if not self.flagged:
                self.flagged = True
                img = os.path.join(os.getcwd(), 'assets', 'warning-sign.png')
                self.setIcon(ImageIcon(img))
            else:
                self.flagged = False
                self.setIcon(None)

    def onLeftClick(self):
        if self.flagged or self.pressed:
            # Nullify the toggle effect
            # by clicking the button Twice
            self.doClick()
            return

        if self.data == 0:
            self.parent_.bfs(self.id)
            pass
        elif self.data < INF:
            self.setText(str(self.data))
        else:
            # GAME OVER
            img = os.path.join(os.getcwd(), 'assets', 'mine.png')
            self.setIcon(ImageIcon(img))
        self.pressed = True
    
    def bfsClick(self):
        if not self.pressed:
            if self.flagged:
                self.onRightClick()
            # always called by parent component
            # during epmpty area bfs
            if 0 < self.data < INF:
                self.setText(str(self.data))
            self.pressed = True
            self.doClick()
    
    def gameOver(self):
        pass
    
    def __str__(self):
        return "Mine: " + str(self.id)
