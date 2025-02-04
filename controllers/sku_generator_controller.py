from ui.sku_generator_ui import SKUGeneratorUI
import os
import sys

class SKUGeneratorController:
    def __init__(self, ui: SKUGeneratorUI):
        self.ui = ui
        self.ui.sku_button.clicked.connect(self.generate_sku)

        # Predefined options
        self.predefined_model = []
        self.predefined_family = []
        self.predefined_colors = ['BLUE', 'RED', 'GREEN']
        self.predefined_sizes = ['1L', '500ml', '2L']
        self.predefined_materials = ['PLASTIC', 'GLASS', 'HDPE']
        self.predefined_virgin = ['01', '02']


    def generate_sku(self):        
        # Get selected or custom values
        supplier = self.ui.supplier_input.currentText().upper()
        model = self.ui.model_input.currentText().upper()
        base_sku = self.ui.family_input.currentText().upper()
        color = self.ui.color_combo.currentText().upper()
        size = self.ui.size_combo.currentText().upper()
        material = self.ui.material_combo.currentText().upper()
        virgin = self.ui.virgin_option.currentText()

        # Check if user entered new custom values, and save them
        if color not in self.predefined_colors:
            self.save_custom_value('color', color)
        
        if size not in self.predefined_sizes:
            self.save_custom_value('size', size)

        if material not in self.predefined_materials:
            self.save_custom_value('material', material)
        
        # Generate SKU (simple concatenation)
        generated_sku = f"{supplier} {model} {base_sku} {color} {size} {virgin} {material}"

        # Set result label
        self.ui.sku_result.setText(f"Generated SKU: {generated_sku}")

    def save_custom_value(self, category, value):
        if category == 'color' and value not in self.predefined_colors:
            self.predefined_colors.append(value)
            self.ui.color_combo.addItem(value)
        elif category == 'size' and value not in self.predefined_sizes:
            self.predefined_sizes.append(value)
            self.ui.size_combo.addItem(value)
        elif category == 'virgin' and value not in self.predefined_virgin:
            self.predefined_virgin.append(value)
            self.ui.virgin_option.addItem(value)
        elif category == 'material' and value not in self.predefined_materials:
            self.predefined_materials.append(value)
            self.ui.material_combo.addItem(value)
        elif category == 'model' and value not in self.predefined_model:
            self.predefined_model.append(value)
            self.ui.model_input.addItem(value)

    
