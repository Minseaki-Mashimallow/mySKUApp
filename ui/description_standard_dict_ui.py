from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QPushButton, QLabel, QComboBox, QApplication

class DescriptionDictionaryUI(QWidget):
    def __init__(self):
        super().__init__()
    
        # Main layout
        self.main_layout = QVBoxLayout(self)