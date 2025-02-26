import customtkinter
from settings_window import settingsWindow
from sendEmail import Email
import json
from config import ConfigParser
from payload import PayloadBuilder, PayloadType
from itertools import chain
from interface_elements.menu import Menu
from interface_elements.email_frame import Email_frame
from interface_elements.settings_frame import Settings_frame
import random
import string

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.configparser: ConfigParser = ConfigParser()
        self.data: dict = self.configparser._get_config()
        self.data_config: dict = self.data["config"]
        self.data_locale: dict = self.data["locale"]
        self.data_payloadKeyMapping = self.data["payloadKeyMapping"]
        self.data_templates: dict = self.data["templates"]
        

        # Frame padding and styling
        self.frame_padx:int = 8
        self.frame_pady:int = 8
        self.frame_corner_radius:int = 10

        self.element_padx:int = 8
        self.element_pady:int = 8

        # Widget elements dictionary
        self.widget_elements:dict[str,object] = {}

        # Initialize email object and set window properties
        self.email:Email = Email()
        self.title("AFS - validator")
        self.geometry("1000x600")
        self.font = customtkinter.CTkFont(family="roboto", size=12, weight="bold")
        self.header_font = customtkinter.CTkFont(family="roboto", size=16, weight="bold")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0), weight=1)

        # menu frame
        self.menu = Menu(self)

        # email frame
        self.email_frame = Email_frame(self)

        # settings frame 
        self.settings_frame = Settings_frame(self)

        self.build_payload()
        self.bind("<KeyRelease>",lambda event:self.event_callback(**{"key":event.keysym}))

    
    def open_settings_callback(self)-> None:
        
        # open settings window if it's not already opened
        if not hasattr(self,"settings_window"):
            self.settings_window:settingsWindow = settingsWindow(self)  # create window if its None or destroyed
            self.settings_window._set(**self.data_config)
            
            self.settings_window.bind("<KeyRelease>",lambda event:self.event_callback(**{"key":event.keysym}))
        else:
            self.settings_window.close_window()


    def close_settings_callback(self):
        
        delattr(self,"settings_window")
        
        
    def event_callback(self,**kwargs):
        
        # Handle state change for checkboxes and dropdowns
        if kwargs.get("state") == "on" and kwargs.get('entry') != None:
            kwargs["entry"].grid() 

        if kwargs.get("state") == "off" and kwargs.get('entry') != None:
            kwargs["entry"].grid_remove()

        if kwargs.get("send email"):
           
            self.send_smtp_email()

            return
        
        # Create the payload and update the data
        self.get_values()
        self.build_payload()
        self.configparser.set_config(**self.data)
        
    def send_smtp_email(self):

        email = Email(**self.data)
        email.send_email()
       
    def build_payload(self):

        # build the payload
        self.payload = PayloadBuilder(self.get_payload_type(),self.data_payloadKeyMapping,self.data_templates,**self.data_config).build()
        self.email_body.delete(0.0, "end")
        self.email_body.insert(0.0, self.generate_html(self.payload))

        # update the data dictionary with the new merged data
        self.data["config"] = self.data_config
        self.data["payload"] = {"html":self.generate_html(self.payload)}

    def get_payload_type(self):

        # map the payload type
        invitation_type:dict = {
            "service review": PayloadType.SERVICE_REVIEW,
            "service & product review(add/update product review)": PayloadType.SERVICE_AND_PRODUCT_REVIEW,
            "service & product review using sku": PayloadType.SERVICE_AND_PRODUCT_REVIEW_SKU
        }

        return invitation_type[str(self.menu.combobox.get()).lower()]

    def get_values(self):
        
        settingsElements:dict = self.checkboxes | self.entryboxes | self.comboboxes | self.combobox_checkboxes | self.template_checkboxes | self.template_combobox
       
        configElementValues:dict = settingsElements| self.widget_elements
        smptElements:dict = {}
        
        if hasattr(self,"settings_window"):
            smptElements:dict = self.settings_window._get()
            
        # configElements:dict = chain(configElementValues.items(),smptElements.items())
        for key,value in chain(configElementValues.items(),smptElements.items()):

            self.data_config[key] = value.get()

    def generate_html(self, payload):
        
        # create an HTML string using the payload data
        sds = json.dumps(payload, indent=1)
        html = f"""<html>\n<head>\n<script type='application/json+trustpilot'>\n{sds}\n</script>\n</head>\n<body>\n<p>Hi!<br>\nHow are you?<br>\n</p>\n</body>\n</html>"""
         
        return html
    
    def generate_random_string(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

    def copy_link_callback(self):
        self.clipboard_clear()
        self.clipboard_append(self.link.get())
        self.update()




