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

    def __init__(self, payload_type,**kwargs):
        
        self.base_payload = BasePayload(**kwargs)
       
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
        "sku": "ABC-1234",
        "gtin": "1234567890",
        "mpn": "7TX1641",
        "brand": "Acme",
        "productCategoryGoogleId": "1253"
        
        }]

class Product_review_sku_payload:
    def __init__(self,**kwargs):
        self.productSkus = [kwargs.get('sku',None)]

class BasePayload:
    def __init__(self, **kwargs):

        for key, value in kwargs.items():

            
            if value == 'on' and self.getPayloadItems(key) is not None:
                
                setattr(self, self.getPayloadItems(key), kwargs.get(str(key).replace('checkbox', 'entry')))
                

    def getPayloadItems(self,key):
        
        data:dict = {
             'recipient_email_checkbox': "recipientEmail",
                        'reference_id_checkbox': "referenceId",
                        'recipient_name_checkbox': "recipientName",
                        'preffered_sendtime_checkbox': "prefferedSendtimeServiceReview",
                        'locale_combobox_checkbox': "locale",
                        'productReviewTemplate': "productReviewTemplateId",
                        'prefferedSendTimeProductReview': "prefferedSendTimeProductReview",
                        'preffered_sendtime': "prefferedSendtimeServiceReview",
                        'preffered_sendtime_entry': "prefferedSendtimeServiceReview",
                        'locale_dropdown': "locale",
                        'template_dropdown': "templateId",
                        'productReviewTemplate_dropdown': "productReviewTemplateId",
                        'productReviewTemplate_entry': "productReviewTemplateId",
                        'tags': "tags",
                        'tags_entry': "tags",
                        'productReviewTemplate_entry': "productReviewTemplateId",
                        'productReviewTemplate_dropdown': "productReviewTemplateId",
                        'prefferedSendTimeProductReview_entry': "prefferedSendTimeProductReview"
            }
        return data.get(key) 
                       
                

       
 
      

        

    
       
       
    

    
       

   

    
    
                



        # self.replyTo = kwargs.get('replyTo',None) if kwargs.get('replyto') == 'on' else None
        # self.locale = kwargs.get('locale', None) if kwargs.get('locale_checkbox') == 'on' else None

        # self.locationId = kwargs.get('location_id',None) if kwargs.get('location_id_checkbox') == 'on' else None
        # self.senderName = kwargs.get('senderName',None)
        # self.senderEmail = kwargs.get('senderEmail',None)
        # self.referenceId = kwargs.get('reference_id',None) if kwargs.get('reference_id_checkbox') == 'on' else None
        # self.recipientName = kwargs.get('recipient_name',None) if kwargs.get('recipient_name_checkbox') == 'on' else None
        # self.recipientEmail = kwargs.get('recipient_email',None) if kwargs.get('recipient_email_checkbox') == 'on' else None
        # self.templateId = kwargs.get('template',None) if kwargs.get('template_checkbox') == 'on' else None
        # self.prefferedSendtimeServiceReview = HelperFunctions(kwargs.get('preffered_send_time',None)).get_preferred_send_time() if kwargs.get('preffered_sendtime_checkbox') == 'on' else None
        # self.redirectURI = kwargs.get('redirectUri',None)
        # self.tags = kwargs.get('tags',None)

        # # product reviews

        # self.productReviewTemplateId = kwargs.get('productReviewTemplate','5c17c7ebb565bb0001046fbd')
        # self.prefferedSendTimeProductReview = kwargs.get('prefferedSendTimeProductReview',0)

    





class HelperFunctions:

    def __init__(self,days):
        self.prefferedSendTime = days

    def get_preferred_send_time(self):
        """Calculates the preferred send time."""

        current_date = datetime.now()
        preferred_date = current_date + timedelta(days=int(self.prefferedSendTime))
        return preferred_date.isoformat(timespec="seconds")
    