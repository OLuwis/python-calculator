from utils.display_utils import DisplayUtils
from re import match
from PySide6.QtWidgets import QWidget
from PySide6.QtCore import QEvent, QObject
from PySide6.QtGui import QKeyEvent

class KeyboardUtils(QObject):
  def __init__(self, parent: QObject, displayUtils: DisplayUtils):
    super().__init__(parent)

    self.displayUtils = displayUtils
  
  def eventFilter(self, window: QWidget, event: QEvent) -> bool:
    if event.type() == QEvent.Type.KeyPress:
      eventKey = QKeyEvent(event).key()
      eventText = QKeyEvent(event).text()
      
      if eventKey == 16777220:
        self.displayUtils.calculate()
        return True
      if eventKey == 67:
        self.displayUtils.clear()
        return True
      if eventKey == 16777219:
        self.displayUtils.delete()
        return True
      if bool(match(r"[0-9]|\.|\+|-|x|/|%", eventText)):
        self.displayUtils.insert(eventText)
        return True
    return False