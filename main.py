from PyQt5.QtWidgets import *
from paint import Ui_Paint


class PaintApp(QMainWindow, Ui_Paint):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.setupUi(self)
        self.show()

        # Connections
        self.actionErase.triggered.connect(self.toggle_eraser)
        self.actionSave.triggered.connect(self.save_file)
        self.actionBrush.triggered.connect(self.resume_drawing)
        self.actionClear.triggered.connect(self.clear_canvas)

        # Eraser width
        self.eraser_size.valueChanged.connect(
            lambda: self.change_eraser_size(self.eraser_size.value())
        )
        # Pen width
        self.brush_size.valueChanged.connect(
            lambda: self.change_brush_size(self.brush_size.value())
        )

        # Color
        self.current_color.clicked.connect(self.choose_color)

    # Save the drawing
    def save_file(self):
        file, _ = QFileDialog.getSaveFileName(
            self, 'Save Image', ':\\', 'JPEG Files (*.jpeg)'
        )
        if file:
            self.canvas.save(file)

    # Choose color
    def choose_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_pen_color(color)
            self.current_color.setStyleSheet(f"background-color: {color.toRgb().name()};")
            self.current_color_label.setText(str(color.toRgb().name()))

    # Brush size
    def change_brush_size(self, value):
        self.canvas.set_pen_width(value)

    # Toggle eraser
    def toggle_eraser(self):
        is_eraser = self.actionErase.isChecked()
        self.canvas.set_eraser_mode(is_eraser)

    # Eraser size
    def change_eraser_size(self, value):
        self.canvas.set_eraser_width(value)

    # Clear the canvas
    def clear_canvas(self, value):
        self.canvas.clear()

    # Clear the canvas
    def resume_drawing(self, value):
        self.canvas.set_eraser_mode(False)
        self.actionErase.setChecked(False)
