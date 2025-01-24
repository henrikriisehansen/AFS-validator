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
        
        if isinstance(self.invitation, Product_review_sku_payload):
            payload = vars(self.base_payload)
            payload.update(vars(self.invitation))

        
        return {k: v for k, v in payload.items() if v != None}

class Service_review_payload:
    def __init__(self,**kwargs):
       pass

class Product_review_payload:
    def __init__(self,**kwargs):
        pass

class Product_review_sku_payload:
    def __init__(self,**kwargs):
        self.productSkus = [kwargs.get('sku',None)]

class BasePayload:
   """Base class for all payload types."""
   def __init__(self, **kwargs):
        
        self.replyTo = kwargs.get('replyTo',None)
        self.locale = kwargs.get('locale', None) if kwargs.get('locale_checkbox') == 'on' else None

        self.locationId = kwargs.get('location_id',None) if kwargs.get('location_id_checkbox') == 'on' else None
        # self.senderName = kwargs.get('senderName',None)
        # self.senderEmail = kwargs.get('senderEmail',None)
        self.referenceId = kwargs.get('reference_id',None) if kwargs.get('reference_id_checkbox') == 'on' else None
        self.recipientName = kwargs.get('recipient_name',None) if kwargs.get('recipient_name_checkbox') == 'on' else None
        self.recipientEmail = kwargs.get('recipient_email',None) if kwargs.get('recipient_email_checkbox') == 'on' else None
        self.templateId = kwargs.get('template',None) if kwargs.get('template_checkbox') == 'on' else None
        self.prefferedSendtimeServiceReview = HelperFunctions(kwargs.get('preffered_send_time',None)).get_preferred_send_time() if kwargs.get('preffered_sendtime_checkbox') == 'on' else None
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
    
# class PayloadData:
#     """
#     Contains data specific to the payload.
#     """
#     def __init__(self, **kwargs):

#         # service reviews
#         self.email_data = kwargs.get('emails')
#         self.settings_data = kwargs.get('settings')

#         self.replyTo = kwargs.get('replyTo',None)
#         self.locale = self.settings_data.get('locale') if self.settings_data.get('locale_checkbox') else None

        

#         self.locationId = kwargs.get('locationId',None)
#         self.senderName = kwargs.get('senderName',None)
#         self.senderEmail = kwargs.get('senderEmail',None)
#         self.referenceId = self.settings_data.get('reference_id',None)
#         self.recipientName = self.email_data.get('recipient_name',None)
#         self.recipientEmail = self.email_data.get('recipient_email',None)
#         self.templateId = kwargs.get('templateId',None)
#         self.prefferedSendtimeServiceReview = kwargs.get('prefferedSendTimeServiceReview',None)
#         self.redirectURI = kwargs.get('redirectUri',None)
#         self.tags = kwargs.get('tags',None)

#         # product reviews

#         self.productReviewTemplateId = kwargs.get('productReviewTemplate','5c17c7ebb565bb0001046fbd')
#         self.prefferedSendTimeProductReview = kwargs.get('prefferedSendTimeProductReview',0)

#         # self.payload_data: dict = map()

#     def generate_random_string(self,length):
#             """Generates a random alphanumeric string of the given length."""
#             return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

#     def get_payload_data(self) -> dict:

#         """Returns the payload data."""
#         self.payload_data = {
#         "replyTo": self.replyTo,
#         # "locale": self.locale,
#         "senderName": self.senderName,
#         "senderEmail": self.senderEmail,
#         "recipientName": self.recipientName,
#         "referenceId": self.referenceId,
#         "locationId": self.locationId,
#         "recipientEmail" : self.recipientEmail,
#         "templateId": self.templateId,
#         "preferredSendTime": self.prefferedSendtimeServiceReview, #HelperFunctions(self.prefferedSendtimeServiceReview).get_preferred_send_time(),
#         "redirectURI": self.redirectURI,
#         "tags": self.tags
        
#         }
        
#         return {k: v for k, v in self.payload_data.items() if v != None}

#     def get_products_payload_data(self):
#         payload_data = {

#         "productUrl": "http://www.companystore.com/.../12345.htm",
#         "imageUrl": "http://www.companystore.com/.../.../12345.jpg",
#         "name": "Metal Toy Car",
#         "sku": "ABC-1234",
#         "gtin": "1234567890",
#         "mpn": "7TX1641",
#         "brand": "Acme",
#         "productCategoryGoogleId": "1253"
        
#         }
        
#         return payload_data
    
#     def get_productsku_payload_data(self):

#         payload_data = ["ABC-1234","ABC-4321"]

#         return payload_data