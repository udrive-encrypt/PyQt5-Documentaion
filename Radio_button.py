from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout=QGridLayout()
        self.setLayout(layout)

        self.radio_button1=QRadioButton("Radio button 1")
        self.radio_button1.setChecked(True)
        self.radio_button1.toggled.connect(self.radio_button_toggled_func)
        layout.addWidget(self.radio_button1,0,0)

        self.radio_button2=QRadioButton("Radio button 2")
        self.radio_button2.toggled.connect(self.radio_button_toggled_func)
        layout.addWidget(self.radio_button2,2,0)

        self.label=QLabel("Selected: ")
        layout.addWidget(self.label,3,0)

    def radio_button_toggled_func(self):
        selected=[]

        if self.radio_button1.isChecked():
            selected.append(self.radio_button1.text())

        if self.radio_button2.isChecked():
            selected.append(self.radio_button2.text())

        self.label.setText("Selected: %s" %selected)
app=QApplication(sys.argv)
screen=Window()
screen.show()
sys.exit(app.exec())