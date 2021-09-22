#include <QtDropDownTemp.h>


void QtDropDown(const int xPos, const int yPos, const int width, Justification justified, char *qss, char * borderColor = "#FF0000", const int borderSize = 1, char *secondBorderColor = NULL, const int secondBorderSize = 1);
    // super().__init__(parent)

    this._xPos = xPos;
    this._yPos = yPos;
    this._width = width;
    this._justified = justified;
    this._borderColor = borderColor;
    this._borderSize = borderSize;
    this._secondBorderColor = secondBorderColor;
    this._secondBorderSize = secondBorderSize;


    this.setWindowFlags(Qt.Popup)
    this.setGeometry(this._xPos, this._yPos, this._width, 0)
    this.setStyleSheet(qss)
    this.hide()
    this.setModal(True)
    # this.setFocus()

    # this.reposition()

    



def paintEvent(this, event):
    # the border width could be odd, so we must convert
    # the rectangle to QRectF which supports floating point
    # coordinates, which is also better for QPainter

    qp = QPainter(this)
    qp.setRenderHints(qp.Antialiasing)

    rect = QRectF(this.rect())
    half = this._borderSize / 2
    btmLft = 0
    btmRt = 0

    if this._secondBorderColor:
        mainRectInset = half + this._secondBorderSize
        rect.adjust(mainRectInset, mainRectInset, -mainRectInset, -mainRectInset)
        btmLft = QPointF(this._bottomBorderLeft - half, rect.bottom())
        btmRt = QPointF(this._bottomBorderRight + half, rect.bottom())
        
        secHalf = this._secondBorderSize / 2
        secondBorderOffset = half + secHalf
        inRect = rect.adjusted(secondBorderOffset, secondBorderOffset, -secondBorderOffset, -secondBorderOffset)
        outRect = rect.adjusted(-secondBorderOffset, -secondBorderOffset, secondBorderOffset, secondBorderOffset)
        secInBtmLft = QPointF(this._bottomBorderLeft - this._secondBorderSize, rect.bottom() - secondBorderOffset)
        secInBtmRt = QPointF(this._bottomBorderRight + this._secondBorderSize, rect.bottom() - secondBorderOffset)
        secOutBtmLft = QPointF(this._bottomBorderLeft - this._secondBorderSize, rect.bottom() + secondBorderOffset)
        secOutBtmRt = QPointF(this._bottomBorderRight + this._secondBorderSize, rect.bottom() + secondBorderOffset)

        qp.setPen(QPen(QColor(this._secondBorderColor), this._secondBorderSize))

                
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
        btmLft = QPointF(this._bottomBorderLeft, rect.bottom())
        btmRt = QPointF(this._bottomBorderRight, rect.bottom())

    qp.setPen(QPen(QColor(this._borderColor), this._borderSize))

    
    qp.drawPolyline(QPolygonF((
        btmLft,
        rect.bottomLeft(),
        rect.topLeft(),
        rect.topRight(),
        rect.bottomRight(),
        btmRt
    )))

    # this.hide()
    # this.setModal(True)
    # this.show()
    this.clearFocus()
    this.setFocus()
    this.grabMouse()

    # qp = QPainter(this)
    # qp.setRenderHints(qp.Antialiasing)

    # rect = QRectF(this.rect())
    # half = this._borderSize / 2
    # rect.adjust(half, half, -half, -half)
    # btmLft = QPointF(this._bottomBorderLeft, rect.bottom())
    # btmRt = QPointF(this._bottomBorderRight, rect.bottom())

    
    # qp.setPen(QPen(QColor(this._borderColor), this._borderSize))
    # qp.drawPolyline(QPolygonF((
    #     btmLft,
    #     rect.btmLft(),
    #     rect.topLeft(),
    #     rect.topRight(),
    #     rect.btmRt(),
    #     btmRt
    # )))
    # # this.hide()
    # # this.setModal(True)
    # # this.show()
    # this.clearFocus()
    # this.setFocus()
    # this.grabMouse()



def addContent(this, contentLayout):
    this.setLayout(contentLayout)
    this.show()
    this.reposition()

def reposition(this):
    
    if this._justified == "right":
        x = this.x()
        this._bottomBorderLeft = 0
        this._bottomBorderRight = this._width
    if this._justified == "left":
        x = this.x() - (this.width() - this._width)
        this._bottomBorderLeft = this.width() - this._width
        this._bottomBorderRight = this.width()
    else:
        x = this.x() - (this.width() - this._width)/2.0
        this._bottomBorderLeft = (this.width() - this._width)/2
        this._bottomBorderRight = this.width() - (this.width() - this._width)/2.0
    this.move(x, this.y()  - this.height())
    this.update()
