
import customtkinter

class Email_frame(customtkinter.CTkFrame):

    def __init__(self,parent):

        super().__init__(parent)

        # Column 1: Email content
        self.email_box_frame = customtkinter.CTkFrame(master=parent,corner_radius=parent.frame_corner_radius,fg_color="transparent") 
        self.email_box_frame.grid(row=0, column=1, sticky="nsew")  
        self.email_box_frame.grid_rowconfigure((0), weight=1)
        self.email_box_frame.grid_columnconfigure((0), weight=1)

        # Frame for email body
        self.email_body_frame = customtkinter.CTkFrame(master=self.email_box_frame,corner_radius=parent.frame_corner_radius,fg_color="transparent")
        self.email_body_frame.grid(row=0, column=0, padx=parent.frame_padx, pady=parent.frame_pady, sticky="nsew")
        self.email_body_frame.grid_rowconfigure((0), weight=1)
        self.email_body_frame.grid_columnconfigure((0), weight=1)

        # Email body text box
        self.email_body = customtkinter.CTkTextbox(master=self.email_body_frame,corner_radius=parent.frame_corner_radius)
        self.email_body.grid(row=0, column=0, sticky="ewsn")

      
        

        