import configparser

class ConfigParser():
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')

        if 'emails' not in self.config:
            self.config['emails'] = {
                'senderEmail': 'senderEmail@gmail.com',
                'recipientEmail': 'recipientEmail@gmail.com',
                'afsEmail': 'domain+1234@invite.trustpilot.com'
            }

    def get_config(self):
        return {
            'senderEmail': self.config.get('emails', 'senderEmail'),
            'recipientEmail': self.config.get('emails', 'recipientEmail'),
            'afsEmail': self.config.get('emails', 'afsEmail')
        }
    def set_config(self,**kwargs):
        for key, value in kwargs.items():
            self.config['emails'][key] = value
            print(self.config['emails'][key])
        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)
    
    

