import customtkinter
from settings_window import settingsWindow
from sendEmail import Email
import json
from config import ConfigParser
from payload import PayloadBuilder, PayloadType

class App(customtkinter.CTk):
    def __init__(self):
        
        super().__init__()

        # Initialize configuration and locale data
        self.configparser:ConfigParser = ConfigParser()
        self.data:dict = self.configparser._get_config()
        
        self.data_settings:dict = self.data["settings"]
        self.data_smtp:dict = self.data["smtp"]
        self.data_emails:dict = self.data["emails"]
        self.data_locale:dict = self.data["locale"]
        self.data_payloadKeyMapping = self.data["payloadKeyMapping"]
        self.data_templates:dict = self.data["templates"]

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

        # Column 0: Email settings
        self.set_email_frame = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.set_email_frame.grid(row=0, column=0, sticky="news")
        self.set_email_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.set_email_frame.grid_columnconfigure((0), weight=1)

        # Email entry frame
        self.set_email_frame_entry = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.set_email_frame_entry.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.set_email_frame_entry.grid_rowconfigure((0), weight=1)
        self.set_email_frame_entry.grid_columnconfigure((0), weight=1)

        # Inner frame for email entry
        self.email_frame_entry_inner_frame = customtkinter.CTkFrame(master=self.set_email_frame_entry,corner_radius=self.frame_corner_radius)
        self.email_frame_entry_inner_frame.grid(row=0, column=0, sticky="new")
        self.email_frame_entry_inner_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.email_frame_entry_inner_frame.grid_columnconfigure((0), weight=1)

        # AFS email label and entry
        self.afs_email_label = customtkinter.CTkLabel(master=self.email_frame_entry_inner_frame, text="AFS email:", fg_color="transparent", font=self.font)
        self.afs_email_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.afs_email_Entry = customtkinter.CTkEntry(master=self.email_frame_entry_inner_frame, placeholder_text="AFS email")
        self.afs_email_Entry.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.afs_email_Entry.insert(0, self.data['emails']['afs_email'])
        self.widget_elements["afs_email"] = self.afs_email_Entry

        # Invitation type combobox
        self.combobox_label = customtkinter.CTkLabel(master=self.email_frame_entry_inner_frame, text="Select invitation type:", fg_color="transparent", font=self.font)
        self.combobox_label.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.combobox_var = customtkinter.StringVar(value="Service Review")
        self.combobox = customtkinter.CTkComboBox(master=self.email_frame_entry_inner_frame, values=["Service review", "Service & Product review using SKU", "Service & Product Review(add/update Product Review)"],
                                                  command=lambda x :self.event_callback(**{"state":self.combobox.get()}), variable=self.combobox_var)
        self.combobox.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.combobox.set(self.data["emails"]["invitation_type"])
        self.widget_elements["invitation_type"] = self.combobox
        
        

        # Buttons frame
        self.set_email_frame_buttons = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius,fg_color="transparent",bg_color="transparent")
        self.set_email_frame_buttons.grid(row=2, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="sewn")
        self.set_email_frame_buttons.grid_rowconfigure((0), weight=1)
        self.set_email_frame_buttons.grid_columnconfigure((0), weight=1)

        # Inner frame for buttons
        self.email_frame_buttons_inner_frame = customtkinter.CTkFrame(master=self.set_email_frame_buttons,corner_radius=self.frame_corner_radius)
        self.email_frame_buttons_inner_frame.grid(row=0, column=0, sticky="sew")
        self.email_frame_buttons_inner_frame.grid_rowconfigure((0,1), weight=1)
        self.email_frame_buttons_inner_frame.grid_columnconfigure((0), weight=1)

        #Generate and send email buttons
        self.settings = customtkinter.CTkButton(master= self.email_frame_buttons_inner_frame, text="Settings", command=lambda:self.open_settings_callback())
        self.settings.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        self.send_email = customtkinter.CTkButton(master= self.email_frame_buttons_inner_frame, text="Send Email", command=lambda:self.event_callback(**{"send email":True}))
        self.send_email.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        # Column 1: Email content
        self.email_box_frame = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent") 
        self.email_box_frame.grid(row=0, column=1, sticky="nsew")  
        self.email_box_frame.grid_rowconfigure((0, 1), weight=1)
        self.email_box_frame.grid_columnconfigure((0), weight=1)

        # Upper frame for email content
        self.email_box_upper_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.email_box_upper_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.email_box_upper_frame.grid_rowconfigure((0), weight=1)
        self.email_box_upper_frame.grid_columnconfigure((0), weight=1)

        # Inner frame for email content
        self.email_box_inner_upper_frame = customtkinter.CTkFrame(master=self.email_box_upper_frame,corner_radius=self.frame_corner_radius)
        self.email_box_inner_upper_frame.grid(row=0, column=0, sticky="new")
        self.email_box_inner_upper_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.email_box_inner_upper_frame.grid_columnconfigure((0), weight=1)

        # Email subject and recipient entries
        self.subject_label = customtkinter.CTkLabel(master=self.email_box_inner_upper_frame, text="Email Subject:", fg_color="transparent", font=self.font)
        self.subject_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.subject = customtkinter.CTkEntry(master=self.email_box_inner_upper_frame, placeholder_text="Email Subject")
        self.subject.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.subject.insert(0, self.data["emails"]["email_subject"])
        self.widget_elements["subject"] = self.subject

        self.to_email_entry_label = customtkinter.CTkLabel(master=self.email_box_inner_upper_frame, text="To Email:", fg_color="transparent", font=self.font)
        self.to_email_entry_label.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.to_email_entry = customtkinter.CTkEntry(master=self.email_box_inner_upper_frame, placeholder_text="To Email")
        self.to_email_entry.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.to_email_entry.insert(0, self.data['settings']['recipient_email_entry'])
        self.widget_elements["to_email"] = self.to_email_entry

        self.BCC_email_entry_label = customtkinter.CTkLabel(master=self.email_box_inner_upper_frame, text="BCC Email:", fg_color="transparent", font=self.font)
        self.BCC_email_entry_label.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.BCC_email_entry = customtkinter.CTkEntry(master=self.email_box_inner_upper_frame, placeholder_text="BCC Email")
        self.BCC_email_entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.BCC_email_entry.insert(0, self.data['emails']['afs_email'])
        self.widget_elements["bcc_email"] = self.BCC_email_entry

        # Frame for email body
        self.email_body_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.email_body_frame.grid(row=1, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="nsew")
        self.email_body_frame.grid_rowconfigure((0), weight=1)
        self.email_body_frame.grid_columnconfigure((0), weight=1)

        # Email body text box
        self.email_body = customtkinter.CTkTextbox(master=self.email_body_frame)
        self.email_body.grid(row=0, column=0, sticky="ewsn")

        # Column 2: Settings
        self.settings_box = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.settings_box.grid(row=0, column=2, sticky="nsew")
        self.settings_box.grid_rowconfigure((0), weight=1)
        self.settings_box.grid_columnconfigure((0), weight=1)

        # Scrollable frame for settings
        self.settings_box_frame = customtkinter.CTkScrollableFrame(master=self.settings_box,corner_radius=self.frame_corner_radius)
        self.settings_box_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.settings_box_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), weight=1)
        self.settings_box_frame.grid_columnconfigure((0), weight=1)

        # Various settings checkboxes and entries

        self.checkboxes = {}  # Dictionary to store dynamically created checkboxes
        self.entryboxes = {} # Dictionary to store dynamically created entry boxes
        self.combobox_checkboxes = {} # Dictionary to store dynamically created checkboxes
        self.comboboxes = {} # Dictionary to store dynamically created comboboxes
        self.template_checkboxes = {} # Dictionary to store dynamically created template checkboxes
        self.template_combobox = {} # Dictionary to store dynamically created template entries

        for key, value in self.data_settings.items():
        
            if "checkbox" in str(key) and "combobox" not in str(key):  
                checkbox_var = customtkinter.StringVar(value=value)
              
                self.checkboxes[key] = customtkinter.CTkCheckBox(
                    master=self.settings_box_frame, 
                    text = ' '.join(str(key).split('_')[:3]) if key == 'preffered_send_time_checkbox'
                    else ' '.join(str(key).split('_')[:5]) if key == 'product_review_invitation_preffered_sendtime_checkbox'
                    else ' '.join(str(key).split('_')[:2]),   
                    command=lambda k=key: self.event_callback(**{"state": self.checkboxes[k].get(),"entry": self.entryboxes[str(k).replace("checkbox", "entry")]}), 
                    variable=checkbox_var, 
                    onvalue="on", 
                    offvalue="off"
                )
                
                # Grid placement
                self.checkboxes[key].grid(row=list(self.data_settings.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ws")
      
            if "entry" in str(key) and "combobox" not in str(key):
                entry_var = customtkinter.StringVar(value=value)

                # Store entry in a dictionary with key as the name
                self.entryboxes[key] = customtkinter.CTkEntry(
                    master=self.settings_box_frame, 
                    placeholder_text=str(key).replace("_", " "),
                    textvariable=entry_var
                )
                
                # Grid placement
                self.entryboxes[key].grid(row=list(self.data_settings.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ewn")
                # check if entry is visible and update
                self.entryboxes[key].grid() if self.checkboxes[str(key).replace("entry","checkbox")].get() == 'on' else self.entryboxes[key].grid_remove()
            
            if "locale_combobox_checkbox" in str(key):
                checkbox_var = customtkinter.StringVar(value=value)
                
                

                # Store checkbox in a dictionary with key as the name
                self.combobox_checkboxes[key] = customtkinter.CTkCheckBox(
                    master=self.settings_box_frame, 
                    text=str(key).replace("_", " "), 
                    command=lambda k=key: self.event_callback(**{"state": self.combobox_checkboxes[k].get(),"entry":self.comboboxes[str(k).replace("checkbox", "entry")]}), 
                    variable=checkbox_var, 
                    onvalue="on", 
                    offvalue="off"
                )
                
                # Grid placement
                self.combobox_checkboxes[key].grid(row=list(self.data_settings.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ws")


            if "locale_combobox_entry" in str(key):
                combobox_var = customtkinter.StringVar(value=value)

                # Store combobox in a dictionary with key as the name
                self.comboboxes[key] = customtkinter.CTkComboBox(
                    master=self.settings_box_frame, 
                    values=[k for (k,v) in self.data_locale.items() if v is not None], 
                    command=lambda k: self.event_callback(**{"state":None,"entry":None}), 
                    variable=combobox_var
                )
                
                # Grid placement
                self.comboboxes[key].grid(row=list(self.data_settings.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ewn")
                
                # Set initial value
                self.comboboxes[key].set(value)

                # check if combobox is visible and update
                self.comboboxes[key].grid() if self.combobox_checkboxes[str(key).replace("entry","checkbox")].get() == 'on' else self.comboboxes[key].grid_remove()

            if "template_combobox_checkbox" in str(key):
                checkbox_var = customtkinter.StringVar(value=value)
                
                # Store checkbox in a dictionary with key as the name
                self.template_checkboxes[key] = customtkinter.CTkCheckBox(
                    master=self.settings_box_frame,
                    text=str(key).replace("_", " "),
                    command=lambda k=key: self.event_callback(**{"state": self.template_checkboxes[k].get(),"entry":self.template_combobox[str(k).replace("checkbox", "entry")]}),
                    variable=checkbox_var,
                    onvalue="on",
                    offvalue="off"
                )

                # Grid placement
                self.template_checkboxes[key].grid(row=list(self.data_settings.keys()).index(key), column=0,
                                                    padx=self.element_padx, pady=self.element_pady, sticky="ws")
                
            if "template_combobox_entry" in str(key):
                
                combobox_var = customtkinter.StringVar(value=value)
                
                # Store combobox in a dictionary with key as the name
                self.template_combobox[key] = customtkinter.CTkComboBox(
                    master=self.settings_box_frame,
                    values=[x for x in self.data_templates.keys()],
                    command=lambda k: self.event_callback(**{"state":None,"entry":None}),
                    variable= combobox_var
                )

                # Grid placement
                self.template_combobox[key].grid(row=list(self.data_settings.keys()).index(key), column=0,
                                                        padx=self.element_padx, pady=self.element_pady, sticky="ewn")
                # Set initial value
                self.template_combobox[key].set(value)
                # check if combobox is visible and update
                self.template_combobox[key].grid() if self.template_checkboxes[str(key).replace("entry","checkbox")].get() == 'on' else self.template_combobox[key].grid_remove()
        self.build_payload()
        self.bind("<KeyRelease>",lambda event:self.event_callback(**{"key":event.keysym}))

    
    def open_settings_callback(self):
        # open settings window if it's not already opened
        if not hasattr(self,"settings_window"):
            self.settings_window = settingsWindow(self)  # create window if its None or destroyed
            self.settings_window._set(**self.data_smtp)
            
            self.settings_window.bind("<KeyRelease>",lambda event:self.event_callback(**{"key":event.keysym}))
        else:
            self.settings_window.focus()  # if window exists focus it


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
        
        # Create the payload and update the state
        self.get_values()
        self.build_payload()
        self.configparser.set_config(**self.data)
        
    def send_smtp_email(self):

        email = Email(**self.data)
        email.send_email()
       
    def build_payload(self):

        # merge the settings and email and smtp data
        data = self.data_settings | self.data_emails | self.data_smtp

        # build the payload
        self.payload = PayloadBuilder(self.get_payload_type(),self.data_payloadKeyMapping,self.data_templates,**data).build()
        self.email_body.delete(0.0, "end")
        self.email_body.insert(0.0, self.generate_html(self.payload))

        # update the data dictionary with the new merged data
        self.data["settings"] = self.data_settings
        self.data["emails"] = self.data_emails
        self.data["smtp"] = self.data_smtp
        self.data["payload"] = {"html":self.generate_html(self.payload)}

    def get_payload_type(self):

        # map the payload type
        invitation_type:dict = {
            "service review": PayloadType.SERVICE_REVIEW,
            "service & product review(add/update product review)": PayloadType.SERVICE_AND_PRODUCT_REVIEW,
            "service & product review using sku": PayloadType.SERVICE_AND_PRODUCT_REVIEW_SKU
        }

        return invitation_type[str(self.combobox.get()).lower()]

    def get_values(self):
        
        settingsElements:dict = self.checkboxes | self.entryboxes | self.comboboxes | self.combobox_checkboxes | self.template_checkboxes | self.template_combobox
       
        for key,value in settingsElements.items():

            self.data_settings[key] = value.get()

        if hasattr(self,"settings_window"):

            smptElements:dict = self.settings_window._get()

            for key, value in smptElements.items():
                
                self.data_smtp[key] = value

        for key,value in self.widget_elements.items():

            self.data_emails[key] = value.get()

    def generate_html(self, payload):
        
        # create an HTML string using the payload data
        sds = json.dumps(payload, indent=1)
        html = f"""<html>\n<head>\n<script type='application/json+trustpilot'>\n{sds}\n</script>\n</head>\n<body>\n<p>Hi!<br>\nHow are you?<br>\n</p>\n</body>\n</html>"""
         
        return html

    def copy_link_callback(self):
        self.clipboard_clear()
        self.clipboard_append(self.link.get())
        self.update()


