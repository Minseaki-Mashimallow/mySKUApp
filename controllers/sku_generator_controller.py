from ui.sku_generator_ui import SKUGeneratorUI
from controllers.description_standard_controller import DescriptionStandardController

class SKUGeneratorController:
    def __init__(self, ui: SKUGeneratorUI):
        self.ui = ui
        self.ui.sku_button.clicked.connect(self.generate_sku)

        # load predefined standards from the description standard controller
        self.saved_standards = DescriptionStandardController.get_saved_descriptions()

    def generate_sku(self):
        """Generates an SKU based on selected attributes."""
        selected_family = self.ui.family_input.currentText().strip()

        # check if theres a set standard
        if selected_family not in self.saved_standards:
            self.ui.sku_result.setText("Error: No standard found. Set a description standard first.")
            return

        attributes = self.saved_standards[selected_family]  # extract attributes from standard
        attribute_values = [self.ui.attribute_fields[attr].currentText().strip().upper() for attr in attributes]

        if not all(attribute_values):  # ensure all attributes are filled
            self.ui.sku_result.setText("Error: Please fill all required attributes.")
            return

        # generate sku based on standard
        generated_sku = f"{selected_family} " + " ".join(attribute_values)
        self.ui.sku_result.setText(f"Generated SKU: {generated_sku}")

        self.ui.copy_button.setEnabled(True)  # enable copy button

