# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import serialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class DeactivationsList(ListResource):

    def __init__(self, version):
        """
        Initialize the DeactivationsList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.deactivation.DeactivationsList
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsList
        """
        super(DeactivationsList, self).__init__(version)

        # Path Solution
        self._solution = {}

    def get(self):
        """
        Constructs a DeactivationsContext

        :returns: twilio.rest.messaging.v1.deactivation.DeactivationsContext
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsContext
        """
        return DeactivationsContext(self._version, )

    def __call__(self):
        """
        Constructs a DeactivationsContext

        :returns: twilio.rest.messaging.v1.deactivation.DeactivationsContext
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsContext
        """
        return DeactivationsContext(self._version, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.DeactivationsList>'


class DeactivationsPage(Page):

    def __init__(self, version, response, solution):
        """
        Initialize the DeactivationsPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.messaging.v1.deactivation.DeactivationsPage
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsPage
        """
        super(DeactivationsPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of DeactivationsInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.messaging.v1.deactivation.DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsInstance
        """
        return DeactivationsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Messaging.V1.DeactivationsPage>'


class DeactivationsContext(InstanceContext):

    def __init__(self, version):
        """
        Initialize the DeactivationsContext

        :param Version version: Version that contains the resource

        :returns: twilio.rest.messaging.v1.deactivation.DeactivationsContext
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsContext
        """
        super(DeactivationsContext, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Deactivations'.format(**self._solution)

    def fetch(self, date=values.unset):
        """
        Fetch the DeactivationsInstance

        :param date date: The date to retrieve deactivated numbers for.

        :returns: The fetched DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsInstance
        """
        data = values.of({'Date': serialize.iso8601_date(date), })

        payload = self._version.fetch(method='GET', uri=self._uri, params=data, )

        return DeactivationsInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.DeactivationsContext {}>'.format(context)


class DeactivationsInstance(InstanceResource):

    def __init__(self, version, payload):
        """
        Initialize the DeactivationsInstance

        :returns: twilio.rest.messaging.v1.deactivation.DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsInstance
        """
        super(DeactivationsInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {'redirect_to': payload.get('redirect_to'), }

        # Context
        self._context = None
        self._solution = {}

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: DeactivationsContext for this DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsContext
        """
        if self._context is None:
            self._context = DeactivationsContext(self._version, )
        return self._context

    @property
    def redirect_to(self):
        """
        :returns: Redirect url to the list of deactivated numbers.
        :rtype: unicode
        """
        return self._properties['redirect_to']

    def fetch(self, date=values.unset):
        """
        Fetch the DeactivationsInstance

        :param date date: The date to retrieve deactivated numbers for.

        :returns: The fetched DeactivationsInstance
        :rtype: twilio.rest.messaging.v1.deactivation.DeactivationsInstance
        """
        return self._proxy.fetch(date=date, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Messaging.V1.DeactivationsInstance {}>'.format(context)