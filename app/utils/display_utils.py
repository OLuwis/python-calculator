from re import match, split, search, sub
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

  def calculate(self, ):
    if not bool(match(r"\+|-|x|/|%|\.", self.resultDisplay.text()[-1])):
      self.equation = self.resultDisplay.text().replace("x", "*")
      if "%" in self.equation:
        self._percentage()
      item = evaluate(self.equation).item()
      result = int(item) if float(item).is_integer() else float(item)
      
      self.equationDisplay.setText(self.resultDisplay.text())
      self.resultDisplay.setText(str(result))

  def _percentage(self):
    equation = search(r"([0-9]+)%([0-9]+)", self.equation).group(0).split("%")
    a, b = equation[0], equation[1]
    item = evaluate("a / 100 * b",
    {
      "a": int(a) if float(a).is_integer() else float(a),
      "b": int(b) if float(b).is_integer() else float(b)
    })

    result = int(item) if float(item).is_integer() else float(item)
    self.equation = sub(r"([0-9]+)%([0-9]+)", str(result), self.equation)

    print(self.equation)

    if "%" in self.equation:
      self._percentage()