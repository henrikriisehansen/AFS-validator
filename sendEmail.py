import smtplib
import ssl
import json
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self):
        pass

    def send_email(self, subject, email_from, email_to, email_bcc, htmlBody):
        smtp_port = 587
        smtp_server = "smtp.gmail.com"
        pswd = os.getenv("APP_PASSWORD")
        simple_email_context = ssl.create_default_context()

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Bcc'] = email_bcc

        html = MIMEText(htmlBody, 'html')
        msg.attach(html)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls(context=simple_email_context)
            server.login(email_from, pswd)
            server.sendmail(email_from, [email_to, email_bcc], msg.as_string())
        except Exception as e:
            print(e)
        finally:
            server.quit()









