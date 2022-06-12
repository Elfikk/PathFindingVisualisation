import sys
from PyQt5.QtWidgets import (QApplication, QLineEdit, QPushButton, QGridLayout,\
    QDialog, QLabel, QGroupBox, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import pyqtSlot

class MainMenu(QDialog):
    def __init__(self, update_method, start_method, reset_method):
        super().__init__()

        self.update_method = update_method
        self.start_method = start_method
        self.reset_method = reset_method

        self.create_labels()
        self.create_entries()
        self.create_headings()
        self.create_buttons()

        main_layout = QGridLayout()
        main_layout.addWidget(self.headings_group, 0, 1)
        main_layout.addWidget(self.label_group, 1, 0)
        main_layout.addWidget(self.entry_group, 1, 1)
        main_layout.addWidget(self.button_group, 2, 1)

        self.setLayout(main_layout)

    def create_labels(self):

        self.label_group = QGroupBox()

        grid_size_label = QLabel("Grid Size:")
        start_label = QLabel("Start Point:")
        target_label = QLabel("Target: ")

        label_layout = QVBoxLayout()
        label_layout.addStretch(1)
        label_layout.addWidget(grid_size_label)
        label_layout.addStretch(1)
        label_layout.addWidget(start_label)
        label_layout.addStretch(1)
        label_layout.addWidget(target_label)
        self.label_group.setLayout(label_layout)

    def create_entries(self):
        
        self.entry_group = QGroupBox()
        entries_layout = QVBoxLayout()

        columns = QLineEdit("50")
        by_label = QLabel("x")
        rows = QLineEdit("50")

        grid_size_layout = QHBoxLayout()
        grid_size_layout.addWidget(columns)
        grid_size_layout.addWidget(by_label)
        grid_size_layout.addWidget(rows)

        start_x_entry = QLineEdit("0")
        start_comma_label = QLabel(",")
        start_y_entry = QLineEdit("0")

        start_layout = QHBoxLayout()
        start_layout.addWidget(start_x_entry)
        start_layout.addWidget(start_comma_label)
        start_layout.addWidget(start_y_entry)

        target_x_entry = QLineEdit("50")
        target_comma_label = QLabel(",")
        target_y_entry = QLineEdit("50")

        target_layout = QHBoxLayout()
        target_layout.addWidget(target_x_entry)
        target_layout.addWidget(target_comma_label)
        target_layout.addWidget(target_y_entry)

        entries_layout.addStretch(1)
        entries_layout.addLayout(grid_size_layout)
        entries_layout.addStretch(1)
        entries_layout.addLayout(start_layout)
        entries_layout.addStretch(1)
        entries_layout.addLayout(target_layout)
        
        self.entry_group.setLayout(entries_layout)

    def create_headings(self):

        self.headings_group = QGroupBox()

        x_column_label = QLabel("x")
        y_column_label = QLabel("y")

        headings_layout = QGridLayout()
        headings_layout.addWidget(x_column_label, 0, 0)
        # headings_layout.addStretch(1)
        headings_layout.addWidget(y_column_label, 0, 2)

        self.headings_group.setLayout(headings_layout)

    def create_buttons(self):

        self.button_group = QGroupBox()

        update_button = QPushButton("Update")
        start_button = QPushButton("Start")
        reset_button = QPushButton("Reset")

        update_button.clicked.connect(self.on_update)
        start_button.clicked.connect(self.on_start)
        reset_button.clicked.connect(self.on_reset)

        buttons_layout = QHBoxLayout()

        buttons_layout.addWidget(update_button)
        buttons_layout.stretch(1)
        buttons_layout.addWidget(start_button)
        buttons_layout.stretch(1)
        buttons_layout.addWidget(reset_button)

        self.button_group.setLayout(buttons_layout)

    @pyqtSlot()
    def on_update(self):
        self.update_method()

    @pyqtSlot()
    def on_start(self):
        self.start_method()

    @pyqtSlot()
    def on_reset(self):
        self.reset_method()

def placeholder():
    pass

if __name__ == "__main__":

    app = QApplication([])
    menu = MainMenu(placeholder, placeholder, placeholder)
    menu.setWindowTitle("Path Finding Visualisation Menu")
    menu.show()
    sys.exit(app.exec())