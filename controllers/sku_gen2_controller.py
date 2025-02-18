from ui.sku_gen2_ui import DescriptionGeneratorUI

class DescriptionGeneratorController:
    def __init__(self, ui: DescriptionGeneratorUI):
        self.ui = ui

    def setup(self):
        """ Initialize the app and set up the UI """
        self.ui.show()
