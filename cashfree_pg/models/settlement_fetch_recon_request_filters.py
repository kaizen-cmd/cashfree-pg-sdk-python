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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist

class SettlementFetchReconRequestFilters(BaseModel):
    """
    Specify either the Settlement ID, Settlement UTR, or start date and end date to fetch the settlement details.
    """
    cf_settlement_ids: Optional[conlist(StrictInt)] = Field(None, description="List of settlement IDs for which you want the settlement reconciliation details.")
    settlement_utrs: Optional[conlist(StrictStr)] = Field(None, description="List of settlement UTRs for which you want the settlement reconciliation details.")
    start_date: Optional[StrictStr] = Field(None, description="Specify the start date from when you want the settlement reconciliation details.")
    end_date: Optional[StrictStr] = Field(None, description="Specify the end date till when you want the settlement reconciliation details.")
    __properties = ["cf_settlement_ids", "settlement_utrs", "start_date", "end_date"]

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
    def from_json(cls, json_str: str) -> SettlementFetchReconRequestFilters:
        """Create an instance of SettlementFetchReconRequestFilters from a JSON string"""
        return cls.from_dict(json.loads(json_str))
    
    @classmethod
    def from_json_for_one_of(cls, json_str: str) -> SettlementFetchReconRequestFilters:
        """Create an instance of SettlementFetchReconRequestFilters from a JSON string"""
        temp_dict = json.loads(json_str)
        if temp_dict["cf_settlement_ids, settlement_utrs, start_date, end_date"] in temp_dict.keys():
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
    def from_dict(cls, obj: dict) -> SettlementFetchReconRequestFilters:
        """Create an instance of SettlementFetchReconRequestFilters from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return SettlementFetchReconRequestFilters.parse_obj(obj)

        _obj = SettlementFetchReconRequestFilters.parse_obj({
            "cf_settlement_ids": obj.get("cf_settlement_ids"),
            "settlement_utrs": obj.get("settlement_utrs"),
            "start_date": obj.get("start_date"),
            "end_date": obj.get("end_date")
        })
        return _obj


