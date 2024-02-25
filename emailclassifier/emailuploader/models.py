import os
from django.db import models
from django import forms

FILE_TYPES = (
    ('.csv', 'csv'),
    ('.json', 'json'),
    ('.pickle', 'pickle')
)


# Create your models here.
class Email(models.Model):
    subject = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)


class EmailFile(models.Model):
    file_type = models.CharField(max_length=10, choices=FILE_TYPES, null=True, default='.csv')
    email_file = models.FileField(upload_to='media/uploads/')

    def __str__(self):
        return os.path.basename(self.email_file.name)
