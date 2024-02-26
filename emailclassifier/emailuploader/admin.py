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
        if 'email_file' not in cleaned_data:
            raise ValidationError('Error uploading file.')

        _, extension = os.path.splitext(cleaned_data.get('email_file').name)
        if extension != cleaned_data.get('file_type'):
            raise ValidationError('File Type does not match the uploaded file')

        if cleaned_data.get('file_type') != '.csv':
            raise ValidationError('Only CSV data can be processed for now.')


# Register your models here.
class EmailFileAdmin(admin.ModelAdmin):
    list_display = ('filename', 'file_type')
    form = EmailFileForm

    def filename(self, obj):
        return os.path.basename(obj.email_file.name)

    filename.short_description = 'Filename'

    def has_change_permission(self, request, obj=None):
        return False

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
