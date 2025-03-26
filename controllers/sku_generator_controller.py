from PyQt6.QtWidgets import QApplication
from ui.sku_generator_ui import SKUGeneratorUI
from controllers.description_standard_controller import DescriptionStandardController
from backend import database as db

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import Levenshtein as lv

class SKUGeneratorController:
    def __init__(self, ui: SKUGeneratorUI):
        self.current_descriptions = db.LoadDescriptions()

        self.ui = ui
        self.ui.sku_button.clicked.connect(self.generate_sku)
        self.ui.similarity_button.clicked.connect(self.check_similarity)
        self.ui.copy_button.clicked.connect(self.copy_description)

    def generate_sku(self):
        """Generates an SKU based on selected attributes."""
        selected_model = self.ui.model_input.currentText().strip()

        # check if theres a set standard
        if selected_model not in db.LoadModels(self.ui.get_product_family()):
            self.ui.copy_message.setText("Error: No standard found. Set a description standard first.")
            return

        attributes = db.LoadModelParameters(self.ui.get_product_model())
        # extract attributes from standard
        attribute_values = [attr.strip() for attr in self.ui.get_attributes() if attr.strip()]

        attribute_check = False

        if(len(attribute_values) != 0):
            for x in attribute_values:
                if x in attributes:
                    attribute_check = True
                    break
        else:
            attribute_check = True

        if attribute_check or not all(attribute_values):  # ensure all attributes are filled
            self.ui.copy_message.setText("Error: Please fill all required attributes.")
            return

        p_no_list = ["Type", "Material", "Size", "Dimension"]
        mod_list = ["Parts", "Color"]
        desc_list = ["Additional Features"]

        part_no = set()
        model_list = set()
        description_list = set()
        for x in attributes:
            current_attribute = db.LoadAttribute(x)
            for attr in attribute_values:
                if attr in current_attribute:
                    if x in p_no_list:
                        part_no.add(attr)

                    if x in mod_list:
                        model_list.add(attr)

                    if x in desc_list:
                        description_list.add(attr)
        
        full_description = f"{selected_model} {' '.join(part_no)} {' '.join(model_list)} {' '.join(description_list)}"

        # Update fields
        self.ui.product_family_display.setText(selected_model)
        self.ui.part_no_input.setText(" ".join(part_no))
        self.ui.model_list_input.setText(" ".join(model_list))
        self.ui.description_input.setText(" ".join(description_list))
        self.ui.full_description_input.setText(full_description)

        self.ui.copy_button.setEnabled(True)  # enable copy  

    def check_similarity(self):
        """ Checks similarity between the generated description and the current descriptions using Levenshtein """
        generated_description = self.ui.full_description_input.text().strip()
    
        if not generated_description:
            self.error_message.setText("Please generate a description first.")
            return
    
        current_descriptions = db.LoadDescriptions()
        current_sku = current_descriptions[0]  # Start with the first description as the current SKU
        list_of_skus = []
        dictionary = {}

        # Iterate through the descriptions and calculate similarity
        for index, sku in enumerate(current_descriptions):
            cur_ratio = lv.jaro_winkler(current_sku, sku)
            if cur_ratio < 0.8:
                dictionary[current_sku] = list_of_skus
                list_of_skus = []
                current_sku = sku
                list_of_skus.append({current_sku: lv.jaro_winkler(current_sku, sku)})
                # Find the best match

        all_descriptions = current_descriptions + [generated_description]
        similarity_scores = [lv.jaro_winkler(generated_description, desc) for desc in current_descriptions]
    
        # Find the top match and display it
        top_index = max(range(len(similarity_scores)), key=similarity_scores.__getitem__)
        top_similarity_score = similarity_scores[top_index]
        top_description = current_descriptions[top_index]
    
        self.ui.similarity_report.setText(f"Top Similarity: {top_description}\nScore: {top_similarity_score:.2f}")


    def copy_description(self):
        """ Copies the generated SKU to clipboard and saves it to the current descriptions """

        generated_description = f"\n{self.ui.model_input.currentText().strip()} " + "\nPart Number: " +  self.ui.part_no_input.text().strip() + "\nModel List: " + self.ui.model_list_input.text().strip() + "\nDescription: " + self.ui.description_input.text().strip() + "\n\nFull Description: " + self.ui.full_description_input.text().strip()
        
        save_long_sku = self.ui.full_description_input.text().strip()
        
        if generated_description is None:
            self.ui.copy_message.setText("Please generate a description first.")
            return
        
        # Copy the generated description to the clipboard
        clipboard = QApplication.clipboard()  
        clipboard.setText(generated_description)  # Set the clipboard text to the generated description

        # Save the generated description to the current descriptions list
        self.current_descriptions.append(save_long_sku) 
        db.AddDescription(save_long_sku)

        # Show a confirmation message
        self.ui.copy_message.setText(f"Description copied and saved! \n{save_long_sku}")