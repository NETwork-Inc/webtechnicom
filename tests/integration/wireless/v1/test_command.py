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


class CommandTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.commands("DCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://wireless.twilio.com/v1/Commands/DCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_command_sms_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "command": "command",
                "command_mode": "text",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "delivery_receipt_requested": true,
                "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "direction": "from_sim",
                "sid": "DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "transport": "sms",
                "url": "https://wireless.twilio.com/v1/Commands/DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.wireless.v1.commands("DCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_fetch_command_ip_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "command": "command",
                "command_mode": "text",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "delivery_receipt_requested": false,
                "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "direction": "to_sim",
                "sid": "DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "transport": "ip",
                "url": "https://wireless.twilio.com/v1/Commands/DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.wireless.v1.commands("DCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.commands.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://wireless.twilio.com/v1/Commands',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "commands": [],
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/Commands?Status=queued&Direction=from_sim&Sim=sim&PageSize=50&Page=0",
                    "key": "commands",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/Commands?Status=queued&Direction=from_sim&Sim=sim&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.wireless.v1.commands.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "commands": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "command": "command",
                        "command_mode": "text",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "delivery_receipt_requested": true,
                        "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "direction": "from_sim",
                        "sid": "DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "queued",
                        "transport": "sms",
                        "url": "https://wireless.twilio.com/v1/Commands/DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/Commands?Status=queued&Direction=from_sim&Sim=sim&PageSize=50&Page=0",
                    "key": "commands",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/Commands?Status=queued&Direction=from_sim&Sim=sim&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.wireless.v1.commands.list()

        self.assertIsNotNone(actual)

    def test_read_ip_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "commands": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "command": "command",
                        "command_mode": "binary",
                        "date_created": "2015-07-30T20:00:00Z",
                        "date_updated": "2015-07-30T20:00:00Z",
                        "delivery_receipt_requested": true,
                        "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "direction": "to_sim",
                        "sid": "DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "status": "queued",
                        "transport": "ip",
                        "url": "https://wireless.twilio.com/v1/Commands/DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
                    }
                ],
                "meta": {
                    "first_page_url": "https://wireless.twilio.com/v1/Commands?Status=queued&Direction=to_sim&Transport=ip&Sim=sim&PageSize=50&Page=0",
                    "key": "commands",
                    "next_page_url": null,
                    "page": 0,
                    "page_size": 50,
                    "previous_page_url": null,
                    "url": "https://wireless.twilio.com/v1/Commands?Status=queued&Direction=to_sim&Transport=ip&Sim=sim&PageSize=50&Page=0"
                }
            }
            '''
        ))

        actual = self.client.wireless.v1.commands.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.commands.create(command="command")

        values = {'Command': "command", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://wireless.twilio.com/v1/Commands',
            data=values,
        ))

    def test_create_command_sms_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "command": "command",
                "command_mode": "text",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "delivery_receipt_requested": true,
                "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "direction": "from_sim",
                "sid": "DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "transport": "sms",
                "url": "https://wireless.twilio.com/v1/Commands/DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.wireless.v1.commands.create(command="command")

        self.assertIsNotNone(actual)

    def test_create_command_ip_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "command": "command",
                "command_mode": "binary",
                "date_created": "2015-07-30T20:00:00Z",
                "date_updated": "2015-07-30T20:00:00Z",
                "delivery_receipt_requested": true,
                "direction": "to_sim",
                "sid": "DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sim_sid": "DEaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "status": "queued",
                "transport": "ip",
                "url": "https://wireless.twilio.com/v1/Commands/DCaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.wireless.v1.commands.create(command="command")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.wireless.v1.commands("DCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://wireless.twilio.com/v1/Commands/DCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.wireless.v1.commands("DCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").delete()

        self.assertTrue(actual)
