import customtkinter
from pprint import pformat
from sendEmail import Email
import json
from config import ConfigParser
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

        self.reciepent_email_label = customtkinter.CTkLabel( self.set_email_frame_entry, text="Recienpent email:", fg_color="transparent", font=self.font)
        self.reciepent_email_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.reciepent_email_Entry = customtkinter.CTkEntry( self.set_email_frame_entry, placeholder_text="Recienpent email")
        self.reciepent_email_Entry.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.reciepent_email_Entry.insert(0, self.config.get('emails','recipientEmail'))

        self.afs_email_label = customtkinter.CTkLabel( self.set_email_frame_entry, text="AFS email:", fg_color="transparent", font=self.font)
        self.afs_email_label.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.afs_email_Entry = customtkinter.CTkEntry( self.set_email_frame_entry, placeholder_text="AFS email")
        self.afs_email_Entry.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.afs_email_Entry.insert(0, self.config.get('emails','afsEmail'))
        
        self.set_email_frame_smtp = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius)
        self.set_email_frame_smtp.grid(row=1, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="new")
        self.set_email_frame_smtp.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        self.set_email_frame_smtp.grid_columnconfigure((0), weight=1)

        self.smtp_label = customtkinter.CTkLabel(master=self.set_email_frame_smtp, text="SMTP:", fg_color="transparent", font=self.header_font)
        self.smtp_label.grid(row=0, column=0, padx=self.element_padx, sticky="wn")

        self.sender_email_label = customtkinter.CTkLabel(master=self.set_email_frame_smtp, text="Sender email:", fg_color="transparent", font=self.font)
        self.sender_email_label.grid(row=1, column=0, padx=self.element_padx, sticky="wn")

        self.sender_email_Entry = customtkinter.CTkEntry(master=self.set_email_frame_smtp, placeholder_text="Sender email")
        self.sender_email_Entry.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.sender_email_Entry.insert(0, self.config.get('smtp','smtpsenderemail'))

        self.smtp_server = customtkinter.CTkLabel(master=self.set_email_frame_smtp, text="smtp_server:", fg_color="transparent", font=self.font)
        self.smtp_server.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.smtp_server_entry = customtkinter.CTkEntry(master=self.set_email_frame_smtp, placeholder_text="smtp_server")
        self.smtp_server_entry.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.smtp_server_entry.insert(0, self.config.get('smtp','smtpServer'))

        self.smtp_port = customtkinter.CTkLabel(master=self.set_email_frame_smtp, text="smtp_port:", fg_color="transparent", font=self.font)
        self.smtp_port.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")
        
        self.smtp_port_entry = customtkinter.CTkEntry(master=self.set_email_frame_smtp, placeholder_text="smtp_port")
        self.smtp_port_entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.smtp_port_entry.insert(0, self.config.get('smtp','smtpPort'))

        self.smtp_password_label = customtkinter.CTkLabel(master=self.set_email_frame_smtp, text="smtp_password:", fg_color="transparent", font=self.font)
        self.smtp_password_label.grid(row=7, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.smtp_password_entry = customtkinter.CTkEntry(master=self.set_email_frame_smtp, placeholder_text="smtp_password")
        self.smtp_password_entry.grid(row=8, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.smtp_password_entry.insert(0, self.config.get('smtp','smtpPassword'))

        self.set_email_frame_buttons = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=self.frame_corner_radius)
        self.set_email_frame_buttons.grid(row=2, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="sew")
        self.set_email_frame_buttons.grid_rowconfigure((0, 1), weight=1)
        self.set_email_frame_buttons.grid_columnconfigure((0), weight=1)

        self.generate_email = customtkinter.CTkButton(self.set_email_frame_buttons, text="Generate Email", command=lambda:self.event_callback("generate email"))
        self.generate_email.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        self.send_email = customtkinter.CTkButton(self.set_email_frame_buttons, text="Send Email", command=lambda:self.event_callback("send email"))
        self.send_email.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")

        #column 1

        self.email_box_frame = customtkinter.CTkFrame(master=self,corner_radius=self.frame_corner_radius,fg_color="transparent") 
        self.email_box_frame.grid(row=0, column=1, sticky="nsew")  
        self.email_box_frame.grid_rowconfigure((0, 1), weight=1)
        self.email_box_frame.grid_columnconfigure((0), weight=1)

        self.email_box_upper_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=self.frame_corner_radius)
        self.email_box_upper_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.email_box_upper_frame.grid_rowconfigure((0, 1, 3, 4, 5, 6), weight=1)
        self.email_box_upper_frame.grid_columnconfigure((0), weight=1)

        self.subject_label = customtkinter.CTkLabel(master=self.email_box_upper_frame, text="Email Subject:", fg_color="transparent", font=self.font)
        self.subject_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.subject = customtkinter.CTkEntry(master=self.email_box_upper_frame, placeholder_text="Email Subject")
        self.subject.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.subject.insert(0, self.config.get('emails', 'emailSubject'))

        self.to_email_entry_label = customtkinter.CTkLabel(master=self.email_box_upper_frame, text="To Email:", fg_color="transparent", font=self.font)
        self.to_email_entry_label.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.to_email_entry = customtkinter.CTkEntry(master=self.email_box_upper_frame, placeholder_text="To Email")
        self.to_email_entry.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.to_email_entry.insert(0, self.config.get('emails', 'recipientEmail'))

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
        self.settings_box.grid_rowconfigure((0), weight=1)
        self.settings_box.grid_columnconfigure((0), weight=1)

        self.settings_box_frame = customtkinter.CTkScrollableFrame(master=self.settings_box,corner_radius=self.frame_corner_radius)
        self.settings_box_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="news")
        self.settings_box_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16), weight=1)
        self.settings_box_frame.grid_columnconfigure((0), weight=1)

        self.combobox_label = customtkinter.CTkLabel(master=self.settings_box_frame, text="Select invitation type:", fg_color="transparent", font=self.font)
        self.combobox_label.grid(row=0, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.combobox_var = customtkinter.StringVar(value="Service Review")
        self.combobox = customtkinter.CTkComboBox(master=self.settings_box_frame, values=["Service Review", "Service & Product review using SKU", "Service & Product Review(add/update Product Review)"],
                                                  command=lambda x :self.event_callback(self.combobox.get()), variable=self.combobox_var)
        self.combobox.set(self.config.get("settings","invitationType"))
        self.combobox.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")

        self.send_afs_directly_checkbox_var = customtkinter.StringVar(value="on")
        self.send_afs_directly_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Send AFS Directly", command=lambda:self.event_callback("send afs direct"), variable=self.send_afs_directly_checkbox_var, onvalue="on", offvalue="off")
        self.send_afs_directly_checkbox.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.send_afs_directly_checkbox._variable.set(self.config.get("settings","sendAfsDirectCheckBox"))

        self.locale_var = customtkinter.StringVar(value="on")
        self.locale_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Locale", command=lambda:self.event_callback(""), variable=self.locale_var, onvalue="on", offvalue="off")
        self.locale_checkbox.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.locale_checkbox._variable.set(self.config.get("settings","localeCheckBox"))

        self.locale_dropdown_var = customtkinter.StringVar(value="en-US")
        self.locale_dropdown = customtkinter.CTkComboBox(master=self.settings_box_frame, values=["en-US", "da-DK", "de-DE", "es-ES", "fr-FR", "it-IT", "nl-NL"], command=lambda x:self.event_callback(self.locale_dropdown.get()),variable=self.locale_dropdown_var)
        self.locale_dropdown.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        
        self.template_checkbox_var = customtkinter.StringVar(value="on")
        self.template_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Template", command=lambda:self.event_callback("set template"), variable=self.template_checkbox_var, onvalue="on", offvalue="off")
        self.template_checkbox.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.template_dropdown_var = customtkinter.StringVar(value="English - Service reviews")
        self.template_dropdown = customtkinter.CTkComboBox(master=self.settings_box_frame, values=["English - Service reviews", "Danish - Service reviews", "German - Service reviews", "Spanish - Service reviews", "French - Service reviews", "Italian - Service reviews", "Dutch - Service reviews"], command=lambda x:self.event_callback("template"), variable=self.template_dropdown_var)
        self.template_dropdown.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")

        self.sku_checkbox_var = customtkinter.StringVar(value="on")
        self.sku_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set SKU", command=lambda:self.event_callback(self.sku_checkbox.get()), variable=self.sku_checkbox_var, onvalue="on", offvalue="off")
        self.sku_checkbox.grid(row=7, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.sku_checkbox._variable.set(self.config.get("settings", "skuCheckBox"))

        self.sku_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="SKU values")
        self.sku_entry.grid(row=8, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.sku_entry.insert(0, self.config.get("settings", "sku"))

        self.location_id_checkbox_var = customtkinter.StringVar(value="on")
        self.location_id_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Location ID", command=lambda:self.event_callback("set location id"), variable=self.location_id_checkbox_var, onvalue="on", offvalue="off")
        self.location_id_checkbox.grid(row=9, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.location_id_checkbox._variable.set(self.config.get("settings", "locationIdCheckBox"))

        self.location_id_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Location ID values")
        self.location_id_entry.grid(row=10, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.location_id_entry.insert(0, self.config.get("settings", "locationId"))

        self.tags_label = customtkinter.CTkLabel(master=self.settings_box_frame, text="Tags:", fg_color="transparent", font=self.font)
        self.tags_label.grid(row=11, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.tags_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Tags")
        self.tags_entry.grid(row=12, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.tags_entry.insert(0, self.config.get("settings", "tags"))

        self.prefferedSendTime_checkbox_var = customtkinter.StringVar(value="on")
        self.prefferedSendTime_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Preffered Send Time", command=lambda:self.event_callback("set preffered send time"), variable=self.prefferedSendTime_checkbox_var, onvalue="on", offvalue="off")
        self.prefferedSendTime_checkbox.grid(row=13, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.prefferedSendTime_checkbox._variable.set(self.config.get("settings", "prefferedSendTimeCheckBox"))

        self.prefferedSendTime_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Preffered Send Time")
        self.prefferedSendTime_entry.grid(row=14, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.prefferedSendTime_entry.insert(0, self.config.get("settings", "prefferedSendTime"))

        self.productReviewInvitationPrefferedSendTime_checkbox_var = customtkinter.StringVar(value="on")
        self.productReviewInvitationPrefferedSendTime_checkbox = customtkinter.CTkCheckBox(master=self.settings_box_frame, text="Set Product Review Invitation Preffered Send Time", command=lambda:self.event_callback("set preffered product send time"), variable=self.productReviewInvitationPrefferedSendTime_checkbox_var, onvalue="on", offvalue="off")
        self.productReviewInvitationPrefferedSendTime_checkbox.grid(row=15, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")
        self.productReviewInvitationPrefferedSendTime_checkbox._variable.set(self.config.get("settings", "productReviewInvitationPrefferedSendTimeCheckBox"))

        self.productReviewInvitationPrefferedSendTime_entry = customtkinter.CTkEntry(master=self.settings_box_frame, placeholder_text="Product Review Invitation Preffered Send Time")
        self.productReviewInvitationPrefferedSendTime_entry.grid(row=16, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        self.productReviewInvitationPrefferedSendTime_entry.insert(0, self.config.get("settings", "productReviewInvitationPrefferedSendTime"))

        self.build_payload()

    def event_callback(self,str:str,**kwargs):

        self.configparser.set_config(self)

        # if str == "generate email":
        #     self.build_payload()

        # if str == "send email":
        #     self.build_payload()

        print(f"Event:{str}")
        print(f"kwargs:{kwargs}")

    def build_payload(self):

        self.payload_type = self.get_payload_type()
        self.payload = PayloadBuilder(self.payload_type,self.config, **self.config).build()
        self.email_body.delete(0.0, "end")
        self.email_body.insert(0.0, self.generate_html(self.payload))

    def update_config(self):

        self.configparser.set_config(self)

    def get_payload_type(self):

        if self.combobox_var.get() == "Service Review":
            return PayloadType.SERVICE_REVIEW
        if self.combobox_var.get() == "Service & Product review using SKU":
            return PayloadType.SERVICE_AND_PRODUCT_REVIEW_SKU
        if self.combobox_var.get() == "Service & Product Review(add/update Product Review)":
            return PayloadType.SERVICE_AND_PRODUCT_REVIEW

    def generate_html(self, payload):
        # TODO: Implement actual payload generation and rendering here.
        sds = json.dumps(payload, indent=1)
        html = f"""<html>\n<head>\n<script type='application/json+trustpilot'>{sds}</script>\n</head>\n<body>\n<p>Hi!<br>\nHow are you?<br>\n</p>\n</body>\n</html>"""
         
        return html

    def copy_link_callback(self):
        self.clipboard_clear()
        self.clipboard_append(self.link.get())
        self.update()


