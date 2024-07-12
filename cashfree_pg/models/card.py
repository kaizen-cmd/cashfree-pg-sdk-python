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
from pydantic import BaseModel, Field, StrictInt, StrictStr, validator

class Card(BaseModel):
    """
    Card Payment method
    """
    channel: StrictStr = Field(..., description="The channel for card payments can be \"link\" or \"post\". Post is used for seamless OTP payments where merchant captures OTP on their own page.")
    card_number: Optional[StrictStr] = Field(None, description="Customer card number for plain card transactions. Token pan number for tokenized card transactions.")
    card_holder_name: Optional[StrictStr] = Field(None, description="Customer name mentioned on the card.")
    card_expiry_mm: Optional[StrictStr] = Field(None, description="Card expiry month for plain card transactions. Token expiry month for tokenized card transactions.")
    card_expiry_yy: Optional[StrictStr] = Field(None, description="Card expiry year for plain card transactions. Token expiry year for tokenized card transactions.")
    card_cvv: Optional[StrictStr] = Field(None, description="CVV mentioned on the card.")
    instrument_id: Optional[StrictStr] = Field(None, description="instrument id of saved card. Required only to make payment using saved instrument.")
    cryptogram: Optional[StrictStr] = Field(None, description="cryptogram received from card network. Required only for tokenized card transactions.")
    token_requestor_id: Optional[StrictStr] = Field(None, description="TRID issued by card networks. Required only for tokenized card transactions.")
    token_reference_id: Optional[StrictStr] = Field(None, description="Token Reference Id provided by Diners for Guest Checkout Token.  Required only for Diners cards.")
    token_type: Optional[StrictStr] = None
    card_display: Optional[StrictStr] = Field(None, description="last 4 digits of original card number. Required only for tokenized card transactions.")
    card_alias: Optional[StrictStr] = Field(None, description="Card alias as returned by Cashfree Vault API.")
    card_bank_name: Optional[StrictStr] = Field(None, description="One of [\"Kotak\", \"ICICI\", \"RBL\", \"BOB\", \"Standard Chartered\"]. Card bank name, required for EMI payments. This is the bank user has selected for EMI")
    emi_tenure: Optional[StrictInt] = Field(None, description="EMI tenure selected by the user")
    __properties = ["channel", "card_number", "card_holder_name", "card_expiry_mm", "card_expiry_yy", "card_cvv", "instrument_id", "cryptogram", "token_requestor_id", "token_reference_id", "token_type", "card_display", "card_alias", "card_bank_name", "emi_tenure"]

    @validator('channel')
    def channel_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('link', 'post'):
            raise ValueError("must be one of enum values ('link', 'post')")
        return value

    @validator('token_type')
    def token_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('ISSUER_TOKEN', 'NETWORK_GC_TOKEN', 'ISSUER_GC_TOKEN'):
            raise ValueError("must be one of enum values ('ISSUER_TOKEN', 'NETWORK_GC_TOKEN', 'ISSUER_GC_TOKEN')")
        return value

    @validator('card_bank_name')
    def card_bank_name_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Kotak', 'ICICI', 'RBL', 'BOB', 'Standard Chartered'):
            raise ValueError("must be one of enum values ('Kotak', 'ICICI', 'RBL', 'BOB', 'Standard Chartered')")
        return value

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
    def from_json(cls, json_str: str) -> Card:
        """Create an instance of Card from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> Card:
        """Create an instance of Card from a JSON string"""
        temp_dict = json.loads(json_str)
        if "channel, card_number, card_holder_name, card_expiry_mm, card_expiry_yy, card_cvv, instrument_id, cryptogram, token_requestor_id, token_reference_id, token_type, card_display, card_alias, card_bank_name, emi_tenure" in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> Card:
        """Create an instance of Card from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Card.parse_obj(obj)

        _obj = Card.parse_obj({
            "channel": obj.get("channel"),
            "card_number": obj.get("card_number"),
            "card_holder_name": obj.get("card_holder_name"),
            "card_expiry_mm": obj.get("card_expiry_mm"),
            "card_expiry_yy": obj.get("card_expiry_yy"),
            "card_cvv": obj.get("card_cvv"),
            "instrument_id": obj.get("instrument_id"),
            "cryptogram": obj.get("cryptogram"),
            "token_requestor_id": obj.get("token_requestor_id"),
            "token_reference_id": obj.get("token_reference_id"),
            "token_type": obj.get("token_type"),
            "card_display": obj.get("card_display"),
            "card_alias": obj.get("card_alias"),
            "card_bank_name": obj.get("card_bank_name"),
            "emi_tenure": obj.get("emi_tenure")
        })
        return _obj


