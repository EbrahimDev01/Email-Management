from Scripts.utilities.database_context import DatabaseContext
from Scripts.utilities.constants_variables import DataBaseName
from Scripts.utilities import hash_sha512


class UserRepository:
    def __init__(self):
        self.database_context = DatabaseContext(DataBaseName)

    def user_create(self, got_username: str, got_password: str):
        got_password = hash_sha512.double_hash_sha512(got_password)
        sql_command = '''
                INSERT 
                    INTO user
                VALUES (NULL, %s, %s);
                '''
        self.database_context.lock_table('user', True)
        self.database_context.database_execute(sql_command, (got_username, got_password))
        self.database_context.database_commit()
        self.database_context.unlock_table()

    def user_is_exist_by_username(self, got_username: str):
        return bool(self.get_user_by_username(got_username))

    def get_user_by_username(self, got_username: str):
        sql_command = '''
        SELECT
            * 
        FROM
            user
        WHERE
           UserName = %s ;
                '''
        self.database_context.lock_table('user')
        self.database_context.database_execute(sql_command, (got_username,))
        user = self.database_context.database_fetchone()
        self.database_context.unlock_table()
        return user

    def get_user_id_by_username(self, got_username: str):
        sql_command = '''
        SELECT
            UserID 
        FROM
            user
        WHERE
           UserName = %s ;
                '''
        self.database_context.lock_table('user')
        self.database_context.database_execute(sql_command, (got_username,))
        user_id = self.database_context.database_fetchone()
        self.database_context.unlock_table()
        if user_id is None:
            raise ValueError('Not Found User')
        return user_id[0]

    def user_exist_by_username_and_password(self, got_username: str, got_password: str):
        got_password = hash_sha512.double_hash_sha512(got_password)
        sql_command = '''
        SELECT
            * 
        FROM
            user
        WHERE
           UserName = %s And
           Password = %s;'''
        self.database_context.lock_table('user')
        self.database_context.database_execute(sql_command, (got_username, got_password))
        user_is_exist = bool(self.database_context.database_fetchone())
        self.database_context.unlock_table()
        return user_is_exist
