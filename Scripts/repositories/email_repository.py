from Scripts.utilities.database_context import DatabaseContext
from Scripts.utilities.constants_variables import DataBaseName
from Scripts.utilities import cryptography_by_user_generated_keys


class EmailRepository:
    def __init__(self, got_key_user, got_user_id):
        self.database_context = DatabaseContext(DataBaseName)
        self.key_user = got_key_user
        self.user_id = got_user_id

    def get_email_address_by_email_id(self, got_email_id):
        sql_command = '''
                        SELECT
                            EmailAddress
                        FROM
                            EMAIL
                        WHERE
                            EmailID=%s And
                            UserID=%s                           
                        '''
        self.database_context.lock_table('email')
        self.database_context.database_execute(sql_command, (got_email_id, self.user_id,))
        email = self.database_context.database_fetchone()
        self.database_context.unlock_table()
        if email:
            return cryptography_by_user_generated_keys.decrypt(email[0], self.key_user)
        return None

    def get_email_by_email_address(self, got_email_address):
        got_email_address = cryptography_by_user_generated_keys.encrypt(got_email_address, self.key_user)
        sql_command = '''
                                SELECT
                                    *
                                FROM
                                    EMAIL
                                WHERE
                                    EmailAddress=%s And
                                    UserID=%s                           
                                '''
        self.database_context.lock_table('email')
        self.database_context.database_execute(sql_command, (got_email_address, self.user_id,))
        email = self.database_context.database_fetchone()
        self.database_context.unlock_table()
        if email:
            return (email[0], cryptography_by_user_generated_keys.decrypt(email[1], self.key_user),
                    cryptography_by_user_generated_keys.decrypt(email[2], self.key_user), email[3])
        return None

    def get_is_exists_email_by_email_address_and_email_id(self, got_email_address, got_email_id=None):
        got_email_address = cryptography_by_user_generated_keys.encrypt(got_email_address, self.key_user)
        params = [got_email_address, self.user_id]
        sql_command = '''
        SELECT
            *
        FROM
            email
        WHERE
            EmailAddress=%s AND
            UserID=%s                            
        '''
        if got_email_id:
            params.append(got_email_id)
            sql_command += 'AND EmailID=%s'

        self.database_context.lock_table('email')
        self.database_context.database_execute(sql_command, params)
        email = self.database_context.database_fetchone()
        self.database_context.unlock_table()
        return bool(email)

    def get_all_email_by_email_address_user_id(self, got_email_address='', got_default_email=None):
        got_email_address = '%' + cryptography_by_user_generated_keys.encrypt(got_email_address, self.key_user) + '%'
        sql_command = '''
                                SELECT
                                    EmailID, EmailAddress, EmailDefault
                                FROM
                                    email
                                WHERE
                                    EmailAddress LIKE %s AND                                    
                                    UserID=%s                         
                                '''

        params = [got_email_address, self.user_id, ]
        if got_default_email is not None:
            sql_command += 'And EmailDefault=%s'
            params.append(got_default_email)

        self.database_context.lock_table('email')
        self.database_context.database_execute(sql_command, params)
        emails = self.database_context.database_fetchall()
        self.database_context.unlock_table()
        if emails:
            for email in emails:
                yield email[0], cryptography_by_user_generated_keys.decrypt(email[1], self.key_user), email[2]
        return None

    def email_add(self, got_email_address: str, got_email_password: str, got_email_default=False):
        email_address = cryptography_by_user_generated_keys.encrypt(got_email_address.lower(), self.key_user)
        email_password = cryptography_by_user_generated_keys.encrypt(got_email_password, self.key_user)
        sql_command = '''
                INSERT 
                    INTO email
                VALUES (NULL, %s, %s, %s, %s);
                '''

        if got_email_default:
            self.email_not_default_all()
        self.database_context.lock_table('email', got_is_write=True)
        self.database_context.database_execute(sql_command, (email_address, email_password,
                                                             got_email_default, self.user_id,))
        self.database_context.database_commit()
        self.database_context.unlock_table()

    def email_edit(self, got_email_id, got_email_address: str, got_email_password: str, got_email_default=False):
        email_address = cryptography_by_user_generated_keys.encrypt(got_email_address.lower(), self.key_user)
        email_password = cryptography_by_user_generated_keys.encrypt(got_email_password, self.key_user)
        sql_command = '''
                UPDATE 
                    email 
                SET 
                    EmailAddress = %s, 
                    EmailPassword = %s, 
                    EmailDefault = %s 
                WHERE 
                    EmailID = %s
                '''

        self.database_context.lock_table('email', got_is_write=True)
        if got_email_default:
            self.email_not_default_all()
        self.database_context.database_execute(sql_command, (email_address, email_password,
                                                             got_email_default, got_email_id,))
        self.database_context.database_commit()
        self.database_context.unlock_table()

    def email_remove(self, got_email_id):
        sql_command = '''
        DELETE FROM 
            email 
        WHERE 
            EmailID=%sAnd
            UserID=%s'''
        self.database_context.lock_table('email', got_is_write=True)
        self.database_context.database_execute(sql_command, (got_email_id, self.user_id))
        self.database_context.database_commit()
        self.database_context.unlock_table()

    def email_not_default_all(self):
        sql_command = '''
        UPDATE 
            email
        SET
            EmailDefault=0
        WHERE
            UserId=%s AND           
            EmailDefault=1;
        '''
        self.database_context.lock_table('email', got_is_write=True)
        self.database_context.database_execute(sql_command, (self.user_id,))
        self.database_context.database_commit()
        self.database_context.unlock_table()

    def set_email_default_by_email_id(self, got_email_id):
        self.email_not_default_all()
        sql_command = '''
        UPDATE 
            email
        SET
            EmailDefault=1
        WHERE
            UserId=%s AND
            EmailID=%s;
        '''
        self.database_context.lock_table('email', got_is_write=True)
        self.database_context.database_execute(sql_command, (self.user_id, got_email_id,))
        self.database_context.database_commit()
        self.database_context.unlock_table()
