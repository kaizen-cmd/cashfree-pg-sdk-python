# coding: utf-8

"""
    Cashfree Payment Gateway APIs

    Cashfree's Payment Gateway APIs provide developers with a streamlined pathway to integrate advanced payment processing capabilities into their applications, platforms and websites.

    The version of the OpenAPI document: 2023-08-01
    Contact: developers@cashfree.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

import cashfree_pg
from cashfree_pg.models.settlement_recon_entity import SettlementReconEntity  # noqa: E501
from cashfree_pg.rest import ApiException

class TestSettlementReconEntity(unittest.TestCase):
    """SettlementReconEntity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SettlementReconEntity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettlementReconEntity`
        """
        model = cashfree_pg.models.settlement_recon_entity.SettlementReconEntity()  # noqa: E501
        if include_optional :
            return SettlementReconEntity(
                cursor = '', 
                limit = 56, 
                data = [
                    cashfree_pg.models.settlement_recon_entity_data_inner.SettlementReconEntity_data_inner(
                        event_id = '', 
                        event_type = '', 
                        event_settlement_amount = 1.337, 
                        event_amount = 1.337, 
                        sale_type = '', 
                        event_status = '', 
                        entity = '', 
                        event_time = '', 
                        event_currency = '', 
                        order_id = '', 
                        order_amount = 1.337, 
                        customer_phone = '', 
                        customer_email = '', 
                        customer_name = '', 
                        payment_amount = 1.337, 
                        payment_utr = '', 
                        payment_time = '', 
                        payment_service_charge = 1.337, 
                        payment_service_tax = 1.337, 
                        cf_payment_id = '', 
                        cf_settlement_id = '', 
                        settlement_date = '', 
                        settlement_utr = '', 
                        split_service_charge = 1.337, 
                        split_service_tax = 1.337, 
                        vendor_commission = 1.337, 
                        closed_in_favor_of = '', 
                        dispute_resolved_on = '', 
                        dispute_category = '', 
                        dispute_note = '', 
                        refund_processed_at = '', 
                        refund_arn = '', 
                        refund_note = '', 
                        refund_id = '', 
                        adjustment_remarks = '', )
                    ]
            )
        else :
            return SettlementReconEntity(
        )
        """

    def testSettlementReconEntity(self):
        """Test SettlementReconEntity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
