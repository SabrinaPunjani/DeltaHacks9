# import sys

# from PyQt6.QtCore import QSize, Qt
# from PyQt6.QtWidgets import QApplication, QSlider, QWidget, QPushButton, QMainWindow, QCheckBox

# #customize main window
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("StudyCam") #name of app
#         self.setFixedSize(QSize(800,600)) #size of window
#         widget = QSlider()
#         widget.setMinimum(0)
#         widget.setMaximum(5)
#         widget.setSingleStep(1)
#         widget.valueChanged.connect(self.value_changed)
#         widget.sliderMoved.connect(self.slider_position)
#         widget.sliderPressed.connect(self.slider_pressed)
#         widget.sliderReleased.connect(self.slider_released)

#         self.setCentralWidget(widget)
        

        
        
#     def startButton(self):
#         button = QPushButton("Start") #button title
#         button.setCheckable(True)
#         button.clicked.connect(self.isClicked)

#     def isClicked(self):
#         button = QPushButton("Stop")
    
#     def isToggled(self, checked):
#         self.isClicked == checked
# '''        
# class endOfSession(QMainWindow):
#     def __init__(self):
#         super(MainWindow).__init__()
#         self.setWindowTitle("End of Study Session")
#         widget = QCheckBox()
#         widget.setCheckState(Qt.CheckState.Checked)
#         widget.stateChanged.connect(self.show_state)
#         self.setCentralWidget(widget)
    
#     def show_state(self, results):
#         print(results == Qt.CheckState.Checked)
#         print(results)
# '''
# app = QApplication(sys.argv)
# window = MainWindow(app)
# window.show()
# app.exec() #start loop

import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
#from layout_colorwidget import Color


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("My App")
        layout = QVBoxLayout()

        layout.addWidget((Color('green')))
        button = QPushButton("Press Me!")

        self.setFixedSize(QSize(400, 300))


        # Set the central widget of the Window.
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()