from django.db import models


# Create your models here.
class Email(models.Model):
    subject = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)


class EmailFile(models.Model):
    email_file = models.FileField(upload_to='media/uploads/')
