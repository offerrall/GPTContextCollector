import os
from PySide6.QtWidgets import QFileDialog, QMessageBox

def file_dialog(mode, last_file_path_cache):
    last_file_path = ""
    if os.path.isfile(last_file_path_cache):
        with open(last_file_path_cache, "r") as file:
            last_file_path = file.read()

    file_dialog = QFileDialog()
    file_dialog.setDirectory(last_file_path)
    file_dialog.setFileMode(mode)

    if file_dialog.exec_():
        file_paths = file_dialog.selectedFiles()
        with open(last_file_path_cache, "w") as file:
            file.write(os.path.dirname(file_paths[0]))
        return file_paths[0] if mode == QFileDialog.ExistingFile or mode == QFileDialog.AnyFile else file_paths

def msg_box(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()