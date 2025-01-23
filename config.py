import configparser, os

class ConfigParser():
    def __init__(self) -> None:
        # Create the config file if it doesn't exist,
        # and populate it with default values if necessary.
        self.config = configparser.ConfigParser()
       
        # Add 'emails' section to config file if it doesn't exist.
        if not os.path.exists('config.ini'):

            self.config.add_section('emails')
            self.config.set('emails','afs_email','')
            self.config.set('emails','recipient_email','recipientEmail@gmail.com')
            self.config.set('emails','recipient_name','recipientName')
            self.config.set('emails','email_subject','test email subject')

            self.config.add_section('smtp')
            self.config.set('smtp','smtp_server','smtp.gmail.com')
            self.config.set('smtp','smtp_port','587')
            self.config.set('smtp','smtp_password','password')
            self.config.set('smtp','smtp_sender_email','senderEmail@gmail.com')

            self.config.add_section('settings')
            self.config.set('settings','invitation_type','Service Review')
            self.config.set('settings','send_afs_direct','off')
            self.config.set('settings','locale_checkbox','off')
            self.config.set('settings','locale','en-US')
            self.config.set('settings','template_checkbox','off')
            self.config.set('settings','template','English - Service reviews')
            self.config.set('settings','sku','1234,12345')
            self.config.set('settings','sku_checkbox','off')
            self.config.set('settings','location_id_checkbox','off')
            self.config.set('settings','location_id','12345')
            self.config.set('settings','tags','testTag,testtag2')
            self.config.set('settings','preffered_sendtime_checkbox','off')
            self.config.set('settings','preffered_send_time','0')
            self.config.set('settings','product_review_invitation_preffered_sendtime_checkbox','off')
            self.config.set('settings','product_review_invitation_preffered_sendtime','0')
            self.config.set('settings','reference_id','1234')
           
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        
        self.config.read('config.ini')
    
    def _get_config(self) -> dict:
        return {s:dict(self.config.items(s)) for s in self.config.sections()}
    
    def set_config(self,**kwargs) -> None:
        
        for s, v in kwargs.items():
            for key, value in v.items():
                self.config.set(s, key, value)
                # print(f"section: {s} key: {key} value: {value}")

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)



