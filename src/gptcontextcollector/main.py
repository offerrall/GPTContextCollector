"""Main application module."""
from functools import partial
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QTableWidgetItem, QPushButton, QFileDialog)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from .ui.main import Ui_Form
from .utils import msg_box, file_dialog, read_file

# Get package directory for resources
PACKAGE_DIR = Path(__file__).parent
UI_DIR = PACKAGE_DIR / "ui"
CACHE_DIR = Path.home() / ".gptcontextcollector"


class MainApp(QMainWindow, Ui_Form):

    def __init__(self):
        super(MainApp, self).__init__()

        self.central_widget = QWidget()
        self.setupUi(self.central_widget)
        self.setCentralWidget(self.central_widget)
        self.resize(600, 400)
        self.setWindowTitle("GPTContextCollector")

        # Set window icon if exists
        icon_path = UI_DIR / "logo.ico"
        if icon_path.exists():
            self.setWindowIcon(QIcon(str(icon_path)))

        self.setup_table()
        self.setup_signals()

        self.bd_files = []
        
        # Use user's home directory for cache
        CACHE_DIR.mkdir(exist_ok=True)
        self.last_file_path = CACHE_DIR / "last_file_cache.txt"
        self.last_open_path = CACHE_DIR / "last_open_cache.txt"
        self.last_save_path = CACHE_DIR / "last_save_cache.txt"

    def setup_signals(self):
        """Connect UI signals to their handlers."""
        self.bt_add_file.clicked.connect(self.add_file)
        self.bt_copy.clicked.connect(self.copy_to_clipboard)

    def setup_table(self):
        """Configure the files table."""
        self.content_table.setColumnCount(2)
        self.content_table.setColumnWidth(0, 50)
        self.content_table.horizontalHeader().setVisible(False)

    def reset_program(self):
        """Clear all files from the list."""
        self.bd_files = []
        self.update_table()

    def delete_file(self, file):
        """Remove a file from the list."""
        self.bd_files.remove(file)
        self.update_table()

    def update_table(self):
        """Refresh the table display with current files."""
        self.content_table.setRowCount(0)
        
        for row, file in enumerate(self.bd_files):
            item = QTableWidgetItem(file)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            
            self.content_table.insertRow(row)
            self.content_table.setItem(row, 1, item)

            # Create delete button
            delete_btn = QPushButton("")
            icon_path = UI_DIR / "delete.ico"
            if icon_path.exists():
                delete_btn.setIcon(QIcon(str(icon_path)))
            else:
                delete_btn.setText("✕")
            delete_btn.setFlat(True)
            delete_btn.clicked.connect(partial(self.delete_file, file))
            self.content_table.setCellWidget(row, 0, delete_btn)

    def open_file(self):
        """Open a saved file list."""
        file_path = file_dialog(QFileDialog.ExistingFile, self.last_open_path)
        if not file_path:
            return msg_box("No file selected")
        
        self.reset_program()
        try:
            content = Path(file_path).read_text()
            for line in content.split("\n"):
                line = line.strip()
                if line and Path(line).exists() and line not in self.bd_files:
                    self.bd_files.append(line)
        except Exception:
            return msg_box(f"Error reading file '{file_path}'")
        
        self.update_table()
            
    def save_file(self):
        """Save the current file list."""
        if not self.bd_files:
            return msg_box("No files to save")
        
        file_path = file_dialog(QFileDialog.AnyFile, self.last_save_path)
        if not file_path:
            return msg_box("No file selected")

        content = "\n".join(self.bd_files)
        Path(file_path).write_text(content)
        msg_box(f"File saved in '{file_path}'")

    def add_file(self):
        """Add files to the list."""
        files = file_dialog(QFileDialog.ExistingFiles, self.last_file_path)
        if not files:
            return msg_box("No files selected")
        
        for f in files:
            if f not in self.bd_files:
                self.bd_files.append(f)
        
        self.update_table()

    def copy_to_clipboard(self):
        """Copy the formatted context to clipboard."""
        main_str = "Query:\n"
        main_str += self.txt_question.toPlainText()
        main_str += "\n\n"

        for file in self.bd_files:
            try:
                main_str += f"- Start file '{file}'\n"
                main_str += read_file(file)
                main_str += "\n- End File\n"
            except Exception as e:
                return msg_box(f"Error reading file '{file}'\n{e}")
        
        if self.ck_delete_spaces.isChecked():
            main_str = main_str.replace(" ", "")
            main_str = main_str.replace("\n", " ")
            main_str = main_str.replace("\t", " ")
        
        QApplication.clipboard().setText(main_str.strip())
        return msg_box("Copied to clipboard")