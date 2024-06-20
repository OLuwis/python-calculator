from PySide6.QtWidgets import QVBoxLayout
from PySide6.QtCore import Qt
from views.widgets.display_widget import DisplayWidget

class DisplayLayout(QVBoxLayout):  
  def __init__(self):
    super().__init__()

    equationDisplay = DisplayWidget(10, Qt.AlignmentFlag.AlignVCenter)
    resultDisplay = DisplayWidget(15, Qt.AlignmentFlag.AlignTop)

    equationDisplay.setText("Equation")
    resultDisplay.setText("Result")

    self.addWidget(equationDisplay)
    self.addWidget(resultDisplay)

    self.setSpacing(0)
    self.setContentsMargins(5,0,5,0)

    self.equationDisplay = equationDisplay
    self.resultDisplay = resultDisplay