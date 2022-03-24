from PyQt5.QtWidgets import QDialog, QListWidgetItem, QMessageBox, QFileDialog
from GUIs.email_send_gui import Ui_Dialog
from Scripts.repositories.email_repository import EmailRepository
from Scripts.utilities import email_manager
from os.path import basename


class EmailSendDialog(QDialog):
    def __init__(self, got_key_user, got_user_id, parent=None):
        super(EmailSendDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setup_event()
        self.user_id = got_user_id
        self.key_user = got_key_user
        self.email_repository = EmailRepository(got_key_user, got_user_id)
        self.load_user_email()
        self.attach_files = None

    def setup_event(self):
        self.ui.btn_cansle.clicked.connect(self.close)
        self.ui.list_widget_my_email.clicked.connect(self.set_send_email)
        self.ui.btn_send_email.clicked.connect(self.send_email)
        self.ui.tool_btn_show_file_dialog.clicked.connect(self.select_attach_files)

    def load_user_email(self):
        emails_user = self.email_repository.get_all_email_by_email_address_user_id()
        for email_user in emails_user:
            item = QListWidgetItem()
            if email_user[2] or len(self.ui.line_Edit_my_emails.text().strip()) == 0:
                self.ui.line_Edit_my_emails.setText(email_user[1])
                item.setSelected(True)
            item.setText(email_user[1])
            self.ui.list_widget_my_email.addItem(item)

    def set_send_email(self):
        selected_email = self.ui.list_widget_my_email.selectedItems()[0]
        self.ui.line_Edit_my_emails.setText(selected_email.text())

    def send_email(self):
        to_emails_address = self.ui.line_edit_email_to.text().split(',')
        for to_email_address in to_emails_address:
            if (validate_email := email_manager.validation_email(to_email_address)) != 1:
                QMessageBox(QMessageBox.Critical, 'to email', 'to ' + validate_email).exec_()
                return

        from_email_address = self.ui.line_Edit_my_emails.text().strip()
        password = self.email_repository.get_email_by_email_address(from_email_address)[2].strip()
        cc_email = self.ui.line_edit_email_cc.text().strip()
        bcc_email = self.ui.line_edit_email_bcc.text().strip()
        subject_email = self.ui.line_edit_email_subject.text().strip()
        use_html = self.ui.check_box_use_html.isChecked()
        email_body = self.ui.text_Edit_email_body.toMarkdown()

        email_manager.send_email(from_email_address, password, to_emails_address, subject_email, email_body,
                                 self.attach_files, use_html, cc_email, bcc_email)

    def select_attach_files(self):
        file = QFileDialog()
        file.setFileMode(QFileDialog.ExistingFiles)
        self.attach_files = file.getOpenFileNames(options=QFileDialog.DontUseCustomDirectoryIcons)[0]

        self.ui.line_edit_show_attach_files.setText(
            ''.join(f'"{basename(attach_file)}" '
                    for attach_file in self.attach_files))


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)
    dialog = EmailSendDialog()
    dialog.exec_()
