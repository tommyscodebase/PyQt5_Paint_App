from main import PaintApp
from PyQt5.QtWidgets import QApplication
import sys

app = QApplication(sys.argv)
app.setStyle('Fusion')
window = PaintApp()
sys.exit(app.exec())
