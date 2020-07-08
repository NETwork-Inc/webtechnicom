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


class FunctionVersionContentTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.serverless.v1.services("ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .functions("ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .function_versions("ZNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                     .function_version_content().fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://serverless.twilio.com/v1/Services/ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Functions/ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Versions/ZNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/Content',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "sid": "ZN00000000000000000000000000000000",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "service_sid": "ZS00000000000000000000000000000000",
                "function_sid": "ZH00000000000000000000000000000000",
                "content": "exports.handler = function (context, event, callback) {\\n    const request = require(\\"request\\");\\n    return request(\\"http://www.google.com\\", function (error, response, body) {\\n        callback(null, response.statusCode);\\n    });\\n};",
                "url": "https://serverless.twilio.com/v1/Services/ZS00000000000000000000000000000000/Functions/ZH00000000000000000000000000000000/Versions/ZN00000000000000000000000000000000/Content"
            }
            '''
        ))

        actual = self.client.serverless.v1.services("ZSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .functions("ZHXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .function_versions("ZNXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                          .function_version_content().fetch()

        self.assertIsNotNone(actual)