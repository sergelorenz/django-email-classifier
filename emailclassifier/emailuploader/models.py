from django.db import models
from django import forms

FILE_TYPES = (
    (".csv", "csv"),
    (".json", "json"),
    (".pickle", "pickle")
)


# Create your models here.
class Email(models.Model):
    subject = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)


class EmailFile(models.Model):
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, null=True, default="1")
    email_file = models.FileField(upload_to='media/uploads/')

