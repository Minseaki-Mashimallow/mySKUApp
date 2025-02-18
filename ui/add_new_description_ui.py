from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QScrollArea, QComboBox

class AddNewDescriptionUI(QWidget):
    def __init__(self):
        super().__init__()

    '''
    Idea of this Tab:
    - Lets Users add new content to the current attributes
    -- Example: User can add "RAINBOW" to "Color" attribute

    - Lets Users delete a content from the list
    -- Example: User can delete "B1 CRATE" in Product Model
    
    Cant say for sure if delete function is good or will be exploited idk huhu
    '''