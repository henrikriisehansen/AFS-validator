from datetime import datetime, timedelta
from enum import Enum
import random
import string

class PayloadType(Enum):
    SERVICE_REVIEW = "serviceReview"
    SERVICE_AND_PRODUCT_REVIEW = "serviceAndProductReview"
    SERVICE_AND_PRODUCT_REVIEW_SKU = "serviceAndProductReviewWithFollowUp"
        
class PayloadBuilder:
    """Builds the payload using composition."""

    def __init__(self, payload_type:Enum,payloadKeyMapping:dict,templates:dict,**kwargs):
        
        self.base_payload = BasePayload(payloadKeyMapping,templates,**kwargs)
       
        if payload_type == PayloadType.SERVICE_REVIEW:
            self.invitation = Service_review_payload(**kwargs)
        
        if payload_type == PayloadType.SERVICE_AND_PRODUCT_REVIEW:
            self.invitation = Product_review_payload(**kwargs)

        if payload_type == PayloadType.SERVICE_AND_PRODUCT_REVIEW_SKU:
            self.invitation = Product_review_sku_payload(**kwargs)

    def build(self):
        """Constructs the final payload."""

        if isinstance(self.invitation,Service_review_payload):
            payload = vars(self.base_payload)
           
        if isinstance(self.invitation, Product_review_payload):
            payload = vars(self.base_payload)
            payload.update(vars(self.invitation))
        
        if isinstance(self.invitation, Product_review_sku_payload):
            payload = vars(self.base_payload)
            payload.update(vars(self.invitation))

        
        return {k: v for k, v in payload.items() if v != None}

class Service_review_payload:
    def __init__(self,**kwargs):
       pass

class Product_review_payload:
    def __init__(self,**kwargs):
        self.products = [
            {

        "productUrl": "http://www.companystore.com/.../12345.htm",
        "imageUrl": "http://www.companystore.com/.../.../12345.jpg",
        "name": "Metal Toy Car",
        "sku": [v for v in kwargs.get("product_sku_entry").split(',') if v != ''],
        "gtin": "1234567890",
        "mpn": "7TX1641",
        "brand": "Acme",
        "productCategoryGoogleId": "1253"
        
        }]

class Product_review_sku_payload:
    def __init__(self,**kwargs):
        self.productSkus = [v for v in kwargs.get("product_sku_entry").split(',') if v != '']

class BasePayload:
    def __init__(self,payloadKeyMapping:dict,templates:dict,**kwargs):

        # parse payload key mapping
        preferred_keys:list = {'preffered_send_time_checkbox', 'product_review_invitation_preffered_sendtime_checkbox'}
        
        # filter payload items based on key mapping and value 'on'
        filteredPayloadItems = {k: v for k,v in kwargs.items() if k in payloadKeyMapping and v == 'on'}
        
        # initialize attributes based on payload key mapping and value from filtered items
        for key in filteredPayloadItems.keys():
            entry_key = key.replace('checkbox', 'entry')
            entryValue = kwargs.get(entry_key, '')

            # handle preferred send time
            if key in preferred_keys:
                entryValue = HelperFunctions(entryValue).get_preferred_send_time()

            # handle tags
            if key == 'tags_checkbox':
                entryValue = [v for v in entryValue.split(',') if v != '']

            # handle template
            if key == 'template_combobox_checkbox':
                entryValue = templates.get(entryValue, '')

            setattr(self, payloadKeyMapping[key], entryValue)



          
class HelperFunctions:

    def __init__(self,days:str):
        
        self.prefferedSendTime:str = days

    def get_preferred_send_time(self):
        """Calculates the preferred send time."""

        if self.prefferedSendTime == '':
            self.prefferedSendTime = '0'

        if len(str(self.prefferedSendTime)) > 7:
            self.prefferedSendTime = self.prefferedSendTime[:7]
        
        current_date = datetime.now()
        preferred_date = current_date + timedelta(days=int(self.prefferedSendTime))
        return preferred_date.isoformat(timespec="seconds")
    