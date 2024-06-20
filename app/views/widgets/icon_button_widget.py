from PySide6.QtWidgets import QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from qfluentwidgets.components.widgets.button import TransparentToolButton

class IconButtonWidget(TransparentToolButton):
  def __init__(self, icon_path: str):
    super().__init__()

    self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    self.setCursor(Qt.CursorShape.PointingHandCursor)
    self.setIcon(QIcon(icon_path))