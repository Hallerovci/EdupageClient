from PyQt5.QtWidgets import QGridLayout, QSizePolicy, QLineEdit
from edupage_api import Edupage, BadCredentialsException
from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class EdupageClient:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.login_formular = QtWidgets.QWidget()
        self.login_layout = QtWidgets.QVBoxLayout()

        #740x532
        self.login_formular.setGeometry(300, 200, 740/2 - 25, 532/2 - 25)
        # self.login_formular.setFixedSize(self.login_formular.size())
        self.login_formular.setWindowTitle("Edupage Client: Login ")

        # Widgety

        self.text = QtWidgets.QLabel("Edupage Client - Login to your account", parent=self.login_formular)
        self.text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.text.setAlignment(QtCore.Qt.AlignCenter)
        self.domain_edit = QtWidgets.QLineEdit()
        self.domain_label = QtWidgets.QLabel(".edupage.org")

        self.user_label = QtWidgets.QLabel("Username: ")
        self.user_edit = QtWidgets.QLineEdit()

        self.pass_label = QtWidgets.QLabel("Password: ")
        self.pass_edit = QtWidgets.QLineEdit()
        self.pass_edit.setEchoMode(QLineEdit.Password)
        self.pass_edit.show()

        self.submit_button = QtWidgets.QPushButton("Login")
        self.submit_button.clicked.connect(self.login)

        # Layouty
        self.login_grid = QGridLayout()
        self.domain_box = QtWidgets.QHBoxLayout()
        self.user_box = QtWidgets.QHBoxLayout()
        self.pass_box = QtWidgets.QHBoxLayout()
        self.submit_box = QtWidgets.QHBoxLayout()

        # Maintain main layout
        self.login_layout.addLayout(self.login_grid)
        self.login_layout.addStretch()

        self.login_layout.addLayout(self.domain_box)
        # self.login_layout.addStretch()

        self.login_layout.addLayout(self.user_box)

        self.login_layout.addLayout(self.pass_box)

        self.login_layout.addStretch()
        self.login_layout.addLayout(self.submit_box)

        # Add widgets
        self.login_grid.addWidget(self.text, 0, 0)

        self.domain_box.addWidget(self.domain_edit)
        self.domain_box.addWidget(self.domain_label)

        self.user_box.addWidget(self.user_label)
        self.user_box.addWidget(self.user_edit)

        self.pass_box.addWidget(self.pass_label)
        self.pass_box.addWidget(self.pass_edit)

        self.submit_box.addWidget(self.submit_button)

        self.login_formular.setLayout(self.login_layout)
        self.login_formular.show()
        sys.exit(self.app.exec_())

    def login(self):
        self.text.setText("TODO: Login spracovat")


EdupageClient()
