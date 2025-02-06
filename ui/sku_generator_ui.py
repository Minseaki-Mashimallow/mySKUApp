from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QPushButton, QLabel, QComboBox, QApplication
from PyQt6.QtCore import Qt

class SKUGeneratorUI(QWidget):
    def __init__(self, available_families):
        super().__init__()

        self.available_families = available_families  # { 'ICE CREAM': ['Color', 'Size'] }
        self.saved_attributes = {}  # store all attributes entered by users ?? idk if need

        # product Family
        self.family_input = QComboBox()
        self.family_input.setEditable(True)
        self.family_input.setPlaceholderText("Select Family")  
        self.family_input.addItems(self.available_families)  
        self.family_input.currentIndexChanged.connect(self.on_family_selected)

        # attribute fields (initially hidden)
        self.attribute_fields = {}  # store dynamically created attribute dropdowns

        # generate SKU Button
        self.sku_button = QPushButton("Generate SKU")
        self.sku_button.setEnabled(False)

        # copy SKU Button
        self.copy_button = QPushButton("Copy SKU")
        self.copy_button.setEnabled(False)

        # clear All Fields Button
        self.clear_button = QPushButton("Clear All Fields")
        self.clear_button.clicked.connect(self.clear_all_fields)

        # result Label
        self.sku_result = QLabel("Generated SKU: ")

        # create Layout
        self.layout = QVBoxLayout(self)
        self.form_layout = QFormLayout()
        
        self.layout.addWidget(self.clear_button)
        self.form_layout.addRow("Product Family:", self.family_input)

        self.layout.addLayout(self.form_layout)
        self.layout.addWidget(self.sku_button)
        self.layout.addWidget(self.sku_result)
        self.layout.addWidget(self.copy_button)

    def on_family_selected(self):
        """Handles product family selection and displays related attributes dynamically."""
        selected_family = self.family_input.currentText().strip()
        
        # hide all existing attribute fields
        for widget in self.attribute_fields.values():
            widget.hide()

        # check if the selected family has a set standard
        if selected_family in self.available_families:
            attributes = self.available_families[selected_family]  # get attributes from the saved standard

            for attr in attributes:
                if attr not in self.attribute_fields:
                    self.attribute_fields[attr] = QComboBox()
                    self.attribute_fields[attr].setEditable(True)  # allow new entries
                    self.attribute_fields[attr].setPlaceholderText(f"Select {attr}")

                    # load existing options for this attribute
                    if attr in self.saved_attributes:
                        self.attribute_fields[attr].addItems(self.saved_attributes[attr])

                    # connect event to detect new entries
                    self.attribute_fields[attr].editTextChanged.connect(lambda text, a=attr: self.add_new_option(a, text))

                    self.form_layout.addRow(f"{attr}:", self.attribute_fields[attr])

                self.attribute_fields[attr].show()

            self.sku_button.setEnabled(True)
        else:
            self.sku_result.setText("Error: No standard found. Set a description standard first.")
            self.sku_button.setEnabled(False)

    def add_new_option(self, attribute, text):
        """Adds a new option to the attribute dropdown if it doesn't already exist."""
        if attribute not in self.saved_attributes:
            self.saved_attributes[attribute] = set()

        if text and text not in self.saved_attributes[attribute]:
            self.saved_attributes[attribute].add(text)
            self.attribute_fields[attribute].addItem(text)

    def clear_all_fields(self):
        """Resets all fields to initial state."""
        self.family_input.setCurrentIndex(-1)
        self.sku_result.setText("Generated SKU: ")

        for widget in self.attribute_fields.values():
            widget.hide()
