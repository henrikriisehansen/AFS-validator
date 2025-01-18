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
            self.config.set('emails','recipientName','recipientName')
            self.config.set('emails','emailSubject','test email subject')

            self.config.add_section('smtp')
            self.config.set('smtp','smtpServer','smtp.gmail.com')
            self.config.set('smtp','smtpPort','587')
            self.config.set('smtp','smtpPassword','password')
            self.config.set('smtp','smtpSenderEmail','senderEmail@gmail.com')

            self.config.add_section('settings')
            self.config.set('settings','invitationType','Service Review')
            self.config.set('settings','sendAfsDirectCheckBox','off')
            self.config.set('settings','localeCheckBox','off')
            self.config.set('settings','locale','en-US')
            self.config.set('settings','templateCheckBox','off')
            self.config.set('settings','template','')
            self.config.set('settings','sku','1234,12345')
            self.config.set('settings','skuCheckBox','off')
            self.config.set('settings','locationIdCheckBox','off')
            self.config.set('settings','locationId','12345')
            self.config.set('settings','tags','testTag,testtag2')
            self.config.set('settings','prefferedSendTimeCheckBox','off')
            self.config.set('settings','prefferedSendTime','08:00')
            self.config.set('settings','productReviewInvitationPrefferedSendTimeCheckBox','off')
            self.config.set('settings','productReviewInvitationPrefferedSendTime','08:00')
           

            with open('config.ini', 'w') as configfile:
                self.config.write(configfile)
        
        self.config.read('config.ini')
       
    def get_config(self):
        return self.config
    
    def set_config(self,interface):
        
        self.config.set('emails','afsEmail',interface.afs_email_Entry.get())
        self.config.set('emails','recipientEmail',interface.reciepent_email_Entry.get())

        self.config.set('smtp','smtpServer',interface.smtp_server_entry.get())
        self.config.set('smtp','smtpPort',interface.smtp_port_entry.get())
        self.config.set('smtp','smtpPassword',interface.smtp_password_entry.get())
        self.config.set('smtp','smtpSenderEmail',interface.sender_email_Entry.get())

        self.config.set('settings','skuCheckBox',interface.sku_checkbox_var.get())
        self.config.set('settings','locationIdCheckBox',interface.location_id_checkbox_var.get())
        self.config.set('settings','tags',interface.tags_entry.get())
        self.config.set('settings','prefferedSendTimeCheckBox',interface.prefferedSendTime_checkbox_var.get())
        self.config.set('settings','productReviewInvitationPrefferedSendTimeCheckBox',interface.productReviewInvitationPrefferedSendTime_checkbox_var.get())

        with open('config.ini', 'w') as configfile:
            self.config.write(configfile)



