from re import match, split
from numexpr import evaluate
from views.layouts.display_layout import DisplayLayout

class DisplayUtils():
  def __init__(self, displayLayout: DisplayLayout):
    super().__init__()

    self.equationDisplay = displayLayout.equationDisplay
    self.resultDisplay = displayLayout.resultDisplay

  def insert(self, value: str):
    if value == ".":
      if "." not in split(r"\+|-|x|/|%", self.resultDisplay.text())[-1]:
        text = self.resultDisplay.text()
        self.resultDisplay.setText(text + value)  
    elif bool(match(r"\+|-|x|/|%", value)):
      if not bool(match(r"\+|-|x|/|%|\.", self.resultDisplay.text()[-1])):
        text = self.resultDisplay.text()
        self.resultDisplay.setText(text + value)
    else:
      text = self.resultDisplay.text()
      self.resultDisplay.setText(text + value)

  def delete(self):
    self.resultDisplay.setText(self.resultDisplay.text()[:-1])
    
  def clear(self):
    self.equationDisplay.setText("")
    self.resultDisplay.setText("")

  def calculate(self):
    if not bool(match(r"\+|-|x|/|%|\.", self.resultDisplay.text()[-1])):
      equation = self.resultDisplay.text().replace("x", "*")
      result = int(evaluate(equation).item()) if float(evaluate(equation).item()).is_integer() else float(evaluate(equation).item())
      
      self.equationDisplay.setText(self.resultDisplay.text())
      self.resultDisplay.setText(str(result))