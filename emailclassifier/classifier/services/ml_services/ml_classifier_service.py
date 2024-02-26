from typing import List

from django.conf import settings
from .sklearn_classifier_service import SklearnClassifier
from .keras_classifier_service import KerasClassifier


class MLClassifier:
    def __init__(self, ml_classifier_settings):
        if ml_classifier_settings == settings.ML_CLASSIFIER.SKLEARN.name:
            self.ml_classifier = SklearnClassifier()
        elif ml_classifier_settings == settings.ML_CLASSIFIER.KERAS.name:
            self.ml_classifier = KerasClassifier()
        else:
            self.ml_classifier = SklearnClassifier()

    def classify(self, text: str):
        return self.ml_classifier.classify(text)
