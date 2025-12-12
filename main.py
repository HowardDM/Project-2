from PyQt6.QtWidgets import QApplication, QMainWindow
from gui import Ui_Form
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.red_prices = {
            "Scout": 285,
            "Soldier": 150,
            "Pyro": 250,
            "Demoman": 220,
            "Heavy": 150,
            "Engineer": 170,
            "Medic": 300,
            "Sniper": 230,
            "Spy": 135
        }
        self.blu_prices = {
            "Scout": 230,
            "Soldier": 110,
            "Pyro": 200,
            "Demoman": 180,
            "Heavy": 130,
            "Engineer": 150,
            "Medic": 240,
            "Sniper": 200,
            "Spy": 120
        }

        self.ui.comboBox_class.currentIndexChanged.connect(self.update_price)
        self.ui.comboBox_team.currentIndexChanged.connect(self.update_price)
        self.ui.radioButton_new.clicked.connect(self.update_price)
        self.ui.radioButton_used.clicked.connect(self.update_price)
        self.ui.lineEdit_3.textChanged.connect(self.update_price)
        self.ui.spinBox.valueChanged.connect(self.update_price)

        def get_price_for_selection(self):
            class_name = self.ui.comboBox_class.currentText()
            team = self.ui.comboBox_team.currentText()

            if class_name == "None" or team == "None":
                return 0

            if team == "Red":
                base_price = self.red_prices[class_name]
            else:
                base_price = self.blu_prices[class_name]

            if self.ui.radioButton_used.isChecked():
                base_price *= 0.5

            amount = self.ui.spinBox.value()
            base_price *= amount

            return base_price
        self.ui.radioButton_new.setChecked(True)
        self.ui.comboBox_team.setCurrentIndex(0)  # RED default

        self.update_price()

    def get_price_for_selection(self):
        class_name = self.ui.comboBox_class.currentText()
        team = self.ui.comboBox_team.currentText()

        # Choose Price
        if team == "Red":
            base_price = self.red_prices[class_name]
        else:
            base_price = self.blu_prices[class_name]

        # Used
        if self.ui.radioButton_used.isChecked():
            base_price *= 0.5

        amount = self.ui.spinBox.value()
        base_price *= amount

        return base_price

    def update_price(self):
        price = self.get_price_for_selection()

        # Update price box
        self.ui.lineEdit_4.setText(f"Price: ${price:.2f}")

        # Get the current class selected
        class_name = self.ui.comboBox_class.currentText()

        # Check budget
        try:
            budget_value = float(self.ui.lineEdit_3.text().replace("Budget:", "").strip())
        except ValueError:
            self.ui.label_canyouaffordit.setText("Enter a valid budget.")
            return

        # Class-specific responses
        if budget_value >= price:  # Saying Yes
            responses = {
                "Scout": "Scout:'Alright, yeah, that's- naw, that's a pretty good job.'",
                "Soldier": "Soldier:'Everyone of you deserves a medal!'",
                "Pyro": "Pyro *in a muffled voice*:'Fhanks a lah!'",
                "Demoman": "Demoman:'If I wasn' the man I was I'd kiss ye!'",
                "Heavy": "Heavy:'Да, this will work!'",
                "Engineer": "Engineer:'Yippee-kiyah-yippee-i-ki-yo!'",
                "Medic": "Medic:'I am ze Übermensch!'",
                "Sniper": "Sniper:'Good on ya mates!'",
                "Spy": "Spy:'The outcome was never really in doubt.'"
            }
        else:  # Saying No
            responses = {
                "Scout": "Scout:'This sucks on ice.'",
                "Soldier": "Soldier:'You are the sorriest excuses for soldiers I have ever seen!'",
                "Pyro": "Pyro *in a muffled voice*:'Eeuaghafvada...'",
                "Demoman": "Demoman:'[Slurred] 'Ooooh, I've realllly hit rock bottom.'",
                "Heavy": "Heavy:'Daaaagh, too many little men on this team!'",
                "Engineer": "Engineer:'Damnit, damnit, damnit, damnit!'",
                "Medic": "Medic:'My skill is VASTED on zis team!'",
                "Sniper": "Sniper:'Should've saved a bullet for some of you, blokes!'",
                "Spy": "Spy:'Well, this was a disappointment!'"
            }

        self.ui.label_canyouaffordit.setText(responses.get(class_name, "Select a valid class."))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
