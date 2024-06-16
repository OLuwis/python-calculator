import resources.resources
from views.window import Window
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase

if __name__ == "__main__":
  app = QApplication([])

  QFontDatabase.addApplicationFont(":/fonts/opensans")
  
  window = Window()
  window.show()
  app.exec()