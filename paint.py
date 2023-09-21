from PyQt5 import QtCore, QtGui, QtWidgets
from canvas import Canvas


class Ui_Paint(object):
    def setupUi(self, Paint):
        Paint.setObjectName("Paint")
        Paint.resize(589, 495)
        font = QtGui.QFont()
        font.setPointSize(12)
        Paint.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/artboard.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Paint.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(Paint)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.canvas_frame = QtWidgets.QFrame(self.centralwidget)
        self.canvas_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.canvas_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.canvas_frame.setObjectName("canvas_frame")
        self.verticalLayout.addWidget(self.canvas_frame)

        # Canvas
        self.canvas_layout = QtWidgets.QVBoxLayout(self.canvas_frame)

        self.canvas = Canvas(self)
        self.canvas_layout.addWidget(self.canvas)

        Paint.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Paint)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 27))
        self.menubar.setObjectName("menubar")
        Paint.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Paint)
        self.statusbar.setObjectName("statusbar")
        Paint.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Paint)
        self.toolBar.setMovable(False)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName("toolBar")
        Paint.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionBrush = QtWidgets.QAction(Paint)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/images/paint brush.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBrush.setIcon(icon1)
        self.actionBrush.setObjectName("actionBrush")
        self.actionSave = QtWidgets.QAction(Paint)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/images/Download.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave.setObjectName("actionSave")
        self.actionErase = QtWidgets.QAction(Paint)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/images/pngtree eraser.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionErase.setIcon(icon3)
        self.actionErase.setCheckable(True)
        self.actionErase.setObjectName("actionErase")
        self.actionClear = QtWidgets.QAction(Paint)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/images/erase.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClear.setIcon(icon4)
        self.actionClear.setObjectName("actionClear")

        # Additions
        self.eraser_size = QtWidgets.QSpinBox(self)
        self.eraser_size.setValue(5)
        self.eraser_size.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.brush_size = QtWidgets.QSpinBox(self)
        self.brush_size.setValue(5)
        self.brush_size.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.colour_label = QtWidgets.QLabel(self)
        self.colour_label.setText('Current Color:')
        self.current_color = QtWidgets.QPushButton(self)
        self.current_color.setMinimumSize(QtCore.QSize(32, 32))
        self.current_color.setMaximumSize(QtCore.QSize(32, 32))
        self.current_color.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.current_color.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.current_color_label = QtWidgets.QLabel(self)
        self.current_color_label.setText("#000000")

        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionBrush)
        self.toolBar.addWidget(self.brush_size)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionErase)
        self.toolBar.addWidget(self.eraser_size)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionClear)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(self.colour_label)
        self.toolBar.addWidget(self.current_color)
        self.toolBar.addWidget(self.current_color_label)

        self.retranslateUi(Paint)
        QtCore.QMetaObject.connectSlotsByName(Paint)

    def retranslateUi(self, Paint):
        _translate = QtCore.QCoreApplication.translate
        Paint.setWindowTitle(_translate("Paint", "Paint App"))
        self.toolBar.setWindowTitle(_translate("Paint", "toolBar"))
        self.actionBrush.setText(_translate("Paint", "Brush"))
        self.actionBrush.setToolTip(_translate("Paint", "Brush"))
        self.actionSave.setText(_translate("Paint", "Save"))
        self.actionSave.setToolTip(_translate("Paint", "Save image"))
        self.actionErase.setText(_translate("Paint", "Erase"))
        self.actionErase.setToolTip(_translate("Paint", "Eraser"))
        self.actionClear.setText(_translate("Paint", "Clear"))
        self.actionClear.setToolTip(_translate("Paint", "Clear the canvas"))
import paint_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Paint = QtWidgets.QMainWindow()
    ui = Ui_Paint()
    ui.setupUi(Paint)
    Paint.show()
    sys.exit(app.exec_())
