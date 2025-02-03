from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout

class SimilaritiesCalculatorUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create input fields, button, and result label
        self.input_string_1 = QLineEdit()
        self.input_string_2 = QLineEdit()

        self.similarity_button = QPushButton("Calculate Similarity")
        self.similarity_result = QLabel("Similarity Result: ")
        self.rename_1 = QPushButton("Rename String 1")
        self.rename_2 = QPushButton("Rename String 2")


        # Create the layout
        layout = QVBoxLayout(self)

        form_layout = QFormLayout()
        form_layout.addRow("String 1:", self.input_string_1)
        form_layout.addRow("String 2:", self.input_string_2)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.rename_1)
        h_layout.addWidget(self.rename_2)

        layout.addLayout(form_layout)
        layout.addWidget(self.similarity_button)
        layout.addWidget(self.similarity_result)
        layout.addLayout(h_layout) 
       