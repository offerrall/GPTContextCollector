from pathlib import Path
from PySide6.QtWidgets import QFileDialog, QMessageBox

def file_dialog(mode, last_file_path_cache):
    last_file_path = ""
    cache_path = Path(last_file_path_cache)
    
    if cache_path.is_file():
        last_file_path = cache_path.read_text().strip()

    dialog = QFileDialog()
    if last_file_path:
        dialog.setDirectory(last_file_path)
    dialog.setFileMode(mode)

    if dialog.exec():
        file_paths = dialog.selectedFiles()
        cache_path.parent.mkdir(parents=True, exist_ok=True)
        cache_path.write_text(str(Path(file_paths[0]).parent))
        
        if mode in (QFileDialog.ExistingFile, QFileDialog.AnyFile):
            return file_paths[0]
        return file_paths
    return None

def msg_box(text):
    msg = QMessageBox()
    msg.setText(text)
    msg.exec()

def read_file(file_path):
    return Path(file_path).read_text(encoding="utf-8")