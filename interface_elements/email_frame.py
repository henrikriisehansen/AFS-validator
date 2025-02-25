
import customtkinter

class Email_frame(customtkinter.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        self = parent

        # Column 1: Email content
        self.email_box_frame = customtkinter.CTkFrame(master=parent,corner_radius=self.frame_corner_radius,fg_color="transparent") 
        self.email_box_frame.grid(row=0, column=1, sticky="nsew")  
        self.email_box_frame.grid_rowconfigure((0, 1), weight=1)
        self.email_box_frame.grid_columnconfigure((0), weight=1)

        # Upper frame for email content
        self.email_box_upper_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=self.frame_corner_radius)
        self.email_box_upper_frame.grid(row=0, column=0, padx=self.frame_padx, pady=self.frame_pady, sticky="new")
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

        self.subject = customtkinter.CTkEntry(master=self.email_box_inner_upper_frame, textvariable=customtkinter.StringVar(value=self.data_config["email_subject"]), state="disabled")
        self.subject.grid(row=1, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.widget_elements["subject"] = self.subject

        self.to_email_entry_label = customtkinter.CTkLabel(master=self.email_box_inner_upper_frame, text="To Email:", fg_color="transparent", font=self.font)
        self.to_email_entry_label.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.to_email_entry = customtkinter.CTkEntry(master=self.email_box_inner_upper_frame, textvariable=customtkinter.StringVar(value=self.data_config['recipient_email_entry']), state="disabled")
        self.to_email_entry.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.widget_elements["to_email"] = self.to_email_entry

        self.BCC_email_entry_label = customtkinter.CTkLabel(master=self.email_box_inner_upper_frame, text="BCC Email:", fg_color="transparent", font=self.font)
        self.BCC_email_entry_label.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ws")

        self.BCC_email_entry = customtkinter.CTkEntry(master=self.email_box_inner_upper_frame,textvariable=customtkinter.StringVar(value=self.data_config['afs_email']), state="disabled")
        self.BCC_email_entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ew")
        self.widget_elements["afs_email"] = self.BCC_email_entry

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

        