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


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, constr

class CardOffer(BaseModel):
    """
    CardOffer
    """
    type: conlist(StrictStr) = Field(...)
    bank_name: constr(strict=True, max_length=100, min_length=3) = Field(..., description="Bank Name of Card.")
    scheme_name: conlist(StrictStr) = Field(...)
    __properties = ["type", "bank_name", "scheme_name"]

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
    def from_json(cls, json_str: str) -> CardOffer:
        """Create an instance of CardOffer from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CardOffer:
        """Create an instance of CardOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CardOffer.parse_obj(obj)

        _obj = CardOffer.parse_obj({
            "type": obj.get("type"),
            "bank_name": obj.get("bank_name"),
            "scheme_name": obj.get("scheme_name")
        })
        return _obj


