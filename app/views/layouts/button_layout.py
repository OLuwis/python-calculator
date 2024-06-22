from PySide6.QtWidgets import QGridLayout
from typing import List
from utils.display_utils import DisplayUtils
from views.widgets.button_widget import ButtonWidget
from views.widgets.icon_button_widget import IconButtonWidget

class ButtonLayout(QGridLayout):
  def __init__(self, displayUtils: DisplayUtils):
    super().__init__()

    self.setContentsMargins(0,0,0,0)
    self.setSpacing(0)

    self.displayUtils = displayUtils
    buttons = self._init_buttons()
    positions = [
      [1,1],
      [1,2],
      [1,3],
      [2,1],
      [2,2],
      [2,3],
      [3,1],
      [3,2],
      [3,3],
      [4,2],
      [2,4],
      [1,4],
      [0,2],
      [0,3],
      [0,1],
      [4,3],
      [0,4],
      [3,4],
      [4,1]
    ]
    
    for i in range(len(buttons)):
      if i == 17:
        self.addWidget(buttons[i], positions[i][0], positions[i][1], 2, 1)
      else:
        self.addWidget(buttons[i], positions[i][0], positions[i][1])

  def _init_buttons(self) -> List[ButtonWidget]:
    self.button1 = ButtonWidget("1")
    self.button2 = ButtonWidget("2")
    self.button3 = ButtonWidget("3")
    self.button4 = ButtonWidget("4")
    self.button5 = ButtonWidget("5")
    self.button6 = ButtonWidget("6")
    self.button7 = ButtonWidget("7")
    self.button8 = ButtonWidget("8")
    self.button9 = ButtonWidget("9")
    self.button0 = ButtonWidget("0")

    self.buttonplus = ButtonWidget("+")
    self.buttonminus = ButtonWidget("-")
    self.buttontimes = ButtonWidget("x")
    self.buttondivide = ButtonWidget("/")
    self.buttonpercentage = ButtonWidget("%")
    self.buttondot = ButtonWidget(".")

    self.buttonbackspace = IconButtonWidget(":/icons/backspace")
    self.buttonequals = ButtonWidget("=")
    self.buttonac = ButtonWidget("AC")

    self.button1.clicked.connect(lambda: self.displayUtils.insert(self.button1.text()))
    self.button2.clicked.connect(lambda: self.displayUtils.insert(self.button2.text()))
    self.button3.clicked.connect(lambda: self.displayUtils.insert(self.button3.text()))
    self.button4.clicked.connect(lambda: self.displayUtils.insert(self.button4.text()))
    self.button5.clicked.connect(lambda: self.displayUtils.insert(self.button5.text()))
    self.button6.clicked.connect(lambda: self.displayUtils.insert(self.button6.text()))
    self.button7.clicked.connect(lambda: self.displayUtils.insert(self.button7.text()))
    self.button8.clicked.connect(lambda: self.displayUtils.insert(self.button8.text()))
    self.button9.clicked.connect(lambda: self.displayUtils.insert(self.button9.text()))
    self.button0.clicked.connect(lambda: self.displayUtils.insert(self.button0.text()))

    self.buttonplus.clicked.connect(lambda: self.displayUtils.insert(self.buttonplus.text()))
    self.buttonminus.clicked.connect(lambda: self.displayUtils.insert(self.buttonminus.text()))
    self.buttontimes.clicked.connect(lambda: self.displayUtils.insert(self.buttontimes.text()))
    self.buttondivide.clicked.connect(lambda: self.displayUtils.insert(self.buttondivide.text()))
    self.buttonpercentage.clicked.connect(lambda: self.displayUtils.insert(self.buttonpercentage.text()))
    self.buttondot.clicked.connect(lambda: self.displayUtils.insert(self.buttondot.text()))

    self.buttonac.clicked.connect(lambda: self.displayUtils.clear())
    self.buttonbackspace.clicked.connect(lambda: self.displayUtils.delete())
    self.buttonequals.clicked.connect(lambda: self.displayUtils.calculate())

    return [
      self.button1,
      self.button2,
      self.button3,
      self.button4,
      self.button5,
      self.button6,
      self.button7,
      self.button8,
      self.button9,
      self.button0,
      self.buttonplus,
      self.buttonminus,
      self.buttontimes,
      self.buttondivide,
      self.buttonpercentage,
      self.buttondot,
      self.buttonbackspace,
      self.buttonequals,
      self.buttonac
    ]