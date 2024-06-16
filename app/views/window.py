from views.calculator.widget import Widget as CalculatorWidget
from PySide6.QtGui import QIcon
from qframelesswindow import FramelessMainWindow, StandardTitleBar

class Window(FramelessMainWindow):
  def __init__(self):
    super().__init__()
    
    self.setTitleBar(StandardTitleBar(self))
    
    self.setWindowTitle("Calculator")
    self.setWindowIcon(QIcon(":/images/logo"))

    self.setCentralWidget(CalculatorWidget())
    self.centralWidget().setContentsMargins(0,32,0,0)

    self.setFixedSize(250, 350)

    self.titleBar.raise_()