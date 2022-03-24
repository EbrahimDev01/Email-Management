from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from PyQt5.QtCore import Qt
from GUIs.email_control_panel_gui import Ui_Dialog
from Scripts.behind_GUIs.email_add_or_edit import EmailAddOrEditDialog
from Scripts.repositories.email_repository import EmailRepository


class EmailControlPanelWindow(QDialog):
    def __init__(self, got_key_user, got_user_id, parent=None):
        super(EmailControlPanelWindow, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.user_id = got_user_id
        self.key_user = got_key_user
        self.child_window = None
        self.ui.setupUi(self)
        self.setup_events()
        self.email_repository = EmailRepository(got_key_user, got_user_id)
        self.refresh_table_email_list()

    def setup_events(self):
        self.ui.btn_add_email.clicked.connect(self.email_add)
        self.ui.btn_remove_email.clicked.connect(self.remove_email_address)
        self.ui.btn_set_default_email.clicked.connect(self.set_default_email)
        self.ui.btn_refresh_email_list.clicked.connect(self.refresh_table_email_list)

    def refresh_table_email_list(self):
        email_address = self.ui.line_edit_search.text().lower().strip()
        email_default = self.ui.combo_box_email_default.currentData()

        self.load_data_to_table_email_list(self.email_repository.get_all_email_by_email_address_user_id(email_address,
                                                                                                        email_default))

    def email_add(self):
        self.create_child_window()

    def create_child_window(self, got_email_id=None):
        if self.child_window is None or self.child_window.email_id != got_email_id:
            self.child_window = EmailAddOrEditDialog(self, got_user_id=self.user_id,
                                                     got_key_user=self.key_user, got_email_id=got_email_id)
        self.child_window.exec_()
        self.refresh_table_email_list()

    def load_data_to_table_email_list(self, data):
        data = tuple(data)
        len_data = len(data)

        self.ui.table_wdget_email_list.setRowCount(len_data)
        if len_data > 0:
            self.ui.table_wdget_email_list.setColumnCount(len(data[0]))

            for i, items in enumerate(data):
                for x, item in enumerate(items):
                    if x == 2:
                        item = 'Email Default' if item else 'Not Default'
                    item = QTableWidgetItem(str(item))
                    item.setFlags(Qt.ItemIsEnabled)
                    self.ui.table_wdget_email_list.setItem(i, x, item)

        self.ui.table_wdget_email_list.setColumnWidth(1, 600)
        self.ui.table_wdget_email_list.setColumnHidden(0, True)
        self.ui.table_wdget_email_list.setHorizontalHeaderLabels(['id', 'Email Address', 'Email Default'])

    def get_current_row_table_email_list(self):
        current_row = self.ui.table_wdget_email_list.currentRow()
        if current_row == -1:
            QMessageBox(QMessageBox.Critical, 'select row', f'You did not select a row.\nPlease select a row').exec_()
        return current_row

    def get_item_table_email_list(self):
        current_row = self.get_current_row_table_email_list()
        if current_row == -1:
            return False, False, False

        columns = (self.ui.table_wdget_email_list.item(current_row, 0).text(),
                   self.ui.table_wdget_email_list.item(current_row, 1).text(),
                   self.ui.table_wdget_email_list.item(current_row, 2).text(),)

        return columns

    def remove_row_table_email_list(self):
        current_row = self.get_current_row_table_email_list()
        if current_row == -1:
            return False
        self.ui.table_wdget_email_list.removeRow(current_row)
        return True

    def remove_email_address(self):
        email_id, email_address, _ = self.get_item_table_email_list()
        if email_id:
            result_message_box = QMessageBox(QMessageBox.Warning, 'Remove Email', f'you want remove {email_address}',
                                             QMessageBox.Yes | QMessageBox.No).exec_()
            if result_message_box == QMessageBox.Yes:
                self.email_repository.email_remove(email_id)
                self.remove_row_table_email_list()
        self.ui.table_wdget_email_list.setCurrentCell(-1, -1)

    def set_default_email(self):
        email_id, email_address, email_default = self.get_item_table_email_list()
        if email_default == 'Email Default':
            QMessageBox(QMessageBox.Warning, 'Email Default',
                        f'{email_address} is Email Default').exec_()
        elif email_id:
            result_message_box = QMessageBox(QMessageBox.Warning, 'Set Email Default',
                                             f'you want Set Email Default {email_address}',
                                             QMessageBox.Yes | QMessageBox.No).exec_()
            if result_message_box == QMessageBox.Yes:
                self.email_repository.set_email_default_by_email_id(email_id)

                for row in range(self.ui.table_wdget_email_list.rowCount()):
                    if self.ui.table_wdget_email_list.item(row, 2).text() == 'Email Default':
                        self.ui.table_wdget_email_list.setItem(row, 2, QTableWidgetItem('Not Default'))

                self.ui.table_wdget_email_list.setItem(self.get_current_row_table_email_list(), 2,
                                                       QTableWidgetItem('Email Default'))
        self.ui.table_wdget_email_list.setCurrentCell(-1, -1)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    ui_main_window = EmailControlPanelWindow()
    ui_main_window.show()
    sys.exit(app.exec_())
