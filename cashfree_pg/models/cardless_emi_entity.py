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


from typing import List, Optional
from pydantic import BaseModel, conlist, constr
from cashfree_pg.models.emi_plans_array import EMIPlansArray

class CardlessEMIEntity(BaseModel):
    """
    cardless EMI object
    """
    payment_method: Optional[constr(strict=True, max_length=50, min_length=3)] = None
    emi_plans: Optional[conlist(EMIPlansArray)] = None
    __properties = ["payment_method", "emi_plans"]

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
    def from_json(cls, json_str: str) -> CardlessEMIEntity:
        """Create an instance of CardlessEMIEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in emi_plans (list)
        _items = []
        if self.emi_plans:
            for _item in self.emi_plans:
                if _item:
                    _items.append(_item.to_dict())
            _dict['emi_plans'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CardlessEMIEntity:
        """Create an instance of CardlessEMIEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CardlessEMIEntity.parse_obj(obj)

        _obj = CardlessEMIEntity.parse_obj({
            "payment_method": obj.get("payment_method"),
            "emi_plans": [EMIPlansArray.from_dict(_item) for _item in obj.get("emi_plans")] if obj.get("emi_plans") is not None else None
        })
        return _obj


