from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QPushButton, QLabel, QComboBox, QCompleter, QApplication, QHBoxLayout
from PyQt6.QtCore import Qt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein as lv
from backend import database as db

class DescriptionGeneratorUI(QWidget):
    def __init__(self):
        super().__init__()


        self.current_descriptions = db.LoadDescriptions()

        self.attributes = db.LoadAttributes() 

        # Main layout
        self.main_layout = QVBoxLayout(self)

        # Form layout for dropdowns
        self.form_layout = QFormLayout()
        self.dropdowns = {}  # Store dropdown widgets

        # Create dropdowns
        self.make_qcbox_for_attribute("Product Model", self.attributes["Product Model"])
        self.make_qcbox_for_attribute("Material", self.attributes["Material"])
        self.make_qcbox_for_attribute("Size", self.attributes["Size"])
        self.make_qcbox_for_attribute("Dimension", self.attributes["Dimension"])
        self.make_qcbox_for_attribute("Type", self.attributes["Type"])
        self.make_qcbox_for_attribute("Parts", self.attributes["Parts"])
        self.make_qcbox_for_attribute("Shape", self.attributes["Shape"])
        self.make_qcbox_for_attribute("Color", self.attributes["Color"])
        self.make_qcbox_for_attribute("Additional Features", self.attributes["Additional Features"])
            
        self.main_layout.addLayout(self.form_layout)

        # Generated Description Section
        self.generated_label = QLabel("Generated Description:")
        self.error_message = QLabel("")
        self.generated_output = QLabel("")  # Empty label for generated description
        self.similarity_report = QLabel("")
        self.save_message = QLabel("")

        self.reset_button = QPushButton("Reset Description")
        self.main_layout.addWidget(self.reset_button)

        self.main_layout.addWidget(self.generated_label)
        self.main_layout.addWidget(self.error_message)
        self.main_layout.addWidget(self.generated_output)
        self.main_layout.addWidget(self.similarity_report)
        self.main_layout.addWidget(self.save_message)

        # buttons
        self.check_similarity_button = QPushButton("Check Similarity")
        self.copyNsave_button = QPushButton("Copy and Save Description")
        button_layout = QHBoxLayout()

        # Add buttons to the horizontal layout
        button_layout.addWidget(self.check_similarity_button)
        button_layout.addWidget(self.copyNsave_button)

        # Add the button layout to the main layout
        self.main_layout.addLayout(button_layout)
        # Connect button
        self.reset_button.clicked.connect(self.reset_description)
        self.check_similarity_button.clicked.connect(self.check_similarity)
        self.copyNsave_button.clicked.connect(self.copy_and_save_description)


    def make_qcbox_for_attribute(self, attribute, parameters):
        combo_box = QComboBox(self)
        combo_box.setEditable(True)  # Allow typing for searching
        combo_box.setInsertPolicy(QComboBox.InsertPolicy.NoInsert)  # Prevent adding new items
        completer = QCompleter(parameters, self)  # Enable search functionality
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        try:
            completer.setFilterMode(Qt.MatchFlags.MatchContains)
        except:
            completer.setFilterMode(Qt.MatchFlag.MatchContains)
        combo_box.setCompleter(completer)  # Attach completer
        combo_box.addItems(parameters)  # Populate dropdown options

        combo_box.setCurrentIndex(-1)  # Start with an empty field
        self.dropdowns[attribute] = combo_box  # Store reference

        # Connect the selection process to update generated description
        combo_box.activated.connect(self.add_to_description)

        # Connect editingFinished signal from the line edit to clear the dropdown
        combo_box.lineEdit().editingFinished.connect(self.clear_dropdown_after_editing)

        self.form_layout.addRow(attribute, combo_box)

    def add_to_description(self, index):
        """ Add the selected dropdown value to the generated description """
        # Find the combo box that triggered the event
        combo_box = self.sender()
        selected_value = combo_box.currentText()

        # Update the generated description
        new_description = self.generated_output.text()
        if new_description:
            new_description += f" {selected_value}"  # Append the selected value
        else:
            new_description = selected_value  # Set if empty

        self.generated_output.setText(new_description)

    def clear_dropdown_after_editing(self):
        """ Clear the combo box after user finishes editing """
        combo_box = self.sender().parent()  # Get the parent combo box of the line edit
        combo_box.setCurrentIndex(-1)  # Reset the dropdown
        combo_box.lineEdit().clear()   # Clear the typed input (if any)

    def reset_description(self):
        """ Reset the generated description """
        self.generated_output.setText("") 
        self.save_message.setText("")
        self.error_message.setText("")
        # Also reset all dropdowns
        for combo_box in self.dropdowns.values():
            combo_box.setCurrentIndex(-1)  # Clear the selections
    
    def check_similarity(self):
        """ Checks similarity between the generated description and the current descriptions using Levenshtein """
        generated_description = self.generated_output.text()
    
        if not generated_description:
            self.error_message.setText("Please generate a description first.")
            return
    
        current_sku = self.current_descriptions[0]  # Start with the first description as the current SKU
        list_of_skus = []
        dictionary = {}
        list_of_colors = ["black", "blue", "yellow", "orange", "green", "grey", "gray", "natural", "transparent", "gold", "white", "amber", "clear", "platinum", "emerald", "dark"]

        # Iterate through the descriptions and calculate similarity
        for index, sku in enumerate(self.current_descriptions):
            cur_ratio = lv.jaro_winkler(current_sku, sku)
            if cur_ratio < 0.8:
                dictionary[current_sku] = list_of_skus
                list_of_skus = []
                current_sku = sku
                list_of_skus.append({current_sku: lv.jaro_winkler(current_sku, sku)})
            else:
                for color in list_of_colors:
                    if color in sku.lower():
                        sku = sku.replace(color, "")
                        array_of_issues = [cur_ratio, "colors"]
                        list_of_skus.append({sku: array_of_issues})

        # Find the best match
        all_descriptions = self.current_descriptions + [generated_description]
        similarity_scores = [lv.jaro_winkler(generated_description, desc) for desc in self.current_descriptions]
    
        # Find the top match and display it
        top_index = max(range(len(similarity_scores)), key=similarity_scores.__getitem__)
        top_similarity_score = similarity_scores[top_index]
        top_description = self.current_descriptions[top_index]
    
        self.similarity_report.setText(f"Top Similarity: {top_description}\nScore: {top_similarity_score:.2f}")


    def copy_and_save_description(self):
        """ Copies the generated SKU to clipboard and saves it to the current descriptions """
        generated_description = self.generated_output.text()
        
        if not generated_description:
            self.error_message.setText("Please generate a description first.")
            return
        
        # Step 1: Copy the generated description to the clipboard
        clipboard = QApplication.clipboard()  # Access the clipboard
        clipboard.setText(generated_description)  # Set the clipboard text to the generated description

        # Step 2: Save the generated description to the current descriptions list
        self.current_descriptions.append(generated_description)  # Add to the list of current descriptions

        # Optionally, show a confirmation message
        self.save_message.setText(f"Description copied and saved: {generated_description}")
