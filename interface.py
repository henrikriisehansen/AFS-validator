import customtkinter
from pprint import pformat
from sendEmail import Email
import json
from config import ConfigParser
from payload import PayloadBuilder, PayloadType
from locale_dict import LocaleParser


class App(customtkinter.CTk):
    def __init__(self):
        
        super().__init__()

        # Initialize configuration and locale data
        self.configparser:ConfigParser = ConfigParser()
        self.data:dict = self.configparser._get_config()
        self.locale_data:dict = LocaleParser().get_locale()
        # self._data:dict = self.configparser._get_config()

        # print(pformat(self.data))
        # Frame padding and styling
        self.frame_padx:int = 8
        self.frame_pady:int = 8
        self.frame_corner_radius:int = 8

        self.element_padx:int = 8
        self.element_pady:int = 8

        # Widget elements dictionary
        self.widget_elements:dict[str,object] = {}

        # Initialize email object and set window properties
        self.email:Email = Email()
        self.title("AFS - generator")
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
        self.set_email_frame_entry = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius)
        self.set_email_frame_entry.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.set_email_frame_entry.grid_rowconfigure((0), weight=1)
        self.set_email_frame_entry.grid_columnconfigure((0), weight=1)

        # Inner frame for email entry
        self.email_frame_entry_inner_frame = customtkinter.CTkFrame(master=self.set_email_frame_entry,corner_radius=self.frame_corner_radius,fg_color="transparent")
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
        self.combobox = customtkinter.CTkComboBox(master=self.email_frame_entry_inner_frame, values=["Service Review", "Service & Product review using SKU", "Service & Product Review(add/update Product Review)"],
                                                  command=lambda x :self.event_callback(self.combobox.get()), variable=self.combobox_var)
        self.combobox.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.combobox.set(self.data["settings"]["invitation_type"])
        self.widget_elements["invitation_type"] = self.combobox
        
        # SMTP settings frame
        self.set_email_frame_smtp = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius)
        self.set_email_frame_smtp.grid(row=1, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.set_email_frame_smtp.grid_rowconfigure((0), weight=1)
        self.set_email_frame_smtp.grid_columnconfigure((0), weight=1)

        # Scrollable frame for SMTP settings
        self.email_frame_smtp_scrollbar = customtkinter.CTkScrollableFrame(master=self.set_email_frame_smtp, corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.email_frame_smtp_scrollbar.grid(row=0, column=0, rowspan=8, sticky="nsew")
        self.email_frame_smtp_scrollbar.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.email_frame_smtp_scrollbar.grid_columnconfigure((0), weight=1)

        # SMTP settings labels and entries
        self.smtp_label = customtkinter.CTkLabel(master=self.email_frame_smtp_scrollbar, text="SMTP:", fg_color="transparent", font=self.header_font)
        self.smtp_label.grid(row=0, column=0, padx=self.element_padx, sticky="wn")

        self.sender_email_label = customtkinter.CTkLabel(master=self.email_frame_smtp_scrollbar, text="Sender email:", fg_color="transparent", font=self.font)
        self.sender_email_label.grid(row=1, column=0, padx=self.element_padx, sticky="wn")

        self.sender_email_Entry = customtkinter.CTkEntry(master=self.email_frame_smtp_scrollbar, placeholder_text="Sender email")
        self.sender_email_Entry.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.sender_email_Entry.insert(0, self.data['smtp']['smtp_sender_email'])
        self.widget_elements["sender_email"] = self.sender_email_Entry

        self.smtp_server = customtkinter.CTkLabel(master=self.email_frame_smtp_scrollbar, text="smtp_server:", fg_color="transparent", font=self.font)
        self.smtp_server.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.smtp_server_entry = customtkinter.CTkEntry(master=self.email_frame_smtp_scrollbar, placeholder_text="smtp_server")
        self.smtp_server_entry.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.smtp_server_entry.insert(0, self.data['smtp']['smtp_server'])
        self.widget_elements["smtp_server"] = self.smtp_server_entry

        self.smtp_port = customtkinter.CTkLabel(master=self.email_frame_smtp_scrollbar, text="smtp_port:", fg_color="transparent", font=self.font)
        self.smtp_port.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")
        
        self.smtp_port_entry = customtkinter.CTkEntry(master=self.email_frame_smtp_scrollbar, placeholder_text="smtp_port")
        self.smtp_port_entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.smtp_port_entry.insert(0, self.data["smtp"]["smtp_port"])
        self.widget_elements["smtp_port"] = self.smtp_port_entry

        self.smtp_password_label = customtkinter.CTkLabel(master=self.email_frame_smtp_scrollbar, text="smtp_password:", fg_color="transparent", font=self.font)
        self.smtp_password_label.grid(row=7, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.smtp_password_entry = customtkinter.CTkEntry(master=self.email_frame_smtp_scrollbar, placeholder_text="smtp_password")
        self.smtp_password_entry.grid(row=8, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.smtp_password_entry.insert(0, self.data["smtp"]["smtp_password"])
        self.widget_elements["smtp_password"] = self.smtp_password_entry

        # Buttons frame
        self.set_email_frame_buttons = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius)
        self.set_email_frame_buttons.grid(row=2, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="sewn")
        self.set_email_frame_buttons.grid_rowconfigure((0), weight=1)
        self.set_email_frame_buttons.grid_columnconfigure((0), weight=1)

        # Inner frame for buttons
        self.email_frame_buttons_inner_frame = customtkinter.CTkFrame(master=self.set_email_frame_buttons,corner_radius=self.frame_corner_radius,fg_color="transparent")
        self.email_frame_buttons_inner_frame.grid(row=0, column=0, sticky="sew")
        self.email_frame_buttons_inner_frame.grid_rowconfigure((0, 1), weight=1)
        self.email_frame_buttons_inner_frame.grid_columnconfigure((0), weight=1)

        # Generate and send email buttons
        self.generate_email = customtkinter.CTkButton(master= self.email_frame_buttons_inner_frame, text="Generate Email", command=lambda:self.event_callback("generate email"))
        self.generate_email.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        self.send_email = customtkinter.CTkButton(master= self.email_frame_buttons_inner_frame, text="Send Email", command=lambda:self.event_callback("send email"))
        self.send_email.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        # Column 1: Email content
        self.email_box_frame = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent") 
        self.email_box_frame.grid(row=0, column=1, sticky="nsew")  
        self.email_box_frame.grid_rowconfigure((0, 1), weight=1)
        self.email_box_frame.grid_columnconfigure((0), weight=1)

        # Upper frame for email content
        self.email_box_upper_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=self.frame_corner_radius)
        self.email_box_upper_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.email_box_upper_frame.grid_rowconfigure((0), weight=1)
        self.email_box_upper_frame.grid_columnconfigure((0), weight=1)

        # Inner frame for email content
        self.email_box_inner_upper_frame = customtkinter.CTkFrame(master=self.email_box_upper_frame,corner_radius=self.frame_corner_radius,fg_color="transparent")
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
        self.to_email_entry.insert(0, self.data['emails']['recipient_email'])
        self.widget_elements["to_email"] = self.to_email_entry

        self.BCC_email_entry_label = customtkinter.CTkLabel(master=self.email_box_inner_upper_frame, text="BCC Email:", fg_color="transparent", font=self.font)
        self.BCC_email_entry_label.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.BCC_email_entry = customtkinter.CTkEntry(master=self.email_box_inner_upper_frame, placeholder_text="BCC Email")
        self.BCC_email_entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.BCC_email_entry.insert(0, self.data['emails']['bcc_email'])
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
        self.send_afs_directly_checkbox_var = customtkinter.StringVar(value="on")
        self.send_afs_directly_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Send AFS Directly", command=lambda:self.event_callback(**{"state":self.send_afs_directly_checkbox.get(),"entry":None}), variable=self.send_afs_directly_checkbox_var, onvalue="on", offvalue="off")
        self.send_afs_directly_checkbox.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.send_afs_directly_checkbox._variable.set(self.data["settings"]["send_afs_direct"])
        self.send_afs_directly_checkbox.grid_remove

        self.locale_var = customtkinter.StringVar(value="on")
        self.locale_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Locale", command=lambda:self.event_callback(""), variable=self.locale_var, onvalue="on", offvalue="off")
        self.locale_checkbox.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.locale_checkbox._variable.set(self.data["settings"]["locale_checkbox"])
       
        self.locale_dropdown_var = customtkinter.StringVar(value="en-GB")
        self.locale_dropdown = customtkinter.CTkComboBox(master=self.settings_box_frame, values=[k for (k,v) in self.locale_data.items()], command=lambda x:self.event_callback(self.locale_dropdown.get()),variable=self.locale_dropdown_var)
        self.locale_dropdown.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.locale_dropdown.set(self.data["settings"]["locale"])
        self.locale_dropdown.grid_forget()
        
        self.template_checkbox_var = customtkinter.StringVar(value="on")
        self.template_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Template", command=lambda:self.event_callback("set template"), variable=self.template_checkbox_var, onvalue="on", offvalue="off")
        self.template_checkbox.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.template_checkbox._variable.set(self.data["settings"]["template_checkbox"])

        self.template_dropdown_var = customtkinter.StringVar(value="English - Service reviews")
        self.template_dropdown = customtkinter.CTkComboBox(master=self.settings_box_frame, values=["English - Service reviews", "Danish - Service reviews", "German - Service reviews", "Spanish - Service reviews", "French - Service reviews", "Italian - Service reviews", "Dutch - Service reviews"], command=lambda x:self.event_callback("template"), variable=self.template_dropdown_var)
        self.template_dropdown.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.template_dropdown.set(self.data["settings"]["template"])
        self.template_dropdown.grid_forget()

        self.sku_checkbox_var = customtkinter.StringVar(value="on")
        self.sku_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set SKU", command=lambda:self.event_callback(**{"state":self.sku_checkbox.get(),"entry":self.sku_entry}), variable=self.sku_checkbox_var, onvalue="on", offvalue="off")
        self.sku_checkbox.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.sku_checkbox._variable.set(self.data["settings"]["sku_checkbox"])
        
        self.sku_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="SKU values")
        self.sku_entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.sku_entry.insert(0, self.data["settings"]["sku"])
        self.sku_entry.grid_remove()

        self.location_id_checkbox_var = customtkinter.StringVar(value="on")
        self.location_id_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Location ID", command=lambda:self.event_callback("set location id"), variable=self.location_id_checkbox_var, onvalue="on", offvalue="off")
        self.location_id_checkbox.grid(row=7, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.location_id_checkbox._variable.set(self.data["settings"]["location_id_checkbox"])

        self.location_id_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Location ID values")
        self.location_id_entry.grid(row=8, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.location_id_entry.insert(0, self.data["settings"]["location_id"])
        self.location_id_entry.grid_forget()

        self.tags_label = customtkinter.CTkLabel(master=self.settings_box_frame, text="Tags:", fg_color="transparent", font=self.font)
        self.tags_label.grid(row=9, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.tags_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Tags")
        self.tags_entry.grid(row=10, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.tags_entry.insert(0, self.data["settings"]["tags"])
        self.tags_entry.grid_forget()

        self.prefferedSendTime_checkbox_var = customtkinter.StringVar(value=self.data["settings"]["preffered_sendtime_checkbox"])
        self.prefferedSendTime_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Preffered Send Time", command=lambda:self.event_callback("set preffered send time"), variable=self.prefferedSendTime_checkbox_var, onvalue="on", offvalue="off")
        self.prefferedSendTime_checkbox.grid(row=11, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        # self.prefferedSendTime_checkbox._variable.set(self.data["settings"]["preffered_sendtime_checkbox"])

        self.prefferedSendTime_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Preffered Send Time")
        self.prefferedSendTime_entry.grid(row=12, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.prefferedSendTime_entry.insert(0, self.data["settings"]["preffered_send_time"])
        self.prefferedSendTime_entry.grid_forget()

        self.productReviewInvitationPrefferedSendTime_checkbox_var = customtkinter.StringVar(value="on")
        self.productReviewInvitationPrefferedSendTime_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Product Review Invitation Preffered Send Time", command=lambda:self.event_callback("set preffered product send time"), variable=self.productReviewInvitationPrefferedSendTime_checkbox_var, onvalue="on", offvalue="off")
        self.productReviewInvitationPrefferedSendTime_checkbox.grid(row=13, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.productReviewInvitationPrefferedSendTime_checkbox._variable.set(self.data["settings"]["product_review_invitation_preffered_sendtime_checkbox"])
        
        self.productReviewInvitationPrefferedSendTime_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Product Review Invitation Preffered Send Time")
        self.productReviewInvitationPrefferedSendTime_entry.grid(row=14, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.productReviewInvitationPrefferedSendTime_entry.insert(0, self.data["settings"]["product_review_invitation_preffered_sendtime"])
        self.productReviewInvitationPrefferedSendTime_entry.grid_forget()
        
        self.build_payload()

    def event_callback(self,**kwargs):
        
        if kwargs.get("state") == "on" and kwargs.get('entry') != None:
            kwargs["entry"].grid() 

        if kwargs.get("state") == "off" and kwargs.get('entry') != None:
            kwargs["entry"].grid_remove()
        
        self.get_values()
        self.configparser.set_config(**self.data)
        self.build_payload()
       
    def build_payload(self):

        data = self.data['settings'] | self.data['emails']
        
        self.payload = PayloadBuilder(self.get_payload_type(),**data).build()
        self.email_body.delete(0.0, "end")
        self.email_body.insert(0.0, self.generate_html(self.payload))

    def get_payload_type(self):

        if self.combobox_var.get() == "Service Review":
            return PayloadType.SERVICE_REVIEW
        if self.combobox_var.get() == "Service & Product review using SKU":
            return PayloadType.SERVICE_AND_PRODUCT_REVIEW_SKU
        if self.combobox_var.get() == "Service & Product Review(add/update Product Review)":
            return PayloadType.SERVICE_AND_PRODUCT_REVIEW

    def get_values(self):

        # self.data["emails"]["recipient_email"] = self.reciepent_email_Entry.get()
        # self.data["emails"]["afs_email"] = self.afs_email_Entry.get()
        # self.data["emails"]["email_subject"] = self.subject.get()
        # self.data["emails"]["recipient_name"] = self.reciepent_name_Entry.get()

        self.data["smtp"]["smtp_sender_email"] = self.sender_email_Entry.get()
        self.data["smtp"]["smtp_server"] = self.smtp_server_entry.get()
        self.data["smtp"]["smtp_port"] = self.smtp_port_entry.get()
        self.data["smtp"]["smtp_password"] = self.smtp_password_entry.get()
        
        self.data["settings"]["invitation_type"] = self.combobox.get()
        self.data["settings"]["send_afs_direct"] = self.send_afs_directly_checkbox.get()
        self.data["settings"]["locale_checkbox"] = self.locale_checkbox.get()
        self.data["settings"]["template_checkbox"] = self.template_checkbox.get()
        self.data["settings"]["template"] = self.template_dropdown.get()
        self.data["settings"]["locale_checkbox"] = self.locale_checkbox.get()
        self.data["settings"]["locale"] = self.locale_dropdown.get()
        self.data["settings"]["sku_checkbox"] = self.sku_checkbox.get()
        self.data["settings"]["sku"] = self.sku_entry.get()
        self.data["settings"]["location_id_checkbox"] = self.location_id_checkbox.get()
        self.data["settings"]["location_id"] = self.location_id_entry.get()
        self.data["settings"]["tags"] = self.tags_entry.get()
        self.data["settings"]["preffered_sendtime_checkbox"] = self.prefferedSendTime_checkbox.get()
        self.data["settings"]["preffered_send_time"] = self.prefferedSendTime_entry.get()
        self.data["settings"]["product_review_invitation_preffered_sendtime_checkbox"] = self.productReviewInvitationPrefferedSendTime_checkbox.get()
        self.data["settings"]["product_review_invitation_preffered_sendtime"] = self.productReviewInvitationPrefferedSendTime_entry.get()

    def generate_html(self, payload):
        # TODO: Implement actual payload generation and rendering here.
        sds = json.dumps(payload, indent=1)
        html = f"""<html>\n<head>\n<script type='application/json+trustpilot'>\n{sds}\n</script>\n</head>\n<body>\n<p>Hi!<br>\nHow are you?<br>\n</p>\n</body>\n</html>"""
         
        return html

    def copy_link_callback(self):
        self.clipboard_clear()
        self.clipboard_append(self.link.get())
        self.update()


