from PySide2.QtWidgets import * 
from PySide2.QtGui import * 
from PySide2.QtCore import *

class Main(QDialog):
    _borderSize = 1
    _bottomWidth = 140

    def __init__(self, parent=None):
        super().__init__(parent)
        

        self.setWindowFlags(Qt.Popup)

        self.setGeometry(100, 100, 50, 100)
        # self.setStyleSheet(" Main { border: 1px solid red; }")
        self.setStyleSheet(" background-color: #000000; color: #FFFFFF;")
        

        layout_TLP = QHBoxLayout()
        combo_TLPMode = QComboBox()
        combo_TLPMode.addItems(["on (BAT)", "on (AC)", "off"])
        layout_TLP.addWidget(QLabel("TLP Mode: "))
        layout_TLP.addWidget(combo_TLPMode)
        layout_TLP.addStretch()

        layout_sleepTime = QHBoxLayout()
        layout_sleepTime.addWidget(QLabel("SleepTime"))
        layout_sleepTime.addStretch()

        layout_main = QVBoxLayout()
        layout_main.addLayout(layout_TLP)
        layout_main.addLayout(layout_sleepTime)
        # layout_main.addChildWidget(scene)

        self.setLayout(layout_main)
        self.show()
        print(self.minimumWidth())
        # self.move(0, 0)


    def paintEvent(self, event):
        # the border width could be odd, so we must convert
        # the rectangle to QRectF which supports floating point
        # coordinates, which is also better for QPainter
        rect = QRectF(self.rect())
        half = self._borderSize / 2
        rect.adjust(half, half, -half, -half)
        bottomLeft = QPointF(rect.left(), rect.bottom() + half)
        bottomRight = QPointF(self._bottomWidth, rect.bottom())

        qp = QPainter(self)
        qp.setRenderHints(qp.Antialiasing)
        qp.setPen(QPen(Qt.red, self._borderSize))
        qp.drawPolyline(QPolygonF((
            bottomLeft,
            rect.topLeft(),
            rect.topRight(),
            rect.bottomRight(),
            bottomRight
        )))




app = QApplication([])
main = Main()
main.exec_()
