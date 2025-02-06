from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout, QScrollArea, QComboBox

class DescriptionStandardUI(QWidget):
    def __init__(self, existing_families=None, existing_attributes=None):
        super().__init__()

        self.existing_families = ['TROLLEYS', 'SPECIAL SIZE', 'DRUM PALLET', 'GLASS CRATE', 'PAPER TRAY', 'WAREWASH', '80L MOBILE BIN SET', 'ABS SHEET', 'PP JARS', 'PINT', '150ML PET BOTTLE - TAPERED', 'DECK TYPE', 'EXCEL II DESK', 'SUGOI BOTTLE', '5 LT PET SQUARE JAR', 'INFUSION TUB', 'KIDDIE SQUARE TABLE', 'SUMP PUMP BOX', 'PLASTIC BIN', 'SMB PROMO BUCKET', 'DIGESTER', '5 GALLON', 'CUSTOMIZED TROLLEY', 'IRON CAGE', 'COFFEE SOLAR DRYER', 'LEG A&B', 'STEEL RACK', 'MPC 250G', 'TROLLEY ACCESORIES', '500ML ROUND PET BOTTLE', 'DECK TYPE - SOLID', 'PAIL', 'HDPE SHEET', '150ML PET BOTTLE - SQUARE', '350ML PET ROUND JAR', 'DIE CUT-LID', '385ML / 28MM PET BOTTLE', 'FLOORING PALLETS - GRID', 'LIBRARY HUB', 'KNORR SPOON', 'RIVET', 'AIR FREIGHT', 'TROLLEY PARTS', 'SHOE RACK', 'FLOORING PALLETS', 'REPAIR', 'STEAMER', 'J-HOOK', 'SMARTEE PARTS', 'ARM CHAIR', 'SPACE SAVER ROUND', 'COSMETIC SPRAYER', 'SUNLOUNGER', 'SUPPLIES FOR CRATE REWORKS', '2 LT / 4 LT PAIL', 'ARIEL CANISTER', 'KIDDIE CHAIR', 'PLASTIC HUB', 'EGG MATTING', 'HIPS SHEET', 'NO FAMILY', 'SUBCON FINISHED GOODS', 'GRINDING COST', 'FRONT BUMPER', 'OUTLET ACCESSORIES', 'KIDDIE DESK', 'MPC 500G', '4-L PAIL', '500ML/38MM BOTTLE', 'TABLETOP DISPENSER', 'CANS', '300ML PET ROUND JAR', 'WELDING COST', 'PPHS PBOX', '950ML PLASTIC CONTAINER', 'CYLINDER', 'HANGERS', '1810 CLOSURE', '250ML/28MM BOTTLE', 'CONTAINER', '16-L PAIL - PARTS', 'TWIN PACK', 'PUDDING CUP', '"A" SERIES CRATES', '5 TRAY SOLAR DRYER', 'SALT DRYER', 'RACK BASE', 'OVERCAP', 'SPOONS', 'PLASTI-FORM', '500G PET JAR', '4-L PAIL - PARTS', 'ONE PC PALLET', 'STACKABLE CONTAINER', 'MARSLITE BOTTLE', 'INTELLECT PARTS', '170G PET JAR', '4 LT PET SQUARE JAR', 'PARASOL PARTS', 'SILKSCREEN SUPPLIES', 'PLASTIC CONTAINER', 'FOLDABLE PERFORATED CRATES', 'ICE CREAM', '3.5 LT PET ROUND JAR', 'JOHNSONS BOTTLE', 'TUMBLERS', 'MULTI PURPOSE CLIP', 'TAG HOLDER', '520X360', 'LAMINATED ASHINAGA', '38MM PET BOTTLE', '2 LT PET SQUARE JAR', 'LIBRARY ORGANIZER', '2.5-L PAIL - PARTS', 'REVERSIBLE TYPE - GRID', 'NESTABLE / STACKABLE', 'GEOMEMBRANE', '30ML BOTTLE', 'SPOUT', 'HOMO SHEET', 'PE SHEETS', 'TRAYS', 'INSTALLATION CHARGE', 'PLASTIC SEPARATOR', 'TUMBLERS (IMPORTED)', '500ML/28MM BOTTLE', 'RUBBER PAD', 'PARK BENCH PARTS', 'FISH BASKET', 'RENTAL FEE', '150ML PET BOTTLE', 'EGG CRATES', '230G PET JARS', 'PRINTING CHARGE', '400ML PET JAR ROUND', 'GREENHOUSE ROOFING', 'DESIGN CHARGE', 'DIVIDER', '10-L PAIL', 'BOTTOM PALLET', 'MOBILE BIN PARTS', 'DISPLAY RACK', 'FISH DRYER', 'EXCEL II DESK - PARTS', 'DEVELOPMENT FEE', 'SCOOPS', '150ML PET BOTTLE - ROUND', 'OFFICE TABLE', 'REWORKS', '30ML PET JAR', 'STOOL CHAIR', 'MOBILE BIN SET', 'CRATE W/ BUILT IN COVER', 'TUMBLERS (LOCAL)', '150ML PET BOTTLE ONLY', 'TRIO PACK', 'CLIP HANDLE', 'CRATING COST', 'RE-SEALING', 'STEEL FRAME RACK', 'THREAD SPOUT', 'PIPE CLIPS', 'DRAIN HOSE', 'CAGE', 'PLASTIC TRAY', '10-L PAIL - PARTS', 'REFRACTOR', 'SERIVCE CHARGE', 'MAPAL BED PARTS', 'PAIL SEAL', 'WELDING MATERIAL', 'GREENHOUSE COVER', 'BREAD CRATES', 'PPHS PDIV', 'GENESIS SET - PARTS', 'TP CRATES', 'JUMBOX', '1 LT PET SQUARE JAR', '350ML/28MM BOTTLE', 'CUSHION', 'BREATHER TANK', 'TROLLEY 2', '16 KG PAIL', 'PLASTIC CART', 'DELIVERY CHARGE', 'PET JARS', '18-L PAIL - PARTS', 'SIDE CHAIRS', 'HANDLE LOCK', '2-L PAIL', '1.5 LT PET SQUARE JAR', '540X370', 'RAIN SHELTER', 'GENESIS SET', 'BREAD RACK', 'ONE WAY PALLET', 'TABLE PARTS', 'KIDDIE GROUP TABLE', '20-L PAIL - PARTS', 'FLOORING PALLETS - SOLID', 'FLOWERS', '75ML PET BOTTLE', 'HANGER', '16-L PAIL', 'ID HOLDER', '600X400', 'ARRASTRE', 'CLIP BASE', 'SANKO PALLET', '2.5-L PAIL', 'PALLET ACCESSORIES', 'SQUARE TABLE', 'DRYING TRAY', 'ARMCHAIRS', 'BOTTLE HOLDER', 'HOSE HOLDER', '116MM JAR COVER', 'GOLF BALLS', 'BLAST FREEZING', '350ML CYLINDRICAL BOTTLE', 'OTHER PRODUCTS', 'STEEL CUTTING COST', 'EGG TRAY 1 SML', 'MAYO JAR', '50ML PET BOTTLE', 'DECK TYPE - GRID TOP', 'PARK BENCH', 'INTELLECT CHAIR', 'OVAL TABLE', 'BOX FRAME', 'PREFORM', '250ML PET JARS', 'BIN BOX', 'EGG TRAY 2 XL', '500ML H20 PET BOTTLE', 'FOOTING', 'GRASS MATTING', '250ML PET BOTTLE', '340G PET JAR', 'GASTRONORMS', 'PAIL PORTABLE', 'TROLLEY PORTABLE', '350ML PET SQUARE JAR', 'LABOR CHARGES', 'REVERSIBLE TYPE', 'PIVOT', '236ML PET BOTTLE', '5 TRAY SOLAR DRYER PARTS', 'STOVE BOLT W/ WASHER', 'COMPARTMENTS', '2-L PAIL - PARTS', 'BROAD BEAN BAGS', '4 CAN CARRIER', 'CONVEYOR COVER', 'CRATE COVER', 'LINER W/ OUTLET PORT', 'BOTTLE CRATE', 'SOLAR TUNNEL DRYER', '3 LT PET SQUARE JAR', '240L MOBILE BIN SET', 'BLADDER TYPE', '300ML PET SQUARE JAR', 'CHICKEN HOUSE MATTING', '500ML PET SQUARE JAR', 'ROUND TABLE', '1QUART CONTAINER', 'PPHS', 'CONPALLETER', 'PITCHER', 'FOLDABLE CLOSED CRATE', '300ML/28MM BOTTLE', 'GREENHOUSE CURTAIN', 'CARTS', 'INLET PORT', 'SLIP SHEET', '20-L PAIL', '120MM PET JAR', 'SOLID TYPE', 'TANSAN TABLE', '1811 CLOSURE', 'SPACE SAVER SQUARE', '350ML/38MM BOTTLE', 'OVERFLOW PIPE', 'TROLLEY 1', 'nan', 'FREIGHT COST', 'PAIL HANDLE', 'PALLET 1012', 'PALLET CUT OUT', '3.5 LT PET SQUARE JAR', '1-L PET JARS', 'TENT', 'CUSTOMIZED SHADEHOUSE', 'BANERA', 'FOOD PROCESSING / DISPLAY TRAYS', 'CAPS', '100ML CYLINDRICAL BOTTLE', 'REVERSIBLE TYPE - SOLID', 'CRATE HANDLE', 'TOP PALLET', 'CHICKEN HOUSE FOOTING', 'CHAIR ACCESSORIES', 'TABLE', 'BOTTLE CAPS', 'STEEL CAGE TROLLEY', '135ML BOTTLE', 'PARASOL SET', 'SMARTEE CHAIR']
        self.existing_attributes = ['Model','Color', 'Size', 'Material']

        # Main layout
        self.main_layout = QVBoxLayout(self)

        # Title label
        self.title_label = QLabel("Create New Description Standard")
        self.main_layout.addWidget(self.title_label)

        # Product family
        self.form_layout = QFormLayout()
        self.product_family_input = QComboBox()
        self.product_family_input.setEditable(True)
        self.product_family_input.setPlaceholderText("Select Family")
        self.product_family_input.addItems(self.existing_families)
        self.form_layout.addRow("Select or Enter Product Family:", self.product_family_input)
        self.main_layout.addLayout(self.form_layout)

        # Attribute input
        self.attributes_label = QLabel("Attributes:")
        self.main_layout.addWidget(self.attributes_label)

        # Scroll area for attributes
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.attribute_container = QWidget()
        self.attribute_layout = QVBoxLayout(self.attribute_container)
        self.scroll_area.setWidget(self.attribute_container)
        self.main_layout.addWidget(self.scroll_area)

        # Buttons
        self.add_attribute_button = QPushButton("Add Attribute")
        self.view_button = QPushButton("View")
        self.save_button = QPushButton("Save New Description Standard")
        self.clear_all_button = QPushButton("Clear All")

        # Button layout
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_attribute_button)
        button_layout.addWidget(self.view_button)
        button_layout.addWidget(self.save_button)
        self.main_layout.addLayout(button_layout)

        # Clear All button at the bottom
        self.main_layout.addWidget(self.clear_all_button)

        self.clear_all_button.clicked.connect(self.clear_all_fields)

        # Generated description standard
        self.generated_description_label = QLabel("Generated Standard: /n")
        self.main_layout.addWidget(self.generated_description_label)

        

    def add_attribute_field(self):
        """Adds new attribute input field"""
        attribute_dropdown = QComboBox()
        attribute_dropdown.setEditable(True)
        attribute_dropdown.setPlaceholderText("Select Attribute") 
        attribute_dropdown.addItems(self.existing_attributes)
        self.attribute_layout.addWidget(attribute_dropdown)

    def get_product_family(self):
        """Returns the entered product family"""
        return self.product_family_input.currentText()
    
    def get_attributes(self):
        """Returns selected attributes as a list from dropdowns"""
        attributes = []
        for i in range(self.attribute_layout.count()):
            widget = self.attribute_layout.itemAt(i).widget()
            if isinstance(widget, QComboBox):  
                attributes.append(widget.currentText().strip())
        return attributes

    def set_generated_description(self, text):
        """Updates the generated description label"""
        self.generated_description_label.setText(f"Generated Standard:\n{text}")

    def show_save_confirmation(self):
        """Displays a success message when a new description standard is saved."""
        self.generated_description_label.setText(self.generated_description_label.text() + "\nSaved New Description Standard!")

    def clear_all_fields(self):
        """Resets the UI to its initial state without affecting saved data."""
        self.product_family_input.setCurrentIndex(-1)  # Deselect product family
        self.generated_description_label.setText("Generated Standard: \n")  # Reset text

        # Remove all attribute dropdowns
        while self.attribute_layout.count():
            widget = self.attribute_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

