import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QHBoxLayout, QLabel, QComboBox)

def load_poems_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        poems = content.strip().split("\n\n\n")
        return poems[0], poems[1]
    
de_poem, ru_poem = load_poems_from_file(r"C:\Users\ilrya\Desktop\Python\tests\poem-reader-test\poems.txt")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        self.label = QLabel(de_poem)
        font = self.label.font()
        font.setPointSize(16)
        self.label.setFont(font)

        self.languages = QComboBox()
        self.languages.addItems(["Deutsch", "Русский"])

        self.languages.currentTextChanged.connect(self.text_changed)

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.languages)

        self.setCentralWidget(central_widget)

    def text_changed(self, text):
        if text == "Deutsch":
            self.label.setText(de_poem)
        elif text == "Русский":
            self.label.setText(ru_poem)


app = QApplication(sys.argv)
window = MainWindow()
window.resize(400, 400)
window.show()
app.exec()