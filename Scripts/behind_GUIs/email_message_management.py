from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5.QtCore import Qt
from GUIs.email_message_management_gui import Ui_MainWindow
from Scripts.behind_GUIs.email_control_panel import EmailControlPanelWindow
from Scripts.behind_GUIs.email_send import EmailSendDialog
from Scripts.repositories.email_repository import EmailRepository
from Scripts.utilities import email_manager
from Scripts.utilities import constants_variables
from datetime import datetime
import asyncio


class EmailMessageManagementWindow(QMainWindow):
    def __init__(self, got_key_user, got_user_id, parent=None):
        super(EmailMessageManagementWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # TODO remove example variable
        self.user_id = got_user_id = 1
        self.key_user = got_key_user = 'b43e0e6609ded886dc1b6d192a8ba2be103b34d6c2122412e1b010a572e44a2e92654f1af92' \
                                       'c4b2bd51765ea612cf798155bf0844ccb7dc7b52958969da0fd6c'
        self.child_window = None
        self.email_repository = EmailRepository(got_key_user, got_user_id)
        self.load_email_addresses_to_current_email()
        self.start_emails_list = 1
        self.end_emails_list = 49
        self.len_emails_list = 600
        self.setup_events()
        asyncio.run(self.load_email_inbox_to_table())

    def setup_events(self):
        self.ui.btn_show_email_control_panel.clicked.connect(self.show_email_control_panel)
        self.ui.btn_send_email.clicked.connect(self.show_send_email)
        self.ui.btn_older_email.clicked.connect(self.older_emails_list, Qt.QueuedConnection)
        self.ui.btn_older_email.clicked.connect(self.newer_emails_list)

    def load_email_addresses_to_current_email(self):
        email_addresses = self.email_repository.get_all_email_by_email_address_user_id()
        for email_address in email_addresses or []:
            self.ui.combo_box_current_email.addItem(email_address[1])
            if email_address[2] or len(self.ui.combo_box_current_email.currentText().strip()) == 0:
                self.ui.combo_box_current_email.setCurrentText(email_address[1])

    async def load_email_inbox_to_table(self):
        email_address = self.ui.combo_box_current_email.currentText().strip()
        email_password = self.email_repository.get_email_by_email_address(email_address)[2]
        table = self.ui.table_widget_email_message_list

        table.clearContents()
        table.setColumnCount(4)
        table.setRowCount(49)
        table.hideColumn(0)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        async for i, email in email_manager.get_receiving_emails(email_address, email_password,
                                                                 self.start_emails_list, self.end_emails_list):
            email_message_sender = email_manager.decoder_text_email(email.get('From'))
            email_message_subject = email_manager.decoder_text_email(email.get('subject'))

            datetime_received = email.get('Received').split(';')[1][:-5].strip()
            email_message_datetime = datetime.strptime(datetime_received, constants_variables.DATETIMEFORMAT) \
                .astimezone().strftime('%c')

            item_id = QTableWidgetItem(str(''))
            item_email_message_sender = QTableWidgetItem(email_message_sender)
            item_email_message_subject = QTableWidgetItem(email_message_subject)
            item_email_message_datetime = QTableWidgetItem(email_message_datetime)

            item_id.setFlags(Qt.ItemIsEnabled)
            item_email_message_sender.setFlags(Qt.ItemIsEnabled)
            item_email_message_subject.setFlags(Qt.ItemIsEnabled)
            item_email_message_datetime.setFlags(Qt.ItemIsEnabled)

            row_email = i - 1
            table.setItem(row_email, 0, item_id)
            table.setItem(row_email, 1, item_email_message_sender)
            table.setItem(row_email, 2, item_email_message_subject)
            table.setItem(row_email, 3, item_email_message_datetime)

    def create_child_window(self, type_child_window):
        if self.child_window is None or not isinstance(self.child_window, type_child_window):
            self.child_window = type_child_window(self.key_user, self.user_id, self)
        self.child_window.exec_()

    def show_email_control_panel(self):
        self.create_child_window(EmailControlPanelWindow)

    def show_send_email(self):
        self.create_child_window(EmailSendDialog)

    def newer_emails_list(self):
        if self.start_emails_list >= 50:
            self.start_emails_list -= 49
            self.end_emaisl_list -= 49
            self.load_email_inbox_to_table()
        else:
            self.ui.btn_newer_email.setEnabled(False)
            self.ui.btn_older_email.setEnabled(True)

    async def older_emails_list(self):
        if self.end_emails_list <= self.len_emails_list:
            self.start_emails_list += 49
            self.end_emails_list += 49
            await asyncio.create_task(self.load_email_inbox_to_table())
        else:
            self.ui.btn_newer_email.setEnabled(True)
            self.ui.btn_older_email.setEnabled(False)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui_main_window = EmailMessageManagementWindow(None, None)
    ui_main_window.show()
    sys.exit(app.exec_())
