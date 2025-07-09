import customtkinter
from jsonschema import validate, Draft7Validator
from jsonschema.exceptions import ValidationError
import json

class ValidateJSON(customtkinter.CTkToplevel):
    def __init__(self,parent, **kwargs):
        super().__init__()

        self.geometry("800x600")

        self.parent = parent

        self.font = customtkinter.CTkFont(family="roboto", size=12, weight="bold")
        self.header_font = customtkinter.CTkFont(family="roboto", size=12, weight="bold")
        self.title("Validate JSON")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.attributes("-topmost",True) 
        self.protocol("WM_DELETE_WINDOW", self.close_window)

        self.frame = customtkinter.CTkFrame(master=self,fg_color="transparent")
        self.frame.grid(row=0, column=0, sticky="nsew")
        self.frame.grid_columnconfigure((0,1), weight=1)
        self.frame.grid_rowconfigure((0), weight=1)

        # leftFrame
        self.leftFrame = customtkinter.CTkFrame(master=self.frame,corner_radius=parent.frame_corner_radius,fg_color="transparent")
        self.leftFrame.grid(row=0, column=0,sticky="nsew")
        self.leftFrame.grid_columnconfigure((0), weight=1)
        self.leftFrame.grid_rowconfigure((0), weight=1)

        self.leftInnerFrame = customtkinter.CTkFrame(master=self.leftFrame,corner_radius=parent.frame_corner_radius)
        self.leftInnerFrame.grid(row=0, column=0,padx=parent.element_padx,pady=parent.element_pady,sticky="new")
        self.leftInnerFrame.grid_columnconfigure((0), weight=1)
        self.leftInnerFrame.grid_rowconfigure((0,1,2), weight=1)

        self.label = customtkinter.CTkLabel(master=self.leftInnerFrame, text="JSON Data", font=self.header_font)
        self.label.grid(row=0, column=0,sticky="nw",padx=parent.element_padx,pady=parent.element_pady)

        self.textBox = customtkinter.CTkTextbox(master=self.leftInnerFrame,corner_radius=parent.frame_corner_radius,height=490)
        self.textBox.grid(row=1, column=0,padx=parent.element_padx,pady=2,sticky="nsew")

        self.validateJSONButton = customtkinter.CTkButton(
            master=self.leftInnerFrame,
            text="Validate JSON",
            command=lambda:self.validateJSON(self.textBox.get("0.0", "end-1c"))
           )
        self.validateJSONButton.grid(row=2, column=0,sticky="new",padx=parent.element_padx,pady=parent.element_pady)

        # rightFrame
        self.rightFrame = customtkinter.CTkFrame(master=self.frame,corner_radius=parent.frame_corner_radius,fg_color="transparent")
        self.rightFrame.grid(row=0, column=1,sticky="nsew")
        self.rightFrame.grid_columnconfigure((0), weight=1)
        self.rightFrame.grid_rowconfigure((0), weight=1)  

        self.rightInnerFrame = customtkinter.CTkFrame(master=self.rightFrame,corner_radius=parent.frame_corner_radius)
        self.rightInnerFrame.grid(row=0, column=0,padx=parent.element_padx,pady=parent.element_pady,sticky="new")
        self.rightInnerFrame.grid_columnconfigure((0), weight=1)
        self.rightInnerFrame.grid_rowconfigure((0,1), weight=1)

        self.validationLabel = customtkinter.CTkLabel(master=self.rightInnerFrame, text="Validation Result", font=self.header_font)
        self.validationLabel.grid(row=0, column=0,sticky="nw",padx=parent.element_padx,pady=2)
       
        self.validationTextBox = customtkinter.CTkTextbox(master=self.rightInnerFrame,corner_radius=parent.frame_corner_radius,height=550)
        self.validationTextBox.grid(row=1, column=0,padx=parent.element_padx,pady=parent.element_pady,sticky="nsew")
        
    def close_window(self):
        self.parent.close_validateJSON_callback() # Close the settings window when the main window is closed.
        self.destroy()

    def _display_message_in_output_area(self, message: str, is_error: bool = False):
        """Helper to display messages or data in the right-hand output textbox."""
        self.validationTextBox.configure(state="normal") # Enable to modify
        self.validationTextBox.delete("0.0", "end")
        self.validationTextBox.insert("0.0", message)

        print(f"Displaying message: {message}")  # Debugging output
        if is_error:
            self.validationTextBox.configure(text_color="red")
        else:
           self.validationTextBox.configure(text_color="green")
           

    def validateJSON(self,jsonData):

        if not isinstance(jsonData, str) or not jsonData.strip():
            self.updateTextValidation("No JSON data provided.")
            return

        try:
            data = json.loads(jsonData)
        except json.JSONDecodeError as e:
            # --- Build a user-friendly, visual error message ---
            
            # 1. Split the document into lines
            lines = e.doc.splitlines()
            
            # 2. Get the line where the error occurred
            # Ensure the line number is valid before accessing the list
            error_line_index = e.lineno - 1
            if 0 <= error_line_index < len(lines):
                error_line = lines[error_line_index]
                
                # 3. Create a pointer string to place a '^' under the error column
                # (e.colno - 1) creates the correct number of spaces
                pointer = ' ' * (e.colno - 1) + '^'
                
                # 4. Format the final message
                # The > helps delineate the code snippet
                error_message = (
                    f"JSON Formatting Error: {e.msg}\n\n"
                    f"Error found at line {e.lineno}, column {e.colno}:\n"
                    f"> {error_line}\n"
                    f"> {pointer}\n"
                )
                self._display_message_in_output_area(error_message, is_error=True)
            else:
                # Fallback for rare cases where line number is out of sync
                error_message = f"JSON Error: {e}"

                self._display_message_in_output_area(error_message, is_error=True)

            return
        # If the JSON is valid, proceed with schema validation
        # --- JSON Schema Validation ---
        #Define the JSON schema
        schema = {
            "type": "object",
            "properties": {
                "recipientEmail": {"type": "string", "format": "email"},
                "recipientName": {"type": "string", "minLength": 1},
                "referenceId": {"type": "string", "minLength": 1},
                "templateId": {"type": "string", "minLength": 1},
                "productReviewInvitationTemplateId": {"type": "string"},
                "locale": {"type": "string", "pattern": "^[a-z]{2}(-[A-Z]{2})?$"},
                "senderEmail": {"type": "string", "format": "email"},
                "senderName": {"type": "string", "minLength": 1},
                "replyTo": {"type": "string", "format": "email"},
                "preferredSendTime": {"type": "string", "format": "date-time"},
                "productReviewInvitationPreferredSendTime": {"type": "string", "format": "date-time"},
                "locationId": {"type": "string", "minLength": 1},
                "tags": {
                    "type": "array",
                    "items": {"type": "string"}
                },
                "products": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "productUrl": {"type": "string", "format": "uri"},
                            "imageUrl": {"type": "string", "format": "uri"},
                            "name": {"type": "string", "minLength": 1},
                            "sku": {"type": "string"},
                            "gtin": {"type": "string", "pattern": "^[0-9]+$"},
                            "mpn": {"type": "string"},
                            "brand": {"type": "string"},
                            "productCategoryGoogleId": {"type": "string", "pattern": "^[0-9]+$"}
                        },
                        "required": ["productUrl","imageUrl","name","sku"],
                        "additionalProperties": False
                    }
                },
                "productSkus": {
                    "type": "array",
                    "items": {"type": "string"},
                    "additionalProperties": False
                }
            },
            "required": [
                "recipientEmail",
                "recipientName",
                "referenceId"
            ],
            "additionalProperties": False
        }

        # Validate the JSON data against the schema
        try:
            validate(instance=data, schema=schema)
        except ValidationError as e:
            error_path_str = " -> ".join(map(str, e.path))
            # Attempt to get the problematic value if path is not empty
            problematic_value = e.instance
            if e.path: # If the error is within a nested structure
                temp_data = data
                try:
                    for key in e.path:
                        temp_data = temp_data[key]
                    problematic_value = temp_data
                except (KeyError, TypeError): # Path might point to a missing key or non-subscriptable item
                    problematic_value = "<value not directly accessible or missing>"


            highlighted_error = (
                f"Validation Error:\n"
                f"  Message: {e.message}\n"
                f"  Path in data: {error_path_str or 'root'}\n"
                f"  Problematic Value: '{problematic_value}' (type: {type(problematic_value).__name__})\n"
                f"  Failed on validator: '{e.validator}' with value '{e.validator_value}'\n"
                f"  Schema path: {list(e.schema_path)}"
            )


        validator = Draft7Validator(schema)
        errors = validator.iter_errors(data)

        error_messages = []
        for error in sorted(errors, key=lambda e: e.path): # Sort errors for consistent output
            error_path_str = " -> ".join(map(str, error.path))
            problematic_value = error.instance # The instance fragment that caused the error

            # To get the specific key and its value for object properties:
            key_value_info = ""
            if error.path and isinstance(error.absolute_path, (list, tuple)) and len(error.absolute_path) > 0:
                key_name = error.path[-1] # Last element in the path is usually the key
                parent_path = list(error.absolute_path)[:-1]
                parent_data = data
                try:
                    for p_key in parent_path:
                        parent_data = parent_data[p_key]
                    if isinstance(parent_data, dict) and key_name in parent_data:
                        key_value_info = f"  Key: '{key_name}', Value: '{parent_data[key_name]}'"
                    elif isinstance(parent_data, list) and isinstance(key_name, int) and key_name < len(parent_data):
                        key_value_info = f"  Index: {key_name}, Value: '{parent_data[key_name]}'"
                    else: # This handles cases like 'required' where the key itself is missing
                        key_value_info = f"  Concerning Key/Item: '{key_name}' (value might be missing or path points to structure)"
                except (KeyError, TypeError, IndexError):
                    key_value_info = f"  Concerning Key/Item: '{key_name}' (error accessing parent data)"


            highlighted_error = (
                f"Error: {error.message}\n"
                f"  Path: {error_path_str or 'root'}\n"
                f"{key_value_info}\n"
                f"  Problematic instance part: '{error.instance}'\n"
                f"  Validator: '{error.validator}', Expected: '{error.validator_value}'"

            )
            error_messages.append(highlighted_error)

        if error_messages:
            text:list = []
            text.append("Found validation errors:\n")
            for msg in error_messages:
                text.append(msg + "\n" + "-"*30)

            self._display_message_in_output_area(message="\n".join(text), is_error=True)
        else:
            self._display_message_in_output_area(message="Validation successful!")
            self.validationTextBox.configure(text_color="green")
            


       
       

