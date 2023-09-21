from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPainter, QPen
from PyQt5.QtWidgets import QWidget


class Canvas(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.image = QImage(self.size(), QImage.Format_ARGB32)
        self.image.fill(Qt.white)

        # Last position
        self.last_pos = None
        # Pen color
        self.pen_color = Qt.black
        # Background color
        self.background_color = Qt.white
        # Pen size
        self.pen_width = 5
        # Eraser size
        self.eraser_width = 5

        # Toggle eraser tracker
        self.is_eraser = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(0, 0, self.image)

    def resizeEvent(self, event):
        new_image = QImage(self.size(), QImage.Format_ARGB32)
        new_image.fill(Qt.white)
        painter = QPainter(new_image)
        painter.drawImage(0, 0, self.image)
        self.image = new_image

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton and self.last_pos:
            painter = QPainter(self.image)
            if self.is_eraser:
                painter.setPen(
                    QPen(self.background_color, self.eraser_width,
                         Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin
                         ))
            else:
                painter.setPen(
                    QPen(self.pen_color, self.pen_width,
                         Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin
                         ))
            painter.drawLine(self.last_pos, event.pos())
            self.last_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.last_pos = None

    # Clear the canvas
    def clear(self):
        self.image.fill(self.background_color)
        self.update()

    # Set pen color
    def set_pen_color(self, color):
        self.pen_color = color

    # Set pen width
    def set_pen_width(self, width):
        self.pen_width = width

    # Set eraser width
    def set_eraser_width(self, width):
        self.eraser_width = width

    # Toggle eraser mode
    def set_eraser_mode(self, is_eraser):
        self.is_eraser = is_eraser

    # Save the image
    def save(self, file_path):
        self.image.save(file_path)

