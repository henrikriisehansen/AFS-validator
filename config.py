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
            self.config.set('settings','locale_combobox_checkbox','off')
            self.config.set('settings','locale_combobox_entry','en-US')
            self.config.set('settings','template_combobox_checkbox','off')
            self.config.set('settings','template_combobox_entry','English - Service reviews')
            self.config.set('settings','sku_checkbox','off')
            self.config.set('settings','sku_entry','1234,12345')
            self.config.set('settings','location_id_checkbox','off')
            self.config.set('settings','location_id_entry','12345')
            self.config.set('settings','tags_checkbox','testTag,testtag2')
            self.config.set('settings','tags_entry','1234,1234')
            self.config.set('settings','preffered_send_time_checkbox','off')
            self.config.set('settings','preffered_send_time_entry','0')
            self.config.set('settings','product_review_invitation_preffered_sendtime_checkbox','off')
            self.config.set('settings','product_review_invitation_preffered_sendtime_entry','0')

            self.config.add_section('locale')
            self.config.set('locale','en-US','www.trustpilot.com')
            self.config.set('locale','de-AT','at.trustpilot.com')
            self.config.set('locale','en-AU','au.trustpilot.com')
            self.config.set('locale','pt-BR','br.trustpilot.com')
            self.config.set('locale','en-CA','ca.trustpilot.com')
            self.config.set('locale','de-CH','ch.trustpilot.com')
            self.config.set('locale','de-DE','de.trustpilot.com')
            self.config.set('locale','da-DK','dk.trustpilot.com')
            self.config.set('locale','es-ES','es.trustpilot.com')
            self.config.set('locale','fi-FI','fi.trustpilot.com')
            self.config.set('locale','fr-FR','fr.trustpilot.com')
            self.config.set('locale','fr-BE','fr-be.trustpilot.com')
            self.config.set('locale','en-IE','ie.trustpilot.com')
            self.config.set('locale','it-IT','it.trustpilot.com')
            self.config.set('locale','ja-JP','jp.trustpilot.com')
            self.config.set('locale','nl-NL','nl.trustpilot.com')
            self.config.set('locale','nl-BE','nl-be.trustpilot.com')
            self.config.set('locale','nb-NO','no.trustpilot.com')
            self.config.set('locale','en-NZ','nz.trustpilot.com')
            self.config.set('locale','pl-PL','pl.trustpilot.com')
            self.config.set('locale','pt-PT','pt.trustpilot.com')
            self.config.set('locale','sv-SE','se.trustpilot.com')
            self.config.set('locale','en-GB','uk.trustpilot.com')

            self.config.add_section('payloadKeyMapping')
            self.config.set('payloadKeyMapping','reference_id_checkbox','referenceId')
            self.config.set('payloadKeyMapping','recipient_email_checkbox','recipient_email_checkbox')
            self.config.set('payloadKeyMapping','recipient_name_checkbox','recipientName')
            self.config.set('payloadKeyMapping','locale_combobox_checkbox','locale')
            self.config.set('payloadKeyMapping','location_id_checkbox','locationId')
            self.config.set('payloadKeyMapping','tags_checkbox','tags')
            self.config.set('payloadKeyMapping','template_combobox_checkbox','templateId')
            self.config.set('payloadKeyMapping','preffered_send_time_checkbox','preferredSendTime')
            self.config.set('payloadKeyMapping','product_review_invitation_preffered_sendtime_checkbox','productReviewInvitationPreferredSendTime')
            
            
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



