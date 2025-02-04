from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QLabel, QComboBox, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QClipboard

class SKUGeneratorUI(QWidget):
    def __init__(self):
        super().__init__()

        self.supplier_input = QComboBox()
        self.supplier_input.setEditable(True)
        self.supplier_input.setPlaceholderText("Select Supplier") 
        self.supplier_input.addItems(['INTELLECT'])

        self.model_input = QComboBox()
        self.model_input.setEditable(True)
        self.model_input.setPlaceholderText("Select Model") 
        self.model_input.addItems(['CM-1', 'CM-2', 'CM-3', 'CRATE COVER'])  
        self.model_input.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)
        
        self.family_input = QComboBox()
        self.family_input.setEditable(True)
        self.family_input.setPlaceholderText("Select Family") 
        self.family_input.addItems(['TROLLEYS', 'SPECIAL SIZE', 'DRUM PALLET', 'GLASS CRATE', 'PAPER TRAY', 'WAREWASH', '80L MOBILE BIN SET', 'ABS SHEET', 'PP JARS', 'PINT', '150ML PET BOTTLE - TAPERED', 'DECK TYPE', 'EXCEL II DESK', 'SUGOI BOTTLE', '5 LT PET SQUARE JAR', 'INFUSION TUB', 'KIDDIE SQUARE TABLE', 'SUMP PUMP BOX', 'PLASTIC BIN', 'SMB PROMO BUCKET', 'DIGESTER', '5 GALLON', 'CUSTOMIZED TROLLEY', 'IRON CAGE', 'COFFEE SOLAR DRYER', 'LEG A&B', 'STEEL RACK', 'MPC 250G', 'TROLLEY ACCESORIES', '500ML ROUND PET BOTTLE', 'DECK TYPE - SOLID', 'PAIL', 'HDPE SHEET', '150ML PET BOTTLE - SQUARE', '350ML PET ROUND JAR', 'DIE CUT-LID', '385ML / 28MM PET BOTTLE', 'FLOORING PALLETS - GRID', 'LIBRARY HUB', 'KNORR SPOON', 'RIVET', 'AIR FREIGHT', 'TROLLEY PARTS', 'SHOE RACK', 'FLOORING PALLETS', 'REPAIR', 'STEAMER', 'J-HOOK', 'SMARTEE PARTS', 'ARM CHAIR', 'SPACE SAVER ROUND', 'COSMETIC SPRAYER', 'SUNLOUNGER', 'SUPPLIES FOR CRATE REWORKS', '2 LT / 4 LT PAIL', 'ARIEL CANISTER', 'KIDDIE CHAIR', 'PLASTIC HUB', 'EGG MATTING', 'HIPS SHEET', 'NO FAMILY', 'SUBCON FINISHED GOODS', 'GRINDING COST', 'FRONT BUMPER', 'OUTLET ACCESSORIES', 'KIDDIE DESK', 'MPC 500G', '4-L PAIL', '500ML/38MM BOTTLE', 'TABLETOP DISPENSER', 'CANS', '300ML PET ROUND JAR', 'WELDING COST', 'PPHS PBOX', '950ML PLASTIC CONTAINER', 'CYLINDER', 'HANGERS', '1810 CLOSURE', '250ML/28MM BOTTLE', 'CONTAINER', '16-L PAIL - PARTS', 'TWIN PACK', 'PUDDING CUP', '"A" SERIES CRATES', '5 TRAY SOLAR DRYER', 'SALT DRYER', 'RACK BASE', 'OVERCAP', 'SPOONS', 'PLASTI-FORM', '500G PET JAR', '4-L PAIL - PARTS', 'ONE PC PALLET', 'STACKABLE CONTAINER', 'MARSLITE BOTTLE', 'INTELLECT PARTS', '170G PET JAR', '4 LT PET SQUARE JAR', 'PARASOL PARTS', 'SILKSCREEN SUPPLIES', 'PLASTIC CONTAINER', 'FOLDABLE PERFORATED CRATES', 'ICE CREAM', '3.5 LT PET ROUND JAR', 'JOHNSONS BOTTLE', 'TUMBLERS', 'MULTI PURPOSE CLIP', 'TAG HOLDER', '520X360', 'LAMINATED ASHINAGA', '38MM PET BOTTLE', '2 LT PET SQUARE JAR', 'LIBRARY ORGANIZER', '2.5-L PAIL - PARTS', 'REVERSIBLE TYPE - GRID', 'NESTABLE / STACKABLE', 'GEOMEMBRANE', '30ML BOTTLE', 'SPOUT', 'HOMO SHEET', 'PE SHEETS', 'TRAYS', 'INSTALLATION CHARGE', 'PLASTIC SEPARATOR', 'TUMBLERS (IMPORTED)', '500ML/28MM BOTTLE', 'RUBBER PAD', 'PARK BENCH PARTS', 'FISH BASKET', 'RENTAL FEE', '150ML PET BOTTLE', 'EGG CRATES', '230G PET JARS', 'PRINTING CHARGE', '400ML PET JAR ROUND', 'GREENHOUSE ROOFING', 'DESIGN CHARGE', 'DIVIDER', '10-L PAIL', 'BOTTOM PALLET', 'MOBILE BIN PARTS', 'DISPLAY RACK', 'FISH DRYER', 'EXCEL II DESK - PARTS', 'DEVELOPMENT FEE', 'SCOOPS', '150ML PET BOTTLE - ROUND', 'OFFICE TABLE', 'REWORKS', '30ML PET JAR', 'STOOL CHAIR', 'MOBILE BIN SET', 'CRATE W/ BUILT IN COVER', 'TUMBLERS (LOCAL)', '150ML PET BOTTLE ONLY', 'TRIO PACK', 'CLIP HANDLE', 'CRATING COST', 'RE-SEALING', 'STEEL FRAME RACK', 'THREAD SPOUT', 'PIPE CLIPS', 'DRAIN HOSE', 'CAGE', 'PLASTIC TRAY', '10-L PAIL - PARTS', 'REFRACTOR', 'SERIVCE CHARGE', 'MAPAL BED PARTS', 'PAIL SEAL', 'WELDING MATERIAL', 'GREENHOUSE COVER', 'BREAD CRATES', 'PPHS PDIV', 'GENESIS SET - PARTS', 'TP CRATES', 'JUMBOX', '1 LT PET SQUARE JAR', '350ML/28MM BOTTLE', 'CUSHION', 'BREATHER TANK', 'TROLLEY 2', '16 KG PAIL', 'PLASTIC CART', 'DELIVERY CHARGE', 'PET JARS', '18-L PAIL - PARTS', 'SIDE CHAIRS', 'HANDLE LOCK', '2-L PAIL', '1.5 LT PET SQUARE JAR', '540X370', 'RAIN SHELTER', 'GENESIS SET', 'BREAD RACK', 'ONE WAY PALLET', 'TABLE PARTS', 'KIDDIE GROUP TABLE', '20-L PAIL - PARTS', 'FLOORING PALLETS - SOLID', 'FLOWERS', '75ML PET BOTTLE', 'HANGER', '16-L PAIL', 'ID HOLDER', '600X400', 'ARRASTRE', 'CLIP BASE', 'SANKO PALLET', '2.5-L PAIL', 'PALLET ACCESSORIES', 'SQUARE TABLE', 'DRYING TRAY', 'ARMCHAIRS', 'BOTTLE HOLDER', 'HOSE HOLDER', '116MM JAR COVER', 'GOLF BALLS', 'BLAST FREEZING', '350ML CYLINDRICAL BOTTLE', 'OTHER PRODUCTS', 'STEEL CUTTING COST', 'EGG TRAY 1 SML', 'MAYO JAR', '50ML PET BOTTLE', 'DECK TYPE - GRID TOP', 'PARK BENCH', 'INTELLECT CHAIR', 'OVAL TABLE', 'BOX FRAME', 'PREFORM', '250ML PET JARS', 'BIN BOX', 'EGG TRAY 2 XL', '500ML H20 PET BOTTLE', 'FOOTING', 'GRASS MATTING', '250ML PET BOTTLE', '340G PET JAR', 'GASTRONORMS', 'PAIL PORTABLE', 'TROLLEY PORTABLE', '350ML PET SQUARE JAR', 'LABOR CHARGES', 'REVERSIBLE TYPE', 'PIVOT', '236ML PET BOTTLE', '5 TRAY SOLAR DRYER PARTS', 'STOVE BOLT W/ WASHER', 'COMPARTMENTS', '2-L PAIL - PARTS', 'BROAD BEAN BAGS', '4 CAN CARRIER', 'CONVEYOR COVER', 'CRATE COVER', 'LINER W/ OUTLET PORT', 'BOTTLE CRATE', 'SOLAR TUNNEL DRYER', '3 LT PET SQUARE JAR', '240L MOBILE BIN SET', 'BLADDER TYPE', '300ML PET SQUARE JAR', 'CHICKEN HOUSE MATTING', '500ML PET SQUARE JAR', 'ROUND TABLE', '1QUART CONTAINER', 'PPHS', 'CONPALLETER', 'PITCHER', 'FOLDABLE CLOSED CRATE', '300ML/28MM BOTTLE', 'GREENHOUSE CURTAIN', 'CARTS', 'INLET PORT', 'SLIP SHEET', '20-L PAIL', '120MM PET JAR', 'SOLID TYPE', 'TANSAN TABLE', '1811 CLOSURE', 'SPACE SAVER SQUARE', '350ML/38MM BOTTLE', 'OVERFLOW PIPE', 'TROLLEY 1', 'nan', 'FREIGHT COST', 'PAIL HANDLE', 'PALLET 1012', 'PALLET CUT OUT', '3.5 LT PET SQUARE JAR', '1-L PET JARS', 'TENT', 'CUSTOMIZED SHADEHOUSE', 'BANERA', 'FOOD PROCESSING / DISPLAY TRAYS', 'CAPS', '100ML CYLINDRICAL BOTTLE', 'REVERSIBLE TYPE - SOLID', 'CRATE HANDLE', 'TOP PALLET', 'CHICKEN HOUSE FOOTING', 'CHAIR ACCESSORIES', 'TABLE', 'BOTTLE CAPS', 'STEEL CAGE TROLLEY', '135ML BOTTLE', 'PARASOL SET', 'SMARTEE CHAIR'])  
        self.family_input.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.color_combo = QComboBox()
        self.color_combo.setEditable(True)
        self.color_combo.setPlaceholderText("Select Color") 
        self.color_combo.addItems(['BLUE', 'RED', 'GREEN', 'Black'])  
        self.color_combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.size_combo = QComboBox()
        self.size_combo.setEditable(True)
        self.size_combo.setPlaceholderText("Select Size")
        self.size_combo.addItems(['1L', '500ML', '2L'])  
        self.size_combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.material_combo = QComboBox()
        self.material_combo.setEditable(True)
        self.material_combo.setPlaceholderText("Select Material") 
        self.material_combo.addItems(['PLASTIC', 'GLASS', 'HDPE'])   
        self.material_combo.setInsertPolicy(QComboBox.InsertPolicy.InsertAlphabetically)

        self.virgin_option = QComboBox()
        self.virgin_option.setEditable(True)
        self.virgin_option.setPlaceholderText("Select") 
        self.virgin_option.addItems(['01','02'])
        

        # Generate SKU Button
        self.sku_button = QPushButton("Generate SKU")

        # Copy SKU Button
        self.copy_button = QPushButton("Copy SKU")
        self.copy_button.clicked.connect(self.copy_sku)

        # Clear All Fields Button
        self.clear_button = QPushButton("Clear All Fields")
        self.clear_button.clicked.connect(self.clear_all_fields)

        # Result label
        self.sku_result = QLabel("Generated SKU: ")

        # Create the layout
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()
        
        # Form layout
        layout.addWidget(self.clear_button)

        form_layout.addRow("Supplier:", self.supplier_input)
        form_layout.addRow("Model:", self.model_input)
        form_layout.addRow("Product Family:", self.family_input)
        form_layout.addRow("Color:", self.color_combo)
        form_layout.addRow("Size:", self.size_combo)
        form_layout.addRow("Material:", self.material_combo)
        form_layout.addRow("Virgin:", self.virgin_option)

        layout.addLayout(form_layout)
        layout.addWidget(self.sku_button)
        layout.addWidget(self.sku_result)
        layout.addWidget(self.copy_button)

    def copy_sku(self):
        # Get the generated SKU text from the result label
        sku_text = self.sku_result.text().replace("Generated SKU: ", "")
        
        # Get the system clipboard and set the text
        clipboard = QApplication.clipboard()
        clipboard.setText(sku_text)
        

    def clear_all_fields(self):
        # Reset all the dropdowns to blank
        self.supplier_input.setCurrentIndex(-1)
        self.model_input.setCurrentIndex(-1)
        self.family_input.setCurrentIndex(-1)
        self.color_combo.setCurrentIndex(-1)
        self.size_combo.setCurrentIndex(-1)
        self.material_combo.setCurrentIndex(-1)
        self.virgin_option.setCurrentIndex(-1)
        
        # Clear the result label
        self.sku_result.setText("Generated SKU: ")
