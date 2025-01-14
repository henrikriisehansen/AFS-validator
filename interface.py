import customtkinter
from pprint import pformat
from tkinter import messagebox
from sendEmail import Email
import json
from config.config import ConfigParser
from payload import PayloadBuilder, PayloadType

class App(customtkinter.CTk):
    def __init__(self):
        
        super().__init__()

        ################################################################

        self.configparser:ConfigParser = ConfigParser()
        self.config = self.configparser.get_config()

        self.frame_padx:int = 8
        self.frame_pady:int = 8
        self.frame_corner_radius:int = 8

        self.element_padx:int = 8
        self.element_pady:int = 8
        
        ################################################################

        self.email:Email = Email()
        self.title("AFS - generator")
        self.geometry("1000x600")
        self.font = customtkinter.CTkFont(family="roboto", size=12, weight="bold")
        self.header_font = customtkinter.CTkFont(family="roboto", size=16, weight="bold")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0), weight=1)

        #column 0

        self.set_email_frame = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent")
       
        self.set_email_frame.grid(row=0, column=0, sticky="news")
        self.set_email_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.set_email_frame.grid_columnconfigure((0), weight=1)

        self.set_email_frame_entry = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius)
        self.set_email_frame_entry.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="new")
        self.set_email_frame_entry.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.set_email_frame_entry.grid_columnconfigure((0), weight=1)

        self.set_email_frame_buttons = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius)
        self.set_email_frame_buttons.grid(row=2, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="sew")
        self.set_email_frame_buttons.grid_rowconfigure((0, 1), weight=1)
        self.set_email_frame_buttons.grid_columnconfigure((0), weight=1)

        # self.sender_email_label = customtkinter.CTkLabel(self.set_email_frame, text="Sender email:", fg_color="transparent", font=self.font)
        # self.sender_email_label.grid(row=0, column=0, padx=self.element_padx, sticky="ws")

        # self.sender_email_Entry = customtkinter.CTkEntry(self.set_email_frame, placeholder_text="Sender email")
        # self.sender_email_Entry.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        # self.sender_email_Entry.insert(0, self.config.get('senderEmail'))

        self.reciepent_email_label = customtkinter.CTkLabel( self.set_email_frame_entry, text="Recienpent email:", fg_color="transparent", font=self.font)
        self.reciepent_email_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.reciepent_email_Entry = customtkinter.CTkEntry( self.set_email_frame_entry, placeholder_text="Recienpent email")
        self.reciepent_email_Entry.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.reciepent_email_Entry.insert(0, self.config.get('recipientEmail'))

        self.afs_email_label = customtkinter.CTkLabel( self.set_email_frame_entry, text="AFS email:", fg_color="transparent", font=self.font)
        self.afs_email_label.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.afs_email_Entry = customtkinter.CTkEntry( self.set_email_frame_entry, placeholder_text="AFS email")
        self.afs_email_Entry.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.afs_email_Entry.insert(0, self.config.get('afsEmail'))

        self.generate_email = customtkinter.CTkButton(self.set_email_frame_buttons, text="Generate Email", command=self.generate_email_callback)
        self.generate_email.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        self.send_email = customtkinter.CTkButton(self.set_email_frame_buttons, text="Send Email", command=self.send_email_callback)
        self.send_email.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        #column 1

        self.email_box_frame = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent") 
        self.email_box_frame.grid(row=0, column=1, sticky="nsew")  
        self.email_box_frame.grid_rowconfigure((0, 1), weight=1)
        self.email_box_frame.grid_columnconfigure((0), weight=1)

        self.email_box_upper_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=self.frame_corner_radius)
        self.email_box_upper_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="new")
        self.email_box_upper_frame.grid_rowconfigure((0, 1, 3, 4, 5, 6), weight=1)
        self.email_box_upper_frame.grid_columnconfigure((0), weight=1)

        self.subject_label = customtkinter.CTkLabel(master=self.email_box_upper_frame, text="Email Subject:", fg_color="transparent", font=self.font)
        self.subject_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.subject = customtkinter.CTkEntry(master=self.email_box_upper_frame, placeholder_text="Email Subject")
        self.subject.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        self.to_email_entry_label = customtkinter.CTkLabel(master=self.email_box_upper_frame, text="To Email:", fg_color="transparent", font=self.font)
        self.to_email_entry_label.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.to_email_entry = customtkinter.CTkEntry(master=self.email_box_upper_frame, placeholder_text="To Email")
        self.to_email_entry.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        self.BCC_email_entry_label = customtkinter.CTkLabel(master=self.email_box_upper_frame, text="BCC Email:", fg_color="transparent", font=self.font)
        self.BCC_email_entry_label.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.BCC_email_entry = customtkinter.CTkEntry(master=self.email_box_upper_frame, placeholder_text="BCC Email")
        self.BCC_email_entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        self.email_body_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=self.frame_corner_radius)
        self.email_body_frame.grid(row=1, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="nsew")
        self.email_body_frame.grid_rowconfigure((0, 1), weight=1)
        self.email_body_frame.grid_columnconfigure((0), weight=1)

        self.email_body_label = customtkinter.CTkLabel(master=self.email_body_frame, text="Email Body:", fg_color="transparent", font=self.font)
        self.email_body_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.email_body = customtkinter.CTkTextbox(master=self.email_body_frame,height=238)
        self.email_body.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewsn")

        #column 2

        self.settings_box = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.settings_box.grid(row=0, column=2, sticky="nsew")
        self.settings_box.grid_rowconfigure((0,1), weight=1)
        self.settings_box.grid_columnconfigure((0), weight=1)

        self.settings_box_frame = customtkinter.CTkScrollableFrame(master=self.settings_box,corner_radius=self.frame_corner_radius)
        self.settings_box_frame.grid(row=1, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.settings_box_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        self.settings_box_frame.grid_columnconfigure((0), weight=1)


        # self.settings_box_frame = customtkinter.CTkFrame(master=self.settings_box,corner_radius=self.frame_corner_radius)
        # self.settings_box_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="new")
        # self.settings_box_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)
        # self.settings_box_frame.grid_columnconfigure((0), weight=1)

        # self.settings_box_label = customtkinter.CTkLabel(master=self.settings_box_frame, text="Settings:", fg_color="transparent", font=self.font)
        # self.settings_box_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.combobox_label = customtkinter.CTkLabel(master=self.settings_box_frame, text="Select invitation type:", fg_color="transparent", font=self.font)
        self.combobox_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.combobox_var = customtkinter.StringVar(value="Service Review")
        self.combobox = customtkinter.CTkComboBox(master=self.settings_box_frame, values=["Service Review", "Service & Product review using SKU", "Service & Product Review(add/update Product Review)"],
                                                  command=self.combobox_callback, variable=self.combobox_var)
        self.combobox_var.set("Service Review")
        self.combobox.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")

        self.send_afs_directly_checkbox_var = customtkinter.StringVar(value="on")
        self.send_afs_directly_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Send AFS Directly", command=self.send_afs_directly_callback, variable=self.send_afs_directly_checkbox_var, onvalue="on", offvalue="off")
        self.send_afs_directly_checkbox.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.locale_var = customtkinter.StringVar(value="on")
        self.locale_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Locale", command=self.locale_callback, variable=self.locale_var, onvalue="on", offvalue="off")
        self.locale_checkbox.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        

    def locale_callback(self):
        print(f"locale: {self.locale_var.get()}")

    def send_afs_directly_callback(self):
        print("send afs directly")

    def send_email_callback(self):
        subject = "Trustpilot Review"
        # email_from = self.sender_email_Entry.get()
        email_to = self.reciepent_email_Entry.get()
        email_bcc = self.afs_email_Entry.get()

        payload_type = self.get_payload_type()
        items = {

            "recipientName": "hrh",
            "recipientEmail": email_to
            
           
        }
        payload = PayloadBuilder(payload_type, **items).build()
        self.email_body.insert(0.0, pformat(payload))
        html = self.generate_html(payload)
        # self.email.send_email(subject, email_from, email_to, email_bcc, html)

    def generate_email_callback(self):
        configData = {
            "senderEmail": self.sender_email_Entry.get(),
            "recipientEmail": self.reciepent_email_Entry.get(),
            "afsEmail": self.afs_email_Entry.get()
        }
        self.configparser.set_config(**configData)

        email_from = self.sender_email_Entry.get()
        email_to = self.reciepent_email_Entry.get()
        email_bcc = self.afs_email_Entry.get()

        items = {
            "recipientName": "hrh",
            "recipientEmail": email_to,
            "referenceId": "1234"
        }
        payload_type = self.get_payload_type()
        payload = PayloadBuilder(payload_type, **items).build()

        html = self.generate_html(payload)
        # self.email.send_email(subject, email_from, email_to, email_bcc, html)

    def get_payload_type(self):
        if self.combobox_var.get() == "Service Review":
            return PayloadType.SERVICE_REVIEW
        if self.combobox_var.get() == "Service & Product review using SKU":
            return PayloadType.SERVICE_AND_PRODUCT_REVIEW_SKU
        if self.combobox_var.get() == "Service & Product Review(add/update Product Review)":
            return PayloadType.SERVICE_AND_PRODUCT_REVIEW

    def generate_html(self, payload):
        sds = f"<script type='application/json+trustpilot'>" + json.dumps(payload) + "\n" + "</script>"
        html = f"""
        <html>
          <head>{sds}</head>
          <body>
            <p>Hi!<br>
              How are you?<br>
              Here is the <a href="http://www.python.org">link</a> you wanted.
            </p>
          </body>
        </html>
        """
        return html

    def combobox_callback(self, choice):
        print("combobox dropdown clicked:", choice)

    def copy_link_callback(self):
        self.clipboard_clear()
        self.clipboard_append(self.link.get())
        self.update()


