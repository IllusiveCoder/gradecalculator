import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QFormLayout, QPushButton, QLineEdit


class GradeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Grade Calculator')
        self.setGeometry(300, 300, 300, 200)

        # Create a form layout for the widget
        self.layout = QFormLayout()
        self.setLayout(self.layout)

        # Create labels and add them to the layout
        self.label_grades = QLabel('Grades:')
        self.layout.addRow(self.label_grades)

        # Create an input field for grades and add it to the layout
        self.input_grades = QLineEdit()
        self.layout.addRow(self.input_grades)

        # Create labels and add them to the layout
        self.label_weights = QLabel('Weights:')
        self.layout.addRow(self.label_weights)

        # Create an input field for weights and add it to the layout
        self.input_weights = QLineEdit()
        self.layout.addRow(self.input_weights)

        # Create a button and connect it to the calculation function
        self.btn_calculate = QPushButton('Calculate')
        self.btn_calculate.clicked.connect(self.calculate_average)
        self.layout.addRow(self.btn_calculate)

        # Create a label for displaying the result and add it to the layout
        self.label_result = QLabel()
        self.layout.addRow(self.label_result)

        # Apply style properties using CSS
        self.setStyleSheet('''
            QLabel {
                font-size: 14px;
                padding-bottom: 10px;
            }

            QLineEdit {
                font-size: 14px;
                padding: 6px;
                border-radius: 4px;
            }

            QPushButton {
                font-size: 14px;
                padding: 6px 12px;
                border-radius: 4px;
                background-color: #4CAF50;
                color: white;
            }

            QPushButton:hover {
                background-color: #45a049;
            }
        ''')

    def calculate_average(self):
        # Get grades and weights from the input fields
        grades = self.input_grades.text().split(',')
        weights = self.input_weights.text().split(',')

        # Check if the number of grades and weights is the same
        if len(grades) != len(weights):
            self.label_result.setText('Error: Number of grades and weights must be the same')
            return

        try:
            # Convert grades and weights to floats
            grades = [float(grade) for grade in grades]
            weights = [float(weight) for weight in weights]
        except ValueError:
            self.label_result.setText('Error: Invalid grade or weight value')
            return

        # Check if grades are between 0 and 100 and weights are positive
        if not all(0 <= grade <= 100 for grade in grades) or not all(weight > 0 for weight in weights):
            self.label_result.setText('Error: Grades must be between 0 and 100, weights must be positive')
            return

        # Calculate the weighted sum and total weight
        weighted_sum = sum(grade * weight for grade, weight in zip(grades, weights))
        total_weight = sum(weights)

        # Calculate the average
        average = weighted_sum / total_weight

        # Display the average result
        self.label_result.setText(f'Average: {average:.2f}')

        # Clear the input fields
        self.input_grades.clear()
        self.input_weights.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = GradeCalculator()
    calculator.show()
    sys.exit(app.exec_())