
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QBoxLayout, QLabel)

class widgets_right(QWidget):
    def __init__(self):
        super(widgets_right, self).__init__()
        self.wrbox = QHBoxLayout()
        self.wrbox.setContentsMargins(0,0,10,0)
        self.wrbox.setDirection(QBoxLayout.LeftToRight)
        self.wrbox.setSpacing(0)
        self.setLayout(self.wrbox)
        lbl2 = QLabel("test")
        self.wrbox.addWidget(lbl2)
