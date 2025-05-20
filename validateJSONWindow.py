import customtkinter
from jsonschema import validate
from jsonschema.exceptions import ValidationError

class ValidateJSON(customtkinter.CTkToplevel):
    def __init__(self,parent, **kwargs):
        super().__init__()

        self.geometry("800x600")

        self.parent = parent

        self.font = customtkinter.CTkFont(family="roboto", size=12, weight="bold")
        self.header_font = customtkinter.CTkFont(family="roboto", size=16, weight="bold")
        self.title("Validate JSON")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.attributes("-topmost",True) 
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.frame = customtkinter.CTkFrame(master=self,fg_color="transparent")
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure((0,1), weight=1)
        self.frame.grid_rowconfigure((0), weight=1)

        self.leftFrame = customtkinter.CTkFrame(master=self.frame,corner_radius=parent.frame_corner_radius)
        self.leftFrame.grid(row=0, column=0,padx=parent.element_padx,pady=parent.element_pady,sticky="nsew")
        self.leftFrame.grid_columnconfigure((0), weight=1)
        self.leftFrame.grid_rowconfigure((0), weight=1)


        self.rightFrame = customtkinter.CTkFrame(master=self.frame,corner_radius=parent.frame_corner_radius)
        self.rightFrame.grid(row=0, column=1,padx=parent.element_padx,pady=parent.element_pady,sticky="nsew")

        self.validateJSONButton = customtkinter.CTkButton(
            master=self.leftFrame,
            text="Validate JSON",
            font=self.font)
        self.validateJSONButton.grid(row=0, column=0,sticky="nsew",padx=parent.element_padx,pady=parent.element_pady)
        
    def close_window(self):
        self.parent.close_validateJSON_callback() # Close the settings window when the main window is closed.
        self.destroy()


    def validateJSON(self,jsonData):

        studentSchema = {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "rollnumber": {"type": "number"},
                "marks": {"type": "number"},
            },
        }

        try:
            validate(instance=jsonData, schema=studentSchema)
        except ValidationError as err:
            return False
       

