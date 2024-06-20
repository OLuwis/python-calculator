from PySide6.QtGui import QFont
from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Qt
from qfluentwidgets.components.widgets.button import TransparentPushButton

class ButtonWidget(TransparentPushButton):
  def __init__(self, value: str):
    super().__init__()

    font = QFont("OpenSans")
    font.setPointSizeF(10)

    self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    self.setCursor(Qt.CursorShape.PointingHandCursor)
    self.setFont(font)
    self.setText(value)