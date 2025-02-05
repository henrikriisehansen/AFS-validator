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

    def __init__(self, payload_type:Enum,payloadKeyMapping:dict,**kwargs):
        
        self.base_payload = BasePayload(payloadKeyMapping,**kwargs)
       
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
        "sku": kwargs.get("sku_entry"),
        "gtin": "1234567890",
        "mpn": "7TX1641",
        "brand": "Acme",
        "productCategoryGoogleId": "1253"
        
        }]

class Product_review_sku_payload:
    def __init__(self,**kwargs):
        self.productSkus = str(kwargs.get('sku_entry',None)).split(",")

class BasePayload:
    def __init__(self,payloadKeyMapping:dict,**kwargs):


        # print(payloadKeyMapping.items())
        for key, value in kwargs.items():

            if key in payloadKeyMapping and value == 'on':

                entryValue:str = kwargs.get(str(key).replace('checkbox', 'entry'))

                if (key == 'preffered_send_time_checkbox' or key == 'product_review_invitation_preffered_sendtime_checkbox') and len(entryValue) <= 7:

                    entryValue = HelperFunctions(entryValue).get_preferred_send_time()
                    
                setattr(self, payloadKeyMapping[key], entryValue)
             

class HelperFunctions:

    def __init__(self,days):
        self.prefferedSendTime = days

    def get_preferred_send_time(self):
        """Calculates the preferred send time."""

        current_date = datetime.now()
        preferred_date = current_date + timedelta(days=int(self.prefferedSendTime))
        return preferred_date.isoformat(timespec="seconds")
    