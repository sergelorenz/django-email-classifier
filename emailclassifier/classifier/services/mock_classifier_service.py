import random
from django.conf import settings


class MockClassifier:

    @staticmethod
    def classify(_):
        return random.choice(list(settings.EMAILCLASS))
