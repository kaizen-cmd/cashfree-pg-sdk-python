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
from pydantic import BaseModel, StrictStr
from cashfree_pg.models.offer_details import OfferDetails
from cashfree_pg.models.offer_meta import OfferMeta
from cashfree_pg.models.offer_tnc import OfferTnc
from cashfree_pg.models.offer_validations import OfferValidations

class OfferEntity(BaseModel):
    """
    Offer entity object
    """
    offer_id: Optional[StrictStr] = None
    offer_status: Optional[StrictStr] = None
    offer_meta: Optional[OfferMeta] = None
    offer_tnc: Optional[OfferTnc] = None
    offer_details: Optional[OfferDetails] = None
    offer_validations: Optional[OfferValidations] = None
    __properties = ["offer_id", "offer_status", "offer_meta", "offer_tnc", "offer_details", "offer_validations"]

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
    def from_json(cls, json_str: str) -> OfferEntity:
        """Create an instance of OfferEntity from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> OfferEntity:
        """Create an instance of OfferEntity from a JSON string"""
        temp_dict = json.loads(json_str)
        if temp_dict["offer_id, offer_status, offer_meta, offer_tnc, offer_details, offer_validations"] in temp_dict.keys():
            return cls.from_dict(json.loads(json_str))
        return None

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of offer_meta
        if self.offer_meta:
            _dict['offer_meta'] = self.offer_meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offer_tnc
        if self.offer_tnc:
            _dict['offer_tnc'] = self.offer_tnc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offer_details
        if self.offer_details:
            _dict['offer_details'] = self.offer_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of offer_validations
        if self.offer_validations:
            _dict['offer_validations'] = self.offer_validations.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OfferEntity:
        """Create an instance of OfferEntity from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OfferEntity.parse_obj(obj)

        _obj = OfferEntity.parse_obj({
            "offer_id": obj.get("offer_id"),
            "offer_status": obj.get("offer_status"),
            "offer_meta": OfferMeta.from_dict(obj.get("offer_meta")) if obj.get("offer_meta") is not None else None,
            "offer_tnc": OfferTnc.from_dict(obj.get("offer_tnc")) if obj.get("offer_tnc") is not None else None,
            "offer_details": OfferDetails.from_dict(obj.get("offer_details")) if obj.get("offer_details") is not None else None,
            "offer_validations": OfferValidations.from_dict(obj.get("offer_validations")) if obj.get("offer_validations") is not None else None
        })
        return _obj


