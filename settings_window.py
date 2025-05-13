import customtkinter

class settingsWindow(customtkinter.CTkToplevel):
    def __init__(self,main,**kwargs):
        super().__init__()
        self.geometry("400x450")

        self.element_padx = 8
        self.element_pady = 8

        self.mainFrame = main

        self.font = customtkinter.CTkFont(family="roboto", size=12, weight="bold")
        self.header_font = customtkinter.CTkFont(family="roboto", size=16, weight="bold")
        self.title("Settings")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tab_view = TabView(master=self,width=400,height=450,**kwargs)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20,sticky="news")

        self.attributes("-topmost",True) 

        self.protocol("WM_DELETE_WINDOW", self.close_window)

    def close_window(self):
        self.mainFrame.close_settings_callback() # Close the settings window when the main window is closed.
        self.destroy()

    def _get(self)-> dict: 
        """
        Retrieve all the values from the entry boxes and return them as a dictionary.
        """
        entryBoxes:dict = {
            "smtp_sender_email":self.tab_view.smtp_sender_email_Entry.get(), 
            "smtp_server":self.tab_view.smtp_server_Entry.get(), 
            "smtp_port":self.tab_view.smtp_port_Entry.get(),
            "smtp_password":self.tab_view.smtp_password_Entry.get()
        }

        return entryBoxes
    
class TabView(customtkinter.CTkTabview):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # create tabs
        smtp_tab_frame = self.add("SMTP") # Get the frame when adding
        varius_tab_frame = self.add("Varius settings")

        # --- Configure grid inside the SMTP Tab Frame ---
        smtp_tab_frame.grid_columnconfigure(0, weight=1)
       
        # --- Add widgets to SMTP tab ---
        self.sender_email_label = customtkinter.CTkLabel(master=smtp_tab_frame, text="Sender email:", fg_color="transparent", font=master.font)
        self.sender_email_label.grid(row=0, column=0, padx=master.element_padx, pady=master.element_pady, sticky="wn")

        self.smtp_sender_email_Entry = customtkinter.CTkEntry(master=smtp_tab_frame, placeholder_text="Sender email")
        self.smtp_sender_email_Entry.grid(row=1, column=0, padx=master.element_padx, pady=master.element_pady, sticky="ewn")
        # self.smtp_sender_email_Entry.insert(0,kwargs.get("smtp_sender_email"))

        self.smtp_server = customtkinter.CTkLabel(master=smtp_tab_frame, text="smtp_server:", fg_color="transparent", font=master.font)
        self.smtp_server.grid(row=2, column=0, padx=master.element_padx, pady=master.element_pady, sticky="wn")
        # self.smtp_sender_email_Entry.insert(0,kwargs.get("smtp_server"))

        self.smtp_server_Entry = customtkinter.CTkEntry(master=smtp_tab_frame, placeholder_text="smtp_server")
        self.smtp_server_Entry.grid(row=3, column=0, padx=master.element_padx, pady=master.element_pady, sticky="ewn")

        self.smtp_port = customtkinter.CTkLabel(master=smtp_tab_frame, text="smtp_port:", fg_color="transparent", font=master.font)
        self.smtp_port.grid(row=4, column=0, padx=master.element_padx, pady=master.element_pady, sticky="wn")
        
        self.smtp_port_Entry = customtkinter.CTkEntry(master=smtp_tab_frame, placeholder_text="smtp_port")
        self.smtp_port_Entry.grid(row=5, column=0, padx=master.element_padx, pady=master.element_pady, sticky="ewn")

        self.smtp_password_label = customtkinter.CTkLabel(master=smtp_tab_frame, text="smtp_password:", fg_color="transparent", font=master.font)
        self.smtp_password_label.grid(row=6, column=0, padx=master.element_padx, pady=master.element_pady, sticky="wn")

        self.smtp_password_Entry = customtkinter.CTkEntry(master=smtp_tab_frame, placeholder_text="smtp_password")
        self.smtp_password_Entry.grid(row=7, column=0, padx=master.element_padx, pady=master.element_pady, sticky="ewn")

    def _set(self,**kwargs):

        for k,v in kwargs.items():

            if k == "smtp_sender_email":
                getattr(self, f"{k}_Entry").delete(0, "end")
                getattr(self, f"{k}_Entry").insert(0, v)

            if k == "smtp_server":
                getattr(self, f"{k}_Entry").delete(0, "end")
                getattr(self, f"{k}_Entry").insert(0, v)

            if k == "smtp_port":
                getattr(self, f"{k}_Entry").delete(0, "end")
                getattr(self, f"{k}_Entry").insert(0, v)

            if k == "smtp_password":
                getattr(self, f"{k}_Entry").delete(0, "end")
                getattr(self, f"{k}_Entry").insert(0, v)

        

    


