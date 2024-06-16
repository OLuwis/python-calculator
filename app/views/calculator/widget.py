from views.calculator.display import Display
from views.calculator.buttons import Buttons
from PySide6.QtWidgets import QVBoxLayout, QScrollArea, QWidget
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

class Widget(QWidget):
  def __init__(self):
    super().__init__()

    self.setLayout(Layout())

class SmallWidget(QWidget):
  def __init__(self, display: Display, result: Display):
    super().__init__()

    self.setLayout(Buttons(display, result))

class Layout(QVBoxLayout):
  def __init__(self):
    super().__init__()
    
    font = QFont("OpenSans")
    font.setPointSizeF(10)

    display = Display()
    result = Display()

    display.setFont(font)

    layout = QVBoxLayout()
    layout.addWidget(display)
    layout.addWidget(result)

    widget = QWidget()
    widget.setLayout(layout)

    area = QScrollArea()
    area.setWidget(widget)
    area.setWidgetResizable(True)
    area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    area.setAlignment(Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignRight)
    area.setStyleSheet("""
      border: 0;
    """)
    
    self.addWidget(area, 30)
    self.addWidget(SmallWidget(display, result), 70)