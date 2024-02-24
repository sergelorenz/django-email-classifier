from django.db import models
from django import forms

FILE_TYPES = (
    ("1", "csv"),
    ("2", "json"),
    ("3", "pickle")
)


# Create your models here.
class Email(models.Model):
    subject = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)


class EmailFile(models.Model):
    email_file = models.FileField(upload_to='media/uploads/')
    file_type = models.CharField(max_length=1, choices=FILE_TYPES, null=True, default="1")

