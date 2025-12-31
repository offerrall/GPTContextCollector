"""CLI entry point for GPTContextCollector."""
import sys


def main():
    """Main entry point for the CLI."""
    from PySide6.QtWidgets import QApplication
    from .main import MainApp
    
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()