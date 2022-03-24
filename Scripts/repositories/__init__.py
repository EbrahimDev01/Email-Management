from Scripts.utilities.database_context import DatabaseContext
from Scripts.utilities.constants_variables import DataBaseName


def create_databases(got_database_context):
    sql_command = 'CREATE DATABASE IF NOT EXISTS email_management_db;'
    got_database_context.database_execute(sql_command)


def create_table_user(got_database_context):
    sql_command = '''CREATE TABLE IF NOT EXISTS User(
        UserID INT PRIMARY KEY AUTO_INCREMENT,
        UserName VARCHAR(100) NOT NULL,
        Password VARCHAR(128) NOT NULL);'''
    got_database_context.database_execute(sql_command)


def create_table_email(got_database_context):
    sql_command = '''CREATE TABLE IF NOT EXISTS Email(
        EmailID INT PRIMARY KEY AUTO_INCREMENT,
        EmailAddress VARCHAR(3000) NOT NULL,
        EmailPassword VARCHAR(3000) NOT NULL,
        EmailDefault BOOLEAN NOT NULL DEFAULT TRUE,       
        UserID INT,
        FOREIGN KEY (UserID) REFERENCES User(UserID));'''
    got_database_context.database_execute(sql_command)


with DatabaseContext() as database_context:
    create_databases(database_context)
    database_context.connection.connect(database=DataBaseName)

    create_table_user(database_context)
    create_table_email(database_context)
    database_context.database_commit()
