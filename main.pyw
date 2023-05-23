from functools import partial
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget,
                               QTableWidgetItem, QPushButton, QFileDialog)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from ui.main import Ui_Form

from code.utils import msg_box, file_dialog, read_file
from os.path import exists
from os import mkdir

class MainApp(QMainWindow, Ui_Form):

    def reset_program(self):
        self.bd_files = []
        self.update_table()

    def delete_file(self, file):
        self.bd_files.remove(file)
        self.update_table()

    def update_table(self):
        self.content_table.setRowCount(0)

        for row, file in enumerate(self.bd_files):

            item = QTableWidgetItem(file)
            item.setFlags(item.flags() & ~Qt.ItemIsEditable)
            
            self.content_table.insertRow(row)
            self.content_table.setItem(row, 1, item)

            delete_btn = QPushButton("")
            delete_btn.setIcon(QIcon("./ui/delete.ico"))
            delete_btn.setFlat(True)
            delete_btn.clicked.connect(partial(self.delete_file, file))
            self.content_table.setCellWidget(row, 0, delete_btn)

    def open_file(self):
        file_path = file_dialog(QFileDialog.ExistingFile, self.last_open_path)
        if not file_path:
            return msg_box("No file selected")
        
        self.reset_program()
        with open(file_path, "r") as file:
            read = file.read()

        try:
            for i in read.split("\n"):
                if i:
                    self.bd_files.append(i)
        except:
            return msg_box(f"Error reading file '{file_path}'")
        
        self.update_table()
            
    def save_file(self):
        if not self.bd_files:
            return msg_box("No files to save")
        
        file_path = file_dialog(QFileDialog.AnyFile, self.last_save_path)
        if not file_path:
            return msg_box("No file selected")

        with open(file_path, "w") as file:
            for f in self.bd_files:
                file.write(f"{f}\n")
        
        msg_box(f"File saved in '{file_path}'")

    def add_file(self):
        file = file_dialog(QFileDialog.ExistingFiles, self.last_file_path)
        if not file:
            return msg_box("No files selected")
        
        for f in file:
            if f not in self.bd_files:
                self.bd_files.append(f)
        
        self.update_table()

    def copy_to_clipboard(self):
        main_str = ""

        for file in self.bd_files:
            try:
                main_str += f"- Start file '{file}'\n"
                main_str += read_file(file)
                main_str += "- End File\n"
            except Exception as e:
                return msg_box(f"Error reading file '{file}'\n{e}")
        
        QApplication.clipboard().setText(main_str)

        return msg_box("Copied to clipboard")
    
    def setup_signals(self):
        self.bt_open.clicked.connect(self.open_file)
        self.bt_save.clicked.connect(self.save_file)
        self.bt_add_file.clicked.connect(self.add_file)
        self.bt_copy.clicked.connect(self.copy_to_clipboard)
        self.bt_new.clicked.connect(self.reset_program)

    def setup_table(self):
        self.content_table.setColumnCount(2)
        self.content_table.setColumnWidth(0, 50)
        self.content_table.horizontalHeader().setVisible(False)

    def __init__(self):
        super(MainApp, self).__init__()

        self.central_widget = QWidget()
        self.setupUi(self.central_widget)
        self.setCentralWidget(self.central_widget)
        self.resize(600, 200)
        self.setWindowTitle("GPTContextCollector")
        self.setWindowIconText("GPTContextCollector")
        self.setWindowIcon(QIcon("./ui/logo.ico"))

        self.setup_table()
        self.setup_signals()

        self.bd_files = []
        self.delete_cache = None

        self.cache_folder = "./cache"
        self.last_file_path = self.cache_folder + "/last_file_cache.txt"
        self.last_open_path = self.cache_folder + "/last_open_cache.txt"
        self.last_save_path = self.cache_folder + "/last_save_cache.txt"

        if not exists(self.cache_folder):
            mkdir(self.cache_folder)

if __name__ == "__main__":
    app = QApplication([])
    window = MainApp()
    window.show()
    app.exec()
