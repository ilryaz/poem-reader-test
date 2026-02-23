import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QHBoxLayout, QLabel, QComboBox)

texts = {
    "Deutsch": """Über allen Gipfeln
Ist Ruh,
In allen Wipfeln
Spürest du
Kaum einen Hauch;
Die Vöglein schweigen im Walde,
Warte nur, balde
Ruhest du auch.

-Goethe""",
    "Русский": """Горные вершины
Спят во тьме ночной;
Тихие долины
Полны свежей мглой;
Не пылит дорога,
Не дрожат листы...
Подожди немного,
Отдохнешь и ты.

-М. Ю. Лермонтов"""
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        self.label = QLabel(texts['Deutsch'])
        font = self.label.font()
        font.setPointSize(16)
        self.label.setFont(font)

        self.languages = QComboBox()
        self.languages.addItems(texts.keys())

        self.languages.currentTextChanged.connect(self.text_changed)

        main_layout.addWidget(self.label)
        main_layout.addWidget(self.languages)

        self.setCentralWidget(central_widget)

    def text_changed(self, text):
        self.label.setText(texts[text])


app = QApplication(sys.argv)
window = MainWindow()
window.resize(400, 400)
window.show()
app.exec()