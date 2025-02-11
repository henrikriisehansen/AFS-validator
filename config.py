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
            self.config.set('settings','sender_email_checkbox','off')
            self.config.set('settings','sender_email_entry','senderEmail@domain.com')
            self.config.set('settings','sender_name_checkbox','off')
            self.config.set('settings','sender_name_entry','senderName')
            self.config.set('settings','reply_to_email_checkbox','off')
            self.config.set('settings','reply_to_email_entry','replyToEmail@gmail.com')
            self.config.set('settings','location_id_checkbox','off')
            self.config.set('settings','location_id_entry','12345')
            self.config.set('settings','tags_checkbox','testTag,testtag2')
            self.config.set('settings','tags_entry','1234,1234')
            self.config.set('settings','preffered_send_time_checkbox','off')
            self.config.set('settings','preffered_send_time_entry','0')
            self.config.set('settings','product_review_invitation_preffered_sendtime_checkbox','off')
            self.config.set('settings','product_review_invitation_preffered_sendtime_entry','0')

            self.config.set('settings','sku_checkbox','off')
            self.config.set('settings','sku_entry','1234,12345')

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
            self.config.set('payloadKeyMapping','sender_email_checkbox','senderEmail')
            self.config.set('payloadKeyMapping','sender_name_checkbox','senderName')
            self.config.set('payloadKeyMapping','reply_to_email_checkbox','replyTo')
            self.config.set('payloadKeyMapping','preffered_send_time_checkbox','preferredSendTime')
            self.config.set('payloadKeyMapping','product_review_invitation_preffered_sendtime_checkbox','productReviewInvitationPreferredSendTime')
 
            self.config.add_section('templates')
            self.config.set("templates", "English - Service reviews", "529c0abfefb96008b894ad02")
            self.config.set("templates", "English - Optimized for product reviews", "5c17c7ebb565bb0001046fbd")
            self.config.set("templates", "Danish - Service reviews", "5278a72d0da2b11ee0f0088c")
            self.config.set("templates", "Danish - Optimized for product reviews", "5c505b600e0d37000127c6ff")
            self.config.set("templates", "Dutch - Service reviews", "529c0b84748a510aa8cb03e3")
            self.config.set("templates", "Dutch - Optimized for product reviews", "5c5b121464c50a0001c5a55a")
            self.config.set("templates", "Finnish - Service reviews", "529c0bd4dec7e10ed0ba75ce")
            self.config.set("templates", "Finnish - Optimized for product reviews", "5c5b1351048417000135ad6f")
            self.config.set("templates", "French - Service reviews", "529c0bd6748a510aa8cb03e4")
            self.config.set("templates", "French - Optimized for product reviews", "5c5b1311f366710001540aaa")
            self.config.set("templates", "German - Service reviews", "5278a79c0da2b11ee0f0088e")
            self.config.set("templates", "German - Optimized for product reviews", "5c50357526f61800019768ca")
            self.config.set("templates", "Italian - Service reviews", "5278a7700da2b11ee0f0088d")
            self.config.set("templates", "Italian - Optimized for product reviews", "5c5b12ce3501e50001628e88")
            self.config.set("templates", "Japanese - Service reviews", "5469e6b009dd3a0b08a6f341")
            self.config.set("templates", "Japanese - Optimized for product reviews", "5c5b1292d098210001a66f32")
            self.config.set("templates", "Norwegian - Service reviews", "529c0b06dec7e10ed0ba75cb")
            self.config.set("templates", "Norwegian - Optimized for product reviews", "5c5b11ba47ad0f0001f388da")
            self.config.set("templates", "Polish - Service reviews", "5385f1ad748a510cf820e3e4")
            self.config.set("templates", "Polish - Optimized for product reviews", "5c5b10dd47942a0001639034")
            self.config.set("templates", "Portuguese - Service reviews", "5630afb41088c2088c06c462")
            self.config.set("templates", "Portuguese - Optimized for product reviews", "5c5b0fd73b442a000141e542")
            self.config.set("templates", "Portuguese (Brazil) - Service reviews", "5489736809dd3a0688d5cba6")
            self.config.set("templates", "Portuguese (Brazil) - Optimized for product reviews", "5c5b143d6cdcf00001a8f174")
            self.config.set("templates", "Spanish - Service reviews", "529469ffefb9600ddce7a2d7")
            self.config.set("templates", "Spanish - Optimized for product reviews", "5c5b13c49d4c8600019d8de3")
            self.config.set("templates", "Swedish - Service reviews", "529c0b40dec7e10ed0ba75cc")
            self.config.set("templates", "Swedish - Optimized for product reviews", "5c5b0e17d036820001e42b25")

            self.config.add_section('payload')
            self.config.set('payload','html','')
            
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



