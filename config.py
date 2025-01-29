import configparser, os

class ConfigParser():
    def __init__(self) -> None:
        # Create the config file if it doesn't exist,
        # and populate it with default values if necessary.
        self.config = configparser.ConfigParser()
       
        # Add 'emails' section to config file if it doesn't exist.
        if not os.path.exists('config.ini'):

            self.config.add_section('emails')
            self.config.set('emails','afs_email','domain@trustpilot.com')
            self.config.set('emails','email_subject','test email subject')
            self.config.set('emails','bcc_email','anotherEmail@gmail.com')
            self.config.set('emails','invitation_type','service review')

            self.config.add_section('smtp')
            self.config.set('smtp','smtp_server','smtp.gmail.com')
            self.config.set('smtp','smtp_port','587')
            self.config.set('smtp','smtp_password','password')
            self.config.set('smtp','smtp_sender_email','senderEmail@gmail.com')

            self.config.add_section('settings')
            self.config.set('settings','recipient_email_checkbox','on')
            self.config.set('settings','recipient_email_entry','recipientEmail@gmail.com')
            self.config.set('settings','reference_id_checkbox','on')
            self.config.set('settings','reference_id_entry','1234')
            self.config.set('settings','recipient_name_checkbox','on')
            self.config.set('settings','recipient_name_entry','recipientName')
          
            self.config.set('settings','locale_checkbox','off')
            self.config.set('settings','locale_entry','en-US')
            # self.config.set('settings','template_checkbox','off')
            # self.config.set('settings','template','English - Service reviews')
            # self.config.set('settings','sku','1234,12345')
            # self.config.set('settings','sku_checkbox','off')
            # self.config.set('settings','location_id_checkbox','off')
            # self.config.set('settings','location_id','12345')
            # self.config.set('settings','tags','testTag,testtag2')
            # self.config.set('settings','preffered_sendtime_checkbox','off')
            # self.config.set('settings','preffered_send_time','0')
            # self.config.set('settings','product_review_invitation_preffered_sendtime_checkbox','off')
            # self.config.set('settings','product_review_invitation_preffered_sendtime','0')
            
           
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        
        self.config.read('config.ini')
    
    def _get_config(self) -> dict:
        return {s:dict(self.config.items(s)) for s in self.config.sections()}
    
    def set_config(self,**kwargs) -> None:
        
        for s, v in kwargs.items():
            for key, value in v.items():
                self.config.set(s, key, value)

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)



