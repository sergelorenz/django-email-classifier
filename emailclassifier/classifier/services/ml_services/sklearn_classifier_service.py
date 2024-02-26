import pickle
import os
from typing import List

from django.conf import settings

BASE_DIR = settings.BASE_DIR
MODEL_PATH = os.path.join(BASE_DIR, 'classifier/services/ml_services/training/sklearn_model.sav')


class SklearnClassifier:
    def __init__(self):
        self.model = pickle.load(open(MODEL_PATH, 'rb'))
        self.classes = [tag for tag in settings.EMAILCLASS]

    def classify(self, text: str):
        y_pred = self.model.predict([text])
        return self.classes[y_pred[0]]
