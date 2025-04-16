from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
import matplotlib.pyplot as plt
import pandas as pd
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
        self.init_x_axis_selection_layout()
        self.init_y_axis_selection_layout()
        self.init_plot_type_selection_layout()
        self.init_plot_library_selection_layout()

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

    def init_x_axis_selection_layout(self):
        self.x_axis_selection_layout = QHBoxLayout()

        self.x_axis_selection_layout.addWidget(QLabel("X axis:"))

        self.x_axis_combo = QComboBox()
        self.x_axis_selection_layout.addWidget(self.x_axis_combo)

        self.settings_layout.addLayout(self.x_axis_selection_layout)

    def init_y_axis_selection_layout(self):
        self.y_axis_selection_layout = QHBoxLayout()

        self.y_axis_selection_layout.addWidget(QLabel("Y axis:"))

        self.y_axis_combo = QComboBox()
        self.y_axis_selection_layout.addWidget(self.y_axis_combo)

        self.settings_layout.addLayout(self.y_axis_selection_layout)

    def init_plot_type_selection_layout(self):
        self.plot_type_selection_layout = QHBoxLayout()

        self.plot_type_selection_layout.addWidget(QLabel("Plot type:"))

        self.plot_type_combo = QComboBox()
        self.plot_type_combo.addItems(["bar", "plot", "scatter"])
        self.plot_type_selection_layout.addWidget(self.plot_type_combo)

        self.settings_layout.addLayout(self.plot_type_selection_layout)

    def init_plot_library_selection_layout(self):
        self.plot_library_selection_layout = QHBoxLayout()

        self.plot_library_selection_layout.addWidget(QLabel("Plot library:"))

        self.library_combo = QComboBox()
        self.library_combo.addItems(["Matplotlib"])
        self.plot_library_selection_layout.addWidget(self.library_combo)

        self.settings_layout.addLayout(self.plot_library_selection_layout)

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

            self.data = pd.read_csv(file_name)

            self.x_axis_combo.clear()
            self.x_axis_combo.addItems(self.data.columns)

            self.y_axis_combo.clear()
            self.y_axis_combo.addItems(self.data.columns)


def main():
    app = QApplication(sys.argv)

    window = CraftAPlotApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
