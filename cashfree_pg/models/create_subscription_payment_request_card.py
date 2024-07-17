# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2023-08-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class CreateSubscriptionPaymentRequestCard(BaseModel):
    """
    payment method card.
    """
    channel: Optional[StrictStr] = Field(None, description="Channel. can be link")
    card_number: Optional[StrictStr] = Field(None, description="Card number")
    card_holder_name: Optional[StrictStr] = Field(None, description="Card holder name")
    card_expiry_mm: Optional[StrictStr] = Field(None, description="Card expiry month")
    card_expiry_yy: Optional[StrictStr] = Field(None, description="Card expiry year")
    card_cvv: Optional[StrictStr] = Field(None, description="Card CVV")
    card_network: Optional[StrictStr] = Field(None, description="Card network")
    card_type: Optional[StrictStr] = Field(None, description="Card type")
    __properties = ["channel", "card_number", "card_holder_name", "card_expiry_mm", "card_expiry_yy", "card_cvv", "card_network", "card_type"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> CreateSubscriptionPaymentRequestCard:
        """Create an instance of CreateSubscriptionPaymentRequestCard from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> CreateSubscriptionPaymentRequestCard:
        """Create an instance of CreateSubscriptionPaymentRequestCard from a JSON string"""
        temp_dict = json.loads(json_str)
        if "channel, card_number, card_holder_name, card_expiry_mm, card_expiry_yy, card_cvv, card_network, card_type" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreateSubscriptionPaymentRequestCard:
        """Create an instance of CreateSubscriptionPaymentRequestCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreateSubscriptionPaymentRequestCard.parse_obj(obj)

        _obj = CreateSubscriptionPaymentRequestCard.parse_obj({
            "channel": obj.get("channel"),
            "card_number": obj.get("card_number"),
            "card_holder_name": obj.get("card_holder_name"),
            "card_expiry_mm": obj.get("card_expiry_mm"),
            "card_expiry_yy": obj.get("card_expiry_yy"),
            "card_cvv": obj.get("card_cvv"),
            "card_network": obj.get("card_network"),
            "card_type": obj.get("card_type")
        })
        return _obj


