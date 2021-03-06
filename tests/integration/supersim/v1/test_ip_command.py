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


class IpCommandTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.ip_commands.create(sim="sim", payload="payload", device_port=1)

        values = {'Sim': "sim", 'Payload': "payload", 'DevicePort': 1, }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://supersim.twilio.com/v1/IpCommands',
            data=values,
        ))

    def test_create_full_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sim_iccid": "89883070000123456789",
                "status": "queued",
                "direction": "to_sim",
                "device_ip": "100.64.0.123",
                "device_port": 100,
                "payload_type": "text",
                "payload": "checkin: firmware update",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/IpCommands/HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.ip_commands.create(sim="sim", payload="payload", device_port=1)

        self.assertIsNotNone(actual)

    def test_create_minimal_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "sid": "HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sim_iccid": "89883070000123456789",
                "status": "queued",
                "direction": "to_sim",
                "device_ip": "100.64.0.123",
                "device_port": 100,
                "payload_type": "text",
                "payload": "checkin: firmware update",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/IpCommands/HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.ip_commands.create(sim="sim", payload="payload", device_port=1)

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.ip_commands("HGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://supersim.twilio.com/v1/IpCommands/HGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sim_iccid": "89883070000123456789",
                "status": "queued",
                "direction": "to_sim",
                "device_ip": "100.64.0.123",
                "device_port": 100,
                "payload_type": "text",
                "payload": "checkin: firmware update",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "url": "https://supersim.twilio.com/v1/IpCommands/HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.supersim.v1.ip_commands("HGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.supersim.v1.ip_commands.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://supersim.twilio.com/v1/IpCommands',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "ip_commands": [],
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/IpCommands?Status=received&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "key": "ip_commands",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/IpCommands?Status=received&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.supersim.v1.ip_commands.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://supersim.twilio.com/v1/IpCommands?Status=received&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0",
                    "key": "ip_commands",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://supersim.twilio.com/v1/IpCommands?Status=received&Sim=HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa&PageSize=50&Page=0"
                },
                "ip_commands": [
                    {
                        "sid": "HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sim_sid": "HSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "sim_iccid": "89883070000123456789",
                        "status": "received",
                        "direction": "from_sim",
                        "device_ip": "100.64.0.123",
                        "device_port": 100,
                        "payload_type": "text",
                        "payload": "checkin: firmware update",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "url": "https://supersim.twilio.com/v1/IpCommands/HGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ]
            }
            '''
        ))

        actual = self.client.supersim.v1.ip_commands.list()

        self.assertIsNotNone(actual)
