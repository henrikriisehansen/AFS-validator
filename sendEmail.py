import smtplib
import ssl
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self,**kwargs) -> None:
        
        self.data = kwargs
        

    def send_email(self) -> None:
        
        smtp_port = self.data['smtp']['smtp_port']
        smtp_server = self.data['smtp']['smtp_server']
        smtp_password = self.data['smtp']['smtp_password']
        smtp_sender_email = self.data['smtp']['smtp_sender_email']

        email_subject = self.data['emails']['subject']
        email_to = self.data['settings']['recipient_email_entry']
        email_bcc = self.data['emails']['afs_email']
    
        simple_email_context = ssl.create_default_context()

        msg = MIMEMultipart('alternative')
        msg['Subject'] =  email_subject
        msg['From'] = smtp_sender_email
        msg['To'] = email_to
        msg['Bcc'] = email_bcc

        html = MIMEText(self.data['payload']['html'], 'html')
        msg.attach(html)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls(context=simple_email_context)
            server.login(smtp_sender_email, smtp_password)
            server.send_message(msg)
        except Exception as e:
            print(e)
        finally:
            server.quit()









