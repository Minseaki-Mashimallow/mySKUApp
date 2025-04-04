from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QScrollArea, QComboBox, QListWidget, QMessageBox
from backend import database as db  

class AddNewDescriptionUI(QWidget):
    def __init__(self):
        super().__init__()

        self.attributes = db.LoadAttributes()

        self.main_layout = QVBoxLayout(self)

        self.attribute_selector = QComboBox(self)
        self.attribute_selector.addItems(self.attributes.keys())
        self.attribute_selector.currentTextChanged.connect(self.load_attribute_values)
        self.main_layout.addWidget(QLabel("Select Attribute:"))
        self.main_layout.addWidget(self.attribute_selector)

        # **Search Bar**
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search...")
        self.search_bar.textChanged.connect(self.filter_list)
        self.main_layout.addWidget(self.search_bar)

        self.scroll_area = QScrollArea(self)
        self.list_widget = QListWidget(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.list_widget)
        self.main_layout.addWidget(self.scroll_area)

        self.load_attribute_values()

        self.form_layout = QFormLayout()

        # Input field for new values
        self.new_value_input = QLineEdit(self)
        self.form_layout.addRow("New Value:", self.new_value_input)

        # Buttons 
        self.button_layout = QHBoxLayout()
        self.add_button = QPushButton("Add")
        self.edit_button = QPushButton("Edit")
        self.delete_button = QPushButton("Delete")
        
        self.button_layout.addWidget(self.add_button)
        self.button_layout.addWidget(self.edit_button)
        self.button_layout.addWidget(self.delete_button)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.button_layout)

        # Messages
        self.message_label = QLabel("")
        self.main_layout.addWidget(self.message_label)

        # Connect buttons to functions
        self.add_button.clicked.connect(self.add_value)
        self.edit_button.clicked.connect(self.edit_value)
        self.delete_button.clicked.connect(self.delete_value)

    
    def get_current_attribute_label(self):
        return self.attribute_selector.currentText()

    def load_attribute_values(self):
        """ Loads the values of the selected attribute into the list widget """
        selected_attribute = self.attribute_selector.currentText()
        self.list_widget.clear()
        if selected_attribute in self.attributes:
            self.list_widget.addItems(self.attributes[selected_attribute])

    def filter_list(self):
        """ Filters list based on search bar input """
        search_text = self.search_bar.text().strip().lower()
        for i in range(self.list_widget.count()):
            item = self.list_widget.item(i)
            item.setHidden(search_text not in item.text().lower())

    def add_value(self):
        """ Adds a new value to the selected attribute """
        selected_attribute = self.attribute_selector.currentText()
        new_value = self.new_value_input.text().strip().upper()

        if not new_value:
            self.message_label.setText("Please enter a value.")
            return

        if new_value in self.attributes[selected_attribute]:
            self.message_label.setText("Value already exists.")
            return

        # Update the attribute list
        self.attributes[selected_attribute].append(new_value)
        db.UpdateAttributes(self.attributes, self.get_current_attribute_label())  # Save changes to database
        self.load_attribute_values()  # Refresh list
        self.message_label.setText(f'"{new_value}" added to {selected_attribute}.')

    def edit_value(self):
        """ Edits a selected value in the attribute list """
        selected_attribute = self.attribute_selector.currentText()
        selected_item = self.list_widget.currentItem()

        if not selected_item:
            self.message_label.setText("Please select a value to edit.")
            return

        new_value = self.new_value_input.text().strip().upper()
        if not new_value:
            self.message_label.setText("Please enter a new name.")
            return

        old_value = selected_item.text()
        if new_value in self.attributes[selected_attribute]:
            self.message_label.setText("New value already exists.")
            return

        # Update the list
        index = self.attributes[selected_attribute].index(old_value)
        self.attributes[selected_attribute][index] = new_value
        db.UpdateAttributes(self.attributes, self.get_current_attribute_label())  # Save changes to database
        self.load_attribute_values()  # Refresh list
        self.message_label.setText(f'"{old_value}" changed to "{new_value}".')

    def delete_value(self):
        """ Deletes the selected value from the attribute list """
        selected_attribute = self.attribute_selector.currentText()
        selected_item = self.list_widget.currentItem()

        if not selected_item:
            self.message_label.setText("Please select a value to delete.")
            return

        # Creating a QMessageBox to ask the user
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Confirm Delete")
        msg_box.setText(f"Are you sure you want to delete '{selected_item.text()}'?")
        try:
            msg_box.setStandardButtons(QMessageBox.StandardButtons.Yes | QMessageBox.StandardButtons.No)
        except:
            msg_box.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
    
        # Execute the dialog and check the selected button
        confirm = msg_box.exec()

        # Extract button and compare using standardButton()
        try:
            if msg_box.standardButton(msg_box.clickedButton()) == QMessageBox.StandardButtons.Yes:
                self.attributes[selected_attribute].remove(selected_item.text())
                db.UpdateAttributes(self.attributes, self.get_current_attribute_label())  # Save changes to database
                self.load_attribute_values()  # Refresh
                self.message_label.setText(f'"{selected_item.text()}" deleted from {selected_attribute}.')
        except:
            if msg_box.standardButton(msg_box.clickedButton()) == QMessageBox.standardButtons(msg_box).Yes:
                self.attributes[selected_attribute].remove(selected_item.text())
                db.UpdateAttributes(self.attributes, self.get_current_attribute_label())  # Save changes to database
                self.load_attribute_values()  # Refresh
                self.message_label.setText(f'"{selected_item.text()}" deleted from {selected_attribute}.')


    def update(self):
        self.attributes = db.LoadAttributes()
        self.attribute_selector.clear()
        self.attribute_selector.addItems(self.attributes)
