
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QBoxLayout, QLabel)

class widgets_left(QWidget):
    def __init__(self):
        super(widgets_left, self).__init__()
        self.wlbox = QHBoxLayout()
        self.wlbox.setContentsMargins(0,0,10,0)
        self.wlbox.setDirection(QBoxLayout.LeftToRight)
        self.wlbox.setSpacing(0)
        self.setLayout(self.wlbox)
        lbl1 = QLabel("test")
        self.wlbox.addWidget(lbl1)
