from django.conf import settings
from django.test import TestCase

from ..services.logic_classifier_service import LogicClassifier
from ..services.ml_services.sklearn_classifier_service import SklearnClassifier


class ClassifierServiceTest(TestCase):
    def setUp(self):
        self.test_text_regular = "This is a regular text"
        self.test_text_newsletter = "This is a sample newsletter. subscribe now! Limited offer only!"
        self.classes = list(settings.EMAILCLASS)
        self.logic_classifier = LogicClassifier()
        self.sklearn_classifier = SklearnClassifier()

    def test_regular_logic_classifier_service(self):
        value = self.logic_classifier.classify(self.test_text_regular)
        self.assertIn(value, self.classes)

    def test_newsletter_logic_classifier_service(self):
        value = self.logic_classifier.classify(self.test_text_newsletter)
        self.assertIn(value, self.classes)

    def test_regular_sklearn_classifier_service(self):
        value = self.sklearn_classifier.classify(self.test_text_regular)
        self.assertIn(value, self.classes)

    def test_newsletter_sklearn_classifier_service(self):
        value = self.sklearn_classifier.classify(self.test_text_newsletter)
        self.assertIn(value, self.classes)

