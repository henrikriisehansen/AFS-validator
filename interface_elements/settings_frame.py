import customtkinter

class Settings_frame(customtkinter.CTkFrame):

    def __init__(self,parent):
        
        """Construct a new Settings frame with the given parent"""
     
        super().__init__(parent)

        self.container = customtkinter.CTkFrame(master=parent,corner_radius=parent.frame_corner_radius,fg_color="transparent")
        self.container.grid(row=0, column=2, sticky="news")
        self.container.grid_rowconfigure((0), weight=1)
        self.container.grid_columnconfigure((0), weight=1)

        # Scrollable frame for settings
        self.settings_box_frame = customtkinter.CTkScrollableFrame(master=self.container,corner_radius=parent.frame_corner_radius)
        self.settings_box_frame.grid(row=0, column=0, padx=parent.frame_padx, pady=parent.frame_pady, sticky="news")
        self.settings_box_frame.grid_rowconfigure((0), weight=1)
        self.settings_box_frame.grid_columnconfigure((0), weight=1)

        # Dictionary to store dynamically created frames
        self.frames = {}

       # loop through all the frames 
        for i,(key, value) in enumerate(parent.data_settings.items()):

            index = i * 2

            if value['type'] == 'combobox':
                frame = ComboBox(self.settings_box_frame,parent,index,**value)
        
            if value['type'] == 'entry':
                frame = Entry(self.settings_box_frame,parent,index,**value)
            
            self.frames[key] = frame
            
          
class ComboBox(customtkinter.CTkFrame):
     
    def __init__(self,parent,controller,index,**kwargs):
         
        customtkinter.CTkFrame.__init__(self,parent)

        self.checkbox_var = customtkinter.StringVar(value=kwargs.get('checkbox_value'))

        self.checkBox = customtkinter.CTkCheckBox(
                master=parent,text=kwargs.get('label'),
                variable=self.checkbox_var,
                onvalue='on',
                offvalue='off')
        self.checkBox.grid(row=index, column=0,pady=8,sticky="wn")

        self.combobox_var = customtkinter.StringVar(value=kwargs.get('value'))

        self.combobox = customtkinter.CTkComboBox(
            master=parent, 
            values=[k for (k,v) in getattr(controller,kwargs.get('data')).items() if v is not None],
            variable=self.combobox_var)
        
        self.combobox.grid(row=index+1, column=0, pady=8, sticky="ewn")

        self.checkBox._command = lambda x=self.checkBox:controller.event_callback(**{"state":x.get(),"entry":self.combobox})
        self.combobox._command = lambda y=self.combobox:controller.event_callback(**{"state":"","entry":""})

        self.value = self.combobox._variable


class Entry(customtkinter.CTkFrame):

    def __init__(self,parent,controller,index,**kwargs):
            
            customtkinter.CTkFrame.__init__(self,parent)

            self.checkbox_var = customtkinter.StringVar(value=kwargs.get('checkbox_value'))

            self.checkBox = customtkinter.CTkCheckBox(
                 master=parent,text=kwargs.get('label'),
                 variable=self.checkbox_var,
                 onvalue='on',
                 offvalue='off')
            self.checkBox.grid(row=index, column=0,pady=8,sticky="wn")

            self.entry_var = customtkinter.StringVar(value=kwargs.get('value'))

            self.entry = customtkinter.CTkEntry(master=parent, textvariable=self.entry_var)
            self.entry.grid(row=index+1, column=0,pady=8, sticky="ewn")

            self.checkBox._command = lambda x=self.checkBox:controller.event_callback(**{"state":x.get(),"entry":self.entry})

            self.value = self.entry._textvariable


