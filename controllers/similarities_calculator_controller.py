from ui.similarities_calculator_ui import SimilaritiesCalculatorUI

class SimilaritiesCalculatorController:
    def __init__(self, ui: SimilaritiesCalculatorUI):
        self.ui = ui
        self.ui.similarity_button.clicked.connect(self.calculate_similarity)

    def calculate_similarity(self):
        str1 = self.ui.input_string_1.text()
        str2 = self.ui.input_string_2.text()
        
        # Simple similarity check (Jaccard Index)
        similarity = self.simple_string_similarity(str1, str2)
        self.ui.similarity_result.setText(f"Similarity: {similarity}%")

    def simple_string_similarity(self, str1, str2):
        # Compare the strings based on common words
        set1 = set(str1.lower().split())
        set2 = set(str2.lower().split())
        intersection = set1.intersection(set2)
        union = set1.union(set2)
        return round(len(intersection) / len(union) * 100, 2)  # Return percentage similarity