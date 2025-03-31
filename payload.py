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

    def __init__(self, payload_type:Enum,templates:dict,**kwargs):
        
        self.base_payload = BasePayload(templates,**kwargs)
       
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

        "productUrl":kwargs.get("productUrl").get("value"),
        "imageUrl": kwargs.get("imageUrl").get("value"),
        "name": kwargs.get("name").get("value"),
        "sku": kwargs.get("sku").get("value"),
        "gtin": kwargs.get("gtin").get("value"),
        "mpn":kwargs.get("gtin").get("value"),
        "brand": kwargs.get("brand").get("value"),
        "productCategoryGoogleId": kwargs.get("productCategoryGoogleId").get("value")
        
        }]

class Product_review_sku_payload:
    def __init__(self,**kwargs):

        self.productSkus = [v for v in kwargs.get("productSkus")["value"].split(",") if v != ""]

class BasePayload:
    def __init__(self,templates:dict,**kwargs):

        basePayloadItems = [k for (k,v) in kwargs.items() if v["basePayload"]]

        filtered_payload = { k:v["value"] for k,v in kwargs.items() if v["checkbox_value"] == "on" and k in basePayloadItems}

        for key,value in filtered_payload.items():

            if key == "tags":
                value = [v for v in value.split(',') if v!= '']

            if key in ["preferredSendTime","productReviewInvitationPreferredSendTime"]:
                value = HelperFunctions(value).get_preferred_send_time()

            if key == "templateId":
                value = templates[value]
                
            setattr(self, key, value)

          
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
    