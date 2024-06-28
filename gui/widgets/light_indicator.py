from PyQt5.QtWidgets import  QLabel
from PyQt5.QtGui import QColor, QPainter, QBrush, QRadialGradient
from PyQt5.QtCore import Qt

class LightIndicator(QLabel):
    def __init__(self):
        super().__init__()
        self.status = 'RED'  # Initial status is RED, meaning "LIVE"
        self.setFixedSize(50, 50)
        self.update_color()

    def update_color(self):
        color = QColor()
        if self.status == 'RED':
            color = QColor('red')
        elif self.status == 'ORANGE':
            color = QColor('orange')
        elif self.status == 'GREEN':
            color = QColor('green')
        
        self.setStyleSheet(f"""
            background-color: {color};
            border-radius: 25px;
        """)
        self.setToolTip(f"Status of Live Reconstruction: {self.get_status_text()}")

    def get_status_text(self):
        if self.status == 'RED':
            return "LIVE"
        elif self.status == 'ORANGE':
            return "PAUSED"
        elif self.status == 'GREEN':
            return "OFF"
        
    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        try:
            painter.setRenderHint(QPainter.Antialiasing, True)
            radial_gradient = QRadialGradient(self.width() / 2, self.height() / 2, self.width() / 2)
            if self.status == 'RED':
                radial_gradient.setColorAt(0, QColor(255, 100, 100, 255))
                radial_gradient.setColorAt(1, QColor(255, 0, 0, 0))
            elif self.status == 'ORANGE':
                radial_gradient.setColorAt(0, QColor(255, 200, 100, 255))
                radial_gradient.setColorAt(1, QColor(255, 165, 0, 0))
            elif self.status == 'GREEN':
                radial_gradient.setColorAt(0, QColor(100, 255, 100, 255))
                radial_gradient.setColorAt(1, QColor(0, 255, 0, 0))
            painter.setBrush(QBrush(radial_gradient))
            painter.drawEllipse(0, 0, self.width(), self.height())
        finally:
            painter.end()