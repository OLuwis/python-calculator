from qfluentwidgets import StrongBodyLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Display(StrongBodyLabel):
  def __init__(self):
    super().__init__()

    font = QFont("OpenSans")
    font.setPointSizeF(15)

    self.setFont(font)

    self.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)