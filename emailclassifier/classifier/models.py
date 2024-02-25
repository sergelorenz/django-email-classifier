from django.db import models
from emailuploader.models import EmailFile


CLASSIFICATION_METHOD = (
    ('logic', 'Logic-Based'),
    ('ml', 'Machine Learning Model')
)
ML_CLASSIFIER_TYPE = (
    ('none', 'None'),
    ('lr', 'Logistic Regression'),
    ('keras', 'Keras DL'),
)
CLASSIFICATION_STATUS = (
    ('not_done', 'Not Done'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed')
)
EMAIL_CLASS = (
    ('newsletter', 'Newsletter'),
    ('regular', 'Regular Email')
)


# Create your models here.
class Classification(models.Model):
    email_file = models.ForeignKey(EmailFile, on_delete=models.CASCADE)
    classification_method = models.CharField(max_length=16, choices=CLASSIFICATION_METHOD, null=True, default='logic')
    ml_classifier = models.CharField(max_length=16, choices=ML_CLASSIFIER_TYPE, null=True, default='none')
    classification_status = models.CharField(max_length=16, choices=CLASSIFICATION_STATUS, null=True, default='not_done')


class ClassificationResults(models.Model):
    email_subject = models.CharField(max_length=512)
    email_body = models.CharField(max_length=2048)
    email_class = models.CharField(max_length=16, choices=EMAIL_CLASS, default='regular', null=True)
