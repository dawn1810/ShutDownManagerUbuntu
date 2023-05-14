import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QComboBox, QDesktopWidget, QLineEdit
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Application")
        self.setGeometry(0, 0, 680, 300)
        self.setFixedSize(680, 300)  # Set fixed window size
       

        # Creating a QLabel widget to display text
        quest_txt = QLabel(self)
        quest_txt.setText("What do you want the computer to do?")
        quest_txt.setFont(QFont("Arial", 12))
        quest_txt.setGeometry(120, 50, 500, 50)

        use_txt = QLabel(self)
        use_txt.setText("Closes all apps and turns off the PC.")
        use_txt.setFont(QFont("Arial", 12))
        use_txt.setGeometry(120, 150, 500, 50)

        # Creating a QComboBox widget
        combobox = QComboBox(self)
        combobox.addItem("Power Off")
        combobox.addItem("Restart")
        combobox.addItem("Log Out")
        combobox.addItem("Suspend")
        combobox.setGeometry(120, 100, 500, 30) 
        combobox.currentTextChanged.connect(lambda text: self.update_label_text(use_txt, combobox))
        combobox.currentTextChanged.connect(lambda text: self.update_image(logo, combobox))

        # Creating a QLabel widget to display the image
        logo = QLabel(self)
        pixmap = QPixmap("smiling-face-with-halo.226x256.png")
        scaled_pixmap = pixmap.scaled(50, 50) 
        logo.setPixmap(scaled_pixmap)
        logo.setGeometry(60, 70, scaled_pixmap.width(), scaled_pixmap.height())


        # Creating a button in the center
        ok_btn = QPushButton("Ok", self)
        ok_btn.setGeometry(440, 235, 100, 40)
        ok_btn.clicked.connect(lambda: self.get_combobox_value(combobox))

        # Creating a button in the center
        cancle_btn = QPushButton("Cancle", self)
        cancle_btn.setGeometry(550, 235, 100, 40)
        cancle_btn.clicked.connect(self.close)

        # To get enter event
        self.text_input = QLineEdit(self)
        self.text_input.setGeometry(50, 50, 300, 30)
        self.text_input.setVisible(False)  # Set input box to be invisible

        self.centerWindow()
        
        self.show()
    
    def centerWindow(self):
        window_rect = self.frameGeometry()
        center_point = QDesktopWidget().availableGeometry().center()
        window_rect.moveCenter(center_point)
        self.move(window_rect.topLeft())
    
    def run_shell_script(self, action):
        try:
            subprocess.run(["./actions.sh", action])
        except FileNotFoundError:
            print("The shell script 'actions.sh' was not found.")

    def get_combobox_value(self, combobox):
        selected_value = combobox.currentText()
        if (selected_value == 'Power Off'):
            self.run_shell_script("shutdown")
        elif (selected_value == 'Restart'):
            self.run_shell_script("restart")
        elif (selected_value == 'Log Out'):
            self.run_shell_script("logout")
        elif (selected_value == 'Suspend'):
             self.run_shell_script("suspend")
    
    def update_label_text(self, label, combobox):
        selected_value = combobox.currentText()
        if (selected_value == 'Power Off'):
            label.setText("Closes all apps and turns off the PC.")
        elif (selected_value == 'Restart'):
            label.setText("Closes all apps, turn off the PC, and then turns it on again.")
        elif (selected_value == 'Log Out'):
            label.setText("Closes all apps and signs you out.")
        elif (selected_value == 'Suspend'):
            label.setText("The PC stays on but uses low power. Apps stay open so when the\nPC wakes up, you're instantly back to where you left of")

    def update_image(self, logo, combobox):
        selected_value = combobox.currentText()
         
        if (selected_value == 'Power Off'):
            pixmap = QPixmap('smiling-face-with-halo.226x256.png')
            scaled_pixmap = pixmap.scaled(50, 50)
        elif (selected_value == 'Restart'):
            pixmap = QPixmap('face-with-tongue.254x256.png')
            scaled_pixmap = pixmap.scaled(50, 50)
        elif (selected_value == 'Log Out'):
            pixmap = QPixmap('crying-face.246x256.png')
            scaled_pixmap = pixmap.scaled(50, 50)
        elif (selected_value == 'Suspend'):
            pixmap = QPixmap('shy-face.246x256.png')
            scaled_pixmap = pixmap.scaled(50, 50)
        
        logo.setPixmap(scaled_pixmap)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Perform the desired action when Enter key is pressed
            text = self.text_input.text()
            print(f"Enter key pressed. Input text: {text}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
