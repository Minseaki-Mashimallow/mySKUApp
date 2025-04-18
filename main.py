from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout
from ui.sku_generator_ui import SKUGeneratorUI
from ui.description_standard_ui import DescriptionStandardUI
from ui.sku_gen2_ui import DescriptionGeneratorUI
from ui.add_new_description_ui import AddNewDescriptionUI
from controllers.sku_generator_controller import SKUGeneratorController
from controllers.description_standard_controller import DescriptionStandardController
from controllers.sku_gen2_controller import DescriptionGeneratorController
from controllers.add_new_description_controller import AddNewDescriptionController


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SKU Name Generator")
        self.setGeometry(100, 100, 600, 400)

        # saved product families from DescriptionStandardController
        available_families = ['TROLLEYS', 'SPECIAL SIZE', 'DRUM PALLET', 'GLASS CRATE', 'PAPER TRAY', 'WAREWASH', '80L MOBILE BIN SET', 'ABS SHEET', 'PP JARS', 'PINT', '150ML PET BOTTLE - TAPERED', 'DECK TYPE', 'EXCEL II DESK', 'SUGOI BOTTLE', '5 LT PET SQUARE JAR', 'INFUSION TUB', 'KIDDIE SQUARE TABLE', 'SUMP PUMP BOX', 'PLASTIC BIN', 'SMB PROMO BUCKET', 'DIGESTER', '5 GALLON', 'CUSTOMIZED TROLLEY', 'IRON CAGE', 'COFFEE SOLAR DRYER', 'LEG A&B', 'STEEL RACK', 'MPC 250G', 'TROLLEY ACCESORIES', '500ML ROUND PET BOTTLE', 'DECK TYPE - SOLID', 'PAIL', 'HDPE SHEET', '150ML PET BOTTLE - SQUARE', '350ML PET ROUND JAR', 'DIE CUT-LID', '385ML / 28MM PET BOTTLE', 'FLOORING PALLETS - GRID', 'LIBRARY HUB', 'KNORR SPOON', 'RIVET', 'AIR FREIGHT', 'TROLLEY PARTS', 'SHOE RACK', 'FLOORING PALLETS', 'REPAIR', 'STEAMER', 'J-HOOK', 'SMARTEE PARTS', 'ARM CHAIR', 'SPACE SAVER ROUND', 'COSMETIC SPRAYER', 'SUNLOUNGER', 'SUPPLIES FOR CRATE REWORKS', '2 LT / 4 LT PAIL', 'ARIEL CANISTER', 'KIDDIE CHAIR', 'PLASTIC HUB', 'EGG MATTING', 'HIPS SHEET', 'NO FAMILY', 'SUBCON FINISHED GOODS', 'GRINDING COST', 'FRONT BUMPER', 'OUTLET ACCESSORIES', 'KIDDIE DESK', 'MPC 500G', '4-L PAIL', '500ML/38MM BOTTLE', 'TABLETOP DISPENSER', 'CANS', '300ML PET ROUND JAR', 'WELDING COST', 'PPHS PBOX', '950ML PLASTIC CONTAINER', 'CYLINDER', 'HANGERS', '1810 CLOSURE', '250ML/28MM BOTTLE', 'CONTAINER', '16-L PAIL - PARTS', 'TWIN PACK', 'PUDDING CUP', '"A" SERIES CRATES', '5 TRAY SOLAR DRYER', 'SALT DRYER', 'RACK BASE', 'OVERCAP', 'SPOONS', 'PLASTI-FORM', '500G PET JAR', '4-L PAIL - PARTS', 'ONE PC PALLET', 'STACKABLE CONTAINER', 'MARSLITE BOTTLE', 'INTELLECT PARTS', '170G PET JAR', '4 LT PET SQUARE JAR', 'PARASOL PARTS', 'SILKSCREEN SUPPLIES', 'PLASTIC CONTAINER', 'FOLDABLE PERFORATED CRATES', 'ICE CREAM', '3.5 LT PET ROUND JAR', 'JOHNSONS BOTTLE', 'TUMBLERS', 'MULTI PURPOSE CLIP', 'TAG HOLDER', '520X360', 'LAMINATED ASHINAGA', '38MM PET BOTTLE', '2 LT PET SQUARE JAR', 'LIBRARY ORGANIZER', '2.5-L PAIL - PARTS', 'REVERSIBLE TYPE - GRID', 'NESTABLE / STACKABLE', 'GEOMEMBRANE', '30ML BOTTLE', 'SPOUT', 'HOMO SHEET', 'PE SHEETS', 'TRAYS', 'INSTALLATION CHARGE', 'PLASTIC SEPARATOR', 'TUMBLERS (IMPORTED)', '500ML/28MM BOTTLE', 'RUBBER PAD', 'PARK BENCH PARTS', 'FISH BASKET', 'RENTAL FEE', '150ML PET BOTTLE', 'EGG CRATES', '230G PET JARS', 'PRINTING CHARGE', '400ML PET JAR ROUND', 'GREENHOUSE ROOFING', 'DESIGN CHARGE', 'DIVIDER', '10-L PAIL', 'BOTTOM PALLET', 'MOBILE BIN PARTS', 'DISPLAY RACK', 'FISH DRYER', 'EXCEL II DESK - PARTS', 'DEVELOPMENT FEE', 'SCOOPS', '150ML PET BOTTLE - ROUND', 'OFFICE TABLE', 'REWORKS', '30ML PET JAR', 'STOOL CHAIR', 'MOBILE BIN SET', 'CRATE W/ BUILT IN COVER', 'TUMBLERS (LOCAL)', '150ML PET BOTTLE ONLY', 'TRIO PACK', 'CLIP HANDLE', 'CRATING COST', 'RE-SEALING', 'STEEL FRAME RACK', 'THREAD SPOUT', 'PIPE CLIPS', 'DRAIN HOSE', 'CAGE', 'PLASTIC TRAY', '10-L PAIL - PARTS', 'REFRACTOR', 'SERIVCE CHARGE', 'MAPAL BED PARTS', 'PAIL SEAL', 'WELDING MATERIAL', 'GREENHOUSE COVER', 'BREAD CRATES', 'PPHS PDIV', 'GENESIS SET - PARTS', 'TP CRATES', 'JUMBOX', '1 LT PET SQUARE JAR', '350ML/28MM BOTTLE', 'CUSHION', 'BREATHER TANK', 'TROLLEY 2', '16 KG PAIL', 'PLASTIC CART', 'DELIVERY CHARGE', 'PET JARS', '18-L PAIL - PARTS', 'SIDE CHAIRS', 'HANDLE LOCK', '2-L PAIL', '1.5 LT PET SQUARE JAR', '540X370', 'RAIN SHELTER', 'GENESIS SET', 'BREAD RACK', 'ONE WAY PALLET', 'TABLE PARTS', 'KIDDIE GROUP TABLE', '20-L PAIL - PARTS', 'FLOORING PALLETS - SOLID', 'FLOWERS', '75ML PET BOTTLE', 'HANGER', '16-L PAIL', 'ID HOLDER', '600X400', 'ARRASTRE', 'CLIP BASE', 'SANKO PALLET', '2.5-L PAIL', 'PALLET ACCESSORIES', 'SQUARE TABLE', 'DRYING TRAY', 'ARMCHAIRS', 'BOTTLE HOLDER', 'HOSE HOLDER', '116MM JAR COVER', 'GOLF BALLS', 'BLAST FREEZING', '350ML CYLINDRICAL BOTTLE', 'OTHER PRODUCTS', 'STEEL CUTTING COST', 'EGG TRAY 1 SML', 'MAYO JAR', '50ML PET BOTTLE', 'DECK TYPE - GRID TOP', 'PARK BENCH', 'INTELLECT CHAIR', 'OVAL TABLE', 'BOX FRAME', 'PREFORM', '250ML PET JARS', 'BIN BOX', 'EGG TRAY 2 XL', '500ML H20 PET BOTTLE', 'FOOTING', 'GRASS MATTING', '250ML PET BOTTLE', '340G PET JAR', 'GASTRONORMS', 'PAIL PORTABLE', 'TROLLEY PORTABLE', '350ML PET SQUARE JAR', 'LABOR CHARGES', 'REVERSIBLE TYPE', 'PIVOT', '236ML PET BOTTLE', '5 TRAY SOLAR DRYER PARTS', 'STOVE BOLT W/ WASHER', 'COMPARTMENTS', '2-L PAIL - PARTS', 'BROAD BEAN BAGS', '4 CAN CARRIER', 'CONVEYOR COVER', 'CRATE COVER', 'LINER W/ OUTLET PORT', 'BOTTLE CRATE', 'SOLAR TUNNEL DRYER', '3 LT PET SQUARE JAR', '240L MOBILE BIN SET', 'BLADDER TYPE', '300ML PET SQUARE JAR', 'CHICKEN HOUSE MATTING', '500ML PET SQUARE JAR', 'ROUND TABLE', '1QUART CONTAINER', 'PPHS', 'CONPALLETER', 'PITCHER', 'FOLDABLE CLOSED CRATE', '300ML/28MM BOTTLE', 'GREENHOUSE CURTAIN', 'CARTS', 'INLET PORT', 'SLIP SHEET', '20-L PAIL', '120MM PET JAR', 'SOLID TYPE', 'TANSAN TABLE', '1811 CLOSURE', 'SPACE SAVER SQUARE', '350ML/38MM BOTTLE', 'OVERFLOW PIPE', 'TROLLEY 1', 'nan', 'FREIGHT COST', 'PAIL HANDLE', 'PALLET 1012', 'PALLET CUT OUT', '3.5 LT PET SQUARE JAR', '1-L PET JARS', 'TENT', 'CUSTOMIZED SHADEHOUSE', 'BANERA', 'FOOD PROCESSING / DISPLAY TRAYS', 'CAPS', '100ML CYLINDRICAL BOTTLE', 'REVERSIBLE TYPE - SOLID', 'CRATE HANDLE', 'TOP PALLET', 'CHICKEN HOUSE FOOTING', 'CHAIR ACCESSORIES', 'TABLE', 'BOTTLE CAPS', 'STEEL CAGE TROLLEY', '135ML BOTTLE', 'PARASOL SET', 'SMARTEE CHAIR']

        # Create the tabs
        self.tabs = QTabWidget(self)

        # Tab 1: SKU Generator
        self.sku_ui = SKUGeneratorUI(available_families)
        self.sku_controller = SKUGeneratorController(self.sku_ui)

        # # Tab 2: Set Description Standard
        self.standardization_ui = DescriptionStandardUI()
        self.standardization_controller = DescriptionStandardController(self.standardization_ui)

        # Tab 3: Description Standard Dictionary
        self.description_generator_ui = DescriptionGeneratorUI()
        self.description_generator_controller = DescriptionGeneratorController(self.description_generator_ui)

        # Tab 4: Add New Description
        self.add_new_description_ui = AddNewDescriptionUI()
        self.add_new_description_controller = DescriptionGeneratorController(self.add_new_description_ui)


        # Add tabs to the main window
        self.tabs.addTab(self.standardization_ui, "Set Standard Description")
        self.tabs.addTab(self.sku_ui, "SKU Generator")
        self.tabs.addTab(self.description_generator_ui, "SKU Generator Free Form")
        self.tabs.addTab(self.add_new_description_ui, "Manage Descriptions")


        self.tabs.currentChanged.connect(lambda: self.updateTab(self.tabs.currentWidget()))


        # Layout for the whole window
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

    def updateTab(self, tab):
        tab.update()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
