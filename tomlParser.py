import toml,os


class Config:

    def __init__(self):

        self.data = None

        # if not os.path.exists('config.toml'):

        self.data = self.default_config()
        with open('config.toml', 'w') as f:
                toml.dump(self.data, f)

        try:
            with open("config.toml", "r") as f:
                data = toml.load(f)
            
            self.data = data
            # print(self.data)
        except FileNotFoundError:
            print("Error: config.toml not found")
        except toml.decoder.TomlDecodeError as e:
            print(f"Error decoding TOML: {e}")


    def save_config(self, **kwargs):
        pass


    def get_config(self):
        return self.data



    def default_config(self):
         
        data = {"config": {
            "afs_email": "domain@trustpilot.com",
            "email_subject": "test email subject",
            "bcc_email": "anotherEmail@gmail.com",
            "invitation_type": "service review",
            "smtp_server": "smtp.gmail.com",
            "smtp_port": "587",
            "smtp_password": "password",
            "smtp_sender_email": "senderEmail@gmail.com",
            "recipient_email_checkbox": "on",
            "recipient_email_entry": "recipientEmail@gmail.com",
            "reference_id_checkbox": "on",
            "reference_id_entry": "1234",
            "recipient_name_checkbox": "on",
            "recipient_name_entry": "recipientName",
            "locale_combobox_checkbox": "off",
            "locale_combobox_entry": "en-US",
            "template_combobox_checkbox": "off",
            "template_combobox_entry": "English - Service reviews",
            "sender_email_checkbox": "off",
            "sender_email_entry": "senderEmail@domain.com",
            "sender_name_checkbox": "off",
            "sender_name_entry": "senderName",
            "reply_to_email_checkbox": "off",
            "reply_to_email_entry": "replyToEmail@gmail.com",
            "location_id_checkbox": "off",
            "location_id_entry": "12345",
            "tags_checkbox": "testTag,testtag2",
            "tags_entry": "1234,1234",
            "preffered_send_time_checkbox": "off",
            "preffered_send_time_entry": "0",
            "product_review_invitation_preffered_sendtime_checkbox": "off",
            "product_review_invitation_preffered_sendtime_entry": "0",
            "product_url_checkbox": "off",
            "product_url_entry": "https://www.example.com",
            "product_image_url_checkbox": "off",
            "product_image_url_entry": "https://www.example.com/image.jpg",
            "product_name_checkbox": "off",
            "product_name_entry": "Example Product",
            "product_sku_checkbox": "off",
            "product_sku_entry": "1234,12345",
            "product_gtin_checkbox": "off",
            "product_gtin_entry": "",
            "product_mpn_checkbox": "off",
            "product_mpn_entry": "",
            "product_brand_checkbox": "off",
            "product_brand_entry": "Acme",
            "product_category_google_id_checkbox": "off",
            "product_category_google_id_entry": "1253",
            "generate_random_reference_number": "False"
        },
        "locale": {
            "en-US": "www.trustpilot.com",
            "de-AT": "at.trustpilot.com",
            "en-AU": "au.trustpilot.com",
            "pt-BR": "br.trustpilot.com",
            "en-CA": "ca.trustpilot.com",
            "de-CH": "ch.trustpilot.com",
            "de-DE": "de.trustpilot.com",
            "da-DK": "dk.trustpilot.com",
            "es-ES": "es.trustpilot.com",
            "fi-FI": "fi.trustpilot.com",
            "fr-FR": "fr.trustpilot.com",
            "fr-BE": "fr-be.trustpilot.com",
            "en-IE": "ie.trustpilot.com",
            "it-IT": "it.trustpilot.com",
            "ja-JP": "jp.trustpilot.com",
            "nl-NL": "nl.trustpilot.com",
            "nl-BE": "nl-be.trustpilot.com",
            "nb-NO": "no.trustpilot.com",
            "en-NZ": "nz.trustpilot.com",
            "pl-PL": "pl.trustpilot.com",
            "pt-PT": "pt.trustpilot.com",
            "sv-SE": "se.trustpilot.com",
            "en-GB": "uk.trustpilot.com"
        },
        "payloadKeyMapping": {
            "reference_id_checkbox": "referenceId",
            "recipient_email_checkbox": "recipientEmail",
            "recipient_name_checkbox": "recipientName",
            "locale_combobox_checkbox": "locale",
            "location_id_checkbox": "locationId",
            "tags_checkbox": "tags",
            "template_combobox_checkbox": "templateId",
            "sender_email_checkbox": "senderEmail",
            "sender_name_checkbox": "senderName",
            "reply_to_email_checkbox": "replyTo",
            "preffered_send_time_checkbox": "preferredSendTime",
            "product_review_invitation_preffered_sendtime_checkbox": "productReviewInvitationPreferredSendTime"
        },
        "templates": {
            "English - Service reviews": "529c0abfefb96008b894ad02",
            "English - Optimized for product reviews": "5c17c7ebb565bb0001046fbd",
            "Danish - Service reviews": "5278a72d0da2b11ee0f0088c",
            "Danish - Optimized for product reviews": "5c505b600e0d37000127c6ff",
            "Dutch - Service reviews": "529c0b84748a510aa8cb03e3",
            "Dutch - Optimized for product reviews": "5c5b121464c50a0001c5a55a",
            "Finnish - Service reviews": "529c0bd4dec7e10ed0ba75ce",
            "Finnish - Optimized for product reviews": "5c5b1351048417000135ad6f",
            "French - Service reviews": "529c0bd6748a510aa8cb03e4",
            "French - Optimized for product reviews": "5c5b1311f366710001540aaa",
            "German - Service reviews": "5278a79c0da2b11ee0f0088e",
            "German - Optimized for product reviews": "5c50357526f61800019768ca",
            "Italian - Service reviews": "5278a7700da2b11ee0f0088d",
            "Italian - Optimized for product reviews": "5c5b12ce3501e50001628e88",
            "Japanese - Service reviews": "5469e6b009dd3a0b08a6f341",
            "Japanese - Optimized for product reviews": "5c5b1292d098210001a66f32",
            "Norwegian - Service reviews": "529c0b06dec7e10ed0ba75cb",
            "Norwegian - Optimized for product reviews": "5c5b11ba47ad0f0001f388da",
            "Polish - Service reviews": "5385f1ad748a510cf820e3e4",
            "Polish - Optimized for product reviews": "5c5b10dd47942a0001639034",
            "Portuguese - Service reviews": "5630afb41088c2088c06c462",
            "Portuguese - Optimized for product reviews": "5c5b0fd73b442a000141e542",
            "Portuguese (Brazil) - Service reviews": "5489736809dd3a0688d5cba6",
            "Portuguese (Brazil) - Optimized for product reviews": "5c5b143d6cdcf00001a8f174",
            "Spanish - Service reviews": "529469ffefb9600ddce7a2d7",
            "Spanish - Optimized for product reviews": "5c5b13c49d4c8600019d8de3",
            "Swedish - Service reviews": "529c0b40dec7e10ed0ba75cc",
            "Swedish - Optimized for product reviews": "5c5b0e17d036820001e42b25"
        },
        "payload": {
            "html": ""
        },
        "settings": {
            "recipient_email_entry":{"type": "entry","label": "Recipient Email","value":"on","text":"recipientEmail@gmail.com"}

        }
        }

        return data

       

        
  
        
