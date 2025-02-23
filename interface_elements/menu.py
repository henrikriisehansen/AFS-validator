
import customtkinter

class Menu(customtkinter.CTkFrame):


    def __init__(self,parent):
        
        super().__init__(parent)
        
         # Column 0: Email settings
        self.set_email_frame = customtkinter.CTkFrame(master=parent,corner_radius=parent.frame_corner_radius,fg_color="transparent")
        self.set_email_frame.grid(row=0, column=0, sticky="news")
        self.set_email_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.set_email_frame.grid_columnconfigure((0), weight=1)

        # Email entry frame
        self.set_email_frame_entry = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=parent.frame_corner_radius,fg_color="transparent")
        self.set_email_frame_entry.grid(row=0, column=0, padx=parent.frame_padx, pady=parent.frame_pady, sticky="news")
        self.set_email_frame_entry.grid_rowconfigure((0), weight=1)
        self.set_email_frame_entry.grid_columnconfigure((0), weight=1)

        # Inner frame for email entry
        self.email_frame_entry_inner_frame = customtkinter.CTkFrame(master=self.set_email_frame_entry,corner_radius=parent.frame_corner_radius)
        self.email_frame_entry_inner_frame.grid(row=0, column=0, sticky="new")
        self.email_frame_entry_inner_frame.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.email_frame_entry_inner_frame.grid_columnconfigure((0), weight=1)

        # AFS email label and entry
        self.afs_email_label = customtkinter.CTkLabel(master=self.email_frame_entry_inner_frame, text="AFS email:", fg_color="transparent", font=parent.font)
        self.afs_email_label.grid(row=0, column=0,  padx=parent.frame_padx, pady=parent.frame_pady, sticky="ws")

        self.afs_email_Entry = customtkinter.CTkEntry(master=self.email_frame_entry_inner_frame, placeholder_text="AFS email")
        self.afs_email_Entry.grid(row=1, column=0, padx=parent.frame_padx, pady=parent.frame_pady, sticky="ewn")
        self.afs_email_Entry.insert(0, parent.data_config['afs_email'])
        parent.widget_elements["afs_email"] = self.afs_email_Entry

        # Invitation type combobox
        self.combobox_label = customtkinter.CTkLabel(master=self.email_frame_entry_inner_frame, text="Select invitation type:", fg_color="transparent", font=parent.font)
        self.combobox_label.grid(row=2, column=0, padx=parent.frame_padx, pady=parent.frame_pady, sticky="ws")

        self.combobox_var = customtkinter.StringVar(value="Service Review")
        self.combobox = customtkinter.CTkComboBox(master=self.email_frame_entry_inner_frame, values=["Service review", "Service & Product review using SKU", "Service & Product Review(add/update Product Review)"],
                                                  command=lambda x :parent.event_callback(**{"state":self.combobox.get()}), variable=self.combobox_var)
        self.combobox.grid(row=3, column=0, padx=parent.frame_padx, pady=parent.frame_pady, sticky="ewn")
        self.combobox.set(parent.data_config["invitation_type"])
        parent.widget_elements["invitation_type"] = self.combobox
        

        # Buttons frame
        self.set_email_frame_buttons = customtkinter.CTkFrame(master=self.set_email_frame,corner_radius=parent.frame_corner_radius,fg_color="transparent",bg_color="transparent")
        self.set_email_frame_buttons.grid(row=2, column=0, padx=parent.frame_padx, pady=parent.frame_pady, sticky="sewn")
        self.set_email_frame_buttons.grid_rowconfigure((0), weight=1)
        self.set_email_frame_buttons.grid_columnconfigure((0), weight=1)

        # Inner frame for buttons
        self.email_frame_buttons_inner_frame = customtkinter.CTkFrame(master=self.set_email_frame_buttons,corner_radius=parent.frame_corner_radius)
        self.email_frame_buttons_inner_frame.grid(row=0, column=0, sticky="sew")
        self.email_frame_buttons_inner_frame.grid_rowconfigure((0,1), weight=1)
        self.email_frame_buttons_inner_frame.grid_columnconfigure((0), weight=1)

        #Generate and send email buttons
        self.settings = customtkinter.CTkButton(master= self.email_frame_buttons_inner_frame, text="Settings", command=lambda:parent.open_settings_callback())
        self.settings.grid(row=0, column=0, padx=parent.element_padx, pady=parent.element_pady, sticky="ew")

        self.send_email = customtkinter.CTkButton(master= self.email_frame_buttons_inner_frame, text="Send Email", command=lambda:parent.event_callback(**{"send email":True}))
        self.send_email.grid(row=1, column=0, padx=parent.element_padx, pady=parent.element_pady, sticky="ew")

        