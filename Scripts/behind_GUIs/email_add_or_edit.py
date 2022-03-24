from PyQt5.QtWidgets import QDialog, QLineEdit, QMessageBox
from GUIs.email_add_or_edit_gui import Ui_Dialog
from Scripts.repositories.email_repository import EmailRepository
from Scripts.utilities.email_manager import validation_email


class EmailAddOrEditDialog(QDialog):
    def __init__(self, got_parent=None, got_user_id=None, got_key_user=None, got_email_id=None):
        super(EmailAddOrEditDialog, self).__init__(got_parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_events()
        self.user_id = got_user_id
        self.key_user = got_key_user
        self.email_id = got_email_id
        if self.email_id:
            self.convert_to_edit_mode()
        self.email_repository = EmailRepository(got_key_user, got_user_id)

    def setup_events(self):
        self.ui.btn_show_hide_password_line_edit.clicked.connect(self.show_hide_password_line_edit)
        self.ui.btn_cansle.clicked.connect(self.close)
        self.ui.btn_save.clicked.connect(self.email_add_or_edit)

    def clear_line_edits(self):
        self.ui.line_edit_email_address.clear()
        self.ui.line_edit_email_password.clear()
        self.ui.line_edit_confirm_email_password.clear()

    def convert_to_edit_mode(self):
        self.setWindowTitle('Email Edit')
        email_address = self.email_repository.get_email_address_by_email_id(self.email_id)
        self.ui.line_edit_email_address.setText(email_address)

    def show_hide_password_line_edit(self):
        if self.ui.line_edit_confirm_email_password.echoMode() == QLineEdit.Password:
            self.show_password_line_edit()
        else:
            self.hide_password_line_edit()

    def hide_password_line_edit(self):
        self.ui.line_edit_confirm_email_password.setEchoMode(QLineEdit.Password)
        self.ui.line_edit_email_password.setEchoMode(QLineEdit.Password)
        self.ui.btn_show_hide_password_line_edit.setText('Show')

    def show_password_line_edit(self):
        self.ui.line_edit_confirm_email_password.setEchoMode(QLineEdit.Normal)
        self.ui.line_edit_email_password.setEchoMode(QLineEdit.Normal)
        self.ui.btn_show_hide_password_line_edit.setText('Hide')

    def validation_email_and_password(self, got_email_address, got_email_password, got_confirm_email_password):
        self.ui.label_show_error.clear()

        error_message = None
        if (validate_email := validation_email(got_email_address, got_email_password)) != 1:
            error_message = validate_email
        elif got_email_password != got_confirm_email_password:
            error_message = 'email password and confirm email password must be same'
        elif self.email_repository.get_is_exists_email_by_email_address_and_email_id(got_email_address, self.email_id):
            error_message = 'email is exists'

        if error_message:
            self.ui.label_show_error.setText(error_message)

        return not error_message

    def email_add_or_edit(self):
        email_address = self.ui.line_edit_email_address.text().strip()
        email_password = self.ui.line_edit_email_password.text().strip()
        confirm_email_password = self.ui.line_edit_confirm_email_password.text().strip()

        result_validation = self.validation_email_and_password(email_address, email_password, confirm_email_password)
        if result_validation:
            email_default = self.ui.check_box_email_default.isChecked()

            if self.email_id:
                self.email_repository.email_edit(self.email_id, email_address, email_password, email_default)
                msg = 'Email edited successfully'
                self.hide()
            else:
                self.email_repository.email_add(email_address, email_password, email_default)
                msg = 'Email added successfully'
            self.clear_line_edits()
            QMessageBox(QMessageBox.Information, '', msg).exec_()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = EmailAddOrEditDialog()
    window.show()
    sys.exit(app.exec_())
