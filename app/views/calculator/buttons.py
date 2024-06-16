import re
import numexpr
from views.calculator.display import Display
from qfluentwidgets import TransparentPushButton, TransparentToolButton
from PySide6.QtWidgets import QGridLayout, QSizePolicy
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon

class Buttons(QGridLayout):
  def __init__(self, display: Display, result: Display):
    super().__init__()

    self.setContentsMargins(0,0,0,0)

    self.setSpacing(0)

    font = QFont("OpenSans")
    font.setPointSize(10)

    buttonpr = TransparentPushButton("%")
    buttonpr.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttonpr.setCursor(Qt.CursorShape.PointingHandCursor)
    buttonpr.setFont(font)
    buttonpr.clicked.connect(lambda: result.setText(result.text() + "%") if not bool(re.match(r"\+|-|x|/|%|\.", result.text()[-1])) else result.setText(result.text() + ""))

    buttonx = TransparentPushButton("x")
    buttonx.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttonx.setCursor(Qt.CursorShape.PointingHandCursor)
    buttonx.setFont(font)
    buttonx.clicked.connect(lambda: result.setText(result.text() + "x") if not bool(re.match(r"\+|-|x|/|%|\.", result.text()[-1])) else result.setText(result.text() + ""))

    buttonsl = TransparentPushButton("/")
    buttonsl.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttonsl.setCursor(Qt.CursorShape.PointingHandCursor)
    buttonsl.setFont(font)
    buttonsl.clicked.connect(lambda: result.setText(result.text() + "/") if not bool(re.match(r"\+|-|x|/|%|\.", result.text()[-1])) else result.setText(result.text() + ""))

    buttondel = TransparentToolButton(QIcon(":/icons/backspace"))
    buttondel.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttondel.setCursor(Qt.CursorShape.PointingHandCursor)
    buttondel.setFont(font)
    buttondel.clicked.connect(lambda: result.setText(result.text()[:-1]))

    button7 = TransparentPushButton("7")
    button7.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button7.setCursor(Qt.CursorShape.PointingHandCursor)
    button7.setFont(font)
    button7.clicked.connect(lambda: result.setText(result.text() + "7"))

    button8 = TransparentPushButton("8")
    button8.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button8.setCursor(Qt.CursorShape.PointingHandCursor)
    button8.setFont(font)
    button8.clicked.connect(lambda: result.setText(result.text() + "8"))

    button9 = TransparentPushButton("9")
    button9.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button9.setCursor(Qt.CursorShape.PointingHandCursor)
    button9.setFont(font)
    button9.clicked.connect(lambda: result.setText(result.text() + "9"))

    buttonmin = TransparentPushButton("-")
    buttonmin.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttonmin.setCursor(Qt.CursorShape.PointingHandCursor)
    buttonmin.setFont(font)
    buttonmin.clicked.connect(lambda: result.setText(result.text() + "-") if not bool(re.match(r"\+|-|x|/|%|\.", result.text()[-1])) else result.setText(result.text() + ""))
    
    button4 = TransparentPushButton("4")
    button4.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button4.setCursor(Qt.CursorShape.PointingHandCursor)
    button4.setFont(font)
    button4.clicked.connect(lambda: result.setText(result.text() + "4"))

    button5 = TransparentPushButton("5")
    button5.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button5.setCursor(Qt.CursorShape.PointingHandCursor)
    button5.setFont(font)
    button5.clicked.connect(lambda: result.setText(result.text() + "5"))

    button6 = TransparentPushButton("6")
    button6.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button6.setCursor(Qt.CursorShape.PointingHandCursor)
    button6.setFont(font)
    button6.clicked.connect(lambda: result.setText(result.text() + "6"))

    buttonpl = TransparentPushButton("+")
    buttonpl.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttonpl.setCursor(Qt.CursorShape.PointingHandCursor)
    buttonpl.setFont(font)
    buttonpl.clicked.connect(lambda: result.setText(result.text() + "+") if not bool(re.match(r"\+|-|x|/|%|\.", result.text()[-1])) else result.setText(result.text() + ""))

    button1 = TransparentPushButton("1")
    button1.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button1.setCursor(Qt.CursorShape.PointingHandCursor)
    button1.setFont(font)
    button1.clicked.connect(lambda: result.setText(result.text() + "1"))

    button2 = TransparentPushButton("2")
    button2.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button2.setCursor(Qt.CursorShape.PointingHandCursor)
    button2.setFont(font)
    button2.clicked.connect(lambda: result.setText(result.text() + "2"))

    button3 = TransparentPushButton("3")
    button3.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button3.setCursor(Qt.CursorShape.PointingHandCursor)
    button3.setFont(font)
    button3.clicked.connect(lambda: result.setText(result.text() + "3"))

    buttoneq = TransparentPushButton("=")
    buttoneq.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttoneq.setCursor(Qt.CursorShape.PointingHandCursor)
    buttoneq.setFont(font)
    buttoneq.clicked.connect(lambda: display.setText(result.text()) if not bool(re.match(r"\+|-|x|/|%|\.", result.text()[-1])) else display.setText(display.text()))
    buttoneq.clicked.connect(lambda: result.setText(str(int(numexpr.evaluate(result.text().replace("x", "*")).item()) if float(numexpr.evaluate(result.text().replace("x", "*")).item()).is_integer() else float(numexpr.evaluate(result.text().replace("x", "*")).item()))) if not bool(re.match(r"\+|-|x|/|%|\.", result.text()[-1])) else result.setText(result.text()))

    buttonac = TransparentPushButton("AC")
    buttonac.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttonac.setCursor(Qt.CursorShape.PointingHandCursor)
    buttonac.setFont(font)
    buttonac.clicked.connect(lambda: result.setText(""))
    buttonac.clicked.connect(lambda: display.setText(""))
    
    button0 = TransparentPushButton("0")
    button0.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    button0.setCursor(Qt.CursorShape.PointingHandCursor)
    button0.setFont(font)
    button0.clicked.connect(lambda: result.setText(result.text() + "0"))

    buttondt = TransparentPushButton(".")
    buttondt.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    buttondt.setCursor(Qt.CursorShape.PointingHandCursor)
    buttondt.setFont(font)
    buttondt.clicked.connect(lambda: result.setText(result.text() + ".") if "." not in re.split(r"\+|-|x|/|%", result.text())[-1] else result.setText(result.text() + ""))

    self.addWidget(buttonpr, 0, 1)
    self.addWidget(buttonx, 0, 2)
    self.addWidget(buttonsl, 0, 3)
    self.addWidget(buttondel, 0, 4)
    self.addWidget(button7, 1, 1)
    self.addWidget(button8, 1, 2)
    self.addWidget(button9, 1, 3)
    self.addWidget(buttonmin, 1, 4)
    self.addWidget(button4, 2, 1)
    self.addWidget(button5, 2, 2)
    self.addWidget(button6, 2, 3)
    self.addWidget(buttonpl, 2, 4)
    self.addWidget(button1, 3, 1)
    self.addWidget(button2, 3, 2)
    self.addWidget(button3, 3, 3)
    self.addWidget(buttoneq, 3, 4, 2, 1)
    self.addWidget(buttonac, 4, 1)
    self.addWidget(button0, 4, 2)
    self.addWidget(buttondt, 4, 3)