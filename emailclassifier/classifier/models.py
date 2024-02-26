from django.db import models
from django.conf import settings
from emailuploader.models import EmailFile


CLASSIFICATION_METHOD = (
    ('logic', 'Logic-Based'),
    ('ml', 'Machine Learning Model')
)
ML_CLASSIFIER_TYPE = (
    ('none', 'None'),
    ('sklearn', 'Scikit-Learn'),
    ('keras', 'Keras DL'),
)
CLASSIFICATION_STATUS = (
    ('not_done', 'Not Done'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed')
)


# Create your models here.
class Classification(models.Model):
    email_file = models.ForeignKey(EmailFile, on_delete=models.CASCADE)
    classification_method = models.CharField(max_length=16, choices=CLASSIFICATION_METHOD, null=True, default='logic')
    ml_classifier = models.CharField(max_length=16, choices=ML_CLASSIFIER_TYPE, null=True, default='none')
    classification_status = models.CharField(max_length=16, choices=CLASSIFICATION_STATUS, null=True, default='not_done')

