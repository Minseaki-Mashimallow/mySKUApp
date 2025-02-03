from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel

class SimilaritiesCalculatorUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create input fields, button, and result label
        self.input_string_1 = QLineEdit()
        self.input_string_2 = QLineEdit()

        self.similarity_button = QPushButton("Calculate Similarity")
        self.similarity_result = QLabel("Similarity Result: ")

        # Create the layout
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        form_layout.addRow("String 1:", self.input_string_1)
        form_layout.addRow("String 2:", self.input_string_2)

        layout.addLayout(form_layout)
        layout.addWidget(self.similarity_button)
        layout.addWidget(self.similarity_result)