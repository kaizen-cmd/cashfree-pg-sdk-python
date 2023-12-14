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
from pydantic import BaseModel, Field, StrictStr, conint, constr, validator

class Netbanking(BaseModel):
    """
    Netbanking payment method request body
    """
    channel: StrictStr = Field(..., description="The channel for netbanking will always be `link`")
    netbanking_bank_code: Optional[conint(strict=True)] = Field(None, description="Bank code")
    netbanking_bank_name: Optional[constr(strict=True)] = Field(None, description="String code for bank")
    __properties = []

    @validator('netbanking_bank_name')
    def netbanking_bank_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[A-Z]{5}$", value):
            raise ValueError(r"must validate the regular expression /^[A-Z]{5}$/")
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
    def from_json(cls, json_str: str) -> Netbanking:
        """Create an instance of Netbanking from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Netbanking:
        """Create an instance of Netbanking from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Netbanking.parse_obj(obj)

        _obj = Netbanking.parse_obj({
        })
        return _obj


