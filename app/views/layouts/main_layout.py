from PySide6.QtWidgets import QVBoxLayout, QWidget
from utils.display_utils import DisplayUtils
from views.layouts.display_layout import DisplayLayout
from views.layouts.button_layout import ButtonLayout

class MainLayout(QVBoxLayout):
  def __init__(self):
    super().__init__()

    self.setSpacing(0)

    displayLayout = DisplayLayout()
    self.displayUtils = DisplayUtils(displayLayout)
    buttonLayout = ButtonLayout(self.displayUtils)

    displayWidget = QWidget()
    buttonWidget = QWidget()
    
    displayWidget.setLayout(displayLayout)
    buttonWidget.setLayout(buttonLayout)

    self.addWidget(displayWidget, 30)
    self.addWidget(buttonWidget, 70)