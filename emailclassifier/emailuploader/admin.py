import os

from django.contrib import admin
from django.core.exceptions import ValidationError
from django import forms
from .models import EmailFile
from .services import email_data_reader
from classifier.models import Classification


class EmailFileForm(forms.ModelForm):
    class Meta:
        model = EmailFile
        fields = ['email_file', 'file_type']

    def clean(self):
        cleaned_data = super().clean()
        _, extension = os.path.splitext(cleaned_data.get('email_file').name)
        if extension != cleaned_data.get('file_type'):
            raise ValidationError('File Type does not match the uploaded file')


# Register your models here.
class EmailFileAdmin(admin.ModelAdmin):
    list_display = ('email_file', 'file_type')
    form = EmailFileForm

    def save_model(self, request, obj, form, change):
        file = obj.email_file.file.file
        file_type = obj.file_type
        io_reader = self.get_data_reader(file_type)
        processed_email_obj = io_reader.read_email(file)
        obj.email_file.file = processed_email_obj
        super().save_model(request, obj, form, change)
        self.add_classification(obj)

    @staticmethod
    def get_data_reader(file_type: str):
        if file_type == '.csv':
            return email_data_reader.EmailCSVReader()
        elif file_type == '.json':
            return email_data_reader.EmailJSONReader()
        elif file_type == '.pickle':
            return email_data_reader.EmailPickleReader()

        # validation for file type is already handled
        return email_data_reader.EmailCSVReader()

    @staticmethod
    def add_classification(obj):
        classification = Classification(email_file=obj)
        classification.save()


admin.site.register(EmailFile, EmailFileAdmin)
