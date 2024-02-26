import re
from django.conf import settings


NEWSLETTER_PATTERNS = [
    r'(un)?subscri(be|ption)s?',
    r'(view|click)\s(the|this)?(web)?link',
    r'click\shere',
    r'newsletter',
    r'register\s(right\s)?(here|now)',
    r'http',
    r'for\smore\s(details?|information\s?)',
    r'(special|limited)\s(time\s)?offer\s?',
    r'money\s?back\sguarantee',
    r'visit\sus\s(right)?(today|now)',
    r'learn\smore'
]


class LogicClassifier:
    @staticmethod
    def classify(text):
        for pattern in NEWSLETTER_PATTERNS:
            search = re.search(pattern, text, re.IGNORECASE)
            if search is not None:
                return settings.EMAILCLASS.NEWSLETTER
        return settings.EMAILCLASS.REGULAR
