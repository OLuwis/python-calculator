from PySide6.QtGui import QIcon
from views.layouts.main_layout import MainLayout
from qframelesswindow.windows import WindowsFramelessWindow
from qframelesswindow.titlebar import StandardTitleBar
from utils.keyboard_utils import KeyboardUtils

class Window(WindowsFramelessWindow):
  def __init__(self):
    super().__init__()
    
    self.mainLayout = MainLayout()
    
    self.setLayout(self.mainLayout)
    self.layout().setContentsMargins(0,32,0,0)

    self.setFixedSize(250, 350)

    self.keyboardUtils = KeyboardUtils(self, self.mainLayout.displayUtils)
    self.installEventFilter(self.keyboardUtils)

    self._init_titlebar()

  def _init_titlebar(self):
    self.setTitleBar(StandardTitleBar(self))
    self.setWindowIcon(QIcon(":/images/logo"))
    self.setWindowTitle("Calculator")
    self.titleBar.raise_()