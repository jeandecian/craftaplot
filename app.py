from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
import matplotlib.pyplot as plt
import sys


class CraftAPlotApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CraftAPlot")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QHBoxLayout(self.central_widget)

        self.init_settings_panel()
        self.init_plot_panel()

    def init_settings_panel(self):
        self.settings_layout = QVBoxLayout()

        self.init_file_loading_layout()

        self.layout.addLayout(self.settings_layout)

    def init_file_loading_layout(self):
        self.file_loading_layout = QHBoxLayout()

        self.file_loading_layout.addWidget(QLabel("File:"))

        self.file_path_label = QLabel("No file selected")
        self.file_loading_layout.addWidget(self.file_path_label)

        self.file_loading_button = QPushButton("Load file")
        self.file_loading_button.clicked.connect(self.load_file)
        self.file_loading_layout.addWidget(self.file_loading_button)

        self.settings_layout.addLayout(self.file_loading_layout)

    def init_plot_panel(self):
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasQTAgg(self.figure)

        self.layout.addWidget(self.canvas)

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Load CSV File",
            "",
            "CSV Files (*.csv);;All Files (*)",
            options=QFileDialog.Options(),
        )

        if file_name:
            self.file_path_label.setText(file_name)


def main():
    app = QApplication(sys.argv)

    window = CraftAPlotApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
