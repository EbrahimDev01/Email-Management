# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\Email_Message_Management_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(920, 610)
        MainWindow.setMinimumSize(QtCore.QSize(920, 610))
        MainWindow.setMaximumSize(QtCore.QSize(920, 610))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 901, 593))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.line_edit_search = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.line_edit_search.setFont(font)
        self.line_edit_search.setObjectName("line_edit_search")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.line_edit_search)
        self.combo_box_current_email = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.combo_box_current_email.setObjectName("combo_box_current_email")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combo_box_current_email)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_widget_email_message_list = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.table_widget_email_message_list.setMinimumSize(QtCore.QSize(0, 460))
        self.table_widget_email_message_list.setMaximumSize(QtCore.QSize(16777215, 460))
        self.table_widget_email_message_list.setObjectName("table_widget_email_message_list")
        self.table_widget_email_message_list.setColumnCount(4)
        self.table_widget_email_message_list.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_email_message_list.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_email_message_list.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_email_message_list.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget_email_message_list.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.table_widget_email_message_list)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_newer_email = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_newer_email.setObjectName("btn_newer_email")
        self.horizontalLayout_2.addWidget(self.btn_newer_email)
        self.label_number_page_email = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_number_page_email.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number_page_email.setObjectName("label_number_page_email")
        self.horizontalLayout_2.addWidget(self.label_number_page_email)
        self.btn_older_email = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_older_email.setObjectName("btn_older_email")
        self.horizontalLayout_2.addWidget(self.btn_older_email)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_send_email = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_send_email.setObjectName("btn_send_email")
        self.horizontalLayout.addWidget(self.btn_send_email)
        self.btn_remove_email = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_remove_email.setObjectName("btn_remove_email")
        self.horizontalLayout.addWidget(self.btn_remove_email)
        self.btn_show_details_email = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_show_details_email.setObjectName("btn_show_details_email")
        self.horizontalLayout.addWidget(self.btn_show_details_email)
        self.btn_refresh_email_list = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_refresh_email_list.setObjectName("btn_refresh_email_list")
        self.horizontalLayout.addWidget(self.btn_refresh_email_list)
        self.btn_show_email_control_panel = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_show_email_control_panel.setObjectName("btn_show_email_control_panel")
        self.horizontalLayout.addWidget(self.btn_show_email_control_panel)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email Message Management"))
        self.label.setText(_translate("MainWindow", "search"))
        self.label_2.setText(_translate("MainWindow", "Current Email"))
        item = self.table_widget_email_message_list.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.table_widget_email_message_list.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sender"))
        item = self.table_widget_email_message_list.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Subject"))
        item = self.table_widget_email_message_list.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date Time"))
        self.btn_newer_email.setText(_translate("MainWindow", "Newer"))
        self.label_number_page_email.setText(_translate("MainWindow", "0-0 of 0"))
        self.btn_older_email.setText(_translate("MainWindow", "Older"))
        self.btn_send_email.setText(_translate("MainWindow", "Send Email Message "))
        self.btn_remove_email.setText(_translate("MainWindow", "Remove Email Message "))
        self.btn_show_details_email.setText(_translate("MainWindow", "Show Details Emai Messagel"))
        self.btn_refresh_email_list.setText(_translate("MainWindow", "Refresh Email Message List"))
        self.btn_show_email_control_panel.setText(_translate("MainWindow", "Email Control Panel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
