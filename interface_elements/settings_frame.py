import customtkinter

class Settings_frame(customtkinter.CTkFrame):

    def __init__(self,parent):

     
        super().__init__(parent)

        self = parent

        # Various settings checkboxes and entries

        self.checkboxes = {}  # Dictionary to store dynamically created checkboxes
        self.entryboxes = {} # Dictionary to store dynamically created entry boxes
        self.combobox_checkboxes = {} # Dictionary to store dynamically created checkboxes
        self.comboboxes = {} # Dictionary to store dynamically created comboboxes
        self.template_checkboxes = {} # Dictionary to store dynamically created template checkboxes
        self.template_combobox = {} # Dictionary to store dynamically created template entries

        for key, value in self.data_config.items():
        
            if "checkbox" in str(key) and "combobox" not in str(key):  
                checkbox_var = customtkinter.StringVar(value=value)
              
                self.checkboxes[key] = customtkinter.CTkCheckBox(
                    master=self.settings_box_frame, 
                    text = ' '.join(str(key).split('_')[:3]) if key == 'preffered_send_time_checkbox'
                    else ' '.join(str(key).split('_')[:5]) if key == 'product_review_invitation_preffered_sendtime_checkbox'
                    else ' '.join(str(key).split('_')[:2]),   
                    command=lambda k=key: self.event_callback(**{"state": self.checkboxes[k].get(),"entry": self.entryboxes[str(k).replace("checkbox", "entry")]}), 
                    variable=checkbox_var, 
                    onvalue="on", 
                    offvalue="off"
                )
                
                # Grid placement
                self.checkboxes[key].grid(row=list(self.data_config.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ws")
      
            if "entry" in str(key) and "combobox" not in str(key):
                entry_var = customtkinter.StringVar(value=value)

                # Store entry in a dictionary with key as the name
                self.entryboxes[key] = customtkinter.CTkEntry(
                    master=self.settings_box_frame, 
                    placeholder_text=str(key).replace("_", " "),
                    textvariable=entry_var
                )
                
                # Grid placement
                self.entryboxes[key].grid(row=list(self.data_config.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ewn")
                # check if entry is visible and update
                self.entryboxes[key].grid() if self.checkboxes[str(key).replace("entry","checkbox")].get() == 'on' else self.entryboxes[key].grid_remove()
            
            if "locale_combobox_checkbox" in str(key):
                checkbox_var = customtkinter.StringVar(value=value)
                
                

                # Store checkbox in a dictionary with key as the name
                self.combobox_checkboxes[key] = customtkinter.CTkCheckBox(
                    master=self.settings_box_frame, 
                    text=str(key).replace("_", " "), 
                    command=lambda k=key: self.event_callback(**{"state": self.combobox_checkboxes[k].get(),"entry":self.comboboxes[str(k).replace("checkbox", "entry")]}), 
                    variable=checkbox_var, 
                    onvalue="on", 
                    offvalue="off"
                )
                
                # Grid placement
                self.combobox_checkboxes[key].grid(row=list(self.data_config.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ws")


            if "locale_combobox_entry" in str(key):
                combobox_var = customtkinter.StringVar(value=value)

                # Store combobox in a dictionary with key as the name
                self.comboboxes[key] = customtkinter.CTkComboBox(
                    master=self.settings_box_frame, 
                    values=[k for (k,v) in self.data_locale.items() if v is not None], 
                    command=lambda k: self.event_callback(**{"state":None,"entry":None}), 
                    variable=combobox_var
                )
                
                # Grid placement
                self.comboboxes[key].grid(row=list(self.data_config.keys()).index(key), column=0, 
                                        padx=self.element_padx, pady=self.element_pady, sticky="ewn")
                
                # Set initial value
                self.comboboxes[key].set(value)

                # check if combobox is visible and update
                self.comboboxes[key].grid() if self.combobox_checkboxes[str(key).replace("entry","checkbox")].get() == 'on' else self.comboboxes[key].grid_remove()

            if "template_combobox_checkbox" in str(key):
                checkbox_var = customtkinter.StringVar(value=value)
                
                # Store checkbox in a dictionary with key as the name
                self.template_checkboxes[key] = customtkinter.CTkCheckBox(
                    master=self.settings_box_frame,
                    text=str(key).replace("_", " "),
                    command=lambda k=key: self.event_callback(**{"state": self.template_checkboxes[k].get(),"entry":self.template_combobox[str(k).replace("checkbox", "entry")]}),
                    variable=checkbox_var,
                    onvalue="on",
                    offvalue="off"
                )

                # Grid placement
                self.template_checkboxes[key].grid(row=list(self.data_config.keys()).index(key), column=0,
                                                    padx=self.element_padx, pady=self.element_pady, sticky="ws")
                
            if "template_combobox_entry" in str(key):
                
                combobox_var = customtkinter.StringVar(value=value)
                
                # Store combobox in a dictionary with key as the name
                self.template_combobox[key] = customtkinter.CTkComboBox(
                    master=self.settings_box_frame,
                    values=[x for x in self.data_templates.keys()],
                    command=lambda k: self.event_callback(**{"state":None,"entry":None}),
                    variable= combobox_var
                )

                # Grid placement
                self.template_combobox[key].grid(row=list(self.data_config.keys()).index(key), column=0,
                                                        padx=self.element_padx, pady=self.element_pady, sticky="ewn")
                # Set initial value
                self.template_combobox[key].set(value)
                # check if combobox is visible and update
                self.template_combobox[key].grid() if self.template_checkboxes[str(key).replace("entry","checkbox")].get() == 'on' else self.template_combobox[key].grid_remove()


        
