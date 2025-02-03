from ui.sku_generator_ui import SKUGeneratorUI

class SKUGeneratorController:
    def __init__(self, ui: SKUGeneratorUI):
        self.ui = ui
        self.ui.sku_button.clicked.connect(self.generate_sku)

    def generate_sku(self):
        base_sku = self.ui.sku_input.text()
        # Generate SKU by appending a suffix
        generated_sku = f"{base_sku}-XYZ123"
        self.ui.sku_result.setText(f"Generated SKU: {generated_sku}")