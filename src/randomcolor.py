# This Python file uses the following encoding: utf-8
import sys, random

from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from ui_form import Ui_RandomColor

class RandomColor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_RandomColor()
        self.ui.setupUi(self)

        self.ui.copyRGB.setStyleSheet("background-image:url('../img/copy.png')")
        self.ui.copyHEX.setStyleSheet("background-image:url('../img/copy.png')")

        # Changing window icon
        icon = QIcon()
        icon.addFile("../img/icon.png")
        self.setWindowIcon(icon)

        # Cleaning clipboard
        self.timer = QTimer()
        self.timer.setSingleShot(True)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.clear_cb_label)

        # Generate new random color
        self.ui.pushButton.clicked.connect(self.generate_rgb_color)

        # Copy to clipboard
        self.ui.copyRGB.clicked.connect(self.copy_rgb)
        self.ui.copyHEX.clicked.connect(self.copy_hex)

    def generate_rgb_color(self):
        self.ui.rgbColor.setText("")
        self.ui.hexColor.setText("")
        self.ui.rgbLabel_2.setText("")
        self.ui.hexLabel_2.setText("")

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        self.ui.colorViewer.setStyleSheet(f"background-color:rgb({r},{g},{b})")
        self.ui.rgbColor.setText(f"rgb({r}, {g}, {b})")
        self.ui.hexColor.setText(self.rgb_to_hex(r,g,b))

    def rgb_to_hex(self, r, g, b):
        return '#{:02x}{:02x}{:02x}'.format(r, g, b)
        
    def copy_rgb(self, mod):
        self.ui.rgbLabel_2.setText("Copied!")
        cb = QApplication.clipboard()
        cb.setText(self.ui.rgbColor.text())
        self.timer.start()

    def copy_hex(self, mod):
        self.ui.hexLabel_2.setText("Copied!")
        cb = QApplication.clipboard()
        cb.setText(self.ui.hexColor.text())
        self.timer.start()

    def clear_cb_label(self):
        self.ui.rgbLabel_2.setText("")
        self.ui.hexLabel_2.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = RandomColor()
    widget.show()
    sys.exit(app.exec())
