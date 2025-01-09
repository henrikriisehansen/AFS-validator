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
        self.configparser = ConfigParser()
        self.config = self.configparser.get_config()

        self.email = Email()
        self.title("AFS")
        self.geometry("800x600")
        self.font = customtkinter.CTkFont(family="roboto", size=13, weight="bold")
        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure((0), weight=1)


        #column 0

        self.email_frame = customtkinter.CTkFrame(master=self,corner_radius=20)
       
        self.email_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.email_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), weight=1)
        self.email_frame.grid_columnconfigure((0), weight=1)

        self.sender_email_label = customtkinter.CTkLabel(self.email_frame, text="Sender email:", fg_color="transparent", font=self.font)
        self.sender_email_label.grid(row=0, column=0, padx=20, sticky="ws")

        self.sender_email_Entry = customtkinter.CTkEntry(self.email_frame, placeholder_text="Sender email")
        self.sender_email_Entry.grid(row=1, column=0, padx=20, pady=5, sticky="ewn")
        self.sender_email_Entry.insert(0, self.config.get('senderEmail'))

        self.reciepent_email_label = customtkinter.CTkLabel(self.email_frame, text="Recienpent email:", fg_color="transparent", font=self.font)
        self.reciepent_email_label.grid(row=2, column=0, padx=20, pady=5, sticky="ws")

        self.reciepent_email_Entry = customtkinter.CTkEntry(self.email_frame, placeholder_text="Recienpent email")
        self.reciepent_email_Entry.grid(row=3, column=0, padx=20, pady=5, sticky="ewn")
        self.reciepent_email_Entry.insert(0, self.config.get('recipientEmail'))

        self.afs_email_label = customtkinter.CTkLabel(self.email_frame, text="AFS email:", fg_color="transparent", font=self.font)
        self.afs_email_label.grid(row=4, column=0, padx=20, pady=5, sticky="ws")

        self.afs_email_Entry = customtkinter.CTkEntry(self.email_frame, placeholder_text="AFS email")
        self.afs_email_Entry.grid(row=5, column=0, padx=20, pady=5, sticky="ewn")
        self.afs_email_Entry.insert(0, self.config.get('afsEmail'))

        self.combobox_label = customtkinter.CTkLabel(self.email_frame, text="Select invitation type:", fg_color="transparent", font=self.font)
        self.combobox_label.grid(row=6, column=0, padx=20, pady=5, sticky="ws")

        self.combobox_var = customtkinter.StringVar(value="Service Review")
        self.combobox = customtkinter.CTkComboBox(self.email_frame, values=["Service Review", "Service & Product review using SKU", "Service & Product Review(add/update Product Review)"],
                                                  command=self.combobox_callback, variable=self.combobox_var)
        self.combobox_var.set("Service Review")
        self.combobox.grid(row=7, column=0, padx=20, pady=5, sticky="ewn")

        self.generate_email = customtkinter.CTkButton(self.email_frame, text="Generate Email", command=self.generate_email_callback)
        self.generate_email.grid(row=8, column=0, padx=20, pady=5, sticky="ews")

        self.send_email = customtkinter.CTkButton(self.email_frame, text="Send Email", command=self.send_email_callback)
        self.send_email.grid(row=9, column=0, padx=20, pady=5, sticky="ewn")

        #column 1

        self.entry_box = customtkinter.CTkFrame(master=self,corner_radius=20) 
        self.entry_box.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")  

        self.email_body = customtkinter.CTkTextbox(self.entry_box,height=200,)
        self.email_body.grid(row=1, column=1,rowspan=4, padx=20, pady=5, sticky="ews")

        #column 2

        self.settings_box = customtkinter.CTkFrame(master=self,corner_radius=20)
        self.settings_box.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")

    def send_email_callback(self):
        subject = "Trustpilot Review"
        email_from = self.sender_email_Entry.get()
        email_to = self.reciepent_email_Entry.get()
        email_bcc = self.afs_email_Entry.get()

        payload_type = self.get_payload_type()
        items = {

            "recipientName": "hrh",
            "recipientEmail": email_to
            
           
        }
        payload = PayloadBuilder(payload_type, **items).build()
        self.entry_box.insert(0.0, pformat(payload))
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


