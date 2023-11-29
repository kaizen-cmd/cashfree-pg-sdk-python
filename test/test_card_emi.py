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
from cashfree_pg.models.card_emi import CardEMI  # noqa: E501
from cashfree_pg.rest import ApiException

class TestCardEMI(unittest.TestCase):
    """CardEMI unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CardEMI
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CardEMI`
        """
        model = cashfree_pg.models.card_emi.CardEMI()  # noqa: E501
        if include_optional :
            return CardEMI(
                channel = '', 
                card_number = '', 
                card_holder_name = '', 
                card_expiry_mm = '', 
                card_expiry_yy = '', 
                card_cvv = '', 
                card_alias = '', 
                card_bank_name = 'hdfc', 
                emi_tenure = 56
            )
        else :
            return CardEMI(
                channel = '',
                card_number = '',
                card_expiry_mm = '',
                card_expiry_yy = '',
                card_cvv = '',
                card_bank_name = 'hdfc',
                emi_tenure = 56,
        )
        """

    def testCardEMI(self):
        """Test CardEMI"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
