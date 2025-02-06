from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QScrollArea, QComboBox
from backend import database as db

class DescriptionStandardUI(QWidget):
    def __init__(self, existing_families=None, existing_attributes=None):
        super().__init__()

        self.existing_families = db.LoadFamilies()
        self.existing_attributes = []
        # Main layout
        self.main_layout = QVBoxLayout(self)

        # Title label
        self.title_label = QLabel("Create New Description Standard")
        self.main_layout.addWidget(self.title_label)

        # Product family
        self.form_layout = QFormLayout()
        self.product_family_input = QComboBox()
        self.product_family_input.setEditable(True)
        self.product_family_input.setPlaceholderText("Select Family")
        self.product_family_input.addItems(self.existing_families)

        self.product_family_input.currentTextChanged.connect(self.on_family_input_changed)

        self.form_layout.addRow("Select or Enter Product Family:", self.product_family_input)

        # Product model
        self.product_model_input = QComboBox()
        self.product_model_input.setEditable(True)
        self.form_layout.addRow("Select or Enter Product Model:", self.product_model_input)
        self.main_layout.addLayout(self.form_layout)

        self.product_model_input.currentTextChanged.connect(self.on_model_input_changed)

        # Attribute input
        self.attributes_label = QLabel("Attributes:")
        self.main_layout.addWidget(self.attributes_label)

        # Scroll area for attributes
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.attribute_container = QWidget()
        self.attribute_layout = QVBoxLayout(self.attribute_container)
        self.scroll_area.setWidget(self.attribute_container)
        self.main_layout.addWidget(self.scroll_area)

        # Buttons
        self.add_attribute_button = QPushButton("Add Attribute")
        self.view_button = QPushButton("View")
        self.save_button = QPushButton("Save New Description Standard")
        self.clear_all_button = QPushButton("Clear All")

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_attribute_button)
        button_layout.addWidget(self.view_button)
        button_layout.addWidget(self.save_button)
        self.main_layout.addLayout(button_layout)

        # Clear All button at the bottom
        self.main_layout.addWidget(self.clear_all_button)

        self.clear_all_button.clicked.connect(self.clear_all_fields)

        # Generated description standard
        self.generated_description_label = QLabel("Generated Standard: /n")
        self.main_layout.addWidget(self.generated_description_label)

        

    def add_attribute_field(self, *args):
        """Adds new attribute input field"""
        attribute_dropdown = QComboBox()
        attribute_dropdown.setEditable(True)
        attribute_dropdown.setPlaceholderText("Select Attribute") 
        attribute_dropdown.addItems(args)
        self.attribute_layout.addWidget(attribute_dropdown)

    def get_product_family(self):
        """Returns the entered product family"""
        return self.product_family_input.currentText()
    
    def get_product_model(self):
        """Returns the entered product model"""
        return self.product_model_input.currentText()
    
    def get_attributes(self):
        """Returns selected attributes as a list from dropdowns"""
        attributes = []
        for i in range(self.attribute_layout.count()):
            widget = self.attribute_layout.itemAt(i).widget()
            if isinstance(widget, QComboBox):  
                attributes.append(widget.currentText().strip())
        return attributes

    def set_generated_description(self, text):
        """Updates the generated description label"""
        self.generated_description_label.setText(f"Generated Standard:\n{text}")

    def show_save_confirmation(self):
        """Displays a success message when a new description standard is saved."""
        self.generated_description_label.setText(self.generated_description_label.text() + "\nSaved New Description Standard!")

    def clear_all_fields(self):
        """Resets the UI to its initial state without affecting saved data."""
        self.product_family_input.setCurrentIndex(-1)  # Deselect product family
        self.product_model_input.setCurrentIndex(-1)
        self.generated_description_label.setText("Generated Standard: \n")  # Reset text
        # Removes all attribute dropdowns
        while self.attribute_layout.count():
            widget = self.attribute_layout.takeAt(0).widget()
            if widget:
                widget.hide()
                widget.deleteLater()

    def on_family_input_changed(self):
        ## TODO: UPDATE THIS TO HAVE IT SET TO FALSE IF THERE IS NO AVAILABLE MODELS WITHIN THE FAMILY? 
        models = db.LoadModels(self.get_product_family())
        ## Unsure how to clear this in one go rn
        while(self.product_model_input.count()):
            self.product_model_input.removeItem(0)
        if(len(models) != 0):
            self.product_model_input.addItems(models)
            self.product_model_input.setEditable(True)
        else:
            self.product_model_input.setEditable(True)

    def on_model_input_changed(self):
        ## TODO: SPECIFICALLY CLEAR THE ATTRIBUTES ONLY, NOT INCLUDING THE MODEL AND FAMILY
        ## TODO: HAVE IT SET SO THAT YOU CAN ONLY HAVE THESE AND THEY ARE LOCKED ONCE YOU SELECT A MODEL THAT'S ALREADY MADE 
        ## TODO: POTENTIALLY ALLOW THE USER TO ADD MORE ATTRIBUTES TO THESE IF NECESSARY
        
        if(db.LoadModel(self.get_product_model())):
            parameters = db.LoadModelParameters(self.get_product_model())
            for x in parameters:
                self.add_attribute_field(x)
        else:
            pass
