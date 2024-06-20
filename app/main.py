from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QFontDatabase
from res.resources import qInitResources
from views.window import Window

if __name__ == "__main__":
  app = QApplication([])

  qInitResources()
  QFontDatabase.addApplicationFont(":/fonts/opensans")
  
  window = Window()
  window.show()
  app.exec()