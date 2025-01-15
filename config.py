import configparser, os



class ConfigParser():
    def __init__(self):
        # Create the config file if it doesn't exist,
        # and populate it with default values if necessary.
        self.config = configparser.ConfigParser()
       
        # Add 'emails' section to config file if it doesn't exist.
        if not os.path.exists('config.ini'):

            self.config.add_section('emails')
            self.config.set('emails','afsEmail','domain+1234@invite.trustpilot.com')
            self.config.set('emails','recipientEmail','recipientEmail@gmail.com')

            self.config.add_section('smtp')
            self.config.set('smtp','smtpServer','smtp.gmail.com')
            self.config.set('smtp','smtpPort','587')
            self.config.set('smtp','smtpPassword','password')
            self.config.set('smtp','smtpSenderEmail','senderEmail@gmail.com')
            
            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        
        self.config.read('config.ini')
       
    def get_config(self):
        return self.config
    
    def set_config(self):
        
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
    
    

