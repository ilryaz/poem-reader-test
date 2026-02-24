import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QListWidget, QListWidgetItem, QStackedWidget, QVBoxLayout,
    QHBoxLayout, QLabel, QComboBox
)

def load_poems_from_file(filename):
    """Load poems from file with proper error handling"""
    poems = {}
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        poem_blocks = content.strip().split("\n\n\n\n\n")
        
        for block in poem_blocks:
            if not block.strip():
                continue
                
            parts = block.split("\n\n\n\n")
            if len(parts) < 2:
                continue
                
            title = parts[0].strip()
            versions = parts[1].split("\n\n\n")
            
            if len(versions) >= 2:
                poems[title] = {
                    'de': versions[0].strip(),
                    'ru': versions[1].strip()
                }
    
    return poems

# Load poems
poems = load_poems_from_file(r"C:\Users\ilrya\Desktop\Python\tests\poem-reader-test\poems.txt")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Poem Reader")
        self.setup_ui()
    
    def setup_ui(self):
        # Central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Main horizontal layout
        main_layout = QHBoxLayout(central_widget)
        
        # Left side - List of poems
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        
        # Add label for poem list
        left_layout.addWidget(QLabel("Poems:"))
        
        # Create list widget for poems
        self.poem_list = QListWidget()
        self.poem_list.setMaximumWidth(200)
        
        # Add poems to list
        for title in poems.keys():
            self.poem_list.addItem(QListWidgetItem(title))
        
        # Connect list selection to page change
        self.poem_list.currentTextChanged.connect(self.on_poem_selected)
        
        left_layout.addWidget(self.poem_list)
        
        # Right side - Poem display
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        
        # Language selector
        language_layout = QHBoxLayout()
        language_layout.addWidget(QLabel("Language:"))
        
        self.languages = QComboBox()
        self.languages.addItems(["Deutsch", "Русский"])
        self.languages.currentTextChanged.connect(self.on_language_changed)
        
        language_layout.addWidget(self.languages)
        language_layout.addStretch()
        
        # Stacked widget for poems
        self.stacked_widget = QStackedWidget()
        
        # Create pages for each poem
        self.pages = {}  # Store pages by title
        for title in poems.keys():
            page = self.create_page(title)
            self.pages[title] = page
            self.stacked_widget.addWidget(page)
        
        # Add widgets to right layout
        right_layout.addLayout(language_layout)
        right_layout.addWidget(self.stacked_widget)
        
        # Add left and right to main layout
        main_layout.addWidget(left_widget)
        main_layout.addWidget(right_widget, 1)  # 1 = stretch factor
    
    def create_page(self, title):
        """Create a page for a poem"""
        page = QWidget()
        layout = QVBoxLayout(page)
        
        # Title label
        label_title = QLabel(title)
        label_title.setStyleSheet("font-size: 18px; font-weight: bold;")
        
        # Content label (will be updated when language changes)
        content_label = QLabel()
        content_label.setStyleSheet("font-size: 14px;")
        content_label.setWordWrap(True)  # Allow text wrapping
        
        # Store content label as attribute of page for later access
        page.content_label = content_label
        page.title = title
        
        # Set initial content (German)
        content_label.setText(poems[title]['de'])
        
        layout.addWidget(label_title)
        layout.addWidget(content_label)
        layout.addStretch()
        
        return page
    
    def on_poem_selected(self, title):
        """Handle poem selection from list"""
        if title and title in self.pages:
            # Find index of the selected poem
            index = list(poems.keys()).index(title)
            self.stacked_widget.setCurrentIndex(index)
    
    def on_language_changed(self, language):
        """Handle language change"""
        # Get current page
        current_page = self.stacked_widget.currentWidget()
        if current_page and hasattr(current_page, 'title'):
            title = current_page.title
            
            # Update content based on language
            if language == "Deutsch":
                current_page.content_label.setText(poems[title]['de'])
            elif language == "Русский":
                current_page.content_label.setText(poems[title]['ru'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 400)
    window.show()
    sys.exit(app.exec())