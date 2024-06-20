from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from qfluentwidgets.components.widgets.label import DisplayLabel

class DisplayWidget(DisplayLabel):
  def __init__(self, fontSize: float, verticalAlign: Qt.AlignmentFlag):
    super().__init__()
                       
    font = QFont("OpenSans")
    font.setPointSizeF(fontSize)
    self.setAlignment(verticalAlign | Qt.AlignmentFlag.AlignRight)
    self.setFont(font)