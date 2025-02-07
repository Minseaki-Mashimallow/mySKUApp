from ui.description_standard_ui import DescriptionStandardUI
from backend import database as db

class DescriptionStandardController:
    saved_descriptions = {} # { 'ICE CREAM': 'ICE CREAM-Color-Size' }
    saved_families = db.LoadFamilies() 
    saved_attributes = set()

    def __init__(self, ui: DescriptionStandardUI):
        self.ui = ui
        self.ui.add_attribute_button.clicked.connect(self.add_attribute)
        self.ui.view_button.clicked.connect(self.view_description)
        self.ui.save_button.clicked.connect(self.save_description)

    def add_attribute(self):
        """Adds a new attribute dropdown field"""
        self.ui.add_attribute_field()

    def view_description(self):
        """Generates the product description standard and updates the UI"""
        product_family = self.ui.get_product_family().strip()
        product_model = self.ui.get_product_model().strip()
    
        attributes = [attr.strip() for attr in self.ui.get_attributes() if attr.strip()]

        if not product_family:
            self.ui.set_generated_description("Error: Product family is required.")
            return

        if not attributes:
            self.ui.set_generated_description("Error: At least one attribute is required.")
            return
        
        # Generate the description standard format
        generated_name = f"{product_family}-" + "-".join(attributes)
    
        # Display it to the user
        self.ui.set_generated_description(generated_name)

    def save_description(self):
        """Saves the generated description standard and confirms the save."""
        product_family = self.ui.get_product_family().strip()
        product_model = self.ui.get_product_model().strip()
        attributes = [attr.strip() for attr in self.ui.get_attributes() if attr.strip()]

        ## TODO: FIX THIS TO BE EDITABLE
        category = "placeholder"
    
        if not product_family or not attributes:
            return  # Prevent saving if data is missing

        generated_name = f"{product_family}-" + "-".join(attributes)

        # Save product family if not already saved
        if product_family not in db.LoadFamilies():
            db.CreateFamily(product_family, category)
            self.ui.product_family_input.addItems([product_family])

        # Save product model if not already saved
        # THIS INCLUDES ATTRIBUTES
        if db.LoadModel(product_model):
            self.ui.show_save_fail()
        else:
            print(db.LoadModels(product_family))
            db.CreateModel(product_model, product_family, attributes)
            self.ui.product_model_input.addItems([product_model])
            self.ui.show_save_confirmation()


    
    @classmethod
    def get_saved_descriptions(cls):
        """ Returns saved standards as {product_family: [attributes]} """
        return {family: desc.split("-")[1:] for family, desc in cls.saved_descriptions.items()}
    
    @classmethod
    def get_saved_families(cls):
        """Returns the saved product families"""
        return list(cls.saved_families)

    @classmethod
    def get_saved_attributes(cls):
        """Returns the saved attributes"""
        return list(cls.saved_attributes)


if __name__ == "__main__":
    existing_families = DescriptionStandardController.get_saved_families()
    existing_attributes = DescriptionStandardController.get_saved_attributes()
    ui = DescriptionStandardUI(existing_families, existing_attributes)
    DescriptionStandardController(ui)


