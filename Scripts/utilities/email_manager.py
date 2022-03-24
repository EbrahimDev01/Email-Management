import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import decode_header
from os.path import basename
import imaplib
import email
import requests
import re
from Scripts.utilities import constants_variables


def send_email(got_username, got_password, got_to_mail, got_subject, got_body, got_attach_files=None,
               got_use_html=False, got_cc='', got_bcc='', got_from_mail=None, got_smtp_ssl_host=None,
               got_smtp_ssl_port=465):
    if got_from_mail is None:
        got_from_mail = got_username
    if got_smtp_ssl_host is None:
        got_smtp_ssl_host = get_smtp_ssl_host(got_username)
        if got_smtp_ssl_host is None:
            raise ValueError('Can not find smtp ssl host')
    if isinstance(got_to_mail, list):
        got_to_mail = ', '.join(got_to_mail)

    message = MIMEMultipart("alternative")
    message.attach(MIMEText(got_body, "html" if got_use_html else 'plain'))

    message['Subject'] = got_subject
    message['From'] = got_from_mail
    message['To'] = got_to_mail
    message['cc'] = got_cc
    message['bcc'] = got_bcc

    for attach_file_url in got_attach_files or []:
        with open(attach_file_url, 'rb') as attachment:  # Open the file as binary mode
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                "Content-Disposition",
                "attachment", filename=basename(attach_file_url)
            )
            message.attach(part)

    with smtplib.SMTP_SSL(got_smtp_ssl_host, got_smtp_ssl_port) as server:
        server.login(got_username, got_password)
        server.sendmail(got_from_mail, got_to_mail, message.as_string())


async def get_receiving_emails(got_username, got_password, got_start_list=-1, got_end_list=-50, got_server=None):
    if got_server is None:
        got_server = get_imap_ssl_host(got_username)
        if got_server is None:
            raise ValueError('Can not find smtp ssl host')

    mail = imaplib.IMAP4_SSL(got_server)
    mail.login(got_username, got_password)
    mail.select('inbox')

    status, data = mail.search(None, 'All')

    mail_ids = []
    for block in data:
        mail_ids += block.split()

    for mail_id in range(-got_start_list, -got_end_list, -1):
        status, data = mail.fetch(mail_ids[mail_id], '(RFC822)')

        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])
                yield abs(mail_id), message


def get_smtp_ssl_host(got_username: str):
    got_username = got_username.lower()
    if '@yahoo.com' in got_username:
        return 'smtp.mail.yahoo.com'
    elif '@gmail.com' in got_username:
        return 'smtp.gmail.com'
    elif '@outlook.com' in got_username:
        return 'smtp-mail.outlook.com'
    elif '@hotmail.com' in got_username:
        return 'smtp.live.com'
    else:
        return None


def get_imap_ssl_host(got_username: str):
    got_username = got_username.lower()
    if '@yahoo.com' in got_username:
        return 'imap.mail.yahoo.com'
    elif '@gmail.com' in got_username:
        return 'imap.gmail.com'
    elif '@hotmail.com' in got_username or '@outlook.com' in got_username:
        return 'imap-mail.outlook.com'
    else:
        return None


def validation_email(got_email_address, got_email_password=None):
    if not re.fullmatch(constants_variables.REGULAR_EXPRESSION_OF_EMAIL_ADDRESS, got_email_address):
        return 'format email is wrong'
    elif not (response := requests.get("https://isitarealemail.com/api/email/validate",
                                       params={'email': got_email_address})).ok or \
            response.json()['status'] != 'valid':
        return 'email is wrong'
    if got_email_password is not None:
        if not re.fullmatch(constants_variables.REGULAR_EXPRESSION_OF_EMAIL_PASSWORD, got_email_password):
            return 'format password is wrong'
        server = None
        try:
            smtp_ssl_host = get_smtp_ssl_host(got_email_address)
            server = smtplib.SMTP_SSL(smtp_ssl_host, 465)
            server.login(got_email_address, got_email_password)
        except OSError as e:
            print(e)
            return 'email or password is wrong'
        finally:
            server.quit()
    return 1


def decoder_text_email(text):
    decode_text = ''
    for text_bytes, text_format in decode_header(text):
        if isinstance(text_bytes, str):
            decode_text += text_bytes
            continue

        if text_format is None:
            text_format = 'utf-8'
        decode_text += text_bytes.decode(text_format)

    return decode_text
