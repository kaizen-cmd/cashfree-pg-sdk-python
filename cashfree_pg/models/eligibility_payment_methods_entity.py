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


from typing import Optional
from pydantic import BaseModel, StrictBool, StrictStr
from cashfree_pg.models.eligibility_payment_methods_entity_entity_details import EligibilityPaymentMethodsEntityEntityDetails

class EligibilityPaymentMethodsEntity(BaseModel):
    """
    Eligible payment methods details
    """
    eligibility: Optional[StrictBool] = None
    entity_type: Optional[StrictStr] = None
    entity_value: Optional[StrictStr] = None
    entity_details: Optional[EligibilityPaymentMethodsEntityEntityDetails] = None
    __properties = ["eligibility", "entity_type", "entity_value", "entity_details"]

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
    def from_json(cls, json_str: str) -> EligibilityPaymentMethodsEntity:
        """Create an instance of EligibilityPaymentMethodsEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> EligibilityPaymentMethodsEntity:
        """Create an instance of EligibilityPaymentMethodsEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if temp_dict["eligibility, entity_type, entity_value, entity_details"] in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of entity_details
        if self.entity_details:
            _dict['entity_details'] = self.entity_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> EligibilityPaymentMethodsEntity:
        """Create an instance of EligibilityPaymentMethodsEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return EligibilityPaymentMethodsEntity.parse_obj(obj)

        _obj = EligibilityPaymentMethodsEntity.parse_obj({
            "eligibility": obj.get("eligibility"),
            "entity_type": obj.get("entity_type"),
            "entity_value": obj.get("entity_value"),
            "entity_details": EligibilityPaymentMethodsEntityEntityDetails.from_dict(obj.get("entity_details")) if obj.get("entity_details") is not None else None
        })
        return _obj


