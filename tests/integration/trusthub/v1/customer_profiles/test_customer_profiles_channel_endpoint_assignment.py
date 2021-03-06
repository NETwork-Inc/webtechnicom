# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class CustomerProfilesChannelEndpointAssignmentTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .customer_profiles_channel_endpoint_assignment.create(channel_endpoint_type="channel_endpoint_type", channel_endpoint_sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        values = {
            'ChannelEndpointType': "channel_endpoint_type",
            'ChannelEndpointSid': "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
        }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://trusthub.twilio.com/v1/CustomerProfiles/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ChannelEndpointAssignments',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "customer_profile_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_endpoint_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_endpoint_type": "phone-number",
                "date_created": "2019-07-31T02:34:41Z",
                "url": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments/RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .customer_profiles_channel_endpoint_assignment.create(channel_endpoint_type="channel_endpoint_type", channel_endpoint_sid="ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .customer_profiles_channel_endpoint_assignment.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trusthub.twilio.com/v1/CustomerProfiles/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ChannelEndpointAssignments',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .customer_profiles_channel_endpoint_assignment.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "results": [
                    {
                        "sid": "RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "customer_profile_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_endpoint_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "channel_endpoint_type": "phone-number",
                        "date_created": "2019-07-31T02:34:41Z",
                        "url": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments/RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments?ChannelEndpointSid=PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments?ChannelEndpointSid=PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "results"
                }
            }
            '''
        ))

        actual = self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .customer_profiles_channel_endpoint_assignment.list()

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .customer_profiles_channel_endpoint_assignment("RAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://trusthub.twilio.com/v1/CustomerProfiles/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ChannelEndpointAssignments/RAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "customer_profile_sid": "BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_endpoint_sid": "PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "channel_endpoint_type": "phone-number",
                "date_created": "2019-07-31T02:34:41Z",
                "url": "https://trusthub.twilio.com/v1/CustomerProfiles/BUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/ChannelEndpointAssignments/RAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .customer_profiles_channel_endpoint_assignment("RAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                   .customer_profiles_channel_endpoint_assignment("RAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://trusthub.twilio.com/v1/CustomerProfiles/BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/ChannelEndpointAssignments/RAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.trusthub.v1.customer_profiles("BUXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                        .customer_profiles_channel_endpoint_assignment("RAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
