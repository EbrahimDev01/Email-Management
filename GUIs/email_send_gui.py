# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\UIs\Email_Send_UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 490)
        Dialog.setMinimumSize(QtCore.QSize(730, 490))
        Dialog.setMaximumSize(QtCore.QSize(730, 490))
        self.formLayoutWidget = QtWidgets.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 9, 711, 471))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.line_edit_email_to = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_email_to.setObjectName("line_edit_email_to")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.line_edit_email_to)
        self.label1 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label1.setObjectName("label1")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label1)
        self.line2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.line2.setObjectName("line2")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.line2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.line_edit_email_cc = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_email_cc.setObjectName("line_edit_email_cc")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.line_edit_email_cc)
        self.line_edit_email_bcc = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_email_bcc.setObjectName("line_edit_email_bcc")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.line_edit_email_bcc)
        self.line_edit_email_subject = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_email_subject.setObjectName("line_edit_email_subject")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.line_edit_email_subject)
        self.text_Edit_email_body = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.text_Edit_email_body.setObjectName("text_Edit_email_body")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.text_Edit_email_body)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.line_edit_show_attach_files = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_edit_show_attach_files.setReadOnly(True)
        self.line_edit_show_attach_files.setObjectName("line_edit_show_attach_files")
        self.horizontalLayout.addWidget(self.line_edit_show_attach_files)
        self.tool_btn_show_file_dialog = QtWidgets.QToolButton(self.formLayoutWidget)
        self.tool_btn_show_file_dialog.setObjectName("tool_btn_show_file_dialog")
        self.horizontalLayout.addWidget(self.tool_btn_show_file_dialog)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.check_box_use_html = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.check_box_use_html.setObjectName("check_box_use_html")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.check_box_use_html)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(450, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_send_email = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_send_email.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_send_email.setObjectName("btn_send_email")
        self.horizontalLayout_2.addWidget(self.btn_send_email)
        self.btn_cansle = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_cansle.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btn_cansle.setObjectName("btn_cansle")
        self.horizontalLayout_2.addWidget(self.btn_cansle)
        self.formLayout.setLayout(10, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_Edit_my_emails = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line_Edit_my_emails.setReadOnly(True)
        self.line_Edit_my_emails.setObjectName("line_Edit_my_emails")
        self.verticalLayout.addWidget(self.line_Edit_my_emails)
        self.list_widget_my_email = QtWidgets.QListWidget(self.formLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list_widget_my_email.sizePolicy().hasHeightForWidth())
        self.list_widget_my_email.setSizePolicy(sizePolicy)
        self.list_widget_my_email.setMaximumSize(QtCore.QSize(16777215, 40))
        self.list_widget_my_email.setSizeIncrement(QtCore.QSize(0, 0))
        self.list_widget_my_email.setFocusPolicy(QtCore.Qt.NoFocus)
        self.list_widget_my_email.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.list_widget_my_email.setToolTip("")
        self.list_widget_my_email.setStatusTip("")
        self.list_widget_my_email.setWhatsThis("")
        self.list_widget_my_email.setAccessibleName("")
        self.list_widget_my_email.setAccessibleDescription("")
        self.list_widget_my_email.setAutoFillBackground(False)
        self.list_widget_my_email.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.list_widget_my_email.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.list_widget_my_email.setMidLineWidth(8)
        self.list_widget_my_email.setTabKeyNavigation(False)
        self.list_widget_my_email.setDragEnabled(False)
        self.list_widget_my_email.setDragDropOverwriteMode(False)
        self.list_widget_my_email.setAlternatingRowColors(False)
        self.list_widget_my_email.setProperty("isWrapping", False)
        self.list_widget_my_email.setObjectName("list_widget_my_email")
        self.verticalLayout.addWidget(self.list_widget_my_email)
        spacerItem = QtWidgets.QSpacerItem(20, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Email Send"))
        self.label.setText(_translate("Dialog", "To:"))
        self.label1.setText(_translate("Dialog", "Cc:"))
        self.line2.setText(_translate("Dialog", "Bcc:"))
        self.label_3.setText(_translate("Dialog", "Subject:"))
        self.label_4.setText(_translate("Dialog", "Body:"))
        self.label_2.setText(_translate("Dialog", "If you want to send email to several people with , Separate"))
        self.label_5.setText(_translate("Dialog", "Attach Files"))
        self.tool_btn_show_file_dialog.setText(_translate("Dialog", "..."))
        self.check_box_use_html.setText(_translate("Dialog", "Use HTML"))
        self.btn_send_email.setText(_translate("Dialog", "send email"))
        self.btn_cansle.setText(_translate("Dialog", "Cansle"))
        self.label_6.setText(_translate("Dialog", "From:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())