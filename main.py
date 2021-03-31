#     EdupageClient - Open-source desktop Edupage Client for students
#     Copyright (C) MMXXI Tomáš Lovrant & Adam Vlčko
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import QGridLayout, QSizePolicy, QLineEdit, QMessageBox
from edupage_api import Edupage, BadCredentialsException, LoginDataParsingException, EduStudent
from PyQt5 import QtWidgets, QtCore, QtGui
import sys

class EdupageClient:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.login_formular = QtWidgets.QWidget()
        self.login_layout = QtWidgets.QVBoxLayout()

        #740x532
        self.login_formular.setGeometry(300, 200, 740/2 - 25, 532/2 - 25)
        self.login_formular.setFixedSize(self.login_formular.size())
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

        self.about_button = QtWidgets.QPushButton("About")
        self.about_button.clicked.connect(self.about)


        # Layouty
        self.login_grid = QGridLayout()
        self.domain_box = QtWidgets.QHBoxLayout()
        self.user_box = QtWidgets.QHBoxLayout()
        self.pass_box = QtWidgets.QHBoxLayout()
        self.submit_box = QtWidgets.QHBoxLayout()
        self.about_box = QtWidgets.QHBoxLayout()

        # Maintain main layout
        self.login_layout.addLayout(self.login_grid)
        self.login_layout.addStretch()

        self.login_layout.addLayout(self.domain_box)
        # self.login_layout.addStretch()

        self.login_layout.addLayout(self.user_box)

        self.login_layout.addLayout(self.pass_box)

        self.login_layout.addStretch()
        self.login_layout.addLayout(self.submit_box)

        # self.login_layout.addStretch()
        self.login_layout.addLayout(self.about_box)


        # Add widgets
        self.login_grid.addWidget(self.text, 0, 0)

        self.domain_box.addWidget(self.domain_edit)
        self.domain_box.addWidget(self.domain_label)

        self.user_box.addWidget(self.user_label)
        self.user_box.addWidget(self.user_edit)

        self.pass_box.addWidget(self.pass_label)
        self.pass_box.addWidget(self.pass_edit)

        self.submit_box.addWidget(self.submit_button)

        self.about_box.addWidget(self.about_button)

        self.login_formular.setLayout(self.login_layout)
        self.login_formular.show()
        sys.exit(self.app.exec_())

    def login(self):
        # 1. self.domain_edit 2. self.user_edit 3. self.pass_edit
        domain = self.domain_edit.text()
        user = self.user_edit.text()
        password = self.pass_edit.text()

        try:
            self.edu = Edupage(domain, user, password)
            try:
                self.edu.login()
                self.login_formular.hide()
                eci = EdupageClientIndex(self)
                eci.index_formular.show()

            except BadCredentialsException:
                self.render_err("Bad credentials", "Check login credentials (username/password)!")
            except LoginDataParsingException:
                self.render_err("Login data parsing", "Check internet connection, try again later or contact server "
                                                      "administrators!")
        except UnicodeError:
            return
        except IndexError:
            self.render_err("Indexing error", "Check entered domain, if correct then check internet connection or est!")

    def about(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("EdupageClient Version: 0.1\n\nEdupageClient Copyright (C) MMXXI \nTomáš Lovrant & Adam "
                    "Vlčko\n\nThis program comes "
                    "with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under "
                    "the terms of the GNU General Public License as published by "
                    "the Free Software Foundation, either version 3 of the License, or "
                    "(at your option) any later version.\nSee: https://www.gnu.org/licenses/\n\nClick on Show Details "
                    "... for more information.")
        msg.setDetailedText("THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY APPLICABLE LAW.  EXCEPT "
                            "WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT HOLDERS AND/OR OTHER PARTIES PROVIDE THE "
                            "PROGRAM \"AS IS\" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, "
                            "BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A "
                            "PARTICULAR PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM IS "
                            "WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF ALL NECESSARY "
                            "SERVICING, REPAIR OR CORRECTION.")
        msg.setWindowTitle("About EdupageClient")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setEscapeButton(QMessageBox.Ok)
        msg.exec_()

    def render_err(self, title, description):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(description)
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.Retry)
        msg.setEscapeButton(QMessageBox.Retry)
        msg.exec_()


class EdupageClientIndex:
    def __init__(self, edupageclient):
        #self.edupageclient = edupageclient
        self.index_formular = QtWidgets.QWidget()
        self.index_layout = QtWidgets.QVBoxLayout()
        self.index_formular.setWindowTitle("Edupage Client: Main")
        self.index_formular.setGeometry(300, 200, 345, 245)
        self.index_formular.setFixedSize(self.index_formular.size())
        self.index_formular.setLayout(self.index_layout)

        # sys.exit(self.edupageclient.app.exec_())


EdupageClient()
