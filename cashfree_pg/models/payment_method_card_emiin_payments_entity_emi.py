# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from cashfree_pg.models.payment_method_card_emiin_payments_entity_emi_emi_details import PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails

class PaymentMethodCardEMIInPaymentsEntityEmi(BaseModel):
    """
    PaymentMethodCardEMIInPaymentsEntityEmi
    """
    channel: Optional[StrictStr] = None
    card_number: Optional[StrictStr] = None
    card_network: Optional[StrictStr] = None
    card_type: Optional[StrictStr] = None
    card_country: Optional[StrictStr] = None
    card_bank_name: Optional[StrictStr] = None
    card_network_reference_id: Optional[StrictStr] = None
    emi_tenure: Optional[Union[StrictFloat, StrictInt]] = None
    emi_details: Optional[PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails] = None
    __properties = ["channel", "card_number", "card_network", "card_type", "card_country", "card_bank_name", "card_network_reference_id", "emi_tenure", "emi_details"]

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
    def from_json(cls, json_str: str) -> PaymentMethodCardEMIInPaymentsEntityEmi:
        """Create an instance of PaymentMethodCardEMIInPaymentsEntityEmi from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> PaymentMethodCardEMIInPaymentsEntityEmi:
        """Create an instance of PaymentMethodCardEMIInPaymentsEntityEmi from a JSON string"""
        temp_dict = json.loads(json_str)
        if "channel, card_number, card_network, card_type, card_country, card_bank_name, card_network_reference_id, emi_tenure, emi_details" in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of emi_details
        if self.emi_details:
            _dict['emi_details'] = self.emi_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PaymentMethodCardEMIInPaymentsEntityEmi:
        """Create an instance of PaymentMethodCardEMIInPaymentsEntityEmi from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PaymentMethodCardEMIInPaymentsEntityEmi.parse_obj(obj)

        _obj = PaymentMethodCardEMIInPaymentsEntityEmi.parse_obj({
            "channel": obj.get("channel"),
            "card_number": obj.get("card_number"),
            "card_network": obj.get("card_network"),
            "card_type": obj.get("card_type"),
            "card_country": obj.get("card_country"),
            "card_bank_name": obj.get("card_bank_name"),
            "card_network_reference_id": obj.get("card_network_reference_id"),
            "emi_tenure": obj.get("emi_tenure"),
            "emi_details": PaymentMethodCardEMIInPaymentsEntityEmiEmiDetails.from_dict(obj.get("emi_details")) if obj.get("emi_details") is not None else None
        })
        return _obj


