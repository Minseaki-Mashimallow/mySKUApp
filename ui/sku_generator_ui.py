from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QComboBox, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QClipboard

class SKUGeneratorUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.family_input = QComboBox()
        self.family_input.setEditable(True)
        self.family_input.setPlaceholderText("Select Family") 
        self.family_input.addItems(['EGG TRAY', 'ICE CREAM', 'PAIL BODY', 'PAIL COVER'])  
        self.family_input.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.color_combo = QComboBox()
        self.color_combo.setEditable(True)
        self.color_combo.setPlaceholderText("Select Color") 
        self.color_combo.addItems(['BLUE', 'RED', 'GREEN', 'Black'])  
        self.color_combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.size_combo = QComboBox()
        self.size_combo.setEditable(True)
        self.size_combo.setPlaceholderText("Select Size")
        self.size_combo.addItems(['1L', '500ML', '2L'])  
        self.size_combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.material_combo = QComboBox()
        self.material_combo.setEditable(True)
        self.material_combo.setPlaceholderText("Select Material") 
        self.material_combo.addItems(['PLASTIC', 'GLASS', 'HDPE'])   
        self.material_combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.virgin_option = QComboBox()
        self.virgin_option.setEditable(True)
        self.virgin_option.setPlaceholderText("Select") 
        self.virgin_option.addItems(['01','02'])

        # Generate SKU Button
        self.sku_button = QPushButton("Generate SKU")

        # Copy SKU Button
        self.copy_button = QPushButton("Copy SKU")
        self.copy_button.clicked.connect(self.copy_sku)

        # Clear All Fields Button
        self.clear_button = QPushButton("Clear All Fields")
        self.clear_button.clicked.connect(self.clear_all_fields)

        # Result label
        self.sku_result = QLabel("Generated SKU: ")

        # Create the layout
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Form layout
        layout.addWidget(self.clear_button)

        form_layout.addRow("Product Family:", self.family_input)
        form_layout.addRow("Color:", self.color_combo)
        form_layout.addRow("Size:", self.size_combo)
        form_layout.addRow("Material:", self.material_combo)
        form_layout.addRow("Virgin:", self.virgin_option)

        layout.addLayout(form_layout)
        layout.addWidget(self.sku_button)
        layout.addWidget(self.sku_result)
        layout.addWidget(self.copy_button)

    def copy_sku(self):
        # Get the generated SKU text from the result label
        sku_text = self.sku_result.text().replace("Generated SKU: ", "")
        
        # Get the system clipboard and set the text
        clipboard = QApplication.clipboard()
        clipboard.setText(sku_text)
        

    def clear_all_fields(self):
        # Reset all the dropdowns to blank
        self.family_input.setCurrentIndex(-1)
        self.color_combo.setCurrentIndex(-1)
        self.size_combo.setCurrentIndex(-1)
        self.material_combo.setCurrentIndex(-1)
        self.virgin_option.setCurrentIndex(-1)
        
        # Clear the result label
        self.sku_result.setText("Generated SKU: ")