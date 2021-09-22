import qtDropDown

from PySide2.QtWidgets import * 
from PySide2.QtGui import * 
from PySide2.QtCore import *

app = QApplication([])
main = qtDropDown.QtDropDown(100, 100, 220, "right", "background-color: #000000; color: #FFFFFF;")

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

main.addContent(layout_main)
main.exec_()