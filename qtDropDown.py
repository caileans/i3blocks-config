from PySide2.QtWidgets import * 
from PySide2.QtGui import * 
from PySide2.QtCore import *

class QtDropDown(QDialog):
    _borderSize = 1
    _bottomBorderLeft = 1
    _bottomBorderRight = 1
    _borderColor = "#FF0000"
    _secondBorderColor = None
    _secondBorderSize = None
    _xPos = 0
    _yPos = 0
    _width = 50
    _justified = "center"

    def __init__(self, xPos, yPos, width, justified, qss, borderColor = "#FF0000", borderSize = 1, secondBorderColor = None, secondBorderSize = 1, parent=None):
        super().__init__(parent)

        self._xPos = xPos
        self._yPos = yPos
        self._width = width
        self._justified = justified
        self._borderColor = borderColor
        self._borderSize = borderSize
        self._secondBorderColor = secondBorderColor
        self._secondBorderSize = secondBorderSize


        self.setWindowFlags(Qt.Popup)
        self.setGeometry(self._xPos, self._yPos, self._width, 0)
        self.setStyleSheet(qss)
        self.hide()
        self.setModal(True)
        # self.setFocus()

        # self.reposition()

        



    def paintEvent(self, event):
        # the border width could be odd, so we must convert
        # the rectangle to QRectF which supports floating point
        # coordinates, which is also better for QPainter

        qp = QPainter(self)
        qp.setRenderHints(qp.Antialiasing)

        rect = QRectF(self.rect())
        half = self._borderSize / 2
        btmLft = 0
        btmRt = 0

        if self._secondBorderColor:
            mainRectInset = half + self._secondBorderSize
            rect.adjust(mainRectInset, mainRectInset, -mainRectInset, -mainRectInset)
            btmLft = QPointF(self._bottomBorderLeft - half, rect.bottom())
            btmRt = QPointF(self._bottomBorderRight + half, rect.bottom())
            
            secHalf = self._secondBorderSize / 2
            secondBorderOffset = half + secHalf
            inRect = rect.adjusted(secondBorderOffset, secondBorderOffset, -secondBorderOffset, -secondBorderOffset)
            outRect = rect.adjusted(-secondBorderOffset, -secondBorderOffset, secondBorderOffset, secondBorderOffset)
            secInBtmLft = QPointF(self._bottomBorderLeft - self._secondBorderSize, rect.bottom() - secondBorderOffset)
            secInBtmRt = QPointF(self._bottomBorderRight + self._secondBorderSize, rect.bottom() - secondBorderOffset)
            secOutBtmLft = QPointF(self._bottomBorderLeft - self._secondBorderSize, rect.bottom() + secondBorderOffset)
            secOutBtmRt = QPointF(self._bottomBorderRight + self._secondBorderSize, rect.bottom() + secondBorderOffset)

            qp.setPen(QPen(QColor(self._secondBorderColor), self._secondBorderSize))

                    
            qp.drawPolyline(QPolygonF((
                secInBtmLft,
                inRect.bottomLeft(),
                inRect.topLeft(),
                inRect.topRight(),
                inRect.bottomRight(),
                secInBtmRt,
                secOutBtmRt,
                outRect.bottomRight(),
                outRect.topRight(),
                outRect.topLeft(),
                outRect.bottomLeft(),
                secOutBtmLft
            )))

        
        else:
            rect.adjust(half, half, -half, -half)
            btmLft = QPointF(self._bottomBorderLeft, rect.bottom())
            btmRt = QPointF(self._bottomBorderRight, rect.bottom())

        qp.setPen(QPen(QColor(self._borderColor), self._borderSize))

        
        qp.drawPolyline(QPolygonF((
            btmLft,
            rect.bottomLeft(),
            rect.topLeft(),
            rect.topRight(),
            rect.bottomRight(),
            btmRt
        )))

        # self.hide()
        # self.setModal(True)
        # self.show()
        self.clearFocus()
        self.setFocus()
        self.grabMouse()

        # qp = QPainter(self)
        # qp.setRenderHints(qp.Antialiasing)

        # rect = QRectF(self.rect())
        # half = self._borderSize / 2
        # rect.adjust(half, half, -half, -half)
        # btmLft = QPointF(self._bottomBorderLeft, rect.bottom())
        # btmRt = QPointF(self._bottomBorderRight, rect.bottom())

        
        # qp.setPen(QPen(QColor(self._borderColor), self._borderSize))
        # qp.drawPolyline(QPolygonF((
        #     btmLft,
        #     rect.btmLft(),
        #     rect.topLeft(),
        #     rect.topRight(),
        #     rect.btmRt(),
        #     btmRt
        # )))
        # # self.hide()
        # # self.setModal(True)
        # # self.show()
        # self.clearFocus()
        # self.setFocus()
        # self.grabMouse()
    


    def addContent(self, contentLayout):
        self.setLayout(contentLayout)
        self.show()
        self.reposition()

    def reposition(self):
        
        if self._justified == "right":
            x = self.x()
            self._bottomBorderLeft = 0
            self._bottomBorderRight = self._width
        if self._justified == "left":
            x = self.x() - (self.width() - self._width)
            self._bottomBorderLeft = self.width() - self._width
            self._bottomBorderRight = self.width()
        else:
            x = self.x() - (self.width() - self._width)/2.0
            self._bottomBorderLeft = (self.width() - self._width)/2
            self._bottomBorderRight = self.width() - (self.width() - self._width)/2.0
        self.move(x, self.y()  - self.height())
        self.update()
