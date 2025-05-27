import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self,**kwargs) -> None:
        
        self.data:dict = kwargs.get('config', None)
        self.payload:dict = kwargs.get('payload', None)
        self.settings:dict = kwargs.get('settings', None)


    def send_email(self) -> None:
        
        smtp_port = self.data.get('smtp_port', None)
        smtp_server = self.data.get('smtp_server', None)
        smtp_password = self.data.get('smtp_password', None)
        smtp_sender_email = self.data.get('smtp_sender_email', None)

        email_subject = self.data.get('email_subject', None)
    
        simple_email_context = ssl.create_default_context()

        msg = MIMEMultipart('alternative')
        msg['Subject'] =  email_subject
        msg['From'] = smtp_sender_email
        
        if self.data.get('sendAfsDirect', None) in ['off',None]:
            
            msg['To'] = self.settings['recipientEmail']['value']
            msg['Bcc'] = self.data['afs_email']
            
        else:
            msg['To'] = self.data['afs_email']

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
