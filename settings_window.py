import customtkinter

class settingsWindow(customtkinter.CTkToplevel):
    def __init__(self,main, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x400")

        self.element_padx = 8
        self.element_pady = 8

        self.mainFrame = main

        self.font = customtkinter.CTkFont(family="roboto", size=12, weight="bold")
        self.header_font = customtkinter.CTkFont(family="roboto", size=16, weight="bold")
        self.title("Settings")
        self.grid_columnconfigure((0), weight=1)
        self.grid_rowconfigure((0), weight=1)

        self.smtp_label = customtkinter.CTkLabel(master=self, text="SMTP:", fg_color="transparent", font=self.header_font)
        self.smtp_label.grid(row=0, column=0, padx=self.element_padx, sticky="wn")

        self.sender_email_label = customtkinter.CTkLabel(master=self, text="Sender email:", fg_color="transparent", font=self.font)
        self.sender_email_label.grid(row=1, column=0, padx=self.element_padx, sticky="wn")

        self.smtp_sender_email_Entry = customtkinter.CTkEntry(master=self, placeholder_text="Sender email")
        self.smtp_sender_email_Entry.grid(row=2, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        
        self.smtp_server = customtkinter.CTkLabel(master=self, text="smtp_server:", fg_color="transparent", font=self.font)
        self.smtp_server.grid(row=3, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.smtp_server_Entry = customtkinter.CTkEntry(master=self, placeholder_text="smtp_server")
        self.smtp_server_Entry.grid(row=4, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")
        
        self.smtp_port = customtkinter.CTkLabel(master=self, text="smtp_port:", fg_color="transparent", font=self.font)
        self.smtp_port.grid(row=5, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")
        
        self.smtp_port_Entry = customtkinter.CTkEntry(master=self, placeholder_text="smtp_port")
        self.smtp_port_Entry.grid(row=6, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")

        self.smtp_password_label = customtkinter.CTkLabel(master=self, text="smtp_password:", fg_color="transparent", font=self.font)
        self.smtp_password_label.grid(row=7, column=0, padx=self.element_padx, pady=self.element_pady, sticky="wn")

        self.smtp_password_Entry = customtkinter.CTkEntry(master=self, placeholder_text="smtp_password")
        self.smtp_password_Entry.grid(row=8, column=0, padx=self.element_padx, pady=self.element_pady, sticky="ewn")

        self.attributes("-topmost",True) 

        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        self.mainFrame.close_settings_callback() # Close the settings window when the main window is closed.
        self.destroy()

    def _get(self): 
        """
        Retrieve all the values from the entry boxes and return them as a dictionary.
        """
        entryBoxes:dict = {
            "smtp_sender_email":self.smtp_sender_email_Entry, 
            "smtp_server":self.smtp_server_Entry, 
            "smtp_port":self.smtp_port_Entry,
            "smtp_password":self.smtp_password_Entry
        }

        return entryBoxes
    
   
    def _set(self, **kwargs):

        """
        Set the values in the entry boxes from the given dictionary.
        """
        for key, value in kwargs.items():
            if key in ["smtp_sender_email", "smtp_server", "smtp_port", "smtp_password"]:

                getattr(self, f"{key}_Entry").delete(0, "end")
                getattr(self, f"{key}_Entry").insert(0, value)

    


