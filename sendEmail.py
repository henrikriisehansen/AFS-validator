import smtplib
import ssl
import json
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self):
        pass

    def send_email(self,email_from, email_to, email_bcc, htmlBody):
        smtp_port = 587                 # Standard secure SMTP port
        smtp_server = "smtp.gmail.com"  # Google SMTP Server

        # email_from = "theedge12345678@gmail.com"
        # email_to = "hrh.tp-testing.com+043b8af42f@invite.trustpilot.com"
        # email_bcc = "henrikriisehansen@gmail.com"

        pswd = os.getenv("APP_PASSWORD")

        # Create context
        simple_email_context = ssl.create_default_context()

        # Create message container - the correct MIME type is multipart/alternative.
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Link"
        msg['From'] = email_from
        msg['To'] = email_to
        msg['Bcc'] = email_bcc

        # Add recipient email addresses to the BCC header
          # BCC recipient
        # Create the body of the message (a plain-text and an HTML version).
        # text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"

        items = {
            "recipientName": "hrh",
            "recipientEmail": "hrh+1234@trustpilot.com",
            "referenceId": "1234"
          }

        htmlBody = f"<script type='application/json+trustpilot'>" + json.dumps(items) + "\n" + "</script>"

        print(htmlBody)

        html = f"""\
        <html>
          <head>{htmlBody}</head>
          <body>
            <p>Hi!<br>
              How are you?<br>
              Here is the <a href="http://www.python.org">link</a> you wanted.
            </p>
          </body>
        </html>
        """

        # Record the MIME types of both parts - text/plain and text/html.
        # part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
        # msg.attach(part1)
        msg.attach(part2)


        try:

            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls(context=simple_email_context)
            server.login(email_from, pswd)
            server.sendmail(email_from, [email_to, email_bcc], msg.as_string())


        # If there's an error, print it out
        except Exception as e:
            print(e)

        # Close the port
        finally:
            server.quit()
    
    







