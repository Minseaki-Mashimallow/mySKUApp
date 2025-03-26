from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QHBoxLayout, QFormLayout, QPushButton, QLabel, QComboBox, QApplication, QCompleter
from PyQt6.QtCore import Qt
from backend import database as db 

class SKUGeneratorUI(QWidget):
    def __init__(self, available_families):
        super().__init__()

        self.available_families = None 
        self.family_input = None
        self.model_input = None

        # attribute fields (initially hidden)
        self.attribute_fields = {}  # store dynamically created attribute dropdowns

        self.attribute_layout = QVBoxLayout()

        # generate SKU Button
        self.sku_button = QPushButton("Generate SKU")
        self.sku_button.setEnabled(True)

        # result Label
        self.product_family_display = QLineEdit()
        self.product_family_display.setReadOnly(True)  

        self.part_no_input = QLineEdit()
        self.model_list_input = QLineEdit()
        self.description_input = QLineEdit()
        self.full_description_input = QLineEdit()

        # copy SKU Button
        self.copy_button = QPushButton("Copy and Save SKU")
        self.copy_button.setEnabled(True)
        self.copy_message = QLabel("")

        # clear All Fields Button
        self.clear_button = QPushButton("Clear All Fields")
        self.clear_button.clicked.connect(self.clear_all_fields)

        # create layout
        self.layout = QVBoxLayout(self)
        self.form_layout = QFormLayout()
        
        self.layout.addWidget(self.clear_button)
        self.form_layout.addRow("Product Family:", self.family_input)
        self.form_layout.addRow("Product Model:", self.model_input)
        
        self.layout.addLayout(self.form_layout)
        self.layout.addLayout(self.attribute_layout)
        self.layout.addWidget(self.sku_button)

        self.layout.addWidget(QLabel("Generated SKU:"))
        self.layout.addWidget(self.product_family_display)
        self.layout.addWidget(QLabel("Part Number:"))
        self.layout.addWidget(self.part_no_input)
        self.layout.addWidget(QLabel("Model List:"))
        self.layout.addWidget(self.model_list_input)
        self.layout.addWidget(QLabel("Description:"))
        self.layout.addWidget(self.description_input)
        self.layout.addWidget(QLabel("Full Description:"))
        self.layout.addWidget(self.full_description_input)

        self.layout.addWidget(self.copy_button)
        self.layout.addWidget(self.copy_message)


        self.similarity_layout = QHBoxLayout()

        self.similarity_button = QPushButton("Calculate Similarity")
        self.similarity_text = QLabel("Similarity: ")
        self.similarity_report = QLabel("")

        self.similarity_layout.addWidget(self.similarity_button)
        self.similarity_layout.addWidget(self.similarity_text)
        self.similarity_layout.addWidget(self.similarity_report)

        self.layout.addLayout(self.similarity_layout)


    def on_family_selected(self):
        """Handles product family selection and displays related attributes dynamically."""
        ## TODO: UPDATE THIS TO HAVE IT SET TO FALSE IF THERE IS NO AVAILABLE MODELS WITHIN THE FAMILY? 
        models = db.LoadModels(self.get_product_family())
        ## Unsure how to clear this in one go rn
        while(self.model_input.count()):
            self.model_input.removeItem(0)

        if(len(models) != 0):
            for x in models:
                self.model_input.addItem(x)
                self.model_input.setCurrentIndex(0)
                self.model_input.setEditable(True)
        else:
            self.model_input.setEditable(True)

    def add_attribute_field(self, *arg):
        """Adds new attribute input field"""
        for x in arg:
            attribute_dropdown = QComboBox()
            attribute_dropdown.setEditable(True)
            attribute_dropdown.setPlaceholderText("Select Attribute") 
            ## This guy needed SOMETHING to exist properly and so be able to be removed.
            attribute_dropdown.addItems(db.LoadAttribute(x))

            # add autocompleter functionality
            completer = QCompleter(db.LoadAttribute(x), self)
            completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
            completer.setFilterMode(Qt.MatchFlags.MatchContains)  
            attribute_dropdown.setCompleter(completer)

            label = QLabel(x)
            self.attribute_layout.addWidget(label)
            self.attribute_layout.addWidget(attribute_dropdown)

    def on_model_selected(self):
        ## TODO: SPECIFICALLY CLEAR THE ATTRIBUTES ONLY, NOT INCLUDING THE MODEL AND FAMILY
        ## TODO: HAVE IT SET SO THAT YOU CAN ONLY HAVE THESE AND THEY ARE LOCKED ONCE YOU SELECT A MODEL THAT'S ALREADY MADE 
        ## TODO: POTENTIALLY ALLOW THE USER TO ADD MORE ATTRIBUTES TO THESE IF NECESSARY

        self.clear_attribute_layout()
        if(db.LoadModel(self.get_product_model())):
            parameters = db.LoadModelParameters(self.get_product_model())
            for x in parameters:
                self.add_attribute_field(x)
        
        self.similarity_report.setText("")


    def clear_all_fields(self):
        """Resets all fields to initial state."""
        self.family_input.setCurrentIndex(-1)
        self.product_family_display.clear()
        self.part_no_input.clear()
        self.model_list_input.clear()
        self.description_input.clear()
        self.full_description_input.clear()

        while(self.attribute_layout.count()):
            widget = self.attribute_layout.takeAt(0).widget()
            if widget:
                widget.hide()
                widget.setParent(None)
                widget.deleteLater()

        self.similarity_report.setText("")


    def get_product_family(self):
        """Returns the entered product family"""
        return self.family_input.currentText()
    
    def get_product_model(self):
        """Returns the entered product model"""
        return self.model_input.currentText()
    

    def update(self):
        self.available_families = db.LoadFamilies()
    
        self.clear_form_layout()

        ## TODO: MAKE THIS CLEANER HUHU
        self.family_input = QComboBox()
        self.family_input.setEditable(True)
        self.family_input.setPlaceholderText("Select Family")  
        self.family_input.addItems(self.available_families)  
        self.family_input.currentIndexChanged.connect(self.on_family_selected)

        # autocompleter functionality
        family_completer = QCompleter(self.available_families, self)
        family_completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        family_completer.setFilterMode(Qt.MatchFlags.MatchContains)  
        self.family_input.setCompleter(family_completer)

        self.model_input = QComboBox()
        self.model_input.setEditable(True)
        self.model_input.setPlaceholderText("Select Model")
        self.model_input.currentIndexChanged.connect(self.on_model_selected)
        

        self.form_layout.addRow("Product Family:", self.family_input)
        self.form_layout.addRow("Product Model:", self.model_input)


        self.similarity_report.setText("")


    def clear_form_layout(self):
        while(self.form_layout.count()):
            widget = self.form_layout.takeAt(0).widget()
            if widget:
                widget.hide()
                widget.setParent(None)
                widget.deleteLater()
       
    def clear_attribute_layout(self): 
        while(self.attribute_layout.count()):
            widget = self.attribute_layout.takeAt(0).widget()
            if widget:
                widget.hide()
                widget.setParent(None)
                widget.deleteLater()


 
    def get_attributes(self):
        """Returns selected attributes as a list from dropdowns"""
        attributes = []
        for i in range(self.attribute_layout.count()):
            widget = self.attribute_layout.itemAt(i).widget()
            if isinstance(widget, QComboBox):  
                attributes.append(widget.currentText().strip())
        return attributes