from ui.add_new_description_ui import AddNewDescriptionUI
from backend import database as db

class AddNewDescriptionController:
    def __init__(self, ui: AddNewDescriptionUI):
        self.ui = ui