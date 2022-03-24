import mysql.connector


class DatabaseContext:
    def __init__(self, got_database='', got_user='root', got_password='', got_host='localhost'):
        self.connection = mysql.connector.connect(user=got_user, password=got_password,
                                                  host=got_host, database=got_database)
        self.cursor = self.connection.cursor()

    def database_close(self):
        self.cursor.close()
        self.connection.close()

    def database_commit(self):
        self.connection.commit()

    def database_execute(self, got_operation, got_params=(), got_multi=False):
        self.cursor.execute(got_operation, got_params, got_multi)

    def database_fetchall(self):
        return self.cursor.fetchall()

    def database_fetchone(self):
        return self.cursor.fetchone()

    def lock_table(self, got_table_name, got_is_write=False):
        sql_command = f"LOCK TABLES {got_table_name} {'WRITE' if got_is_write else 'READ'};"
        self.database_execute(sql_command)

    def unlock_table(self):
        sql_command = "UNLOCK TABLES;"
        self.database_execute(sql_command)

    def __enter__(self, got_database='', got_user='root', got_password='', got_host='localhost'):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.database_close()
