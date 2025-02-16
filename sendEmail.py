import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self,**kwargs) -> None:
        
        self.data:dict = kwargs.get('config', None)
        self.payload:dict = kwargs.get('payload', None)

    def send_email(self) -> None:
        
        smtp_port = self.data.get('smtp_port', None)
        smtp_server = self.data.get('smtp_server', None)
        smtp_password = self.data.get('smtp_password', None)
        smtp_sender_email = self.data.get('smtp_sender_email', None)

        email_subject = self.data.get('email_subject', None)
        email_to = self.data.get('email_to', None)
        email_bcc = self.data.get('afs_email', None)
    
        simple_email_context = ssl.create_default_context()

        msg = MIMEMultipart('alternative')
        msg['Subject'] =  email_subject
        msg['From'] = smtp_sender_email
        msg['To'] = email_to
        msg['Bcc'] = email_bcc

        html = MIMEText(self.payload.get('html',None), 'html')
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









