from PyQt5.QtWidgets import QApplication, QDialog, QLineEdit
from GUIs.signup_and_login_gui import Ui_Dialog
from Scripts.repositories.user_repository import UserRepository
from Scripts.utilities import hash_sha512, constants_variables
import re


class SignUpAndLoginWindow(QDialog):
    def __init__(self, parent=None):
        super(SignUpAndLoginWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui_login = False
        self.setup_events()
        self.window_convert_to_login()
        self.user_repository = UserRepository()
        self.key_user = None
        self.user_id = None

    def setup_events(self):
        self.ui.btn_cansle.clicked.connect(self.close)
        self.ui.btn_convert_to_login.clicked.connect(self.window_convert_to_signup_or_login)
        self.ui.btn_signup_and_login.clicked.connect(self.login_or_signup_to_app)

        self.ui.check_box_show_password.clicked.connect(self.show_or_hide_password_text)

    def show_or_hide_password_text(self):
        if self.ui.line_edit_password.echoMode() == QLineEdit.Password:
            self.show_password_text()
        else:
            self.hide_password_text()

    def show_password_text(self):
        self.ui.line_edit_password.setEchoMode(QLineEdit.Normal)
        self.ui.line_edit_confirm_password.setEchoMode(QLineEdit.Normal)

    def hide_password_text(self):
        self.ui.line_edit_password.setEchoMode(QLineEdit.Password)
        self.ui.line_edit_confirm_password.setEchoMode(QLineEdit.Password)

    def clear_content_line_edits(self):
        self.ui.line_edit_user_name.clear()
        self.ui.line_edit_password.clear()
        self.ui.line_edit_confirm_password.clear()

    def window_convert_to_signup_or_login(self):
        self.ui.label_show_error.clear()
        self.clear_content_line_edits()

        if self.ui_login:
            self.window_convert_to_signup()
        else:
            self.window_convert_to_login()

    def window_convert_to_signup(self):
        self.ui.btn_convert_to_login.setText("I have an account")
        self.ui.btn_signup_and_login.setText('Sign Up')
        self.ui.line_edit_confirm_password.show()
        self.ui.label_confirm_password.show()
        self.setWindowTitle('Sign Up')
        self.ui_login = False
        self.clear_content_line_edits()

    def window_convert_to_login(self):
        self.ui.btn_convert_to_login.setText("I don't have an account")
        self.ui.btn_signup_and_login.setText('Login')
        self.ui.line_edit_confirm_password.hide()
        self.ui.label_confirm_password.hide()
        self.setWindowTitle('Login')
        self.ui_login = True
        self.clear_content_line_edits()

    def validation_signup_login_form(self, got_username, got_password, got_confirm_password=None):
        self.ui.label_show_error.clear()

        message_error = None
        if not re.fullmatch(constants_variables.REGULAR_EXPRESSION_OF_USERNAME, got_username) or \
                not re.fullmatch(constants_variables.REGULAR_EXPRESSION_OF_PASSWORD, got_password):
            message_error = 'user name and password should only have "A-Z a-z 0-9 _ @ # ." and length 7-50'
        elif not self.ui_login:
            if got_password != got_confirm_password:
                message_error = 'password and confirm password must be same'
            elif self.user_repository.user_is_exist_by_username(got_username):
                message_error = 'username is wrong'

        if message_error:
            self.ui.label_show_error.setText(message_error)

        return not message_error

    def login_or_signup_to_app(self):
        username = self.ui.line_edit_user_name.text().strip()
        password = self.ui.line_edit_password.text().strip()
        confirm_password = self.ui.line_edit_confirm_password.text().strip()

        if self.validation_signup_login_form(username, password, confirm_password):
            if self.ui_login:
                self.login_to_app(username, password)
            else:
                self.signup_to_app(username, password)

    def login_to_app(self, got_username, got_password):
        if self.user_repository.user_exist_by_username_and_password(got_username, got_password):
            self.user_id = self.user_repository.get_user_id_by_username(got_username)
            self.key_user = hash_sha512.hash_sha512(got_username + hash_sha512.hash_sha512(got_password))
            self.accept()
        self.ui.label_show_error.setText('username or password is wrong')

    def signup_to_app(self, got_username, got_password):
        self.user_repository.user_create(got_username, got_password)
        self.window_convert_to_login()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui_signup_and_login = SignUpAndLoginWindow()

    if ui_signup_and_login.exec_() == QDialog.Accepted:
        from email_message_management import EmailMessageManagementWindow

        ui_main_window_email_message_management = EmailMessageManagementWindow(
            got_key_user=ui_signup_and_login.key_user, got_user_id=ui_signup_and_login.user_id)
        print('user id:', ui_signup_and_login.user_id)
        print('key user:', ui_signup_and_login.key_user)
        ui_main_window_email_message_management.show()
        sys.exit(app.exec_())
