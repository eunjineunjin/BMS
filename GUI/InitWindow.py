import sys, os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from GUI import SecondWindow

class MemoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("메모리 덤프")
        self.explanation1 = QLabel("메모리는 시스템이 활성화되어 있는 동안 시스템 런타임 상태의")
        self.explanation2 = QLabel("중요 정보를 포함하고 있습니다.")
        self.blank = QLabel()
        self.question = QLabel("추후 분석을 위해 메모리를 덤프하시겠습니까?")

        self.yn = None
        self.checkbox1 = QCheckBox("예")
        self.checkbox2 = QCheckBox("아니오")
        self.checkbox1.setChecked(True)
        self.checkbox1.stateChanged.connect(self.checkbox1_state)
        self.checkbox2.stateChanged.connect(self.checkbox2_state)

        self.pushButton = QPushButton("다음")
        self.pushButton.clicked.connect(self.pushButtonClicked)

        layout = QGridLayout()
        layout.addWidget(self.explanation1, 0, 0)
        layout.addWidget(self.explanation2, 1, 0)
        layout.addWidget(self.blank, 2, 0)
        layout.addWidget(self.question, 3, 0)
        layout.addWidget(self.checkbox1, 4, 0)
        layout.addWidget(self.checkbox2, 5, 0)
        layout.addWidget(self.pushButton, 6, 0)
        self.setLayout(layout)

    def checkbox1_state(self):
        if self.checkbox1.isChecked():
            self.checkbox2.setChecked(False)
        else:
            self.checkbox2.setChecked(True)

    def checkbox2_state(self):
        if self.checkbox2.isChecked():
            self.checkbox1.setChecked(False)
        else:
            self.checkbox1.setChecked(True)

    def pushButtonClicked(self):
        if self.checkbox1.isChecked():
            os.system("E:\파이참\MemoryDump\DumpIt.exe")
            self.yn = 1
        else:
            self.yn = 0
        self.close()

form_class = uic.loadUiType("Initial Window.ui")[0]
class InitWindow(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Believe Me Sister")
        self.pushButton.clicked.connect(self.buttonFunction)

        self.window2 = SecondWindow.MainWindow()
        self.window2.hide()

        self.qPixmap = QPixmap()
        self.qPixmap.load("BoB.png")
        self.logo.setPixmap(self.qPixmap)

    def buttonFunction(self) :
        dlg = MemoryDialog()
        dlg.exec_()
        self.window2.show()
        self.hide()

if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = InitWindow()
    myWindow.show()
    app.exec_()