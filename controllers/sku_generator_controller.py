from ui.sku_generator_ui import SKUGeneratorUI
from controllers.description_standard_controller import DescriptionStandardController
from backend import database as db

class SKUGeneratorController:
    def __init__(self, ui: SKUGeneratorUI):
        self.ui = ui
        self.ui.sku_button.clicked.connect(self.generate_sku)

    def generate_sku(self):
        """Generates an SKU based on selected attributes."""
        selected_model = self.ui.model_input.currentText().strip()

        # check if theres a set standard
        if selected_model not in db.LoadModels(self.ui.get_product_family()):
            self.ui.sku_result.setText("Error: No standard found. Set a description standard first.")
            return

        attributes = db.LoadModelParameters(self.ui.get_product_model())
        # extract attributes from standard
        attribute_values = [attr.strip() for attr in self.ui.get_attributes() if attr.strip()]

        attribute_check = False

        for x in attribute_values:
            if x in attributes:
                attribute_check = True
                break

        if not all(attribute_values) or attribute_check:  # ensure all attributes are filled
            self.ui.sku_result.setText("Error: Please fill all required attributes.")
            return

        attribute_dict = {}

        # generate sku based on standard
        generated_sku = f"{selected_model} " + " ".join(attribute_values)
        self.ui.sku_result.setText(f"Generated SKU: {generated_sku}")

        self.ui.copy_button.setEnabled(True)  # enable copy  




