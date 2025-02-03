from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel

class SKUGeneratorUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create input fields, button, and result label
        self.sku_input = QLineEdit()
        self.sku_input.setPlaceholderText("Enter SKU Base")

        self.sku_button = QPushButton("Generate SKU")

        self.sku_result = QLabel("Generated SKU: ")

        # Create the layout
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        form_layout.addRow("Base SKU:", self.sku_input)

        layout.addLayout(form_layout)
        layout.addWidget(self.sku_button)
        layout.addWidget(self.sku_result)