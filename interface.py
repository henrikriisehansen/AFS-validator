import random
import string
import customtkinter
import json
import os
import re
import webbrowser
from pprint import pformat

BaseUrl = "https://www.trustpilot.com/evaluate-bgl/"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("AFS")
        self.geometry("1000x680")
        self.font  = customtkinter.CTkFont(family="roboto", size=13, weight="bold")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

        self.reciepent_email_label = customtkinter.CTkLabel(self, text="Recienpent email:", fg_color="transparent",font=self.font)
        self.reciepent_email_label.grid(row=0, column=0, padx=20, pady=5, sticky="ws")

        self.reciepent_email_Entry = customtkinter.CTkEntry(self, placeholder_text="Recienpent email")
        self.reciepent_email_Entry.grid(row=1, column=0, padx=20, pady=5, sticky="ewn")

        self.afs_email_label = customtkinter.CTkLabel(self, text="AFS email:", fg_color="transparent",font=self.font)
        self.afs_email_label.grid(row=2, column=0, padx=20, pady=5, sticky="ws")

        self.domain_Entry = customtkinter.CTkEntry(self, placeholder_text="AFS email")
        self.domain_Entry.grid(row=3, column=0, padx=20, pady=5, sticky="ewn")

        self.combobox_var = customtkinter.StringVar(value="Service Review")
        self.combobox = customtkinter.CTkComboBox(self, values=["Service Review", "Service & Product review using SKU","Service & Product Review(add/update Product Review)" ],
                                     command=self.combobox_callback, variable=self.combobox_var)
        self.combobox_var.set("Service Review")
        self.combobox.grid(row=4, column=0, padx=20, pady=5, sticky="ewn")
        
    def combobox_callback(self,choice):
        print("combobox dropdown clicked:", choice)
        
    def random_string(self):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    
    def copy_link_callback(self):

        self.clipboard_clear()
        self.clipboard_append(self.link.get())
        self.update()

    def is_base64(self,string):
        pattern = re.compile(r'^[A-Za-z0-9+/]+={0,2}$')
        return bool(pattern.fullmatch(string))
    
    def link_btn_clicked(self):
        webbrowser.open_new(f"{self.link.get()}")
