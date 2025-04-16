from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel, QMainWindow, QWidget
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
        self.layout.addWidget(QLabel("Settings Panel"))

    def init_plot_panel(self):
        self.layout.addWidget(QLabel("Plot Panel"))


def main():
    app = QApplication(sys.argv)

    window = CraftAPlotApp()
    window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
