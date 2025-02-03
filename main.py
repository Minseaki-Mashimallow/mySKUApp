from PyQt6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout
from ui.sku_generator_ui import SKUGeneratorUI
from ui.similarities_calculator_ui import SimilaritiesCalculatorUI
from controllers.sku_generator_controller import SKUGeneratorController
from controllers.similarities_calculator_controller import SimilaritiesCalculatorController

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SKU Generator and Similarities Calculator")
        self.setGeometry(100, 100, 600, 400)

        # Create the tabs
        self.tabs = QTabWidget(self)

        # Tab 1: SKU Generator
        self.sku_ui = SKUGeneratorUI()
        self.sku_controller = SKUGeneratorController(self.sku_ui)

        # Tab 2: Similarities Calculator
        self.similarity_ui = SimilaritiesCalculatorUI()
        self.similarity_controller = SimilaritiesCalculatorController(self.similarity_ui)

        # Add tabs to the main window
        self.tabs.addTab(self.sku_ui, "SKU Generator")
        self.tabs.addTab(self.similarity_ui, "Similarities Calculator")

        # Layout for the whole window
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.tabs)
        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()