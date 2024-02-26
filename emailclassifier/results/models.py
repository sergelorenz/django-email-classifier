from django.db import models
from django.conf import settings


# Create your models here.
class ClassificationResult(models.Model):
    email_subject = models.CharField(max_length=512)
    email_body = models.CharField(max_length=2048)
    email_class = models.CharField(max_length=16, choices=[(tag.name, tag.value) for tag in settings.EMAILCLASS],
                                   default='regular', null=True)