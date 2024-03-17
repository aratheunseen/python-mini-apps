from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit,\
    QPushButton, QComboBox
import sys

class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Average Speed Calculator')
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time = QLineEdit()

        self.options = QComboBox()
        self.options.addItems(['Metric (km)','Imperial (miles)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate)

        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance, 0, 1)
        grid.addWidget(self.options,0,2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate(self):
        distance = float(self.distance.text())
        time = float(self.time.text())

        speed = distance / time

        # Check what user chose in the combo
        if self.options.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            unit = 'km/h'
        if self.options.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'

        # Display the result
        self.output_label.setText(f"Average Speed: {speed} {unit}")

app = QApplication(sys.argv)
average_speed_calculator = AverageSpeedCalculator()
average_speed_calculator.show()
sys.exit(app.exec())