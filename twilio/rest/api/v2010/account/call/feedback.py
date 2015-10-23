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


class FeedbackList(ListResource):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the FeedbackList
        
        :param Version version: Version that contains the resource
        :param account_sid: The account_sid
        :param call_sid: A 34 character string that uniquely identifies this resource.
        
        :returns: FeedbackList
        :rtype: FeedbackList
        """
        super(FeedbackList, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }

    def get(self):
        """
        Constructs a FeedbackContext
        
        :returns: FeedbackContext
        :rtype: FeedbackContext
        """
        return FeedbackContext(self._version, **self._kwargs)

    def __call__(self):
        """
        Constructs a FeedbackContext
        
        :returns: FeedbackContext
        :rtype: FeedbackContext
        """
        return FeedbackContext(self._version, **self._kwargs)

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Api.V2010.FeedbackList>'


class FeedbackContext(InstanceContext):

    def __init__(self, version, account_sid, call_sid):
        """
        Initialize the FeedbackContext
        
        :param Version version
        :param account_sid: The account_sid
        :param call_sid: The call sid that uniquely identifies the call
        
        :returns: FeedbackContext
        :rtype: FeedbackContext
        """
        super(FeedbackContext, self).__init__(version)
        
        # Path Solution
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }
        self._uri = '/Accounts/{account_sid}/Calls/{call_sid}/Feedback.json'.format(**self._kwargs)

    def create(self, quality_score, issue=values.unset):
        """
        Create a new FeedbackInstance
        
        :param unicode quality_score: The quality_score
        :param feedback.issues issue: The issue
        
        :returns: Newly created FeedbackInstance
        :rtype: FeedbackInstance
        """
        data = values.of({
            'QualityScore': quality_score,
            'Issue': issue,
        })
        
        return self._version.create(
            FeedbackInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def fetch(self):
        """
        Fetch a FeedbackInstance
        
        :returns: Fetched FeedbackInstance
        :rtype: FeedbackInstance
        """
        params = values.of({})
        
        return self._version.fetch(
            FeedbackInstance,
            self._kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def update(self, quality_score, issue=values.unset):
        """
        Update the FeedbackInstance
        
        :param unicode quality_score: An integer from 1 to 5
        :param feedback.issues issue: Issues experienced during the call
        
        :returns: Updated FeedbackInstance
        :rtype: FeedbackInstance
        """
        data = values.of({
            'QualityScore': quality_score,
            'Issue': issue,
        })
        
        return self._version.update(
            FeedbackInstance,
            self._kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.FeedbackContext {}>'.format(context)


class FeedbackInstance(InstanceResource):

    def __init__(self, version, payload, account_sid, call_sid):
        """
        Initialize the FeedbackInstance
        
        :returns: FeedbackInstance
        :rtype: FeedbackInstance
        """
        super(FeedbackInstance, self).__init__(version)
        
        # Marshaled Properties
        self._properties = {
            'account_sid': payload['account_sid'],
            'date_created': deserialize.rfc2822_datetime(payload['date_created']),
            'date_updated': deserialize.rfc2822_datetime(payload['date_updated']),
            'issues': payload['issues'],
            'quality_score': deserialize.integer(payload['quality_score']),
            'sid': payload['sid'],
        }
        
        # Context
        self._instance_context = None
        self._kwargs = {
            'account_sid': account_sid,
            'call_sid': call_sid,
        }

    @property
    def _context(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context
        
        :returns: FeedbackContext for this FeedbackInstance
        :rtype: FeedbackContext
        """
        if self._instance_context is None:
            self._instance_context = FeedbackContext(
                self._version,
                self._kwargs['account_sid'],
                self._kwargs['call_sid'],
            )
        return self._instance_context

    @property
    def account_sid(self):
        """
        :returns: The account_sid
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def date_created(self):
        """
        :returns: The date_created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The date_updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def issues(self):
        """
        :returns: The issues
        :rtype: feedback.issues
        """
        return self._properties['issues']

    @property
    def quality_score(self):
        """
        :returns: 1 to 5 quality score
        :rtype: unicode
        """
        return self._properties['quality_score']

    @property
    def sid(self):
        """
        :returns: The sid
        :rtype: unicode
        """
        return self._properties['sid']

    def create(self, quality_score, issue=values.unset):
        """
        Create a new FeedbackInstance
        
        :param unicode quality_score: The quality_score
        :param feedback.issues issue: The issue
        
        :returns: Newly created FeedbackInstance
        :rtype: FeedbackInstance
        """
        return self._context.create(
            quality_score,
            issue=issue,
        )

    def fetch(self):
        """
        Fetch a FeedbackInstance
        
        :returns: Fetched FeedbackInstance
        :rtype: FeedbackInstance
        """
        return self._context.fetch()

    def update(self, quality_score, issue=values.unset):
        """
        Update the FeedbackInstance
        
        :param unicode quality_score: An integer from 1 to 5
        :param feedback.issues issue: Issues experienced during the call
        
        :returns: Updated FeedbackInstance
        :rtype: FeedbackInstance
        """
        return self._context.update(
            quality_score,
            issue=issue,
        )

    def __repr__(self):
        """
        Provide a friendly representation
        
        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._kwargs.items())
        return '<Twilio.Api.V2010.FeedbackInstance {}>'.format(context)