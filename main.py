import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyPyQtApp")
        self.setGeometry(100, 100, 400, 300)  # x, y, width, height

        # Create a central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a layout
        layout = QVBoxLayout(self.central_widget)

        # Create a label
        self.label = QLabel("Hello, PyQt!", self)
        layout.addWidget(self.label)

        # Create a button
        self.button = QPushButton("Click Me", self)
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.button)

        # Set layout
        self.central_widget.setLayout(layout)

    def button_clicked(self):
        self.label.setText("Button Clicked!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())