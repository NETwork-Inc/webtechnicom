# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class TriggerList(ListResource):

    def __init__(self, version, account_sid):
        super(TriggerList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
        }
        self._uri = "/Accounts/{account_sid}/Usage/Triggers.json".format(**self._kwargs)

    def create(self, callback_url, trigger_value, usage_category,
               callback_method=values.unset, friendly_name=values.unset,
               recurring=values.unset, trigger_by=values.unset):
        data = values.of({
            "CallbackUrl": callback_url,
            "TriggerValue": trigger_value,
            "UsageCategory": usage_category,
            "CallbackMethod": callback_method,
            "FriendlyName": friendly_name,
            "Recurring": recurring,
            "TriggerBy": trigger_by,
        })
        
        return self._version.create(
            TriggerInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, recurring=values.unset, trigger_by=values.unset,
             usage_category=values.unset, limit=None, page_size=None, **kwargs):
        limits = self._version.read_limits(limit, page_size)
        
        params = values.of({
            "Recurring": recurring,
            "TriggerBy": trigger_by,
            "UsageCategory": usage_category,
            'PageSize': limits['page_size'],
        })
        params.update(kwargs)
        
        return self._version.read(
            self,
            TriggerInstance,
            self._kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, recurring=values.unset, trigger_by=values.unset,
             usage_category=values.unset, page_token=None, page_number=None,
             page_size=None, **kwargs):
        params = values.of({
            "Recurring": recurring,
            "TriggerBy": trigger_by,
            "UsageCategory": usage_category,
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._version.page(
            self,
            TriggerInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def __call__(self, sid):
        return TriggerContext(self._version, sid=sid, **self._kwargs)

    def __repr__(self):
        return '<Twilio.Api.V2010.TriggerList>'


class TriggerContext(InstanceContext):

    def __init__(self, version, account_sid, sid):
        super(TriggerContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/Usage/Triggers/{sid}.json".format(**self._kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._version.fetch(
            TriggerInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, callback_method=values.unset, callback_url=values.unset,
               friendly_name=values.unset):
        data = values.of({
            "CallbackMethod": callback_method,
            "CallbackUrl": callback_url,
            "FriendlyName": friendly_name,
        })
        
        return self._version.update(
            TriggerInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def delete(self):
        return self._version.delete("delete", self._uri)


class TriggerInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, sid=None):
        super(TriggerInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'api_version': payload['api_version'],
            'callback_method': payload['callback_method'],
            'callback_url': payload['callback_url'],
            'current_value': payload['current_value'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_fired': deserialize.rfc2822_datetime(payload['date_fired']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'friendly_name': payload['friendly_name'],
            'recurring': payload['recurring'],
            'sid': payload['sid'],
            'trigger_by': payload['trigger_by'],
            'trigger_value': payload['trigger_value'],
            'uri': payload['uri'],
            'usage_category': payload['usage_category'],
            'usage_record_uri': payload['usage_record_uri'],
        }
        
        # Context
        self._lazy_context = None
        self._context_properties = {
            'account_sid': account_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = TriggerContext(
                self._version,
                self._context_properties['account_sid'],
                self._context_properties['sid'],
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._properties['account_sid']

    @property
    def api_version(self):
        """ The api_version """
        return self._properties['api_version']

    @property
    def callback_method(self):
        """ The callback_method """
        return self._properties['callback_method']

    @property
    def callback_url(self):
        """ The callback_url """
        return self._properties['callback_url']

    @property
    def current_value(self):
        """ The current_value """
        return self._properties['current_value']

    @property
    def date_created(self):
        """ The date_created """
        return self._properties['date_created']

    @property
    def date_fired(self):
        """ The date_fired """
        return self._properties['date_fired']

    @property
    def date_updated(self):
        """ The date_updated """
        return self._properties['date_updated']

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._properties['friendly_name']

    @property
    def recurring(self):
        """ The recurring """
        return self._properties['recurring']

    @property
    def sid(self):
        """ The sid """
        return self._properties['sid']

    @property
    def trigger_by(self):
        """ The trigger_by """
        return self._properties['trigger_by']

    @property
    def trigger_value(self):
        """ The trigger_value """
        return self._properties['trigger_value']

    @property
    def uri(self):
        """ The uri """
        return self._properties['uri']

    @property
    def usage_category(self):
        """ The usage_category """
        return self._properties['usage_category']

    @property
    def usage_record_uri(self):
        """ The usage_record_uri """
        return self._properties['usage_record_uri']

    def fetch(self):
        self._context.fetch()

    def update(self, callback_method=values.unset, callback_url=values.unset,
               friendly_name=values.unset):
        self._context.update(
            callback_method=callback_method,
            callback_url=callback_url,
            friendly_name=friendly_name,
        )

    def delete(self):
        self._context.delete()