# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2022-09-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import cashfree_pg
from cashfree_pg.models.offer_entity import OfferEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestOfferEntity(unittest.TestCase):
    """OfferEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OfferEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OfferEntity`
        """
        model = cashfree_pg.models.offer_entity.OfferEntity()  # noqa: E501
        if include_optional :
            return OfferEntity(
                offer_id = 'd2b430fb-1afe-455a-af31-66d00377b29a', 
                offer_status = 'active', 
                offer_meta = {"offer_title":"some title","offer_description":"some offer description","offer_code":"CFTESTOFFER","offer_start_time":"2023-03-21T08:09:51Z","offer_end_time":"2023-03-29T08:09:51Z"}, 
                offer_tnc = {"offer_tnc_type":"text","offer_tnc_value":"TnC for the Offer."}, 
                offer_details = {"offer_type":"DISCOUNT_AND_CASHBACK","discount_details":{"discount_type":"flat","discount_value":"10","max_discount_amount":"10"},"cashback_details":{"cashback_type":"percentage","cashback_value":"20","max_cashback_amount":"150"}}, 
                offer_validations = {"min_amount":10,"payment_method":{"wallet":{"issuer":"paytm"}},"max_allowed":2}
            )
        else :
            return OfferEntity(
        )
        """

    def testOfferEntity(self):
        """Test OfferEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
